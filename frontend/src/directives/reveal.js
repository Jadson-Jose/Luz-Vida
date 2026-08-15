export const reveal = {
  mounted(el) {
    el.classList.add("reveal");
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("in");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12 },
      );
      observer.observe(el);
      el._observer = observer;
    } else {
      el.classList.add("in");
    }
  },
  unmounted(el) {
    if (el._observer) el._observer.disconnect();
  },
};
