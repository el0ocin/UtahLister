(function () {
  var carousel = document.querySelector("[data-sample-carousel]");
  if (!carousel) return;

  var slides = Array.prototype.slice.call(carousel.querySelectorAll("[data-sample-slide]"));
  var prev = carousel.querySelector("[data-sample-prev]");
  var next = carousel.querySelector("[data-sample-next]");
  var status = carousel.querySelector("[data-sample-status]");
  if (!slides.length || !prev || !next || !status) return;

  var index = 0;

  function render() {
    slides.forEach(function (slide, slideIndex) {
      var active = slideIndex === index;
      slide.classList.toggle("is-active", active);
      slide.setAttribute("aria-hidden", active ? "false" : "true");
    });

    status.textContent = "Page " + (index + 1) + " of " + slides.length;
    prev.disabled = index === 0;
    next.disabled = index === slides.length - 1;
  }

  prev.addEventListener("click", function () {
    if (index > 0) {
      index -= 1;
      render();
    }
  });

  next.addEventListener("click", function () {
    if (index < slides.length - 1) {
      index += 1;
      render();
    }
  });

  carousel.addEventListener("keydown", function (event) {
    if (event.key === "ArrowLeft" && index > 0) {
      index -= 1;
      render();
    }
    if (event.key === "ArrowRight" && index < slides.length - 1) {
      index += 1;
      render();
    }
  });

  render();
}());
