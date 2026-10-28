# PDF Conversion Guide for Lab Submission

## 📄 Document to Submit: LAB_ISE2_Documentation.md

This guide will help you convert the markdown documentation to PDF format for submission.

---

## Method 1: Using Visual Studio Code (Recommended)

### Step 1: Install Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Markdown PDF"
4. Install "Markdown PDF" by yzane
5. Reload VS Code

### Step 2: Update Personal Information
1. Open `LAB_ISE2_Documentation.md`
2. Find and replace:
   - `[Enter Your Name]` → Your actual name
   - `[Enter Your Roll Number]` → Your roll number
   - `[Enter Your Repository URL]` → Your GitHub URL
   - `[Your Name]` → Your actual name (appears multiple times)

### Step 3: Add Screenshots
1. Take all screenshots as per Section 6 checklist
2. Save screenshots in a folder named `screenshots`
3. Insert images in markdown:
   ```markdown
   ![Description](screenshots/image-name.png)
   ```

### Step 4: Convert to PDF
1. Open `LAB_ISE2_Documentation.md` in VS Code
2. Press `Ctrl+Shift+P`
3. Type "Markdown PDF: Export (pdf)"
4. Press Enter
5. PDF will be created in the same folder

---

## Method 2: Using Microsoft Word

### Step 1: Copy Content
1. Open `LAB_ISE2_Documentation.md` in any text editor
2. Select all content (Ctrl+A)
3. Copy (Ctrl+C)

### Step 2: Paste in Word
1. Open Microsoft Word
2. Create new document
3. Paste content (Ctrl+V)
4. Word will automatically format markdown

### Step 3: Format Document
1. Apply heading styles (Heading 1, 2, 3)
2. Format code blocks with Courier New font and gray background
3. Insert screenshots in appropriate locations
4. Add page numbers
5. Add table of contents (optional)

### Step 4: Save as PDF
1. File → Save As
2. Choose location
3. File type: PDF
4. File name: `ISE2_CICD_Pipeline_YourName_YourRollNumber.pdf`
5. Click Save

---

## Method 3: Online Converter

### Option A: Markdown to PDF Online
1. Visit: https://www.markdowntopdf.com/
2. Upload `LAB_ISE2_Documentation.md`
3. Click "Convert"
4. Download PDF

### Option B: Google Docs
1. Visit: https://docs.google.com
2. Create new document
3. Paste markdown content
4. Format as needed
5. Insert screenshots
6. File → Download → PDF

---

## ✅ Pre-Submission Checklist

Before converting to PDF, ensure:

### Personal Information
- [ ] Student Name filled
- [ ] Roll Number filled
- [ ] Department confirmed (CSE Data Science)
- [ ] Academic Year correct (A.Y 2026-27)
- [ ] GitHub Repository URL added

### Content Completeness
- [ ] All sections present (1-12 + Appendices)
- [ ] All commands documented
- [ ] Expected outputs included
- [ ] Troubleshooting section complete
- [ ] References included

### Screenshots
- [ ] Python version output
- [ ] Flask installation and running
- [ ] Git initialization and commits
- [ ] GitHub repository page
- [ ] Docker build and run
- [ ] Jenkins dashboard
- [ ] Pipeline execution success
- [ ] Application screenshots (home, add, health check)

### Formatting
- [ ] Headings properly formatted
- [ ] Code blocks clearly visible
- [ ] Tables properly aligned
- [ ] Screenshots inserted and captioned
- [ ] Page numbers (if applicable)

### Technical Accuracy
- [ ] All commands tested and verified
- [ ] Outputs match actual execution
- [ ] File paths correct
- [ ] URLs accurate

---

## 📸 Screenshot Best Practices

### Taking Screenshots on Windows
```powershell
# Full screen
Win + PrintScreen

# Snipping Tool
Win + Shift + S

# Screenshots saved to:
# C:\Users\YourName\Pictures\Screenshots
```

### Screenshot Guidelines
1. **Crop appropriately** - Show only relevant content
2. **High resolution** - Clear and readable text
3. **Label clearly** - Add captions below each image
4. **Organize** - Name files descriptively (e.g., `docker_build_success.png`)

### Suggested Screenshot Names
```
01_python_version.png
02_flask_running.png
03_app_browser.png
04_git_init.png
05_git_commit.png
06_github_repo.png
07_github_push.png
08_docker_version.png
09_docker_build.png
10_docker_ps.png
11_docker_app_running.png
12_jenkins_dashboard.png
13_jenkins_pipeline.png
14_jenkins_build_success.png
15_jenkins_stages.png
16_app_home_page.png
17_app_add_student.png
18_health_check.png
```

---

