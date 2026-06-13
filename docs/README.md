# LeakShield AI

AI-powered question paper leak detection and risk analysis system.

## Problem Statement

Question paper leaks are a major challenge for educational institutions and examination authorities. Leaks can lead to unfair advantages, exam cancellations, financial losses, and reduced trust in the examination process.

## Solution

LeakShield AI is an intelligent platform that detects potential question paper leaks using OCR (Optical Character Recognition) and AI-powered semantic similarity analysis. The system compares suspicious documents with official question banks and generates a leak probability score.

## Key Features

* OCR-based text extraction from images and PDFs
* AI-powered semantic similarity detection
* Leak probability scoring
* Dashboard analytics
* PDF and image upload support
* Risk assessment and reporting

## Tech Stack

### Frontend

* React
* Tailwind CSS

### Backend

* FastAPI
* Python

### AI & ML

* Sentence Transformers
* Tesseract OCR

### Database

* Firebase

## Project Structure

```text
LeakShield-AI
│
├── frontend
├── backend
├── screenshots
├── docs
└── README.md
```

## Workflow

1. Upload Official Question Paper
2. Upload Suspected Leak Document
3. Extract Text using OCR
4. Compare using AI Similarity Model
5. Generate Leak Probability Score
6. Display Results on Dashboard

## Expected Output

* Similarity Percentage
* Leak Probability Score
* Number of Matched Questions
* Risk Classification (Low, Medium, High)

## Future Scope

* Telegram monitoring
* WhatsApp leak detection
* Real-time alerts
* Examination authority dashboard
* Multi-language support

## Team

Avishek Dutta

## Status

Hackathon MVP Development in Progress 🚀
