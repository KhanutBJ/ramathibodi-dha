/* Ramathibodi Digital Health & AI Club - interactions */
(function () {
  "use strict";

  /* ---- Theme ---------------------------------------------------------- */
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem("dha-theme"); } catch (e) {}
  if (!stored) {
    stored = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  root.setAttribute("data-theme", stored);

  function setTheme(t) {
    root.setAttribute("data-theme", t);
    try { localStorage.setItem("dha-theme", t); } catch (e) {}
  }

  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]");
    if (t) {
      setTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark");
    }
  });

  /* ---- Nav scroll state ---------------------------------------------- */
  var nav = document.querySelector(".nav");
  function onScroll() {
    if (!nav) return;
    nav.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---- Mobile menu ---------------------------------------------------- */
  var burger = document.querySelector("[data-burger]");
  var menu = document.querySelector(".mobile-menu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      document.body.style.overflow = open ? "hidden" : "";
    });
    menu.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { menu.classList.remove("is-open"); document.body.style.overflow = ""; }
    });
  }

  /* ---- Scroll reveal -------------------------------------------------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---- Login gate (client-side, static hosting) ----------------------
     Note: this is a soft gate for a static site, not real security.
     Access code is shared with members; swap for a real auth backend
     when one is available. ------------------------------------------- */
  var ACCESS = { academy: "RAMA-DHA", fellowship: "RAMA-FELLOW" };

  function gateKey(scope) { return "dha-access-" + scope; }
  function hasAccess(scope) {
    try { return localStorage.getItem(gateKey(scope)) === "1"; } catch (e) { return false; }
  }

  var gate = document.querySelector("[data-gate]");
  if (gate) {
    var scope = gate.getAttribute("data-gate");
    var target = gate.getAttribute("data-gate-target");
    if (hasAccess(scope)) { window.location.replace(target); return; }
    var form = gate.querySelector("form");
    var input = gate.querySelector("input");
    var msg = gate.querySelector(".gate__msg");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var code = (input.value || "").trim().toUpperCase();
      if (code === ACCESS[scope]) {
        try { localStorage.setItem(gateKey(scope), "1"); } catch (e2) {}
        window.location.assign(target);
      } else {
        msg.textContent = "That access code was not recognised. Check with your programme lead.";
        input.focus();
      }
    });
  }

  /* protect gated pages: redirect to gate if no access */
  var guard = document.querySelector("[data-guard]");
  if (guard) {
    var gscope = guard.getAttribute("data-guard");
    var gate_url = guard.getAttribute("data-guard-gate");
    if (!hasAccess(gscope)) { window.location.replace(gate_url); }
  }

  /* sign out links */
  document.addEventListener("click", function (e) {
    var so = e.target.closest("[data-signout]");
    if (so) {
      e.preventDefault();
      var sc = so.getAttribute("data-signout");
      try { localStorage.removeItem(gateKey(sc)); } catch (e3) {}
      window.location.assign(so.getAttribute("href"));
    }
  });
})();
