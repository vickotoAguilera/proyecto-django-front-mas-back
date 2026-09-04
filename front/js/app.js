/* ============================================
   Directorio de Cursos — app.js
   Lee data/cursos.json y renderiza las páginas
   ============================================ */

const DATA_URL = "data/cursos.json";
const $ = (sel) => document.querySelector(sel);

let data = null;

/* ---------- Utilidades ---------- */

function formatPrice(precio) {
  return new Intl.NumberFormat("es-CL", {
    style: "currency",
    currency: "CLP",
    maximumFractionDigits: 0,
  }).format(precio);
}

function iniciales(nombre) {
  return nombre
    .split(" ")
    .slice(0, 2)
    .map((p) => p[0])
    .join("")
    .toUpperCase();
}

function levelClass(nivel) {
  return nivel.toLowerCase();
}

function buscarCategoria(id) {
  return data.categorias.find((c) => c.id === id);
}

function buscarInstructor(id) {
  return data.instructores.find((i) => i.id === id);
}

/* ---------- Iconos SVG ---------- */

const ICONS = {
  clock: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
  user: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
  arrow: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
};

/* ---------- Carga de datos ---------- */

async function loadData() {
  try {
    const res = await fetch(DATA_URL);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    data = await res.json();
    return true;
  } catch (err) {
    console.error("No se pudo cargar cursos.json:", err);
    return false;
  }
}

function showDataError() {
  const target = $("#cursosGrid") || $("#detalleMain");
  if (!target) return;
  target.innerHTML = `
    <div class="empty">
      <h3>No se pudieron cargar los datos</h3>
      <p>Abre este sitio con un servidor local para que el navegador pueda leer data/cursos.json:</p>
      <p style="margin-top:10px"><code>python -m http.server 3000</code> y luego visita http://localhost:3000</p>
    </div>`;
}

/* ---------- Tarjeta de curso ---------- */

function cardHTML(curso) {
  const cat = buscarCategoria(curso.categoria_id);
  const instr = buscarInstructor(curso.instructor_id);
  const imgSrc = curso.imagen || `img/cursos/${curso.slug}.jpg`;
  return `
    <a class="card" href="detalle.html?id=${curso.id}">
      <div class="card__cover" style="position: relative; width: 100%; height: 185px; overflow: hidden; background: var(--emerald-100);">
        <img src="${imgSrc}" alt="${curso.titulo}" class="card__img" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy">
        <span class="level-badge ${levelClass(curso.nivel)}">${curso.nivel}</span>
      </div>
      <div class="card__body">
        <div class="card__top">
          <span class="category-badge">${cat ? cat.nombre : "Sin categoría"}</span>
        </div>
        <h3>${curso.titulo}</h3>
        <p class="card__desc">${curso.descripcion}</p>
        <div class="card__meta">
          <span>${ICONS.clock} ${curso.duracion_horas} horas</span>
          <span>${ICONS.user} ${instr ? instr.nombre : "Sin instructor"}</span>
        </div>
        <div class="card__bottom">
          <span class="price">${formatPrice(curso.precio)}</span>
          <span class="card__link">Ver detalle ${ICONS.arrow}</span>
        </div>
      </div>
    </a>`;
}

/* ---------- Página principal ---------- */

function renderStats() {
  $("#statCursos").textContent = data.cursos.length;
  $("#statCategorias").textContent = data.categorias.length;
  $("#statInstructores").textContent = data.instructores.length;
}

function renderFilters() {
  const container = $("#filtros");
  const buttons = [{ id: "todos", nombre: "Todos" }, ...data.categorias.map((c) => ({ id: c.id, nombre: c.nombre }))];
  container.innerHTML = buttons
    .map(
      (b) =>
        `<button class="filter-pill ${b.id === "todos" ? "active" : ""}" data-categoria="${b.id}">${b.nombre}</button>`
    )
    .join("");
}

