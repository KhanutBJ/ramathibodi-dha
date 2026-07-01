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

  /* ---- Language (EN / TH) -------------------------------------------- */
  var storedLang = null;
  try { storedLang = localStorage.getItem("dha-lang"); } catch (e) {}
  if (!storedLang) {
    storedLang = "th"; // Thai-first
  }
  root.setAttribute("data-lang", storedLang);
  root.setAttribute("lang", storedLang);

  function syncPlaceholders(l) {
    var key = l === "th" ? "phTh" : "phEn";
    var nodes = document.querySelectorAll("[data-ph-en],[data-ph-th]");
    for (var i = 0; i < nodes.length; i++) {
      var v = nodes[i].dataset[key];
      if (v != null) nodes[i].setAttribute("placeholder", v);
    }
  }

  function setLang(l) {
    root.setAttribute("data-lang", l);
    root.setAttribute("lang", l);
    try { localStorage.setItem("dha-lang", l); } catch (e) {}
    syncPlaceholders(l);
  }
  syncPlaceholders(storedLang);
  document.addEventListener("click", function (e) {
    if (e.target.closest("[data-lang-toggle]")) {
      setLang(root.getAttribute("data-lang") === "th" ? "en" : "th");
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

  /* ---- Role-based sign in -------------------------------------------- */
  var ROLES = {
    student: { code: "RAMA-STUDENT", grant: "academy",     dest: "academy/learn/index.html" },
    faculty: { code: "RAMA-FACULTY", grant: "academy",     dest: "academy/learn/index.html" },
    fellow:  { code: "RAMA-FELLOW",  grant: "fellowship",  dest: "fellowship/portal/index.html" },
    partner: { code: "RAMA-PARTNER", grant: "partner",     dest: "platform.html" },
    admin:   { code: "RAMA-ADMIN",   grant: "admin",       dest: "admin.html" }
  };
  var signinEl = document.querySelector("[data-signin]");
  if (signinEl) {
    var chosen = null;
    var formEl = signinEl.querySelector(".signin-form");
    var inputEl = signinEl.querySelector("input");
    var msgEl = signinEl.querySelector(".gate__msg");
    signinEl.querySelectorAll(".role").forEach(function (b) {
      b.addEventListener("click", function () {
        signinEl.querySelectorAll(".role").forEach(function (x) { x.classList.remove("is-sel"); });
        b.classList.add("is-sel");
        chosen = b.getAttribute("data-role");
        formEl.style.display = "block";
        msgEl.textContent = "";
        inputEl.focus();
      });
    });
    formEl.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!chosen) return;
      var r = ROLES[chosen];
      var code = (inputEl.value || "").trim().toUpperCase();
      var th = root.getAttribute("data-lang") === "th";
      if (code === r.code) {
        try {
          localStorage.setItem("dha-access-" + r.grant, "1");
          localStorage.setItem("dha-role", chosen);
        } catch (e2) {}
        window.location.assign(r.dest);
      } else {
        msgEl.textContent = th ? "รหัสไม่ถูกต้อง ลองอีกครั้งหรือติดต่อผู้ดูแลโปรแกรม" : "That code was not recognised. Check with your programme lead.";
        inputEl.focus();
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
