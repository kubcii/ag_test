# 🚀 Quick Deployment Guide

## **Fastest & Cheapest Options:**

### 1. **GitHub Pages (Recommended) - FREE & 5 minutes**

**Steps:**
1. Go to [GitHub.com](https://github.com) and create account
2. Create new repository: `andrej-gyure-cv`
3. Upload files or use GitHub Desktop
4. Go to Settings → Pages → Source: "Deploy from a branch"
5. Select "main" branch → Save
6. Your CV will be live at: `https://yourusername.github.io/andrej-gyure-cv`

**Cost:** $0/month
**Time:** 5 minutes
**Features:** Custom domain support, SSL, CDN

---

### 2. **Netlify - FREE & 3 minutes**

**Steps:**
1. Go to [Netlify.com](https://netlify.com)
2. Drag & drop your `cv_andty` folder
3. Get instant URL like: `https://random-name.netlify.app`
4. Optional: Connect custom domain

**Cost:** $0/month
**Time:** 3 minutes
**Features:** Automatic deployments, form handling

---

### 3. **Vercel - FREE & 2 minutes**

**Steps:**
1. Go to [Vercel.com](https://vercel.com)
2. Import from GitHub (if you used GitHub)
3. Or drag & drop folder
4. Instant deployment

**Cost:** $0/month
**Time:** 2 minutes
**Features:** Edge network, automatic scaling

---

### 4. **Firebase Hosting - FREE & 5 minutes**

**Steps:**
1. Install Firebase CLI: `npm install -g firebase-tools`
2. Run: `firebase login`
3. Run: `firebase init hosting`
4. Run: `firebase deploy`

**Cost:** $0/month
**Time:** 5 minutes
**Features:** Google's infrastructure

---

## **Quick GitHub Pages Setup:**

```bash
# If you have the files locally:
git remote add origin https://github.com/yourusername/andrej-gyure-cv.git
git push -u origin main

# Then enable GitHub Pages in repository settings
```

## **Custom Domain (Optional):**

1. Buy domain (Namecheap, GoDaddy, etc.) - ~$10/year
2. Add to GitHub Pages settings
3. Update DNS records

## **SEO Optimization:**

Add to `<head>` of each HTML file:
```html
<meta name="description" content="Andrej Gyure - Professional Alpine Skiing Coach with 30+ years experience">
<meta name="keywords" content="alpine skiing, coach, trainer, olympic, world cup">
<meta property="og:title" content="Andrej Gyure - CV">
<meta property="og:description" content="Professional Alpine Skiing Coach">
```

## **Analytics (Optional):**

Add Google Analytics:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## **Recommended Approach:**

1. **Start with GitHub Pages** (free, reliable, professional)
2. **Add custom domain** later if needed
3. **Add analytics** to track visitors
4. **Share link** on LinkedIn, email signatures, etc.

## **Files to Upload:**

- `index.html` (main page)
- `improved_cv_en_v4.html` (English)
- `improved_cv_sk_v4.html` (Slovak)
- `improved_cv_de_v4.html` (German)
- `improved_cv_es_v4.html` (Spanish)
- `README.md` (documentation)

---

**Total Cost:** $0-10/year (domain optional)
**Total Time:** 5-10 minutes
**Result:** Professional online CV portfolio! 🎉