/*
 * IBYOS Design & Architecture — Custom scripts
 * Cinematic interactions and lightweight scroll behaviors
 * Author: IBYOS Design & Architecture
 */
//
// Custom scripts
//

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

    // Fallback for missing gallery images
    document.querySelectorAll('.portfolio-box img').forEach(img => {
        img.addEventListener('error', () => {
            img.style.display = 'none';
            const placeholder = document.createElement('div');
            placeholder.className = 'image-fallback';
            placeholder.textContent = 'Image unavailable';
            if (img.parentNode) {
                img.parentNode.appendChild(placeholder);
                img.parentNode.classList.add('image-missing');
                img.parentNode.style.pointerEvents = 'none';
            }
        });
    });
    
        // Cinematic reveal on scroll (IntersectionObserver)
        if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
            const revealObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('reveal-visible');
                        revealObserver.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.12 });
        
            document.querySelectorAll('.reveal, .portfolio-card, .portfolio-highlight, .service-card, .feature-card').forEach(el => {
                revealObserver.observe(el);
            });
        } else {
            // Respect reduced motion: show elements immediately
            document.querySelectorAll('.reveal, .portfolio-card, .portfolio-highlight, .service-card, .feature-card').forEach(el => {
                el.classList.add('reveal-visible');
            });
        }
    
        // Lightweight parallax for image elements with data-parallax
        const parallaxEls = Array.from(document.querySelectorAll('[data-parallax]'));
        if (parallaxEls.length && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
            let ticking = false;
            const onScroll = () => {
                if (!ticking) {
                    window.requestAnimationFrame(() => {
                        const centerY = window.innerHeight / 2;
                        parallaxEls.forEach(el => {
                            const rect = el.getBoundingClientRect();
                            const distance = (rect.top + rect.height / 2) - centerY;
                            const max = 80; // px
                            const y = Math.max(-max, Math.min(max, -distance * 0.06));
                            el.style.transform = `translate3d(0, ${y}px, 0)`;
                        });
                        ticking = false;
                    });
                    ticking = true;
                }
            };
            document.addEventListener('scroll', onScroll, { passive: true });
            onScroll();
        }

});
