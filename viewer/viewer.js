document.addEventListener('DOMContentLoaded', () => {
  // Tab switching
  const tabs = document.querySelectorAll('.tab-btn');
  const panels = document.querySelectorAll('.view-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      const target = document.getElementById(tab.dataset.target);
      if (target) target.classList.add('active');
    });
  });

  // T-Shirt person toggle (Prince vs Kenneth)
  const shirtSelect = document.getElementById('shirtPersonSelect');
  const shirtImg = document.getElementById('shirtPreviewImg');
  if (shirtSelect && shirtImg) {
    shirtSelect.addEventListener('change', (e) => {
      if (e.target.value === 'prince') {
        shirtImg.src = '../designs/shirts/shirt-prince.svg';
      } else {
        shirtImg.src = '../designs/shirts/shirt-kenneth.svg';
      }
    });
  }

  // Zoom controls for Banner
  let bannerZoom = 1;
  const bannerImg = document.getElementById('bannerPreviewImg');
  const zoomInBtn = document.getElementById('bannerZoomIn');
  const zoomOutBtn = document.getElementById('bannerZoomOut');
  const zoomResetBtn = document.getElementById('bannerZoomReset');

  if (zoomInBtn && bannerImg) {
    zoomInBtn.addEventListener('click', () => {
      bannerZoom = Math.min(bannerZoom + 0.2, 2.5);
      bannerImg.style.transform = `scale(${bannerZoom})`;
    });
    zoomOutBtn.addEventListener('click', () => {
      bannerZoom = Math.max(bannerZoom - 0.2, 0.5);
      bannerImg.style.transform = `scale(${bannerZoom})`;
    });
    zoomResetBtn.addEventListener('click', () => {
      bannerZoom = 1;
      bannerImg.style.transform = `scale(1)`;
    });
  }
});
