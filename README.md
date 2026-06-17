# Personal Portfolio

Modern, responsive portfolio website showcasing my work as a Junior QA Tester and my journey in software development. Features both a visual portfolio and terminal-style interface.

## Features

- Clean, modern design with dark/light theme support
- Responsive layout for all devices
- Terminal mode for a command-line experience
- Smooth animations and transitions
- SEO optimized with Open Graph tags
- Fast loading with optimized assets

## Project Structure

```
1portfolio/
├── index.html              # Main portfolio page
├── terminal.html           # Terminal-style portfolio interface
├── README.md               # Project documentation
├── PRODUCT.md              # Product strategy and brand guidelines
├── DESIGN.md               # Design system documentation
├── .gitignore              # Git ignore rules
│
├── css/                    # Stylesheets
│   ├── main.css           # Main stylesheet
│   └── terminal.css       # Terminal-specific styles
│
├── js/                     # JavaScript modules
│   ├── main.js            # Main application logic
│   └── terminal.js        # Terminal functionality
│
├── assets/                 # Static assets
│   ├── documents/         # Resume and other documents
│   └── images/            # Profile photos and images
│
├── tools/                  # Development and maintenance scripts
│   ├── refactor.py        # Build script for extracting CSS/JS
│   ├── build_new_index.py # Script to rebuild clean HTML
│   ├── generate_cv.py     # CV generation utility
│   └── ...                # Other utility scripts
│
├── .impeccable/            # Design system tooling (generated)
│   ├── design.json        # Design tokens and component library
│   ├── live/              # Live mode configuration
│   └── critique/          # UX critique snapshots
│
├── .backups/               # Backup files (not tracked in git)
│   └── index.html.backup  # Original monolithic version
│
└── node_modules/           # Dependencies (not tracked in git)
    └── @playwright/        # Testing framework
```

## Tech Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS variables
- **Vanilla JavaScript** - No frameworks, pure JS
- **Google Fonts** - Plus Jakarta Sans & Fira Code
- **Devicons** - Technology icons

## Local Development

1. Clone the repository
2. Open `index.html` in a browser
3. No build process required - pure HTML/CSS/JS

For the terminal mode:
- Open `terminal.html` directly, or
- Click the "Terminal" button in the main portfolio

## Theme System

The portfolio supports automatic dark/light theme switching based on system preferences, with manual toggle available. Theme preference is saved to localStorage.

**Theme CSS Variables:**
- `--bg-primary`, `--bg-secondary`, `--bg-card`
- `--accent`, `--accent-light`, `--accent-dark`
- `--text-primary`, `--text-secondary`, `--text-dim`
- `--border`, `--shadow-sm`, `--shadow-md`, `--shadow-lg`

## Terminal Mode

Interactive terminal interface with command-line navigation:

**Available Commands:**
- `whoami` - Who is Syefdi
- `about` - Background and current status
- `skills` - Technical skills and tools
- `experience` - Work experience
- `education` - Education background
- `projects` - Personal and work projects
- `certifications` - Courses and credentials
- `contact` - Contact information
- `cv` - Download resume
- `clear` - Clear terminal
- `help` - Show help message

**Easter Eggs:**
- `secret` - Hidden message
- `sudo` - Permission denied
- `rm -rf /` - Nice try
- `matrix` - Matrix rain effect
- `quote` - Random dev quotes

**Features:**
- Tab autocomplete for commands
- Command history with arrow keys
- Typing animation (25ms per character)
- Queue system for concurrent commands
- Blinking cursor that follows input

## Sections

### About
Personal introduction, current status, and education background. Includes profile photo and availability status.

### Experience
Timeline of work experience at CV Gemilang Inti Teknologi with detailed responsibilities and achievements.

### Projects
Showcase of 6 projects with role badges (QA, Dev, Build), descriptions, and live links:
1. ERM System
2. CRM System
3. Document Management System
4. HRIS / Attendance System
5. PD System
6. Bug Report Management Tool

### Skills
Grouped skills display:
- Testing & QA methodologies
- Tools & Workflow (with icons)
- Currently Learning tags

### Certifications
List of completed courses from Dicoding and AWS with verification links.

### Contact
Multiple contact methods with hover effects and direct links.

## Responsive Design

- **Desktop (>1024px)**: Fixed sidebar with navigation
- **Tablet (768px-1024px)**: Adjusted spacing and font sizes
- **Mobile (<768px)**: Hamburger menu, stacked layout

## Performance Optimizations

- CSS and JS separated into external files
- Font preconnect for faster loading
- Lazy loading for images
- Minimal external dependencies
- FOUC prevention with inline theme script

## Deployment

### GitHub Pages
1. Push to GitHub repository
2. Enable GitHub Pages in Settings
3. Select branch and root directory
4. Access via `username.github.io`

### Custom Domain
1. Add CNAME file with your domain
2. Configure DNS A records to GitHub IPs
3. Enable HTTPS in repository settings

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Maintenance

### Adding New Projects
Edit `index.html`, add project card in the Projects section with appropriate badges.

### Updating Certifications
Add new cert-card in the Certifications section with verification link.

### Modifying Styles
Edit `css/main.css` - all styles use CSS variables for easy theming.

### Terminal Commands
Edit `terminal.js` - add new commands to the `commands` object.

## File Size Stats

- **index.html**: 587 lines (down from 2295 lines - 74% reduction!)
- **css/main.css**: 1410 lines
- **js/main.js**: 2258 lines
- **Total**: ~4,255 lines (well-structured and modular)

## Development Files

### Tools Directory
Contains Python scripts for maintenance and development:
- **refactor.py**: Extract CSS/JS from inline HTML
- **build_new_index.py**: Rebuild clean HTML structure
- **generate_cv.py**: Generate resume in various formats
- **clean_files.py**: Cleanup and formatting utilities

### Backups Directory
Original files stored in `.backups/` (gitignored):
- `index.html.backup`: Original monolithic version for reference

### Design System
Portfolio uses the Impeccable design system:
- **PRODUCT.md**: Brand strategy, anti-references, design principles
- **DESIGN.md**: Complete visual system with color palette, typography, components
- **.impeccable/**: Generated design tokens and critique snapshots

## License

Personal portfolio project. Feel free to use as inspiration for your own portfolio.

## Contact

- Email: syefdifasmawi@gmail.com
- GitHub: github.com/Syefdi
- LinkedIn: linkedin.com/in/syefdi-fasmawi-syaban-6b6531337
- Portfolio: syefdi.github.io
