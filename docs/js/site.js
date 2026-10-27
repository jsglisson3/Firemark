/* Firemark v2 site script. Small, dependency-free, progressive. */
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

  /* The one orchestrated moment: the search types in, the pin drops onto Main St, the glow opens, and your business
     appears as the result. Runs once. With reduced motion (or no JavaScript) the finished picture shows immediately. */
  var hero = document.querySelector('[data-hero]');
  if (hero && !reduceMotion) {
    var pin = hero.querySelector('.map-pin'), ring = hero.querySelector('.map-ring'), card = hero.querySelector('.place-card');
    var q = hero.querySelector('[data-q]'), query = q ? q.textContent : '';
    var show = function (el, cls) { if (el) el.classList.add(cls || 'is-shown'); };
    if (q) { q.textContent = ''; hero.classList.add('hero-typing'); }
    setTimeout(function () { show(card); }, 250);
    for (var i = 1; i <= query.length; i++) {
      (function (n) { setTimeout(function () { q.textContent = query.slice(0, n); }, 500 + n * 45); })(i);
    }
    var t = 500 + query.length * 45 + 200;
    setTimeout(function () { hero.classList.remove('hero-typing'); show(pin); }, t);
    setTimeout(function () { show(ring); }, t + 250);
    setTimeout(function () { show(card, 'is-found'); }, t + 450);
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

    required.forEach(function (name) {
      var input = form.elements[name];
      input.addEventListener('blur', function () {
        if (input.value.trim() || input.getAttribute('aria-invalid') === 'true') setFieldState(name, errorFor(name));
      });
      input.addEventListener('input', function () {
        if (input.getAttribute('aria-invalid') === 'true' && !errorFor(name)) setFieldState(name, '');
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
      var endpoint = keyField && keyField.value && keyField.value.indexOf('PLACEHOLDER') === -1 ? form.getAttribute('action') : '';
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
