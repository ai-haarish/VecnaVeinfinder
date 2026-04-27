# 🩸 VecnaVeinfinder

> **A functional NIR vein detection system built for ₹300.**  
> Three computer vision models. One modified smartphone. One old laptop. Real-time vein visualization.

---

## What is this?

VecnaVeinfinder is an open-source, low-cost vein detection system that uses **Near Infrared (NIR) imaging** and three different computer vision models to detect and visualize veins beneath the skin — in real time.

Commercial vein finders cost ₹50,000 to ₹5,00,000.  
This one costs **₹300** (just the NIR LEDs).

---

## How it works

Blood absorbs NIR light differently than surrounding tissue. By illuminating the skin with NIR LEDs and capturing footage with an IR-cut-filter-removed smartphone, veins become visible in the camera feed.

That footage is streamed (via WiFi or USB) to a laptop, where three models process it in real time to highlight tube-like vein structures.

```
NIR LEDs → Modified Phone Camera → WiFi / USB → Laptop → Vein Detection Output
```

---

## The Three Models

| Model | Approach |
|-------|----------|
| **CLAHE** | Contrast Limited Adaptive Histogram Equalization — enhances vein contrast in NIR images |
| **Frangi Filter** | Scikit-image implementation — multiscale vessel/tubular structure detection |
| **Hessian Math Model** | Pure mathematical model using Hessian matrix eigenvalue analysis — no ML library, math only |

All three models detect **tube-like structures** in the image — veins appear as dark tubular regions under NIR illumination.

The Hessian model is built entirely from mathematical principles with no machine learning framework — making it fully transparent and interpretable.

---

## ⚠️ Current Status — Rewrite in Progress

The current implementation is written in Python, which introduces significant overhead for real-time image processing.

We are actively rewriting the pipeline in a low-level language for dramatically improved performance and lower latency. Performance benchmarks will be published after the rewrite is complete.

Contributions welcome — especially if you have experience with real-time computer vision in C/C++ or Rust.

---

## Hardware Setup

| Component | Cost |
|-----------|------|
| NIR LEDs (850nm) | ~₹300 |
| Android smartphone (IR cut filter removed) | Already owned |
| Laptop (any old one works) | Already owned |
| **Total** | **~₹300** |

### Steps to replicate:
1. Remove the IR cut filter from an Android phone camera
2. Set up NIR LEDs to illuminate the area
3. Stream phone footage to laptop via USB (faster) or WiFi
4. Run any of the three models on the incoming stream

---

## Why this matters

Vein visualization is used in:
- IV insertions and blood draws
- Surgical guidance
- Dermatology

Existing devices are expensive and out of reach for rural clinics and low-resource healthcare settings.  
VecnaVeinfinder is a proof-of-concept that this technology can be replicated with everyday hardware and open-source software.

---

## Installation

```bash
git clone https://github.com/ai-haarish/VecnaVeinfinder
cd VecnaVeinfinder
pip install -r requirements.txt
python main.py
```

> *(Update this section with your actual run instructions)*

---

## Requirements

```
opencv-python
scikit-image
numpy
```

---

## Team

| Name | Role |
|------|------|
| **Haarish Jayakumar** | Founder — AI model, system architecture |
| **Kirubha Mugilan** | Collaborator — Hessian math model, computer vision |
| **Jaya Prakesh** | Team member |
| **Akilesh** | Team member |

---

## License

Open source. Built for the community.

---

## Contributing

Pull requests welcome. If you replicate this with different hardware, improve performance, or want to contribute to the low-level rewrite — open an issue.

---

*Built with ₹300 and a lot of curiosity.*

  
