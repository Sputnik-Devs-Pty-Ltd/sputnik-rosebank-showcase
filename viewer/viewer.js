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
    zoomResetBtn.addEventListener('click', () => {
      bannerZoom = 1;
      bannerImg.style.transform = `scale(1)`;
    });
  }

  // Zoom controls for Tablecloth
  let tcZoom = 1;
  const tcImg = document.getElementById('tcPreviewImg');
  const tcZoomInBtn = document.getElementById('tcZoomIn');
  const tcZoomOutBtn = document.getElementById('tcZoomOut');
  const tcZoomResetBtn = document.getElementById('tcZoomReset');

  if (tcZoomInBtn && tcImg) {
    tcZoomInBtn.addEventListener('click', () => {
      tcZoom = Math.min(tcZoom + 0.25, 3.5);
      tcImg.style.transform = `scale(${tcZoom})`;
    });
    tcZoomOutBtn.addEventListener('click', () => {
      tcZoom = Math.max(tcZoom - 0.25, 0.4);
      tcImg.style.transform = `scale(${tcZoom})`;
    });
    tcZoomResetBtn.addEventListener('click', () => {
      tcZoom = 1;
      tcImg.style.transform = `scale(1)`;
    });
  }
});
