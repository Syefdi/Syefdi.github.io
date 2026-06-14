// Scroll progress bar
        const scrollProgress = document.getElementById('scroll-progress');
        
        function updateScrollProgress() {
            const scrollTotal = document.documentElement.scrollHeight - window.innerHeight;
            const scrollCurrent = window.pageYOffset;
            const scrollPercentage = (scrollCurrent / scrollTotal) * 100;
            scrollProgress.style.width = scrollPercentage + '%';
        }

        window.addEventListener('scroll', updateScrollProgress);

        // Intersection Observer for sections
        const sections = document.querySelectorAll('section');
        const observerOptions = {
            threshold: 0.15,
            rootMargin: '0px 0px -100px 0px'
        };

        const sectionObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                    }, index * 100);
                }
            });
        }, observerOptions);

        sections.forEach(section => {
            sectionObserver.observe(section);
        });

        // Active nav link on scroll
        const navLinks = document.querySelectorAll('.nav-link');
        
        function updateActiveNav() {
            let current = '';
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (window.pageYOffset >= sectionTop - 200) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + current) {
                    link.classList.add('active');
                }
            });
        }

        window.addEventListener('scroll', updateActiveNav);

        // Mobile menu toggle
        const hamburger = document.getElementById('hamburger');
        const mobileMenu = document.getElementById('mobileMenu');

        if (hamburger && mobileMenu) {
            hamburger.addEventListener('click', () => {
                mobileMenu.classList.toggle('active');
                document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
            });

            // Close mobile menu when clicking a link
            const mobileMenuLinks = mobileMenu.querySelectorAll('a');
            mobileMenuLinks.forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.remove('active');
                    document.body.style.overflow = '';
                });
            });
        }

        // Smooth scroll for all links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    const offset = window.innerWidth > 1024 ? 0 : 80;
                    const targetPosition = target.offsetTop - offset;
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Cursor spotlight effect (desktop only)
        if (window.matchMedia('(hover: hover)').matches) {
            document.body.classList.add('has-spotlight');
            document.addEventListener('mousemove', (e) => {
                document.documentElement.style.setProperty('--mouse-x', e.clientX + 'px');
                document.documentElement.style.setProperty('--mouse-y', e.clientY + 'px');
            });
        }

        // Theme Toggle Logic
        const themeToggle = document.getElementById('theme-toggle');

        function getTheme() {
            const storedTheme = localStorage.getItem('theme');
            if (storedTheme) {
                return storedTheme;
            }
            return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        }

        function setTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
        }

        function toggleTheme() {
            const currentTheme = getTheme();
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            setTheme(newTheme);
        }

        // Attach event listener to the floating toggle button
        if (themeToggle) {
            themeToggle.addEventListener('click', toggleTheme);
        }

        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            if (!localStorage.getItem('theme')) {
                setTheme(e.matches ? 'dark' : 'light');
            }
        });

        // Back to Top Button
        const backToTop = document.getElementById('back-to-top');
        
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        // Project Modal
        const projectData = {
            'ERM System': {
                title: 'ERM System',
                company: 'CV Gemilang Inti Teknologi',
                client: 'PT ABM Investama',
                role: 'QA, Build',
                description: 'Enterprise Resource Management system built for PT ABM Investama. The system was undergoing a major revamp while the legacy production version was still actively used. I handled QA on both tracks simultaneously, running functional and regression tests on each weekly release to make sure neither version broke during the transition period. This involved coordinating with the development team to understand changes in both versions, writing test cases that covered overlapping functionality, and ensuring feature parity where needed. The dual-track approach meant I had to context-switch between two different codebases regularly and validate that fixes applied to one version did not introduce regressions in the other.',
                link: 'https://erm.gemilangteknologi.com/',
                linkText: 'View Live',
                linkType: 'live'
            },
            'CRM System': {
                title: 'CRM System',
                company: 'CV Gemilang Inti Teknologi',
                client: null,
                role: 'QA, Dev, Build',
                description: 'Customer Relationship Management platform handling live client data for CV Gemilang Inti Teknologi. Beyond regular QA cycles, I had direct write access to the production system and handled minor fixes when issues were caught outside of testing hours. Also involved in parts of the build process alongside the dev team. My role on this project extended beyond standard QA work because the team was small and needed someone who could both test and implement fixes quickly without waiting for a full development cycle. This meant I spent time reading the codebase, understanding the database schema, and making small updates to frontend logic or backend validation rules when bugs were straightforward enough to fix on the spot.',
                link: 'https://crms.gemilangteknologi.com/',
                linkText: 'View Live',
                linkType: 'live'
            },
            'Document Management System': {
                title: 'Document Management System',
                company: 'CV Gemilang Inti Teknologi',
                client: null,
                role: 'Dev, Build',
                description: 'Web-based document management solution built internally at CV Gemilang Inti Teknologi. I was involved from early stages, contributing to parts of the codebase and the build process. This project leaned more toward development than QA compared to the others. I worked on implementing file upload logic, building out the folder structure UI, and setting up permission checks for document access. Since this was an internal tool and the requirements were relatively clear from the start, the focus was less on extensive testing and more on building features that worked correctly from the beginning. I still ran basic QA checks, but my time was mostly spent writing code rather than writing test cases.',
                link: 'https://github.com/Syefdi/Document_Management_System',
                linkText: 'View on GitHub',
                linkType: 'github'
            },
            'HRIS / Attendance System': {
                title: 'HRIS / Attendance System',
                company: 'CV Gemilang Inti Teknologi',
                client: 'PT Inti Power Abadi',
                role: 'QA, Dev',
                description: 'Web-based employee attendance tracking application built for PT Inti Power Abadi. I joined during early development, establishing functional test coverage for core workflows and edge cases before the first production deployment. The system needed to handle different types of attendance records like clock-in, clock-out, leave requests, and overtime tracking. My job was to make sure all these flows worked correctly and that edge cases like duplicate clock-ins or missing clock-outs were handled properly. I also contributed small fixes when I found bugs that were simple enough to patch myself rather than handing them back to the dev team. This helped speed up the QA cycle since I could verify fixes immediately after making them.',
                link: 'https://absensi.intipowerabadi.com/',
                linkText: 'View Live',
                linkType: 'live'
            },
            'PD System': {
                title: 'PD System',
                company: 'CV Gemilang Inti Teknologi',
                client: 'PT Kencana Zavira',
                role: 'QA, Dev',
                description: 'Internal management dashboard built for PT Kencana Zavira. Contributed to minor development work and ran QA checks to validate features before the system went live. Shorter engagement than the others but involved on both the dev and testing side. The dashboard was used to track internal operations and generate reports, so accuracy was critical. I worked on validating data flows, making sure reports showed correct numbers, and implementing small UI tweaks based on feedback from the client during demos. Since the timeline was tight, I handled both building features and testing them rather than waiting for a separate QA phase. This required staying organized and making sure I did not skip testing steps even when switching between development and QA modes.',
                link: 'https://pds.kencana-zavira.com/',
                linkText: 'View Live',
                linkType: 'live'
            }
        };

        const modal = document.getElementById('projectModal');
        const modalClose = document.getElementById('modalClose');
        const projectCards = document.querySelectorAll('.project-card');

        function openModal(projectTitle) {
            const data = projectData[projectTitle];
            if (!data) return;

            // Set modal title
            document.getElementById('modalTitle').textContent = data.title;

            // Build info grid
            const infoGrid = document.getElementById('modalInfoGrid');
            infoGrid.innerHTML = '';

            // Add Company
            infoGrid.innerHTML += `
                <div class="modal-info-label">Company</div>
                <div class="modal-info-value">${data.company}</div>
            `;

            // Add Client if exists
            if (data.client) {
                infoGrid.innerHTML += `
                    <div class="modal-info-label">Client</div>
                    <div class="modal-info-value">${data.client}</div>
                `;
            }

            // Add Role
            infoGrid.innerHTML += `
                <div class="modal-info-label">Role</div>
                <div class="modal-info-value">${data.role}</div>
            `;

            // Set description
            document.getElementById('modalDescription').textContent = data.description;

            // Set link
            const footerContainer = document.getElementById('modalFooter');
            footerContainer.innerHTML = `
                <a href="${data.link}" class="modal-link ${data.linkType}" target="_blank" rel="noopener noreferrer">
                    <span>${data.linkText}</span>
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/>
                        <polyline points="15 3 21 3 21 9"/>
                        <line x1="10" y1="14" x2="21" y2="3"/>
                    </svg>
                </a>
            `;

            // Show modal
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Add click handlers to project cards
        projectCards.forEach(card => {
            card.addEventListener('click', (e) => {
                // Don't open modal if clicking on a link
                if (e.target.closest('a')) return;
                
                const title = card.querySelector('h3').textContent;
                openModal(title);
            });
        });

        // Close modal handlers
        modalClose.addEventListener('click', closeModal);
        
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeModal();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                closeModal();
            }
        });

        // Initial calls
        updateScrollProgress();
        updateActiveNav();