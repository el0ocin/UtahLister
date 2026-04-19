# Intake, Readiness, and Pricing-Lane Process (UtahLister Research Report)

## 1. Research Scope Summary  
This research focuses on designing UtahLister’s customer-facing intake and qualification workflow. We examine which customer inputs are essential, how to verify asset quality (especially photos), and how to classify jobs into pricing tiers and payment steps. We rely on marketplace listing and UX best practices to ground our recommendations. For example, intake forms should be as concise as possible to maximize completion (fewer fields boost conversion【44†L185-L193】) and should validate required inputs before submission to reduce rework【64†L21-L24】. This report integrates findings from online marketplaces (e.g. Amazon, eBay, Facebook), UX research on forms, and freelance pricing advice to produce actionable rules for UtahLister’s intake, review, and pricing processes.

## 2. Executive Summary  
- **Essential Fields:** Only collect information needed to prepare a listing. Core fields include seller contact (name, email, phone) and key item details (title, category, condition, brand/model, asking price)【13†L175-L178】【47†L96-L104】. Additional details (e.g. size, color) can be optional. Mandatory fields should be clearly marked (e.g. with “*”) and unambiguous【13†L175-L178】【44†L199-L207】.  
- **Photo Requirements:** Require multiple high-quality images. Guideline: at least 3–5 photos (e.g. front, back, sides, close-ups of any wear)【76†L272-L280】【51†L90-L95】. Images must be high-resolution (1000+ px on the long side) and adhere to marketplace norms (no borders/watermarks, sRGB color, product filling ~80% of frame)【20†L99-L107】【39†L125-L133】. For example, Amazon and eBay recommend ≥1000–1600 px with white backgrounds【39†L125-L133】【20†L99-L107】, and Facebook allows up to 10 photos at ~1200×628 px【50†L475-L483】. UtahLister should explicitly instruct clients on these standards.  
- **Readiness Check:** Before acceptance, verify all required inputs and photo standards. Ideally enforce field validation on the intake form to block incomplete submissions【64†L21-L24】. In review, if all criteria are met, mark the job as *Ready*. If minor info is missing or images need improvement, ask the client to clarify (e.g. “Please upload a clear front-view photo with a plain background”). Jobs missing critical data or violating rules (e.g. no usable photos or disallowed items) should be *Declined* early to avoid wasted effort. Use a structured triage: “Accept” only if all checks pass; otherwise “Clarify” or “Decline” based on severity【86†L1-L4】.  
- **Pricing Lanes:** Assign jobs to pricing tiers based on factors affecting effort and value. Key factors include item value, category (rarity/complexity), research burden, turnaround urgency, number of photos, condition clarity, and platform. For example, UtahLister might define lanes like “Standard” (straightforward items, common category, self-explanatory condition), “Premium” (high-value or rare items requiring deep research), and an *Rush* tier for expedited service. Resolution Photomatching, a comparable service, uses item value and research complexity to split into “Full” vs “Standard” tiers【57†L56-L63】. Likewise, freelancers set rates by project complexity and value delivered【55†L11-L15】. UtahLister should codify threshold rules (e.g. item >$X or “urgent” flagged → higher tier) and test with examples.  
- **Payment Gate:** Because UtahLister’s service is custom and intangible, require payment upfront once a job is accepted. Industry advice is clear: for custom services with no collateral, collect payment before doing work【70†L318-L327】【70†L349-L358】. UtahLister should trigger an invoice or payment request immediately upon finalizing a job lane, and only begin listing work after payment is secured. This avoids non-payment risk (freelancers often collect deposits for the same reason【70†L318-L327】).  
- **Avoiding Mistakes:** Common intake pitfalls include asking too many questions (which lowers completion rates【74†L134-L142】) and not optimizing for mobile devices. Keep forms lean and use conditional logic to hide irrelevant fields【74†L134-L142】. Also, clearly explain any complex requirements so clients know what high-quality photos look like. In summary, this report recommends a focused form, strict asset standards, a clear accept/clarify/decline flow, tiered pricing rules, and an upfront payment policy.

