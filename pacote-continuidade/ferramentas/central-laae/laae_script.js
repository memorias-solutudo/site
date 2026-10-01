<script>
  var itemLast = null;
  function openItem(key, el){
    var src = document.getElementById('if-' + key);
    if(!src) return;
    itemLast = el || null;
    var dw = document.getElementById('dw');
    dw.innerHTML = '<div class="dw-top"><h3 id="dw-title">' + src.dataset.title + '</h3>' +
      '<button class="dw-close" onclick="closeItem()" aria-label="Fechar ficha do item">✕</button></div>' +
      '<div class="dw-body">' + src.innerHTML + '</div>';
    dw.classList.add('on');
    document.getElementById('dw-back').classList.add('on');
    document.body.style.overflow = 'hidden';
    var b = dw.querySelector('.dw-close'); if(b) b.focus();
  }
  function closeItem(){
    var dw = document.getElementById('dw'); if(!dw) return;
    dw.classList.remove('on');
    document.getElementById('dw-back').classList.remove('on');
    document.body.style.overflow = '';
    if(itemLast){ itemLast.focus(); itemLast = null; }
  }
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){
      var dw = document.getElementById('dw');
      if(dw && dw.classList.contains('on')) closeItem();
    }
  });
  function show(which, keep){
    ['parc','dest','site','gmb','soc','cont'].forEach(function(k){
      document.getElementById('p-'+k).classList.toggle('on', which===k);
      document.getElementById('t-'+k).classList.toggle('on', which===k);
    });
    closeItem();
    history.replaceState(null,'','#'+which);
    if(!keep) window.scrollTo({top:0,behavior:'smooth'});
  }
  function tbh(){ var t = document.querySelector('.topbar'); if(t) document.documentElement.style.setProperty('--tbh', t.offsetHeight + 'px'); }
  tbh(); window.addEventListener('resize', tbh);
  function panelOf(el){ var p = el && el.closest('.panel'); return p ? p.id.replace('p-','') : null; }
  function goSec(id){
    var el = document.getElementById(id); if(!el) return false;
    show(panelOf(el) || 'cont', true);
    setTimeout(function(){ el.scrollIntoView({behavior:'smooth', block:'start'}); history.replaceState(null,'','#'+id); }, 30);
    return false;
  }
  function copyPrompt(btn){ copyBlock(btn, 'prompt-text', 'Copiar o prompt'); }
  function copyBlock(btn, id, label){
    var t = document.getElementById(id).textContent;
    function ok(){ btn.textContent = 'Copiado ✓'; setTimeout(function(){ btn.textContent = label; }, 2200); }
    function fallback(){
      var ta = document.createElement('textarea'); ta.value = t; ta.setAttribute('readonly',''); ta.style.position = 'fixed'; ta.style.left = '-9999px';
      document.body.appendChild(ta); ta.select();
      try{ document.execCommand('copy'); ok(); }catch(e){}
      document.body.removeChild(ta);
    }
    if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(t).then(ok, fallback); } else { fallback(); }
  }
  (function(){
    if(!('IntersectionObserver' in window)) return;
    // um observador por aba com menu lateral (Solusite e Conteúdo)
    [].slice.call(document.querySelectorAll('.cont-layout')).forEach(function(lay){
      var menu = lay.querySelector('.cont-menu');
      var links = [].slice.call(lay.querySelectorAll('.cm-i'));
      var secs = [].slice.call(lay.querySelectorAll('.csec'));
      if(!secs.length) return;
      var io = new IntersectionObserver(function(es){
        es.forEach(function(e){
          if(!e.isIntersecting) return;
          var id = e.target.id;
          links.forEach(function(l){ l.classList.toggle('on', l.getAttribute('href') === '#' + id); });
          // no celular o menu é uma faixa horizontal: traz o chip ativo para a vista
          var on = menu && menu.querySelector('.cm-i.on');
          if(on && getComputedStyle(menu).flexDirection === 'row'){ menu.scrollTo({left: Math.max(0, on.offsetLeft - 12), behavior:'smooth'}); }
        });
      }, {rootMargin:'-25% 0px -65% 0px', threshold:0});
      secs.forEach(function(x){ io.observe(x); });
    });
  })();
  var h = location.hash.replace('#','');
  if(['dest','site','gmb','soc','cont'].indexOf(h) >= 0) show(h);
  else if(h && document.getElementById(h) && document.getElementById(h).classList.contains('csec')){
    show(panelOf(document.getElementById(h)) || 'cont', true);
    var jump = function(){ var el = document.getElementById(h); if(!el) return; var de = document.documentElement, prev = de.style.scrollBehavior; de.style.scrollBehavior = 'auto'; el.scrollIntoView({block:'start'}); de.style.scrollBehavior = prev; };
    setTimeout(jump, 50);
    // a página muda de altura enquanto a fonte e as imagens carregam: repete o salto a cada mudança,
    // por até 3 s, e para na primeira interação do leitor
    var ro = null;
    var stop = function(){ if(ro){ ro.disconnect(); ro = null; } };
    if('ResizeObserver' in window){
      ro = new ResizeObserver(function(){ jump(); });
      ro.observe(document.body);
      setTimeout(stop, 3000);
      ['wheel','touchstart','keydown'].forEach(function(ev){ window.addEventListener(ev, stop, {passive:true, once:true}); });
    }
  }
</script>