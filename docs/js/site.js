/* Firemark site script (v12). Small, dependency-free, progressive: the page is complete without it. */
(function () {
  'use strict';
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Mobile menu: the button sits right before the menu, so Tab moves from the button into the links. */
  var toggle = document.querySelector('[data-menu-toggle]');
  var nav = document.getElementById('site-nav');
  var menuLabel = document.querySelector('[data-menu-label]');
  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
      if (menuLabel) menuLabel.textContent = open ? 'Close' : 'Menu';
      var icon = toggle.querySelector('use');
      if (icon) icon.setAttribute('href', open ? '#i-close' : '#i-menu');
    };
    toggle.addEventListener('click', function () { setOpen(toggle.getAttribute('aria-expanded') !== 'true'); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    /* Tapping outside the sheet closes it */
    document.addEventListener('click', function (e) {
      if (toggle.getAttribute('aria-expanded') === 'true' && !nav.contains(e.target) && !toggle.contains(e.target)) setOpen(false);
    });
    var closeIfOutside = function (e) {
      var next = e.relatedTarget;
      if (toggle.getAttribute('aria-expanded') === 'true' && next && !nav.contains(next) && next !== toggle) setOpen(false);
    };
    nav.addEventListener('focusout', closeIfOutside);
    toggle.addEventListener('focusout', closeIfOutside);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { setOpen(false); toggle.focus(); }
    });
  }

  /* Header hairline once the page scrolls */
  var header = document.querySelector('[data-header]');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* The one big moment: the map flies in to Main St (CSS), the search types in, the pin drops onto Main St at
     S Colony Blvd, the glow opens and your business appears on the map. Runs once. With reduced motion (or no JavaScript) the finished picture shows immediately. */
  var hero = document.querySelector('[data-hero]');
  var card = hero && hero.querySelector('.hero-card');
  var q = hero && hero.querySelector('[data-q]');
  var shop = hero && hero.querySelector('.hero-card [data-name]');
  var pin = hero && hero.querySelector('.map-pin');
  var kind = hero && hero.querySelector('.hero-card [data-kind]');
  var hours = hero && hero.querySelector('.hero-card [data-hours]');
  var typeTimers = [];
  var typeQuery = function (text, start, done) {
    typeTimers.forEach(clearTimeout); typeTimers = [];
    q.textContent = ''; hero.classList.add('is-typing');
    for (var i = 1; i <= text.length; i++) {
      (function (n) { typeTimers.push(setTimeout(function () { q.textContent = text.slice(0, n); }, start + n * 45)); })(i);
    }
    typeTimers.push(setTimeout(function () { hero.classList.remove('is-typing'); if (done) done(); }, start + text.length * 45 + 150));
  };
  var ring = hero && hero.querySelector('.map-ring');
  var show = function (el) { if (el) el.classList.add('is-shown'); };
  if (hero && q && !reduceMotion) {
    typeQuery(q.textContent, 900, function () {
      show(pin);
      setTimeout(function () { show(ring); }, 250);
      setTimeout(function () { show(card); }, 450);
    });
  }

  /* The live part: pick your trade and the search, the result and the pin follow. */
  var tryBox = hero && hero.querySelector('[data-try]');
  if (tryBox && q && shop) {
    tryBox.hidden = false;
    var buttons = tryBox.querySelectorAll('[data-trade]');
    Array.prototype.forEach.call(buttons, function (b) {
      b.addEventListener('click', function () {
        Array.prototype.forEach.call(buttons, function (o) { o.setAttribute('aria-pressed', String(o === b)); });
        var text = b.getAttribute('data-trade') + ' near me';
        var fill = function () {
          shop.textContent = b.getAttribute('data-shop');
          if (kind) kind.textContent = b.getAttribute('data-kind');
          if (hours) hours.textContent = b.getAttribute('data-hours');
        };
        if (reduceMotion) { q.textContent = text; fill(); return; }
        [pin, ring, card].forEach(show);
        /* The old result stays while the search types, then the card refreshes with the new one */
        typeQuery(text, 0, function () {
          card.classList.add('is-swapping');
          pin.classList.remove('is-bounce'); void pin.offsetWidth; pin.classList.add('is-bounce');
          setTimeout(function () { fill(); card.classList.remove('is-swapping'); }, 170);
        });
      });
    });
  }

  /* Each section's parts rise into place once, in order (heading, words, picture). Opt-in, see site.css. */
  var reveals = document.querySelectorAll('[data-reveal]');
  if (reveals.length && !reduceMotion && 'IntersectionObserver' in window) {
    Array.prototype.forEach.call(reveals, function (r) {
      Array.prototype.forEach.call(r.children, function (c, i) { c.style.setProperty('--i', String(Math.min(i, 6))); });
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    /* Anything already on screen is shown straight away, so nothing ever blinks out */
    Array.prototype.forEach.call(reveals, function (r) {
      var box = r.getBoundingClientRect();
      if (box.top < window.innerHeight * 0.92 && box.bottom > 0) r.classList.add('is-in');
      else io.observe(r);
    });
    document.documentElement.classList.add('rv-ready');
  }

  /* Free check form.
     Baymard: mark required and optional fields, validate when a field is left (not while typing),
     clear an error as soon as it's fixed, confirm valid fields, and still check everything on submit.
     UI UX Pro Max: on a failed submit, show a focusable error summary that links to each field. */
  var form = document.querySelector('[data-check-form]');
  if (form) {
    var status = form.querySelector('[data-form-status]');
    var summary = form.querySelector('[data-error-summary]');
    var summaryList = summary ? summary.querySelector('ul') : null;
    var required = ['name', 'business', 'email'];
    var emailOk = function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); };
    var messages = {
      name: 'Enter your name so Firemark knows who to reply to.',
      business: 'Enter your business name so it can be looked up.',
      email: 'Enter an email address for your report.',
      emailFormat: 'Check the email address. It should look like name@example.com.'
    };

    var errorFor = function (name) {
      var input = form.elements[name];
      var v = input.value.trim();
      if (!v) return messages[name];
      if (name === 'email' && !emailOk(v)) return messages.emailFormat;
      return '';
    };
    var setFieldState = function (name, msg) {
      var input = form.elements[name];
      var field = input.closest('.field');
      var errId = input.id + '-error';
      var err = document.getElementById(errId);
      var described = (input.getAttribute('aria-describedby') || '').split(' ').filter(function (d) { return d && d !== errId; });
      if (msg) {
        if (!err) {
          err = document.createElement('span');
          err.className = 'field-error';
          err.id = errId;
          input.insertAdjacentElement('afterend', err);
        }
        err.textContent = msg;
        input.setAttribute('aria-invalid', 'true');
        described.push(errId);
        field.classList.remove('is-valid');
      } else {
        if (err) err.remove();
        input.removeAttribute('aria-invalid');
        field.classList.toggle('is-valid', !!input.value.trim());
      }
      if (described.length) input.setAttribute('aria-describedby', described.join(' '));
      else input.removeAttribute('aria-describedby');
    };

    /* As each problem is fixed, it leaves the summary; the summary goes once everything is fixed. */
    var titleFor = function (n) { return n === 1 ? 'One quick fix and it\u2019s ready to send:' : (n === 2 ? 'Two' : 'Three') + ' quick fixes and it\u2019s ready to send:'; };
    var refreshSummary = function () {
      if (!summary || summary.hidden || !summaryList) return;
      Array.prototype.slice.call(summaryList.children).forEach(function (li) {
        var a = li.querySelector('a');
        var input = a && document.getElementById(a.getAttribute('href').slice(1));
        if (input && input.getAttribute('aria-invalid') !== 'true') li.remove();
      });
      var left = summaryList.children.length;
      if (!left) { summary.hidden = true; return; }
      var t = summary.querySelector('[data-error-title]');
      if (t) t.textContent = titleFor(left);
    };

    required.forEach(function (name) {
      var input = form.elements[name];
      input.addEventListener('blur', function () {
        if (input.value.trim() || input.getAttribute('aria-invalid') === 'true') setFieldState(name, errorFor(name));
      });
      input.addEventListener('input', function () {
        if (input.getAttribute('aria-invalid') === 'true' && !errorFor(name)) { setFieldState(name, ''); refreshSummary(); }
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var trap = form.elements.fm_trap_field;
      if (trap && trap.value) return; // filled by a bot, not a person
      var problems = [];
      required.forEach(function (name) {
        var msg = errorFor(name);
        setFieldState(name, msg);
        if (msg) problems.push({ id: form.elements[name].id, msg: msg });
      });
      if (problems.length) {
        if (summary && summaryList) {
          summaryList.innerHTML = '';
          problems.forEach(function (p) {
            var li = document.createElement('li');
            var a = document.createElement('a');
            a.href = '#' + p.id;
            a.textContent = p.msg;
            a.addEventListener('click', function (ev) { ev.preventDefault(); document.getElementById(p.id).focus(); });
            li.appendChild(a);
            summaryList.appendChild(li);
          });
          var title = summary.querySelector('[data-error-title]');
          if (title) title.textContent = titleFor(problems.length);
          summary.hidden = false;
          summary.focus();
        } else {
          document.getElementById(problems[0].id).focus();
        }
        return;
      }
      if (summary) summary.hidden = true;

      /* Web3Forms (v9): the form posts to its action. Until the access key is pasted in, it opens a pre-filled email instead. */
      var keyField = form.querySelector('[data-access-key]');
      var endpoint = keyField && keyField.value.trim() ? form.getAttribute('action') : '';
      var subjectField = form.querySelector('[data-subject]');
      if (subjectField) subjectField.value = 'Free check request from ' + form.elements.business.value.trim();
      var data = new FormData(form);
      var fallback = form.getAttribute('data-fallback-email');
      var button = form.querySelector('button[type="submit"]');
      var firstName = (data.get('name') || '').trim().split(/\s+/)[0];
      var emailTo = (data.get('email') || '').trim();
      /* A pre-filled email with the same details, used when there is no form service or a send fails, so no lead is lost. */
      var lines = [
        'Name: ' + data.get('name'),
        'Business: ' + data.get('business'),
        'Email: ' + data.get('email'),
        'Phone: ' + (data.get('phone') || ''),
        'Website or Google listing: ' + (data.get('site') || ''),
        'Would help most: ' + [['help_website', 'A website'], ['help_listing', 'Google listing'], ['help_email', 'Email at own name'], ['help_unsure', 'Not sure yet']]
          .filter(function (h) { return data.get(h[0]); }).map(function (h) { return h[1]; }).join(', '),
        '',
        data.get('note') || ''
      ];
      var href = 'mailto:' + fallback +
        '?subject=' + encodeURIComponent('Free check request: ' + data.get('business')) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      var showEmailOption = function (lead) {
        status.textContent = '';
        status.appendChild(document.createTextNode(lead + ' '));
        var link = document.createElement('a');
        link.href = href;
        link.textContent = 'Email ' + fallback + ' instead';
        status.appendChild(link);
        status.appendChild(document.createTextNode('. Your details are filled in for you.'));
      };
      if (endpoint) {
        button.disabled = true;
        status.textContent = 'Sending your request…';
        fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (!r.ok) throw new Error('bad status');
            form.reset();
            form.querySelectorAll('.is-valid').forEach(function (f) { f.classList.remove('is-valid'); });
            form.classList.add('is-sent');
            status.textContent = 'Thanks, ' + firstName + '. Your free check is on its way. Jeremy will email it to ' + emailTo + ' within 7 days.';
            status.focus();
          })
          .catch(function () { showEmailOption('That didn\u2019t send.'); })
          .then(function () { button.disabled = false; });
        return;
      }
      /* No form service yet: open the pre-filled email, and show the link in case no mail app opens. */
      showEmailOption('Your email app should open with your details filled in. Press send there to finish. If nothing opens:');
      window.location.href = href;
    });
  }

  /* Footer year */
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
})();