## 3. Recommended Intake Requirements  
UtahLister’s intake form should gather all information needed to create a complete listing while minimizing burden. Key fields include:  
- **Seller Contact:** Full name, email address, and phone number (required). These are essential to reach the seller and confirm details【13†L175-L178】.  
- **Item Title & Category:** A concise item title and selection of the correct category (e.g. electronics, furniture) for the platform. Category helps determine which item specifics are needed.  
- **Brand/Model/Specifications:** If applicable, capture brand name, model number, size, color, etc. These details improve listing quality (eBay advises providing all relevant item specifics to maximize visibility【47†L167-L175】).  
- **Condition:** A dropdown (e.g. New, Like New, Used-Good, etc.) plus a brief free-text description. Being honest and specific about condition is crucial【47†L128-L131】. For example: “Light surface scratches on top, all functions tested.”  
- **Quantity:** How many of this item are being listed (if >1). Default to “1” if unspecified.  
- **Asking Price:** The seller’s target price or price range. This helps UtahLister and will influence lane selection. (If uncertain, a quick market value estimate is required.)  
- **Photos:** Upload fields for images. The form should require at least one image (the main photo) and allow multiple uploads. Instructions should note ideal photo count (e.g. 3+) and quality guidelines.  
- **Optional Details:** Any additional notes the seller wishes to provide (e.g. history of the item, bundle components, or special conditions). Also an optional “Preferred Platforms/Locations” field if listing on specific marketplaces matters.

Each field should be clearly labeled. Required fields (contact info, item title, category, price, condition, at least one photo) must be marked as such. The form should allow saving progress and editing before final submission to ensure completeness.

## 4. Recommended Mandatory vs Optional Intake Fields  
To balance low friction with completeness, distinguish essential vs. nice-to-have inputs:  
- **Required Fields:** Mark these explicitly (e.g. with an asterisk). Based on our analysis, UtahLister should at minimum require: Seller Name, Email, Phone, Item Title, Category, Item Condition, Asking Price, and at least **one photo**. These are truly needed to start work【13†L175-L178】【47†L96-L104】. For example, contact info is non-negotiable for communication【13†L175-L178】, and a photo is needed to even begin formatting a listing.  
- **Optional Fields:** Everything else can be optional, with labels indicating that. This includes extra item specifics (color, material), additional photos beyond the first, and any descriptive notes. Marking optional fields relieves user friction【44†L199-L207】.  
- **UX Tip:** Only mark fields as required if they’re truly essential to avoid drop-offs【74†L134-L142】. As one guideline puts it: *focus on collecting essential info up front*【74†L134-L142】. All required fields should be clearly distinguished (asterisks or labels)【44†L199-L207】, and the form should only display conditional fields when relevant (e.g. size charts only if “clothing” category selected).  
  No limit on optional data fields; these can be hidden or collapsible to keep the form from overwhelming the customer.

## 5. Recommended Photo and Asset Standards  
【61†embed_image】 UtahLister should enforce clear photo guidelines to ensure quality. Product images must be high-resolution, focused, and prominently feature the item. Specifically:  
- **File Specs:** JPEG or PNG format in sRGB color, with no added borders or watermarks【20†L99-L107】. Images should be at least 1000×1000px (preferably 1600px on the long side) so buyers can zoom in【39†L125-L133】【20†L99-L107】. For context, Amazon and eBay require similar standards (Amazon main images must be ≥1000px on a white background【39†L125-L133】).  
- **Background & Framing:** The main (cover) photo should ideally be on a plain white or neutral background【39†L136-L144】. The item should fill about 80–85% of the frame【39†L125-L133】 so it’s easy to see. Secondary photos can have lifestyle or contextual backgrounds (per Facebook’s advice), but should still be uncluttered.  
- **Angles & Details:** Require multiple images: e.g. front view, back view, side(s), top-down (for clothing), and close-ups of important details (tags, serial numbers, or wear/damage)【76†L272-L280】【51†L90-L95】. Poshmark-style guidance is relevant: list every angle and include any flaws or sizing tags for scale【51†L90-L95】. More photos = better clarity.  
- **Quantity & Platform:** For Facebook Marketplace, allow up to 10 photos (per FB rules) and advise ~1200×628px dimensions【50†L475-L483】. KSL Classifieds historically recommended ~640×480px to speed uploads【78†L249-L253】; UtahLister should at least meet that and prefer higher.  
- **Quality Check:** During review, verify images are in focus, well-lit, and true-to-life (no heavy filters). If the main product is too small in the frame or photos are blurry, the job should be flagged for clarification.  
- **Metadata:** Ensure images are not locked or copyrighted by third parties (some marketplaces disallow trademark logos in pictures). Photographs should be original or have permission.  

