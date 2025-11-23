# 🚀 CS637 Dynamic Scheduler

A Python-based **Dynamic Scheduling Framework for Cyber-Physical Systems (CPS)** inspired by the EMSOFT24 paper  
**"Revisiting Dynamic Scheduling of Control Tasks: A Performance-Aware Fine-Grained Approach"**

This repository demonstrates the **implementation, replication, and enhancement** of a performance-aware fine-grained scheduling framework, with extensions for **machine learning prediction** and **energy optimization**.

---

## 🧠 Features

- ⚙️ **LTI System Modeling**
  - Implements continuous-to-discrete conversion for system dynamics.
- 📊 **LMI-based Stability Analysis**
  - Uses convex optimization to verify Lyapunov stability via LMIs.
- 🔄 **Control Skipping Automaton (CSA)**
  - Encodes safe transitions between control modes.
- 🧩 **ACESS Library Generator**
  - Generates valid scheduling sequences (in `c4b82162-e4b8-4aa3-b9e7-ad6d10368a74.py`).
- 🕹️ **Online Dynamic Scheduler**
  - Feedback-driven algorithm that adapts task utilization in real-time.
- 🔋 **Energy-Aware Co-Design**
  - Optimizes for both performance and energy consumption.
- 🧠 **ML-based Proactive Scheduler**
  - Uses GRU networks to anticipate cost violations.



