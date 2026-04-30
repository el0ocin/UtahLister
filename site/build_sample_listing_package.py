from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import pypdfium2 as pdfium


SITE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = SITE_ROOT.parent
APP_ROOT = REPO_ROOT / "apps" / "operator-web"
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from models import (  # noqa: E402
    ApprovalGate,
    AssetRecord,
    CompEntry,
    DeliveryPacket,
    EvidenceRecord,
    ExternalValidationResult,
    ItemDossier,
    ItemImage,
    PlatformDraft,
    PricingRecommendation,
    ReplyTemplates,
    ScoreBreakdown,
    StructuredFacts,
)
from pdf_builder import ListingPacketPdfBuilder  # noqa: E402


CREAM = "#F6F0E8"
CREAM_LIGHT = "#FFF9F2"
GREEN = "#2F7A4E"
GREEN_DEEP = "#225B39"
INK = "#1A1517"
MUTED = "#6E6562"
LINE = "#DCCFC2"


def rounded(img: Image.Image, radius: int = 36) -> Image.Image:
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.size[0], img.size[1]), radius=radius, fill=255)
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def framed_page(src: Image.Image, width: int) -> Image.Image:
    ratio = width / src.size[0]
    resized = src.resize((width, int(src.size[1] * ratio)), Image.LANCZOS)
    framed = Image.new("RGBA", (resized.size[0] + 26, resized.size[1] + 26), (255, 255, 255, 255))
    framed.paste(resized, (13, 13))
    framed = rounded(framed, 28)
    ImageDraw.Draw(framed).rounded_rectangle((1, 1, framed.size[0] - 2, framed.size[1] - 2), radius=28, outline=LINE, width=2)
    return framed


