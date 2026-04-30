const pages = ['dashboard', 'asistencia', 'ninos', 'metricas', 'impacto'];
const labels = { dashboard: 'Dashboard', asistencia: 'Asistencia', ninos: 'Niños', metricas: 'Métricas', impacto: 'Impacto' };
let sideOpen = false;
let profileOpen = false;

function nav(id, el) {
  pages.forEach(s => {
    document.getElementById('s-' + s).classList.remove('active');
    document.getElementById('s-' + s).classList.add('hidden');
    document.getElementById('tb-' + s).classList.add('hidden');
  });
  document.getElementById('s-' + id).classList.remove('hidden');
  document.getElementById('s-' + id).classList.add('active');
  document.getElementById('tb-' + id).classList.remove('hidden');
  document.querySelectorAll('.side-btn').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
  closeProfile();
}

function toggleSide() {
  sideOpen = !sideOpen;
  document.getElementById('side').classList.toggle('expanded', sideOpen);
  document.getElementById('togBtn').textContent = sideOpen ? '⇤' : '⇄';
  closeProfile();
}

function toggleProfile() {
  profileOpen = !profileOpen;
  const popup = document.getElementById('profilePopup');
  const logo = document.getElementById('logoBtn');
  popup.classList.toggle('show', profileOpen);
  logo.style.outline = profileOpen ? '2px solid rgba(255,255,255,0.5)' : 'none';
}

function closeProfile() {
  profileOpen = false;
  document.getElementById('profilePopup').classList.remove('show');
  document.getElementById('logoBtn').style.outline = 'none';
}

function toggleBtn(btn) {
  btn.classList.toggle('on');
  btn.classList.toggle('off');
}

document.addEventListener('click', e => {
  if (!e.target.closest('#profilePopup') && !e.target.closest('#logoBtn')) closeProfile();
});

const tip = document.getElementById('tip');
document.querySelectorAll('.side-btn').forEach(btn => {
  const id = btn.id.replace('btn-', '');
  btn.addEventListener('mouseenter', () => {
    if (sideOpen) return;
    const r = btn.getBoundingClientRect();
    tip.textContent = labels[id];
    tip.style.top = (r.top + 10) + 'px';
    tip.style.left = '66px';
    tip.classList.add('show');
  });
  btn.addEventListener('mouseleave', () => tip.classList.remove('show'));
});