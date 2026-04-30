(function () {
  const config = window.UTAHLISTER_CONFIG || {};

  /* ── Selectors ────────────────────────────────────────────────── */
  const form = document.getElementById("intake-form");
  const formNote = document.getElementById("form-note");
  const formStatus = document.getElementById("form-status");
  const submitButton = document.getElementById("submit-button");
  const serviceSelect = document.getElementById("service-path");
  const contactActions = document.getElementById("contact-actions");
  const revealNodes = document.querySelectorAll(".reveal");
  const countNodes = document.querySelectorAll("[data-count-to]");
  const barNodes = document.querySelectorAll("[data-bar-width]");
  const reviewTrack = document.querySelector("[data-review-track]");
  const reviewPrev = document.querySelector("[data-review-prev]");
  const reviewNext = document.querySelector("[data-review-next]");
  const newsletterForm = document.getElementById("newsletter-form");
  const newsletterStatus = document.getElementById("newsletter-status");

  const prefersReducedMotion =
    window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ── Countup animation ────────────────────────────────────────── */
  function animateCount(node) {
    const raw = node.getAttribute("data-count-to");
    const target = parseFloat(raw);
    if (!Number.isFinite(target)) return;

    const isDecimal = String(raw).includes(".");
    const decimals = isDecimal ? (String(raw).split(".")[1] || "").length : 0;

    if (prefersReducedMotion) {
      node.textContent = isDecimal ? target.toFixed(decimals) : String(target);
      return;
    }

    const duration = 950;
    const startedAt = performance.now();

    function tick(now) {
      const progress = Math.min((now - startedAt) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const value = target * eased;
      node.textContent = isDecimal
        ? value.toFixed(decimals)
        : String(Math.round(value));
      if (progress < 1) requestAnimationFrame(tick);
    }

    requestAnimationFrame(tick);
  }

  /* ── Bar fill animation ───────────────────────────────────────── */
  function animateBar(bar) {
    const targetPct = Number(bar.getAttribute("data-bar-width")) || 0;
    if (prefersReducedMotion) {
      bar.style.width = targetPct + "%";
      return;
    }
    requestAnimationFrame(function () {
      bar.style.width = targetPct + "%";
    });
  }

  /* ── IntersectionObserver wiring ─────────────────────────────── */
  if ("IntersectionObserver" in window) {
    /* Reveal fade-in */
    const revealObs = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("is-visible");
            revealObs.unobserve(e.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -6% 0px" }
    );
    revealNodes.forEach(function (n) { revealObs.observe(n); });

    /* Countup numbers */
    if (countNodes.length) {
      const countObs = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (e) {
            if (e.isIntersecting) {
              animateCount(e.target);
              countObs.unobserve(e.target);
            }
          });
        },
        { threshold: 0.4 }
      );
      countNodes.forEach(function (n) { countObs.observe(n); });
    }

    /* Bar chart fills */
    if (barNodes.length) {
      const barObs = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (e) {
            if (e.isIntersecting) {
              animateBar(e.target);
              barObs.unobserve(e.target);
            }
          });
        },
        { threshold: 0.3 }
      );
      barNodes.forEach(function (n) { barObs.observe(n); });
    }
  } else {
    /* Fallback: no IntersectionObserver */
    revealNodes.forEach(function (n) { n.classList.add("is-visible"); });
    countNodes.forEach(animateCount);
    barNodes.forEach(animateBar);
  }

  /* ── Review carousel ─────────────────────────────────────────── */
  if (reviewTrack && reviewPrev && reviewNext) {
    var getScrollAmt = function () {
      var card = reviewTrack.querySelector(".review-card");
      return card
        ? card.getBoundingClientRect().width + 16
        : reviewTrack.clientWidth * 0.85;
    };
    reviewPrev.addEventListener("click", function () {
      reviewTrack.scrollBy({ left: -getScrollAmt(), behavior: "smooth" });
    });
    reviewNext.addEventListener("click", function () {
      reviewTrack.scrollBy({ left: getScrollAmt(), behavior: "smooth" });
    });
  }

  /* ── Conditional intake form fields ─────────────────────────── */
  var fieldSets = {
    new_listing_build: document.getElementById("fields-new-listing"),
    listing_rescue: document.getElementById("fields-rescue"),
    buy_direct: document.getElementById("fields-buy"),
    not_sure: document.getElementById("fields-not-sure")
  };

  /* pre-select path if a card CTA was clicked (data-path attribute) */
  document.querySelectorAll("[data-path]").forEach(function (link) {
    link.addEventListener("click", function () {
      var path = link.getAttribute("data-path");
      if (serviceSelect && serviceSelect.querySelector('option[value="' + path + '"]')) {
        serviceSelect.value = path;
        showFieldsForPath(path);
      }
    });
  });

  function showFieldsForPath(val) {
    Object.keys(fieldSets).forEach(function (key) {
      var el = fieldSets[key];
      if (!el) return;
      if (key === val) {
        el.removeAttribute("hidden");
      } else {
        el.setAttribute("hidden", "");
      }
    });
    /* Show submit button only after a path is selected */
    if (contactActions) {
      if (val && val !== "") {
        contactActions.removeAttribute("hidden");
      } else {
        contactActions.setAttribute("hidden", "");
      }
    }
  }

  if (serviceSelect) {
    serviceSelect.addEventListener("change", function () {
      showFieldsForPath(serviceSelect.value);
    });
    /* Run once on load in case browser restored a value */
    showFieldsForPath(serviceSelect.value);
  }

  /* ── Newsletter form ─────────────────────────────────────────── */
  if (newsletterForm && newsletterStatus) {
    newsletterForm.addEventListener("submit", async function (e) {
      e.preventDefault();
      var emailInput = newsletterForm.querySelector('input[type="email"]');
      if (!emailInput || !emailInput.value.trim()) return;

      var btn = newsletterForm.querySelector("button[type='submit']");
      if (btn) { btn.disabled = true; btn.textContent = "Subscribing…"; }
      newsletterStatus.textContent = "";

      try {
        var res = await fetch("https://formspree.io/f/maqlnklb", {
          method: "POST",
          body: JSON.stringify({ email: emailInput.value.trim(), lead_source: "newsletter" }),
          headers: { "Content-Type": "application/json", "Accept": "application/json" }
        });
        if (!res.ok) throw new Error("Network error");
        newsletterStatus.textContent = "You're subscribed — talk soon!";
        newsletterForm.reset();
      } catch (_) {
        newsletterStatus.textContent = "Something went wrong. Try again in a moment.";
      } finally {
        if (btn) { btn.disabled = false; btn.textContent = "Subscribe"; }
      }
    });
  }

  /* ── Intake form submission ──────────────────────────────────── */
  if (!form || !formNote || !formStatus || !submitButton) return;

  var hasEndpoint =
    typeof config.formAction === "string" && config.formAction.trim().length > 0;

  if (hasEndpoint) {
    form.action = config.formAction.trim();
    form.method =
      typeof config.formMethod === "string" && config.formMethod.trim().length > 0
        ? config.formMethod.trim()
        : "POST";
    if (config.readyMessage) formNote.textContent = config.readyMessage;

    form.addEventListener("submit", async function (event) {
      event.preventDefault();

      /* Honeypot check */
      if (form.company && form.company.value.trim() !== "") {
        formStatus.textContent = "Submission blocked.";
        formStatus.classList.add("is-error");
        return;
      }

      submitButton.disabled = true;
      submitButton.textContent = "Sending…";
      formStatus.textContent = "";
      formStatus.classList.remove("is-error");

      try {
        var response = await fetch(form.action, {
          method: form.method || "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" }
        });
        if (!response.ok) throw new Error("Request failed.");
        form.reset();
        showFieldsForPath("");
        window.location.href = "thanks.html";
      } catch (_) {
        formStatus.textContent =
          "Something went wrong while sending. Please try again or email youreachednicole@gmail.com.";
        formStatus.classList.add("is-error");
      } finally {
        submitButton.disabled = false;
        submitButton.textContent = "Send intake";
      }
    });

    return;
  }

  /* No endpoint configured */
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (form.company && form.company.value.trim() !== "") {
      formStatus.textContent = "Submission blocked.";
      formStatus.classList.add("is-error");
      return;
    }
    formStatus.textContent =
      config.pendingMessage ||
      "Form routing not yet connected. Use the intake checklist until it is.";
    formStatus.classList.add("is-error");
    submitButton.blur();
  });
})();

// Carousel functionality for the homepage listing package preview
document.addEventListener('DOMContentLoaded', () => {
  const carousel = document.querySelector('.package-carousel');
  if (!carousel) return;

  const slides = Array.from(carousel.querySelectorAll('.carousel-slide'));
  const nextBtn = carousel.querySelector('.next-btn');
  const prevBtn = carousel.querySelector('.prev-btn');

  if (!slides.length || !nextBtn || !prevBtn) return;

  let currentIndex = 0;

  function updateCarousel() {
    slides.forEach((slide, index) => {
      const active = index === currentIndex;
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', active ? 'false' : 'true');
    });
  }

  nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
  });

  prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateCarousel();
  });

  updateCarousel();
});