By applying these standards (source-combined from marketplace guides【20†L99-L107】【39†L125-L133】 and photography best practices【76†L272-L280】【51†L90-L95】), UtahLister will consistently receive usable visuals. Provide these rules clearly in the customer instructions so clients know what “ready” photos look like.

## 6. Readiness Review Logic  
Define a structured checklist to decide if a job is *Ready to Execute* or needs action. Before any work begins, UtahLister should verify:  
- **Complete Submission:** All *required* intake fields (from Section 4) are filled. Use form validation to enforce this when possible【64†L21-L24】. If the customer has skipped a required field (e.g. price or category), the form should ideally prevent submission, or the reviewer should catch it immediately.  
- **Photo Compliance:** The required number of images has been uploaded, and each meets quality guidelines (resolution, framing, background). If any image is missing or sub-par, mark *Clarify*.  
- **Item Consistency:** The description should match the photos (e.g. condition stated matches visible wear). If condition is vague (“old, works fine”) or conflicting, the reviewer should ask for clarification.  
- **Policy Check:** Quick scan for disallowed items or content (e.g. check that the listing is legal and allowed by the chosen platform’s terms). If anything is illegal or violates terms, immediately *Decline*.  
- **Market Feasibility:** (Optional) If the asking price is wildly outside normal range, flag for review. This can affect pricing lane or need consultation.  

If **all** readiness criteria are satisfied, the job is marked *Ready* (Accept). If **minor** issues exist (e.g. one photo too dark, or one small missing detail), move to *Clarification* rather than outright rejecting the client. For *Clarification*, use a focused request (one issue at a time) to get exactly what’s missing【86†L1-L4】. If **major** issues exist (no usable photo, essential info completely missing, or item not serviceable), mark *Declined* and notify the client with the reason. In summary: “Ready” = proceed; “Clarify” = ask fixable questions; “Decline” = reject unrecoverable cases. This two-tiered gate (automatic validation plus reviewer check) minimizes rework【64†L21-L24】 and enforces quality.

## 7. Accept / Clarify / Decline Decision Framework  
UtahLister should use a clear triage flow once a submission is reviewed:  
- **Accept (Ready):** All mandatory data and assets are present and meet standards. The job is queued for pricing and listing. Example: “Photo resolution is high, item condition is clearly described, price is provided.”  
- **Clarify:** The submission is salvageable but incomplete or ambiguous. Use targeted communication to get what’s missing. E.g., “Please upload one more photo of the back of the item,” or “Specify the brand/model for more accurate pricing.” Standardize these as canned email responses. As one best practice notes, reviewers should have templated options to *“request clarification”* with precise questions【86†L1-L4】. This keeps the workflow efficient.  
- **Decline:** The job cannot proceed. Reasons include lack of any usable photo, no contact info, or prohibited item. When declining, give a brief explanation (e.g., “We cannot list items without at least one photo”). A decline action should also trigger a concise reason code for internal tracking【86†L1-L4】.  

