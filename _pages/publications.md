---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
classes:
  - publications-page
---

<div class="publications-intro">
  <p>Research in econometrics, empirical macroeconomics, and climate and energy policy. Use the filters to browse journal articles, working papers, and policy reports.</p>
  <a class="scholar-link" href="{{ site.author.googlescholar }}">Google Scholar ↗</a>
</div>

<div class="publication-tools" aria-label="Filter publications" hidden>
  <input class="publication-search" type="search" placeholder="Search by title, author, journal, or year" aria-label="Search publications" data-publication-search>
  <button class="publication-filter is-active" type="button" data-filter="all" aria-pressed="true">All</button>
  <button class="publication-filter" type="button" data-filter="journal" aria-pressed="false">Journal articles</button>
  <button class="publication-filter" type="button" data-filter="working-paper" aria-pressed="false">Working papers</button>
  <button class="publication-filter" type="button" data-filter="report" aria-pressed="false">Reports</button>
</div>

<p class="publication-count" role="status" aria-live="polite" data-publication-count>{{ site.data.publications | size }} publications</p>

<div class="publication-list" data-publication-list>
  {% for publication in site.data.publications %}
    {% include publication-card.html publication=publication %}
  {% endfor %}
</div>

<p class="publication-empty" data-publication-empty hidden>No publications match this search.</p>


<script src="{{ "/assets/js/publications.js" | relative_url }}" defer></script>