function renderCourses() {
  const catSel = $("#filtros .filter-pill.active").dataset.categoria;
  const busqueda = $("#busqueda").value.trim().toLowerCase();
  const grid = $("#cursosGrid");
  const count = $("#contador");

  const filtrados = data.cursos.filter((c) => {
    const okCat = catSel === "todos" || c.categoria_id === Number(catSel);
    const okBusq =
      !busqueda ||
      c.titulo.toLowerCase().includes(busqueda) ||
      c.descripcion.toLowerCase().includes(busqueda);
    return okCat && okBusq;
  });

  count.textContent = `${filtrados.length} de ${data.cursos.length} cursos`;

  grid.innerHTML = filtrados.length
    ? filtrados.map(cardHTML).join("")
    : `<div class="empty">
         <h3>Sin resultados</h3>
         <p>No encontramos cursos con ese filtro o búsqueda.</p>
       </div>`;
}

function initIndex() {
  renderStats();
  renderFilters();
  renderCourses();

  $("#filtros").addEventListener("click", (e) => {
    if (!e.target.classList.contains("filter-pill")) return;
    document.querySelectorAll(".filter-pill").forEach((p) => p.classList.remove("active"));
    e.target.classList.add("active");
    renderCourses();
  });

  $("#busqueda").addEventListener("input", renderCourses);
  $("#formBusqueda").addEventListener("submit", (e) => e.preventDefault());
}

/* ---------- Página de detalle ---------- */

function renderDetalle(curso) {
  const cat = buscarCategoria(curso.categoria_id);
  const instr = buscarInstructor(curso.instructor_id);
  const imgSrc = curso.imagen || `img/cursos/${curso.slug}.jpg`;

  $("#detalleMain").innerHTML = `
    <div class="detail__cover">
      <img src="${imgSrc}" alt="${curso.titulo}" class="detail__cover-img">
    </div>
    <span class="category-badge">${cat ? cat.nombre : "Sin categoría"}</span>
    <span class="level-badge ${levelClass(curso.nivel)}" style="margin-left:8px">${curso.nivel}</span>
    <h1>${curso.titulo}</h1>
    <p class="lead">${curso.descripcion}</p>
    <ul class="info-list">
      <li><small>Categoría</small><strong>${cat ? cat.nombre : "—"}</strong></li>
      <li><small>Nivel</small><strong>${curso.nivel}</strong></li>
      <li><small>Duración</small><strong>${curso.duracion_horas} horas</strong></li>
      <li><small>Precio</small><strong>${formatPrice(curso.precio)}</strong></li>
    </ul>`;

  $("#detalleSide").innerHTML = instr
    ? `
      <div class="instructor-card">
        <span class="avatar avatar--lg">${iniciales(instr.nombre)}</span>
        <h3>${instr.nombre}</h3>
        <p>${instr.especialidad}</p>
        <p>${instr.anios_experiencia} años de experiencia</p>
        <a class="btn" href="mailto:${instr.email}">Contactar al instructor</a>
      </div>`
    : `<div class="empty"><p>Sin instructor asignado.</p></div>`;

  const relacionados = data.cursos
    .filter((c) => c.categoria_id === curso.categoria_id && c.id !== curso.id)
    .slice(0, 3);

  $("#relacionados").innerHTML = relacionados.length
    ? `<div class="grid">${relacionados.map(cardHTML).join("")}</div>`
    : `<p style="color:var(--muted)">No hay otros cursos en esta categoría.</p>`;
}

async function initDetail() {
  const params = new URLSearchParams(window.location.search);
  const id = Number(params.get("id"));
  const curso = data.cursos.find((c) => c.id === id);

  if (!curso) {
    $("#detalleMain").innerHTML = `<div class="empty">
      <h3>Curso no encontrado</h3>
      <p>El curso que buscas no existe o el enlace es incorrecto.</p>
      <a class="btn" href="index.html" style="margin-top:14px;display:inline-block">Volver al inicio</a>
    </div>`;
    return;
  }

  renderDetalle(curso);
}

/* ---------- Arranque ---------- */

document.addEventListener("DOMContentLoaded", async () => {
  const ok = await loadData();
  if (!ok) {
    showDataError();
    return;
  }
  if (document.body.dataset.page === "detalle") {
    initDetail();
  } else {
    initIndex();
  }
});