def paste_with_shadow(
    base: Image.Image,
    img: Image.Image,
    xy: tuple[int, int],
    *,
    angle: int = 0,
    shadow_offset: tuple[int, int] = (18, 24),
    shadow_blur: int = 24,
    shadow_alpha: int = 75,
) -> None:
    rotated = img.rotate(angle, resample=Image.BICUBIC, expand=True)
    mask = rotated.getchannel("A")
    shadow = Image.new("RGBA", rotated.size, (0, 0, 0, 0))
    shadow.paste((0, 0, 0, shadow_alpha), (0, 0), mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
    base.alpha_composite(shadow, (xy[0] + shadow_offset[0], xy[1] + shadow_offset[1]))
    base.alpha_composite(rotated, xy)


def build_sample_dossier() -> ItemDossier:
    image_cover = SITE_ROOT / "trek-bike-outdoor.jpg"
    image_full = SITE_ROOT / "trek-bike-proof.png"
    image_secondary = SITE_ROOT / "proof-trek-before.png"
    return ItemDossier(
        item_id="public-sample-trek-marlin-5",
        workflow_type="new_listing_build",
        stage="customer_pdf_generated",
        item_name="Trek Marlin 5 Mountain Bike - Large 29er",
        requested_marketplaces=["Facebook Marketplace", "KSL"],
        sale_goal="quick sale",
        city_region="Lehi, UT",
        zip_code="84043",
        neighborhood_or_area="Holbrook Farms",
        preferred_public_landmark="Holbrook Farms Park",
        structured_facts=StructuredFacts(
            brand="Trek",
            item_type="Hardtail mountain bike",
            model="Marlin 5",
            color="Black / charcoal with silver logos",
            material="Aluminum hardtail frame with front suspension and disc brakes",
            category_pack="bikes_outdoor_gear",
            condition_choice="excellent_used",
            condition_rationale="The bike appears barely ridden, clean, and mechanically complete with only light cosmetic wear visible.",
            included_pieces="Trek Marlin 5 bike, bottle cage, and saddle bag shown in the photos",
            visible_defects="Light dust and normal minor signs of use consistent with limited riding",
            size="Large frame (L 29 CH)",
            fit_notes="29-inch hardtail setup suited for general trail riding and neighborhood cruising",
        ),
        evidence=EvidenceRecord(
            brain_dump=(
                "Trek Marlin 5 hardtail mountain bike, large frame with 29-inch wheels, in Lehi. "
                "The first pass sat at $600 with weak traction. The stronger lane moved to $475 with a better outdoor cover image, "
                "cleaner proof photos, and clearer value framing around the condition and included accessories."
            ),
            operator_notes="Public website sample. Keep the packet concise and easy to skim.",
            local_comps=[
                CompEntry(
                    comp_id="comp-1",
                    marketplace="Facebook Marketplace",
                    title="Trek Marlin 5 Mountain Bike (L 29 CH) - Barely Ridden",
                    price=475.0,
                    condition="excellent used",
                    location="Lehi, UT",
                    status="sold",
                    notes="Revised fast-sale lane that sold the next day after the listing was rebuilt.",
                ),
                CompEntry(
                    comp_id="comp-2",
                    marketplace="Original local ask",
                    title="Trek Marlin 5 first-pass listing",
                    price=600.0,
                    condition="excellent used",
                    location="Lehi, UT",
                    status="active",
                    notes="Original price lane that sat for about seven days without meaningful traction.",
                ),
                CompEntry(
                    comp_id="comp-3",
                    marketplace="Local resale band",
                    title="Comparable hardtail mountain bikes in Utah County",
                    price=525.0,
                    condition="used",
                    location="Utah County",
                    status="active",
                    notes="Typical middle ask for branded entry-level hardtails in usable condition.",
                ),
            ],
            retail_price_new=749.0,
            used_price_observations=(
                "Comparable used hardtail bikes in this class tend to cluster from the high $400s into the mid $500s depending on condition and urgency."
            ),
            external_validation=ExternalValidationResult(
                normalized_item_name="Trek Marlin 5 Mountain Bike - Large 29er",
                likely_brand="Trek",
                likely_specs=["Marlin 5", "Large frame", "29-inch wheels", "Hardtail mountain bike"],
                retail_price_low=699.0,
                retail_price_high=799.0,
                demand_strength="strong",
                market_notes=[
                    "Branded hardtail bikes with a clear size callout and outdoor proof photos tend to outperform flat indoor-only listings.",
                    "Fast-sale performance improves when the price leaves room below the first-pass aspirational ask.",
                ],
                confidence_notes=[],
                source_notes=[
                    "Founder case-study proof screenshots retained from the sold listing.",
                    "Local resale band based on Utah County hardtail ask ranges supplied in the operator notes.",
                ],
            ),
            confidence_flags=[],
        ),
        assets=AssetRecord(
            images=[
                ItemImage(
                    image_id="img-01",
                    filename="01-trek-bike-outdoor.jpg",
                    file_path=str(image_cover),
                    preview_url="trek-bike-outdoor.jpg",
                    is_cover=True,
                    order_index=1,
                ),
                ItemImage(
                    image_id="img-02",
                    filename="02-trek-bike-proof.png",
                    file_path=str(image_full),
                    preview_url="trek-bike-proof.png",
                    order_index=2,
                ),
                ItemImage(
                    image_id="img-03",
                    filename="03-proof-trek-before.png",
                    file_path=str(image_secondary),
                    preview_url="proof-trek-before.png",
                    order_index=3,
                ),
            ],
            chosen_cover_image_id="img-01",
            ordered_image_ids=["img-01", "img-02", "img-03"],
            embedded_image_ids=["img-01", "img-02", "img-03"],
        ),
        pricing=PricingRecommendation(
            quick_sale_price=475.0,
            max_sale_price=550.0,
            recommended_price=475.0,
            recommended_lane="quick sale",
            rationale_summary=(
                "The bike already proved that the faster lane was the right move. "
                "At $600, the listing sat. At $475 with a stronger image set and clearer positioning, it generated buyer activity and sold quickly."
            ),
            evidence_summary=[
                "The retained screenshots show the revised $475 listing sold after the weaker $600 lane stalled.",
                "The outdoor hero image improves trust and click-through for a bike more than the original flat indoor presentation.",
                "Comparable used hardtails in Utah County support a realistic band from the high $400s into the mid $500s.",
            ],
            market_strength_score=82,
            confidence_score=91,
            key_comp_anchors=[
                "Founder proof listing | sold at $475 | visible post-rebuild result",
                "Original stalled ask | $600 | too high for the traction level",
                "Local middle band | about $525 | comparable Utah County hardtail asks",
            ],
            score_breakdown=ScoreBreakdown(
                demand_strength_score=83,
                condition_confidence_score=89,
                brand_value_strength_score=84,
                local_competitiveness_score=86,
                urgency_score=78,
                friction_score=36,
                marketplace_fit_score=88,
            ),
        ),
        platform_drafts=[
            PlatformDraft(
                marketplace="Facebook Marketplace",
                recommended_category="Bicycles",
                recommended_posted_price=475.0,
                pricing_note="List at $475 if the goal is to move the bike in the proven fast-sale lane instead of defending the old $600 ask.",
                title="Trek Marlin 5 Mountain Bike (L 29 CH) - Barely Ridden",
                description=(
                    "Trek Marlin 5 hardtail mountain bike in excellent condition, large frame with 29-inch wheels. "
                    "Barely ridden and kept clean. Includes the bottle cage and saddle bag shown in the photos. "
                    "Strong option for neighborhood rides, light trail use, or anyone wanting a clean branded hardtail without paying full retail. "
                    "Pickup near Holbrook Farms Park in Lehi."
                ),
                posting_notes=[
                    "Lead with the outdoor rock-wall photo first because it gives the bike more presence and trust.",
                    "Use the full side-view photo second so the frame size and overall condition are easy to judge.",
                ],
                warning_notes=[
                    "Keep the location at the public-landmark level only.",
                ],
                reply_templates=ReplyTemplates(
                    is_this_available="Yes, it is available. Pickup is near Holbrook Farms Park in Lehi.",
                    whats_your_lowest="I priced it at $475 because it is a clean Trek Marlin 5 in strong condition and already sits in the fast-sale lane.",
                    lowball_offer="That is lower than I want to be right now. If you can meet in Lehi soon, send your best serious offer.",
                    pickup_coordination="Pickup is near Holbrook Farms Park in Lehi. Send a day and time window that works for you.",
                ),
            ),
            PlatformDraft(
                marketplace="KSL",
                recommended_category="Mountain Bikes",
                recommended_posted_price=475.0,
                pricing_note="Start at $475 to match the proven fast-sale lane. Only test higher if the seller is willing to hold longer for a narrower buyer pool.",
                title="Trek Marlin 5 (L 29 CH) Hardtail Mountain Bike - Excellent Condition",
                description=(
                    "Trek Marlin 5 hardtail mountain bike in excellent condition. Large frame with 29-inch wheels, clean overall presentation, and ready for riding. "
                    "Includes the bottle cage and saddle bag shown in the photo set. "
                    "Pickup in Lehi near Holbrook Farms Park."
                ),
                posting_notes=[
                    "Keep the large-frame size and 29-inch wheel setup visible in the first lines.",
                    "Use the outdoor cover image first and the indoor side-view second.",
                ],
                warning_notes=[
                    "Do not publish an exact home address in the listing text.",
                ],
                reply_templates=ReplyTemplates(
                    is_this_available="Yes, the bike is still available. Pickup is in Lehi near Holbrook Farms Park.",
                    whats_your_lowest="I listed it at $475 because that is the strongest realistic lane for a clean Trek Marlin 5 in this condition.",
                    lowball_offer="Thanks for the offer. I am not planning to drop below the fast-sale lane right now.",
                    pickup_coordination="I can meet near Holbrook Farms Park in Lehi. Send a pickup window that works for you.",
                ),
            ),
        ],
        final_checklist=[],
        approval_gate=ApprovalGate(
            facts_reviewed=True,
            price_lane_approved=True,
            marketplaces_approved=True,
            missing_questions_resolved=True,
            approved_by="UtahLister sample build",
            approved_at="2026-04-29T17:00:00",
        ),
        delivery_packet=DeliveryPacket(
            selected_marketplaces=["Facebook Marketplace", "KSL"],
            embedded_image_ids=["img-01", "img-02", "img-03"],
            google_drive_link_included=False,
            approval_timestamp="2026-04-29T17:00:00",
            generated_timestamp="2026-04-29T17:00:00",
        ),
    )


def render_pdf_pages(pdf_path: Path, renders_dir: Path) -> list[Path]:
    renders_dir.mkdir(parents=True, exist_ok=True)
    for existing in renders_dir.glob("page-*.png"):
        existing.unlink()
    pdf = pdfium.PdfDocument(str(pdf_path))
    paths: list[Path] = []
    for index in range(len(pdf)):
        page = pdf[index]
        bitmap = page.render(scale=2.1)
        image = bitmap.to_pil()
        out = renders_dir / f"page-{index + 1:02d}.png"
        image.save(out)
        paths.append(out)
    return paths


def build_homepage_hero(pages: list[Image.Image], out_path: Path) -> None:
    font_display = ImageFont.truetype(str(SITE_ROOT / "fonts" / "syne-700.ttf"), 58)
    font_body = ImageFont.truetype(str(SITE_ROOT / "fonts" / "inter-600.ttf"), 28)
    font_small = ImageFont.truetype(str(SITE_ROOT / "fonts" / "inter-500.ttf"), 22)

    hero = Image.new("RGBA", (1600, 1200), CREAM)
    draw = ImageDraw.Draw(hero)
    for bbox, fill in [((60, 70, 680, 640), (208, 103, 87, 32)), ((1020, 80, 1540, 520), (47, 122, 78, 28)), ((980, 760, 1500, 1160), (208, 103, 87, 20))]:
        layer = Image.new("RGBA", hero.size, (0, 0, 0, 0))
        ImageDraw.Draw(layer).ellipse(bbox, fill=fill)
        layer = layer.filter(ImageFilter.GaussianBlur(60))
        hero.alpha_composite(layer)

    draw.rounded_rectangle((110, 110, 420, 166), radius=28, fill=(47, 122, 78, 26), outline=(47, 122, 78, 50), width=2)
    draw.text((138, 122), "Sample listing package", font=font_small, fill=GREEN_DEEP)
    draw.text((110, 220), "See the exact PDF\ncustomers receive.", font=font_display, fill=INK, spacing=8)
    draw.text((112, 390), "Pricing rationale, photo plan, posting copy, and buyer replies\nin one clean packet.", font=font_body, fill=MUTED, spacing=8)
    draw.line((110, 500, 420, 500), fill=(34, 91, 57, 70), width=3)
    draw.text((110, 525), "One PDF · posting-ready · built around the item", font=font_body, fill=GREEN)

    page_cover = framed_page(pages[0], 340)
    page_mid = framed_page(pages[min(1, len(pages) - 1)], 270)
    page_end = framed_page(pages[min(len(pages) - 1, 2)], 270)
    paste_with_shadow(hero, page_mid, (840, 190), angle=-8)
    paste_with_shadow(hero, page_end, (1120, 250), angle=10)
    paste_with_shadow(hero, page_cover, (930, 120), shadow_blur=30, shadow_alpha=92)
    hero.convert("RGB").save(out_path, quality=95)


def build_vertical_preview(
    pages: list[Image.Image],
    out_path: Path,
    *,
    title: str,
    width: int,
    page_width: int,
    include_subtitle: bool,
) -> None:
    font_display = ImageFont.truetype(str(SITE_ROOT / "fonts" / "syne-700.ttf"), 56)
    font_body = ImageFont.truetype(str(SITE_ROOT / "fonts" / "inter-600.ttf"), 22)

    framed = [framed_page(page, page_width) for page in pages]
    top_padding = 120 if title else 36
    subtitle_height = 40 if include_subtitle else 0
    gap = 28
    stack_height = sum(image.size[1] for image in framed) + gap * (len(framed) - 1)
    height = top_padding + subtitle_height + stack_height + 80

    canvas = Image.new("RGBA", (width, height), CREAM_LIGHT)
    draw = ImageDraw.Draw(canvas)
    for bbox, fill in [((80, 30, 520, 360), (47, 122, 78, 24)), ((width - 500, 40, width - 60, 320), (208, 103, 87, 24))]:
        layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ImageDraw.Draw(layer).ellipse(bbox, fill=fill)
        layer = layer.filter(ImageFilter.GaussianBlur(70))
        canvas.alpha_composite(layer)

    if title:
        draw.text((42, 32), title, font=font_display, fill=INK)
    if include_subtitle:
        draw.text((44, 98), "The live sample PDF is linked below this preview on the website.", font=font_body, fill=MUTED)

    y = top_padding + subtitle_height
    for idx, image in enumerate(framed):
        x = (width - image.size[0]) // 2
        angle = -2 if idx % 2 == 0 else 2
        paste_with_shadow(canvas, image, (x, y), angle=angle, shadow_offset=(10, 16), shadow_blur=18, shadow_alpha=60)
        y += image.size[1] + gap

    canvas.convert("RGB").save(out_path, quality=95)


def main() -> None:
    dossier = build_sample_dossier()
    pdf_path = SITE_ROOT / "sample-listing-package.pdf"
    ListingPacketPdfBuilder().build_packet(dossier, pdf_path)

    render_paths = render_pdf_pages(pdf_path, SITE_ROOT / "sample-listing-package-renders")
    pages = [Image.open(path).convert("RGBA") for path in render_paths]

    build_homepage_hero(pages, SITE_ROOT / "sample-listing-package-hero.png")
    build_vertical_preview(
        pages,
        SITE_ROOT / "sample-listing-package-preview.png",
        title="Listing package preview",
        width=860,
        page_width=610,
        include_subtitle=False,
    )
    build_vertical_preview(
        pages,
        SITE_ROOT / "sample-listing-package-full-preview.png",
        title="",
        width=980,
        page_width=760,
        include_subtitle=False,
    )
    print(pdf_path)


if __name__ == "__main__":
    main()