This framework ensures consistency: anything meeting *Ready* criteria moves forward, while flaws trigger either a remedial clarification step or termination if irreparable. Periodic reviews of decline/clarify reasons (as recommended in other domains) can refine the rules over time【86†L1-L4】.

## 8. Recommended Pricing-Lane Selection Logic  
UtahLister’s pricing lanes should reflect the work effort. We suggest a multi-factor decision tree:  
- **Item Value:** Higher-priced items justify more work. For instance, one leading service moved to value-based tiers: “Full” research vs “Standard” processing depending on estimated item value【57†L56-L63】. Use a threshold (e.g. <$50, $50–$200, >$200) to split basic vs premium lanes.  
- **Category Complexity:** Some categories have many attributes (e.g. fashion with sizes/colors or tech with specs). Jobs in complex categories (or requiring category-specific keywords) should be upsized.  
- **Research Burden:** Rare or unique items (antique, collectibles, unusual brands) require extra research time. If the staff must search specialized sources or find comps, bump the job to a higher tier【57†L56-L63】.  
- **Urgency:** Rush jobs deserve an upcharge. Like many consultants, UtahLister can add a “Rush Fee” (for example, +20–50% for same-day or 24-hour turnaround). This is standard in service pricing: urgent tasks command a premium.  
- **Number of Photos:** More images means more listing work (renaming, formatting, etc.). If a client uploads the max (10+) photos, consider whether that workload merits a higher lane.  
- **Condition Ambiguity:** Vague or poor condition requires more time (e.g. editing a photo, writing cautionary notes). Jobs flagged with “Used – Poor” or lots of defects may shift up a tier.  
- **Platform Complexity:** If listing on multiple platforms (Facebook *and* KSL) or specialized platforms, account for the extra formatting.  
- **Communication Load:** If a client requires frequent updates or revisions (e.g. multiple back-and-forths in “Clarify”), factor that as well.  

In practice, score each job by these factors and define lanes by thresholds. For example: *Standard Lane* might be for common items (<$100, clear condition, 3-4 photos, no rush) and charged at base rate; *Premium Lane* for high-value or research-heavy listings (with a 1.5× rate); *Rush Tier* for any job needing expedited handling. Each lane’s pricing should be clear and defensible. This multi-factor approach is analogous to how freelancers set rates by complexity and client value【55†L11-L15】 and how product servicing (like photomatching) links price to item value【57†L56-L63】. UtahLister should document exact cutoffs (e.g. “item over $X → Silver Lane, plus 20% for rush”) and use the intake data to assign the lane automatically or flag for human review.

## 9. How to Handle Edge Cases and Non-Fit Jobs  
Some submissions may not fit neatly into a lane. In such cases:  
- **Manual Review:** Designate a “Complex Case” path. If a job falls on boundary conditions (e.g. a moderately high-value item with an unusually large number of photos), a human should override the lane selection. Build a simple override mechanism (for example, allow support staff to bump any job to a higher tier if needed).  
- **Custom Quote:** If an item is extremely unusual or an outlier (e.g. requires travel photography or legal checks), UtahLister can offer a custom quote outside standard lanes. This avoids forcing inappropriate pricing.  
- **Incomplete/Niche Requests:** If the submission lacks clarity but seems worthwhile, proactively ask the client (e.g. “This item is rare; can you provide any additional provenance?”). If the client cannot clarify, UtahLister may decline to avoid wasted effort.  
- **Decline with Explanation:** For clearly out-of-scope requests (e.g. illegal goods, items outside stated service boundaries), promptly decline with a brief note. This ensures UtahLister’s resources aren’t spent on untenable jobs.  
Essentially, treat edge cases flexibly but transparently: don’t rigidly force a lane if the job calls for special handling. Keep a fallback plan (like manual estimation) and communicate promptly with the client if non-standard processing is needed.