## 📋 Final PDF Structure

Your PDF should contain:

1. **Cover Page** (from Section 1)
   - Title: CICD Pipeline and Monitoring Tools
   - Subtitle: Summary Report
   - Student details table

2. **Problem Statement** (Section 1)

3. **Tools & Environment Setup** (Section 2)
   - Python & Flask
   - Git
   - GitHub
   - Docker
   - Jenkins
   (Each with commands, outputs, and screenshots)

4. **Workflow** (Section 3)

5. **Application Features** (Section 4)

6. **Project Structure** (Section 5)

7. **Screenshots Section** (Section 6)

8. **Commands Summary** (Section 7)

9. **Troubleshooting** (Section 8)

10. **Learning Outcomes** (Section 9)

11. **Conclusion** (Section 10)

12. **References** (Section 11)

13. **Submission Details** (Section 12)

14. **Appendices** (A & B)

---

## 📤 Submission Format

### File Naming Convention
```
ISE2_CICD_Pipeline_[YourName]_[RollNumber].pdf

Example:
ISE2_CICD_Pipeline_RahulSharma_2026001.pdf
```

### Submission Requirements
1. **Format:** PDF only
2. **File Size:** Under 20 MB (compress if needed)
3. **Quality:** High-resolution screenshots
4. **Completeness:** All sections included
5. **Accuracy:** All personal information correct

### Where to Submit
- **Platform:** ERP Portal
- **Course:** ML DevOps Laboratory (UDSPC0732)
- **Assignment:** ISE-2
- **Deadline:** 29th October 2026

---

## 🔍 Quality Check

Before final submission, review:

### Readability
- [ ] Text is clear and legible
- [ ] Code blocks are monospaced
- [ ] Tables are properly formatted
- [ ] Screenshots are high quality

### Completeness
- [ ] All 12 sections present
- [ ] Both appendices included
- [ ] All checklists completed
- [ ] References cited

### Accuracy
- [ ] Commands tested and verified
- [ ] Outputs match execution
- [ ] Personal info correct
- [ ] GitHub URL accessible

### Professionalism
- [ ] No spelling errors
- [ ] Consistent formatting
- [ ] Professional appearance
- [ ] Proper structure

---

## 💡 Tips for Better PDF

1. **Use Clear Headings**
   - Make section numbers and titles bold
   - Use consistent font sizes

2. **Format Code Properly**
   - Use monospace font (Courier New, Consolas)
   - Add light gray background
   - Ensure syntax highlighting if possible

3. **Optimize Screenshots**
   - Compress images if PDF is too large
   - Use tools like TinyPNG or ImageOptim
   - Maintain readability after compression

4. **Add Page Numbers**
   - Helps in navigation
   - Professional appearance

5. **Include Table of Contents**
   - Optional but recommended
   - Makes navigation easier
   - Shows document structure

---

## 🆘 Common Issues and Solutions

### Issue: PDF is too large (>20 MB)
**Solution:**
- Compress screenshots before inserting
- Use JPEG instead of PNG for photos
- Reduce screenshot dimensions
- Use online PDF compressor: https://www.ilovepdf.com/compress_pdf

### Issue: Code formatting lost in Word
**Solution:**
- Select code block
- Format with monospace font (Courier New)
- Add gray background color
- Use "Keep with next" to prevent breaks

### Issue: Screenshots not displaying
**Solution:**
- Ensure image paths are correct
- Use absolute paths or embedded images
- Check image file formats (PNG, JPG)

### Issue: Markdown not converting properly
**Solution:**
- Try different converter
- Check markdown syntax
- Remove any special characters
- Use simpler formatting

---

## 📞 Support

**Course In-charge:** Mr. Shekhar Jalane  
**Course Code:** UDSPC0732  
**Department:** CSE (Data Science)

For any issues with PDF conversion or submission:
1. Contact course in-charge
2. Verify ERP portal access
3. Check submission guidelines on ERP

---

## ⏰ Time Management

Allocate time for PDF preparation:
- Screenshot capture: 20 minutes
- Personal info update: 5 minutes
- Screenshot insertion: 15 minutes
- Formatting review: 10 minutes
- PDF conversion: 5 minutes
- Quality check: 10 minutes
- **Total:** ~65 minutes

---

## 🎯 Final Reminder

✅ Update personal information  
✅ Add all screenshots  
✅ Test all commands before documenting  
✅ Review for accuracy  
✅ Check file size  
✅ Name file correctly  
✅ Submit before deadline  

**Good luck with your submission! 📚✨**

---

**Document Version:** 1.0  
**Last Updated:** 27th October 2026  
**Purpose:** Guide for converting lab documentation to PDF format
