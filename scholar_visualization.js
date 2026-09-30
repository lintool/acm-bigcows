(() => {
  const DATA = window.SCHOLAR_DATA;
  if (!DATA || DATA.schemaVersion !== 1 || !Array.isArray(DATA.rows) || !DATA.metadata ||
      DATA.metadata.award !== document.body.dataset.award) {
    document.getElementById('table').hidden = true;
    const message = document.getElementById('empty');
    message.textContent = 'Citation data could not be loaded for this award. Keep the matching data script alongside this page and reload.';
    message.classList.add('visible');
    return;
  }
  // Use one display window for both awards, regardless of dataset coverage.
  const YEAR_MAX = new Date().getUTCFullYear();
  const YEAR_MIN = 1986;
  const YEARS = Array.from({length: YEAR_MAX - YEAR_MIN + 1}, (_, index) => String(YEAR_MIN + index));
  document.documentElement.style.setProperty('--year-count', YEARS.length);
  const state = { query: '', showMissing: false, sortKey: 'year', sortDirection: -1 };
  const nameCollator = new Intl.Collator('en', { sensitivity: 'base' });
  const numberFormatter = new Intl.NumberFormat('en-US');
  const nameSuffixPattern = String.raw`(?:Jr\.?|Sr\.?|II|III|IV)`;
  const nameSuffix = new RegExp(`^${nameSuffixPattern}$`, 'i');
  const trailingNameSuffix = new RegExp(String.raw`,?\s+${nameSuffixPattern}$`, 'i');
  const columns = [
    { key: 'year', label: 'Year', className: 'year', value: row => row.year, format: value => value || '' },
    { key: 'name', label: 'Name', sortLabel: 'last name', className: 'author', title: row => row.name, value: row => row.name,
      format: (_, row) => authorCell(row), compare: compareNames, initialDirection: 1 },
    { key: 'citations', label: 'Cites', headerTitle: 'total citations from Google Scholar', className: 'metric', align: 'right', value: row => scholarMetric(row, 'citations') },
    { key: 'approximate_citations_at_induction', label: 'cites at award', headerHtml: 'cites<br>at award', headerTitle: 'estimated citations from Google Scholar at year of award',
      className: 'metric', align: 'right', value: awardCitationsValue,
      format: (value, row) => predatesTuringEstimate(row) ? '-' : fmt(value) },
    { key: 'hIndex', label: 'h-index', headerTitle: 'h-index from Google Scholar', className: 'metric', align: 'right', value: row => scholarMetric(row, 'hIndex') },
  ];
  const columnsByKey = new Map(columns.map(column => [column.key, column]));
  const profiles = [
    ['ACM', 'acmProfile', '<img class="profile-icon-acm" src="./assets/acm-icon.svg" width="18" height="18" alt="">'],
    ['Google Scholar', 'scholarProfile', '<img src="./assets/google-g.png" width="18" height="18" alt="">'],
    ['DBLP', 'dblpProfile', '<img src="./assets/dblp-icon.png" width="18" height="18" alt="">'],
  ];
  const citationAxis = axisHtml();
  // Source rows stay untouched; their names and rendered cells are fixed for this page load.
  const preparedRows = new Map(DATA.rows.map(row => {
    const name = parseName(row.name);
    return [row, {lastName: name.lastName, searchNames: [searchText(row.name), searchText(name.givenFirst)], html: rowHtml(row)}];
  }));

  const table = document.getElementById('table');
  const summary = document.getElementById('summary');
  summary.textContent = `Annual citations from Google Scholar for ${YEAR_MIN}–${YEAR_MAX}.`;
  const empty = document.getElementById('empty');
  const hideTooltip = setupTooltip(table, document.getElementById('citation-tooltip'));
  const scholarProfiles = DATA.rows.filter(row => row.scholarProfile).length;
  const dblpProfiles = DATA.rows.filter(row => row.dblpProfile).length;
  function captureRange(profileKey, dateKey) {
    const dates = DATA.rows.filter(row => row[profileKey] && row[dateKey]).map(row => row[dateKey]).sort();
    if (!dates.length) return 'Unavailable';
    return dates[0] === dates.at(-1) ? escapeHtml(dates[0]) : `${escapeHtml(dates[0])} – ${escapeHtml(dates.at(-1))}`;
  }
  document.getElementById('coverage').innerHTML = `
    <p class="coverage-total"><strong>${fmt(DATA.rows.length)}</strong> total recipients</p>
    <table class="profile-coverage" aria-label="Linked profile coverage">
      <thead><tr><th scope="col">Profiles</th><th scope="col">With</th><th scope="col">Without</th><th scope="col">Capture dates (UTC)</th></tr></thead>
      <tbody>
        <tr><th scope="row">Google Scholar</th><td>${fmt(scholarProfiles)}</td><td>${fmt(DATA.rows.length - scholarProfiles)}</td><td class="capture-dates">${captureRange('scholarProfile', 'crawlDate')}</td></tr>
        <tr><th scope="row">DBLP</th><td>${fmt(dblpProfiles)}</td><td>${fmt(DATA.rows.length - dblpProfiles)}</td><td class="capture-dates">${captureRange('dblpProfile', 'dblpCrawlDate')}</td></tr>
      </tbody>
    </table>`;

  document.getElementById('search').addEventListener('input', event => { state.query = searchText(event.target.value); render(); });
  document.getElementById('showMissing').addEventListener('change', event => { state.showMissing = event.target.checked; render(); });
  table.addEventListener('click', event => {
    const button = event.target.closest('button[data-sort]');
    if (!button) return;
    const key = button.dataset.sort;
    const column = columnsByKey.get(key);
    if (!column) return;
    state.sortDirection = state.sortKey === key ? -state.sortDirection : (column.initialDirection ?? -1);
    state.sortKey = key;
    render();
    document.getElementById(`sort-${key}`).focus();
  });
  function fmt(value) {
    return value == null ? '' : numberFormatter.format(value);
  }

  function tooltipPosition(x, y, bounds, viewport) {
    const margin = 8;
    const pointerOffset = 12;
    return {
      left: Math.max(margin, Math.min(x + pointerOffset, viewport.width - bounds.width - margin)),
      top: Math.max(margin, y + pointerOffset + bounds.height > viewport.height - margin ?
        y - bounds.height - pointerOffset : y + pointerOffset),
    };
  }

  function setupTooltip(container, tooltip) {
    let activeTarget = null;
    let bounds;
    function hide() {
      tooltip.style.display = 'none';
      activeTarget = null;
    }
    function show(target, x, y) {
      if (target !== activeTarget) {
        tooltip.textContent = target.dataset.tooltip;
        tooltip.style.display = 'block';
        bounds = tooltip.getBoundingClientRect();
        activeTarget = target;
      }
      const position = tooltipPosition(x, y, bounds,
        {width: window.innerWidth, height: window.innerHeight});
      tooltip.style.left = `${position.left}px`;
      tooltip.style.top = `${position.top}px`;
    }
    container.addEventListener('pointermove', event => {
      const target = event.target.closest('[data-tooltip]');
      if (!target) { hide(); return; }
      show(target, event.clientX, event.clientY);
    });
    container.addEventListener('focusin', event => {
      const target = event.target.closest('[data-tooltip]');
      if (!target) { hide(); return; }
      const anchor = event.target.getBoundingClientRect();
      show(target, anchor.left, anchor.bottom);
    });
    container.addEventListener('focusout', hide);
    container.addEventListener('pointerleave', hide);
    window.addEventListener('scroll', hide, true);
    window.addEventListener('resize', hide);
    document.addEventListener('keydown', event => { if (event.key === 'Escape') hide(); });
    return hide;
  }

  function parseName(name) {
    const comma = name.indexOf(',');
    if (comma >= 0 && !nameSuffix.test(name.slice(comma + 1).trim())) {
      return { lastName: name.slice(0, comma).trim(), givenFirst: `${name.slice(comma + 1)} ${name.slice(0, comma)}` };
    }
    const parts = name.trim().replace(trailingNameSuffix, '').split(/\s+/);
    return { lastName: parts[parts.length - 1], givenFirst: name };
  }

  function searchText(value) {
    return value.toLowerCase().replace(/,/g, ' ').replace(/\s+/g, ' ').trim();
  }

  function matchesName(row, query) {
    return preparedRows.get(row).searchNames.some(name => name.includes(query));
  }

  function compareNames(a, b) {
    return nameCollator.compare(preparedRows.get(a).lastName, preparedRows.get(b).lastName) || nameCollator.compare(a.name, b.name);
  }

  function compareRows(a, b) {
    const column = columnsByKey.get(state.sortKey);
    if (column.compare) {
      return state.sortDirection * column.compare(a, b) || (b.year || 0) - (a.year || 0);
    }
    const av = column.value(a), bv = column.value(b);
    // Keep unavailable metrics last in either direction; zero is a valid value.
    if ((av == null) !== (bv == null)) return av == null ? 1 : -1;
    return state.sortDirection * ((av ?? 0) - (bv ?? 0)) ||
      (b.year || 0) - (a.year || 0) || compareNames(a, b);
  }

  function filteredRows() {
    return DATA.rows.filter(row => {
      if (!state.showMissing && !row.hasScholar) return false;
      if (!state.query) return true;
      return matchesName(row, state.query);
    }).sort(compareRows);
  }

  function chart(row) {
    if (!row.hasScholar) return '<div class="chart-cell missing" role="cell">No Google Scholar data</div>';
    const values = YEARS.map(year => row.citationByYear[year] || 0);
    const max = Math.max(...values) || 1;
    const bars = YEARS.map((year, index) => {
      const value = values[index];
      const height = value ? Math.max(2, Math.round((value / max) * 100)) : 1;
      const beforeInduction = row.year != null && +year < row.year;
      const cls = `bar${value ? '' : ' zero'}${beforeInduction ? ' before-induction' : ''}`;
      const count = Object.hasOwn(row.citationByYear, year) ? `${fmt(value)} cites` : 'no captured data';
      const label = `${year}: ${count}`;
      return `<div class="${cls}" style="height:${height}%" data-tooltip="${label}" aria-label="${label}"></div>`;
    }).join('');
    const lowQuality = row.scholarQuality === 'N';
    return `<div class="chart-cell" role="cell"><div class="chart${lowQuality ? ' quality-low' : ''}" aria-label="Citation history for ${escapeHtml(row.name)}${lowQuality ? '; Google Scholar profile quality N' : ''}">${bars}</div></div>`;
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  }

  function authorCell(row) {
    const name = escapeHtml(row.name);
    const links = profiles.map(([service, field, icon]) => row[field] ?
      `<a class="profile-link" href="${escapeHtml(row[field])}" title="${service} profile" aria-label="${service} profile for ${name}">${icon}</a>` :
      '<span class="profile-slot" aria-hidden="true"></span>'
    ).join('');
    return `<span class="author-name">${name}</span><span class="profile-links">${links}</span>`;
  }

  function scholarMetric(row, field) {
    return row.hasScholar ? row[field] : null;
  }

  function predatesTuringEstimate(row) {
    return DATA.metadata.award === 'turing' && row.year != null && row.year < 1986;
  }

  function awardCitationsValue(row) {
    return predatesTuringEstimate(row) ? null : scholarMetric(row, 'approximate_citations_at_induction');
  }

  function axisHtml() {
    const ticks = YEARS.map(year => {
      const labeled = +year % 5 === 0;
      return `<span class="axis-year${labeled ? ' tick' : ''}" title="${year}">${labeled ? `<span class="axis-label">${year}</span>` : ''}</span>`;
    }).join('');
    return `<div role="columnheader" class="axis" aria-label="Citation year">${ticks}</div>`;
  }

  function headersHtml() {
    return columns.map(({key, label, headerHtml, headerTitle, sortLabel, align}) => {
      const active = state.sortKey === key;
      const direction = state.sortDirection === 1 ? 'ascending' : 'descending';
      const arrow = active ? (state.sortDirection === 1 ? '↑' : '↓') : '↕';
      return `<div role="columnheader"${headerTitle ? ` data-tooltip="${escapeHtml(headerTitle)}"` : ''}${align === 'right' ? ' class="metric-header"' : ''}${active ? ` aria-sort="${direction}"` : ''}><button type="button" id="sort-${key}" class="sort-button" data-sort="${key}"${headerTitle ? ` aria-describedby="description-${key}"` : ''} aria-label="Sort by ${sortLabel || label}"><span class="sort-label">${headerHtml || label}</span><span class="sort-arrow" aria-hidden="true">${arrow}</span></button>${headerTitle ? `<span id="description-${key}" hidden>${escapeHtml(headerTitle)}</span>` : ''}</div>`;
    }).join('');
  }

  function rowHtml(row) {
    const cells = columns.map(column => {
      const title = column.title ? ` title="${escapeHtml(column.title(row))}"` : '';
      const content = (column.format || fmt)(column.value(row), row);
      return `<div class="${column.className}" role="cell"${title}>${content}</div>`;
    }).join('');
    return `<div class="row" role="row">${cells}${chart(row)}</div>`;
  }

  function render() {
    hideTooltip();
    const rows = filteredRows();
    empty.classList.toggle('visible', rows.length === 0);
    table.style.display = rows.length ? '' : 'none';

    table.innerHTML = `<div class="row head" role="row">${headersHtml()}${citationAxis}</div>` + rows.map(row => preparedRows.get(row).html).join('');
  }

  render();
})();
