# Project Structure - Restructured Files

## Overview
The original monolithic `dr-madhavi-retina-v2.html` file has been restructured into a modern, organized file structure following best practices for code separation and maintainability.

## Directory Structure

```
Dr-Madhavi-Retina-Eye-Care/
├── index.html              # Main HTML file (entry point)
├── css/
│   └── styles.css          # All CSS styles
├── js/
│   └── script.js           # All JavaScript functionality
├── dr-madhavi-retina-v2.html  # Original file (can be deleted)
└── README.md               # This file
```

## File Descriptions

### 1. **index.html** (Main HTML File)
- **Purpose:** Contains all HTML structure and content
- **Size:** ~35KB (clean, readable markup)
- **Key Features:**
  - Meta tags for SEO and social media sharing
  - Semantic HTML5 structure
  - References to external CSS and JavaScript files
  - Four main page sections: Home, Doctor Profile, Services, and Contact
  - Responsive layout with mobile navigation

**Usage:** Open this file in a browser or serve via web server

### 2. **css/styles.css** (Stylesheet)
- **Purpose:** All styling and layout rules
- **Size:** ~40KB
- **Key Features:**
  - CSS custom properties (variables) for consistent theming
  - Mobile-first responsive design
  - Smooth animations and transitions
  - Comprehensive styling for:
    - Navigation and menus
    - Hero sections
    - Cards and service listings
    - Forms and contact information
    - Footer and floating widgets
  - Breakpoints for tablet (1000px) and mobile (640px)

**Color Scheme:**
- Primary: Teal (#0d8fa0)
- Secondary: Dark Teal (#086475)
- Light Teal: #14b8ce
- Neutral: Various shades of gray

**Fonts:**
- Headings: Playfair Display (serif)
- Body: Inter (sans-serif)

### 3. **js/script.js** (JavaScript)
- **Purpose:** All interactive functionality
- **Size:** ~2KB
- **Key Features:**
  - Page routing system (show() function)
  - Mobile hamburger menu toggle
  - Navigation scroll effects
  - Intersection Observer for fade-in animations
  - Form submission handling
  - Dynamic page titles
  - Date input validation

**Main Functions:**
- `show(page)` - Switches between pages (home, doctor, services, contact)
- `toggleMenu()` - Opens/closes mobile menu
- `submitForm()` - Handles appointment form submission
- `initObs()` - Initializes fade-in animations on page load

## Benefits of Restructuring

✅ **Separation of Concerns** - HTML, CSS, and JS in separate files
✅ **Maintainability** - Easier to locate and modify specific code
✅ **Reusability** - CSS and JS can be applied to other projects
✅ **Performance** - Browsers can cache static files independently
✅ **Scalability** - Easy to add more pages or components
✅ **Collaboration** - Multiple developers can work on different files
✅ **Testing** - Easier to test components in isolation

## How to Use

### Direct in Browser
```bash
# Simply open in a browser
Open the folder: Dr-Madhavi-Retina-Eye-Care
Double-click: index.html
```

### With a Local Web Server (Recommended)
```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (with http-server)
npx http-server

# Using VS Code Live Server
# Right-click index.html → Open with Live Server
```

Then navigate to `http://localhost:8000` in your browser.

## Navigation Structure

The website is a single-page application (SPA) with four main sections:

1. **Home** (pg-home)
   - Hero section with doctor introduction
   - Trust metrics
   - Featured services
   - About section
   - Photo gallery
   - Why choose us
   - Testimonials
   - CTA banner

2. **Doctor Profile** (pg-doctor)
   - Hero section with doctor details
   - Professional journey timeline
   - Surgical expertise grid
   - Philosophy banner

3. **Services** (pg-services)
   - Service hero section
   - Detailed service cards:
     - Diabetic Retinopathy
     - Retinal Detachment
     - Macular Diseases
     - Intravitreal Injections
     - Cataract Surgery

4. **Contact** (pg-contact)
   - Appointment request form
   - Clinic information card
   - Google Maps embed
   - WhatsApp and call buttons

## Customization Guide

### Change Colors
Edit CSS variables in `css/styles.css`:
```css
:root {
  --teal: #0d8fa0;        /* Primary color */
  --teal-dk: #086475;     /* Dark variant */
  --teal-lt: #14b8ce;     /* Light variant */
  /* ... other colors ... */
}
```

### Modify Content
Edit the HTML in `index.html` directly. Sections are clearly marked with comments.

### Add New Page
1. Create new page div with `class="pg"` and unique `id`
2. Add navigation link pointing to the new page
3. Add case in the `titles` object within `show()` function in `script.js`

### Change Fonts
Edit font links in `index.html` `<head>`:
```html
<link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
```

Then update CSS variable in `styles.css`:
```css
h1,h2,h3,h4{font-family:'New Font',serif;}
body{font-family:'New Font',sans-serif;}
```

## Mobile Responsiveness

The website is fully responsive with breakpoints:
- **Desktop:** Full layout (1001px+)
- **Tablet:** Adjusted grid (641px - 1000px)
- **Mobile:** Single column, stacked layout (<640px)

## Performance Tips

1. **Image Optimization:** Replace placeholder Unsplash images with optimized local images
2. **Lazy Loading:** Images use `loading="lazy"` attribute
3. **Caching:** Static files (CSS, JS) can be cached by browsers
4. **Minification:** Minify CSS and JS for production using tools like:
   - CSS: cssnano, clean-css
   - JS: terser, uglify-js

## Browser Support

- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

Supported CSS features:
- CSS Grid
- CSS Flexbox
- CSS Custom Properties
- Backdrop Filter
- CSS Animations

## Deployment

This is a static website. Deploy to:
- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront
- Traditional web hosting

Simply upload all files maintaining the directory structure.

## Original File

The original `dr-madhavi-retina-v2.html` file is still present for reference and can be deleted once you've verified everything works correctly.

---

**Last Updated:** April 2025
**Structure Version:** 2.0
