(function () {
  'use strict';
  var search = document.querySelector('[data-publication-search]');
  if (!search) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('[data-publication]'));
  var filters = Array.prototype.slice.call(document.querySelectorAll('[data-filter]'));
  var empty = document.querySelector('[data-publication-empty]');
  var count = document.querySelector('[data-publication-count]');
  var activeType = 'all';
  function normalise(value) {
    return value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[–—-]/g, ' ');
  }
  function update() {
    var terms = normalise(search.value).trim().split(/\s+/).filter(Boolean);
    var visible = 0;
    cards.forEach(function (card) {
      var text = normalise(card.getAttribute('data-search'));
      var show = (activeType === 'all' || card.getAttribute('data-type') === activeType) && terms.every(function (term) { return text.indexOf(term) !== -1; });
      card.hidden = !show;
      if (show) visible += 1;
    });
    empty.hidden = visible !== 0;
    count.textContent = visible + ' of ' + cards.length + ' publications';
  }
  filters.forEach(function (button) {
    button.addEventListener('click', function () {
      activeType = button.getAttribute('data-filter');
      filters.forEach(function (item) {
        item.classList.toggle('is-active', item === button);
        item.setAttribute('aria-pressed', String(item === button));
      });
      update();
    });
  });
  search.addEventListener('input', update);
  document.querySelector('.publication-tools').hidden = false;
  update();
}());