## 10. Recommended Payment Timing and Gate Rules  
Because UtahLister’s listing creation is a custom, intangible service, standard practice is to collect payment *before* doing the work【70†L318-L327】【70†L349-L358】. We recommend: once a job is qualified (accepted into a lane), immediately send an invoice or payment link for the full fee (or a defined deposit) and only proceed after payment clears. Key reasons: without physical collateral, there’s no leverage if a client fails to pay for intangible work【70†L318-L327】. This aligns with advice that custom orders (like signage or design) should have upfront deposits【70†L349-L358】. UtahLister should make this explicit in the workflow: no listing editing occurs until payment is confirmed. If a client balks, the job can be canceled rather than proceed on credit. In short, treat payment as a gateway: *qualification → payment → work*. This secures revenue and lets UtahLister reallocate resources confidently.

## 11. Biggest Intake and Qualification Risks  
Potential pitfalls include:  
- **Excessive Friction:** Asking too many or irrelevant questions will drop off clients【74†L134-L142】【44†L185-L193】. Focus is needed to avoid form abandonment.  
- **Poor Photo Submissions:** Low-quality images lead to poor listings and unhappy customers. To mitigate, enforce standards early.  
- **Incomplete Data:** If fields aren’t validated, jobs may enter the pipeline incomplete, causing delays. Building a pre-submit check is critical【64†L21-L24】.  
- **Pricing Misclassification:** Without clear rules, jobs might be underpriced or confused, hurting profitability. Meticulously test the lane logic before launch.  
- **Non-payment:** Doing work before payment poses a big risk. As noted, intangible services require upfront payment to avoid losses【70†L318-L327】【70†L349-L358】.  
- **Overpromising Turnaround:** Accepting too many rush jobs could overwhelm staff. Set realistic limits on “rush” availability.  
Overall, reducing intake complexity and automating checks minimizes these risks. Regularly reviewing declined/clarified cases (as some QA process suggests) can further improve rules【86†L1-L4】.

## 12. Recommended Actions for UtahLister Right Now  
To move forward, UtahLister should:  
- **Define Mandatory Fields:** Finalize exactly which intake fields will be required vs optional based on the above guidance. For example, decide if “Price” and “Condition detail” are compulsory or optional.  
- **Set Photo Guidelines:** Create a clear photo standards document for customers (with examples) and decide how to enforce it (e.g. in-form tips or a checklist).  
- **Detail Ready Criteria:** Write down the accept/clarify/decline criteria in operational language. This includes specifying what constitutes “enough” photos, etc.  
- **Configure Pricing Lanes:** Choose lane names and thresholds. For instance, set the dollar breakpoints for each tier and define what qualifies as “rush” or “complex.” Pilot test these with sample listings.  
- **Establish Payment Policy:** Finalize the payment request approach (100% upfront vs a deposit schedule) and integrate it into the workflow. Update customer-facing terms to reflect this gate.  

Doing these decision tasks will clarify the rules needed for system implementation.

## 13. What Should Be Saved to UtahLister’s Internal Database  
- **Intake Fields:** List of all form fields (with labels and required/optional status). e.g., Name, Email*, Phone*, Item Title*, Category*, Condition*, Price*, Description, Photos (min 1)*, etc.  
- **Required Assets:** Photo specifications (min resolution, background, angles) and any other file requirements.  
- **Readiness Status Types:** Status values (e.g. `Ready`, `Needs Clarification`, `Declined`).  
- **Accept/Clarify/Decline Criteria:** A checklist or table mapping each status to its triggers. e.g., *Ready if* (all req’d fields + ≥1 quality image); *Clarify if* (minor missing data); *Decline if* (key data absent or prohibited item).  
- **Pricing-Lane Factors:** Enumerated factors used in lane decision (Item Value, Category Complexity, Research Effort, Urgency, Photo Count, Condition Clarity, Platform Count, Communication). These should be configured as part of the pricing logic.  
- **Payment Gate Rules:** The rule (e.g. “Require 100% payment upon acceptance”). Possibly an order status or flag in the CRM once payment is taken.

