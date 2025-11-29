document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    document.querySelectorAll('button[type="submit"]').forEach(button => {
        button.addEventListener('click', function() {
            if (this.form && this.form.checkValidity()) {
                this.classList.add('loading');
            }
        });
    });

    function animateNeuralNetwork() {
        const nodes = document.querySelectorAll('.node');
        if (nodes.length === 0) return;

        setInterval(() => {
            nodes.forEach(node => {
                if (Math.random() > 0.7) {
                    node.classList.toggle('active');
                }
            });
        }, 1000);
    }
    animateNeuralNetwork();

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.feature-card, .step, .tech-card').forEach(el => {
        observer.observe(el);
    });

    let performanceMetrics = {
        pageLoadTime: performance.now(),
        interactions: 0
    };

    document.addEventListener('click', function() {
        performanceMetrics.interactions++;
    });

    console.log('TruthGuard 2025 - Fake News Detection System');
    console.log('Performance Metrics:', performanceMetrics);
});

const Utils = {
    formatPercent: (value) => {
        return (value * 100).toFixed(1) + '%';
    },

    formatTime: (seconds) => {
        return seconds.toFixed(2) + 's';
    },

    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    validateText: (text, minLength = 50) => {
        return text.trim().length >= minLength;
    }
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { Utils };
}