// ═════════════════════════════════════════
// DR. MADHAVI RETINA EYE CARE
// MAIN JAVASCRIPT
// ═════════════════════════════════════════

// ── PAGE ROUTING ──
function show(p){
  document.querySelectorAll('.pg').forEach(s=>s.classList.remove('on'));
  document.querySelectorAll('.nlinks a').forEach(a=>a.classList.remove('act'));
  document.getElementById('pg-'+p).classList.add('on');
  const nl=document.getElementById('nav-'+p);
  if(nl)nl.classList.add('act');
  window.scrollTo({top:0,behavior:'smooth'});
  initObs();
  const titles={
    home:'Dr. Madhavi Retina Eye Care | Retina Specialist Tirupati',
    doctor:'Dr. V. Madhavi – Retina Specialist Tirupati',
    services:'Retina Services Tirupati | Diabetic Retinopathy & Laser',
    contact:'Book Appointment | Dr. Madhavi Retina Eye Care Tirupati'
  };
  document.title=titles[p]||document.title;
}

// ── HAMBURGER MENU ──
function toggleMenu(){
  document.getElementById('ham').classList.toggle('open');
  document.getElementById('mmenu').classList.toggle('open');
}

// Close menu when clicking outside
document.addEventListener('click',e=>{
  const m=document.getElementById('mmenu'),h=document.getElementById('ham');
  if(m.classList.contains('open')&&!m.contains(e.target)&&!h.contains(e.target)){
    m.classList.remove('open');
    h.classList.remove('open');
  }
});

// ── NAV SCROLL EFFECT ──
window.addEventListener('scroll',()=>{
  document.getElementById('mainNav').classList.toggle('scrolled',scrollY>20);
});

// ── INTERSECTION OBSERVER FOR FADE-IN ANIMATIONS ──
function initObs(){
  const items=document.querySelectorAll('.pg.on .fade');
  const obs=new IntersectionObserver((entries)=>{
    entries.forEach((e,i)=>{
      if(e.isIntersecting){
        setTimeout(()=>e.target.classList.add('vis'),i*70);
        obs.unobserve(e.target);
      }
    });
  },{threshold:.1});
  items.forEach(el=>obs.observe(el));
}

// ── FORM SUBMISSION ──
document.getElementById('submit-request').addEventListener('click', () => {
  const n=document.getElementById('fn').value.trim(),
        p=document.getElementById('fp').value.trim(),
        d=document.getElementById('fd').value.trim();
  
  if(!n||!p){
    alert('Please enter your name and phone number.');
    return;
  }
  
  // Build WhatsApp message
  const lines = [
    '*New Appointment Request*',
    '━━━━━━━━━━━━━━━━━━━━',
    `Name: ${n}`,
    `Phone: ${p}`,
    d    ? `Preferred Date: ${d}` : '',
    '━━━━━━━━━━━━━━━━━━━━'
  ].filter(Boolean).join('\n');

  // Open WhatsApp with pre-filled message to clinic number
  const waURL = 'https://wa.me/917075442266?text=' + encodeURIComponent(lines);
  window.open(waURL, '_blank');
  
  // Show success message
  const s=document.getElementById('fsucc');
  s.style.display='block';
  
  // Clear form fields
  ['fn','fp','fd'].forEach(id=>document.getElementById(id).value='');
  
  // Hide success message after 8 seconds
  setTimeout(()=>s.style.display='none',8000);
});

// ── INITIALIZATION ──
document.addEventListener('DOMContentLoaded',()=>{
  // Initialize fade-in observer
  initObs();
  
  // Set minimum date for appointment form to today
  const d=document.getElementById('fd');
  if(d)d.min=new Date().toISOString().split('T')[0];
});