## 14. MANUAL WORK REQUIRED AFTER RESEARCH  
- **Build Intake Form:** Implement the front-end form (in Typeform, web builder, etc.) with the specified fields and validation logic.  
- **Develop Asset Checklists:** Create internal checklists or scripts for the review team to use in the “review photos” stage (based on the standards above).  
- **Design Pricing Lanes:** Finalize the actual pricing amounts or percentages for each lane, and encode them into pricing tables or software.  
- **Write Customer Instructions:** Draft user-friendly instructions (on the website or in emails) for submitting good photos and information.  
- **Set Up Payment Integration:** Configure payment processing to trigger immediately after qualification (e.g. Stripe or invoice system).  
- **Train Staff:** Educate the operations team on the new criteria and workflows, including use of any new tools or macros for clarifications.  

These are the hands-on tasks to translate this plan into UtahLister’s system.

## 15. Metadata Block  
- Topic: UtahLister Intake and Qualification Workflow  
- Date: 2026-04-09  
- Required Intake Fields: Name, Email, Phone, Item Title, Category, Condition, Price, Description, Photos (min 1)  
- Readiness Status Types: Ready; Needs Clarification; Declined  
- Pricing Lane Factors: Item Value; Category Complexity; Research Needed; Urgency; Number of Photos; Condition Clarity; Platform Count; Communication Load  
- Payment Gate Recommendation: Collect full payment upon job acceptance (100% upfront)  
- Source Types Used: Marketplace listing guidelines (Amazon/eBay/FB), UX design best practices, e-commerce photo guides, freelance pricing/deposit recommendations  
- Confidence Level: Medium (recommendations backed by industry practices and multiple sources)  
- Key Keywords: Intake Form; Listing Service; Photo Guidelines; Pricing Tiers; Qualification Workflow; Payment Terms; Customer Experience  
- Suggested File Name: UtahLister_IntakePricingWorkflow_2026-04-09.md  
- Suggested Notion Tags: UtahLister, Intake, Workflow, Pricing, Photos, Payment, Research

**A. FOUNDER DECISIONS TO MAKE NOW:**  
- Finalize which intake fields are mandatory vs optional (e.g. require price or not).  
- Specify exact photo requirements communicated to clients.  
- Decide pricing tier thresholds and rush surcharge amount.  
- Choose payment terms (full upfront vs deposit) and gate point.  

**B. DATABASE-READY ENTRIES:**  
- **Intake Fields:** Name; Email; Phone; Item Title; Category; Condition; Brand/Model; Price; Quantity; Description; Photos (min X).  
- **Required Assets:** High-res product images (JPEG/PNG); Min 1000px; white/neutral background; multiple angles (front/back/close-ups).  
- **Readiness Statuses:** Ready; Needs Clarification; Declined.  
- **Accept/Clarify/Decline Criteria:** *Ready* if all required fields present and photos meet standards; *Clarify* if minor info or image corrections needed; *Decline* if critical data missing or item unacceptable.  
- **Pricing-Lane Factors:** Item value; Item complexity (category); Research effort; Deadline urgency; Number of photos; Condition ambiguity; Platform count; Expected communication.  
- **Payment Gate Rules:** “Payment upon acceptance” – require full payment before beginning any work.  

**C. MANUAL WORK REQUIRED AFTER RESEARCH:**  
- Build and test the intake form with validation.  
- Develop photo-quality checklists for the review process.  
- Define exact pricing lanes (names, criteria, prices) and implement them.  
- Draft customer instructions (how to take/upload photos, what info to provide).  
- Configure the payment system to enforce upfront payment on accepted jobs.  
- Train the team on the new qualification workflow and decision criteria.  

**D. FILE AND STORAGE INSTRUCTIONS:**  
- **File name:** `UtahLister_IntakePricingWorkflow_2026-04-09.md`  
- **Folder/Category:** “UtahLister Research” (under broader Project folders)  
- **Database Title:** “Intake & Pricing Workflow Guidelines”