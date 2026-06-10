# Portfolio Website - Syefdi Fasmawi Syaban

Personal portfolio website showcasing my work as a Junior QA Tester and developer. Built with vanilla HTML, CSS, and JavaScript - no frameworks, just clean and performant code.

**Live Site**: [syefdi.github.io](https://syefdi.github.io) 

## About Me

I'm a 19-year-old QA Tester based in South Jakarta, currently working at CV Gemilang Inti Teknologi while studying Informatics Engineering at Universitas Pamulang on weekends. My work involves testing enterprise web systems, writing detailed bug reports, and occasionally contributing to development work.

## Features

### Core Sections
- **About**: Brief introduction, education history, and current learning focus
- **Experience**: Detailed work history with quantifiable achievements
- **Projects**: 5 enterprise projects I've worked on, with interactive modals for detailed information
- **Skills**: Technical skills organized by Testing & QA, and Tools & Workflow
- **Certifications**: Courses and credentials from Dicoding and AWS
- **Contact**: Multiple ways to reach me

### UI/UX Features
- **Dark/Light Theme Toggle**: Persistent theme preference with smooth transitions
- **Project Modals**: Click any project card to see detailed information in a modal
- **Smooth Animations**: Hover effects on cards, scroll animations, fade-in sections
- **Back to Top Button**: Appears after scrolling 300px
- **Responsive Design**: Mobile-first approach with hamburger menu for small screens
- **Cursor Spotlight Effect**: Subtle radial gradient follows cursor on desktop
- **Scroll Progress Bar**: Visual indicator at top of page

### Technical Implementation
- **No Framework Dependencies**: Pure HTML, CSS, JavaScript
- **Theme System**: CSS custom properties with localStorage persistence
- **Intersection Observer**: For scroll-triggered animations
- **Modal System**: Reusable modal component for project details
- **SEO Optimized**: Meta tags for search engines and social sharing
- **Accessible**: Semantic HTML, ARIA labels, keyboard navigation support

## Project Structure

```
portfolio/
├── assets/
│   ├── documents/
│   │   └── resume.pdf           # Downloadable resume
│   └── images/
│       └── SyefdiSyaban-IMG.png # Profile Picture
├── scripts/
│   └── generate_cv.py           # CV generation utility
├── index.html                   # Main HTML file (all-in-one)
└── README.md                    # This file
```

## Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Custom properties, grid, flexbox, animations
- **JavaScript (ES6+)**: Intersection Observer, localStorage, DOM manipulation
- **Fonts**: Plus Jakarta Sans (body), Fira Code (monospace)

## Color Scheme

### Light Mode
- Background: `#fafafa`
- Card Background: `#ffffff`
- Primary Text: `#0f172a`
- Accent: `#0ea5e9`

### Dark Mode
- Background: `#0f172a`
- Card Background: `#1e293b`
- Primary Text: `#f1f5f9`
- Accent: `#38bdf8`

## Key Design Decisions

### Why No Framework?
This portfolio intentionally uses vanilla JavaScript to demonstrate:
- Understanding of web fundamentals
- Ability to write clean, performant code without dependencies
- Knowledge of modern browser APIs
- Performance optimization (no bundle overhead)

### Single HTML File
The entire website is contained in one HTML file with embedded CSS and JavaScript:
- **Pros**: Simple deployment, no build process, fast initial load
- **Cons**: Harder to maintain at scale (not an issue for a portfolio)

### Theme Inspiration
Design inspired by [brittanychiang.com](https://brittanychiang.com) - clean, minimal, developer-focused aesthetic.

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/Syefdi/Syefdi.github.io.git
cd Syefdi.github.io
```

2. Open with a local server (to avoid CORS issues):
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (if you have http-server installed)
npx http-server

# VS Code Live Server
# Install "Live Server" extension and click "Go Live"
```

3. Visit `http://localhost:8000` in your browser

## Deployment

This portfolio is deployed on GitHub Pages:

1. Push changes to main branch
2. GitHub Pages automatically deploys from main branch
3. Site is live at `https://syefdi.github.io`

No build process required - just push and deploy.

## Browser Support

- Chrome/Edge (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Mobile browsers (iOS Safari, Chrome Android)

**Note**: Uses modern CSS features like CSS Grid, Custom Properties, and Intersection Observer. No IE11 support.

## Performance

- **Lighthouse Score**: 95+ (Performance, Accessibility, Best Practices, SEO)
- **No external dependencies**: Zero npm packages
- **Inline CSS/JS**: No separate file requests
- **Optimized fonts**: Google Fonts with preconnect
- **Lazy-loaded sections**: Intersection Observer for scroll animations

## Customization Guide

Want to use this as a template? Here's what to change:

### Personal Information
1. Update meta tags in `<head>` (lines 5-22)
2. Change name, tagline, and availability in sidebar (lines 1257-1263)
3. Update about section text (lines 1528-1534)
4. Modify education cards (lines 1536-1560)
5. Replace experience bullet points (lines 1584-1589)
6. Update project cards and modal data (lines 1611-1695, 2044-2099)

### Contact Information
1. Update email links (search for `syefdifasmawi@gmail.com`)
2. Change WhatsApp number (search for `6282123439121`)
3. Update LinkedIn URL (search for `syefdi-fasmawi-syaban`)
4. Update GitHub username (search for `Syefdi`)

### Resume
Replace `assets/documents/resume.pdf` with your own resume file.

### Colors
Modify CSS custom properties in `:root` (lines 33-49) and `[data-theme="dark"]` (lines 51-67).

## Known Issues

None currently. If you find a bug, please open an issue.

## Future Enhancements

Potential features to add:
- [ ] Blog section for writing about QA and testing
- [ ] Animations with more polish
- [ ] More project case studies with detailed breakdowns
- [ ] Testimonials section
- [ ] Download resume button analytics

## License

This project is open source and available under the [MIT License](LICENSE).

Feel free to use this as inspiration or a template for your own portfolio. If you do use it, a link back to this repo would be appreciated but is not required.

## Contact

- **Email**: syefdifasmawi@gmail.com
- **LinkedIn**: [linkedin.com/in/syefdi-fasmawi-syaban](https://www.linkedin.com/in/syefdi-fasmawi-syaban-6b6531337/)
- **GitHub**: [github.com/Syefdi](https://github.com/Syefdi)
- **WhatsApp**: +62 821-2343-9121

---

**Built by Syefdi Fasmawi Syaban**

Last updated: June 2026
