# 🚀 CS637 Dynamic Scheduler

A Python-based **Dynamic Scheduling Framework for Cyber-Physical Systems (CPS)** inspired by the EMSOFT24 paper  
**"Revisiting Dynamic Scheduling of Control Tasks: A Performance-Aware Fine-Grained Approach"**

This repository demonstrates the **implementation, replication, and enhancement** of a performance-aware fine-grained scheduling framework, with extensions for **machine learning prediction** and **energy optimization**.

---

## 🧩 Features

- ⚙️ **System Modeling (system_model.py)**  
  Models continuous-time LTI systems and performs discretization.

- 🧠 **Subsystem Generator (subsystem_generator.py)**  
  Generates subsystem matrices for different sampling periods and skip counts.

- 📊 **Stability Analysis (stability_analyzer.py)**  
  Verifies stability using Linear Matrix Inequalities (LMIs) and Lyapunov analysis.

- 🔄 **Control Skipping Automaton (csa_synthesizer.py)**  
  Constructs the automaton encoding valid transitions between control modes.

- 🔁 **ACESS Sequence Generator (acess_generator.py)**  
  Generates valid control execution skipping sequences from the CSA.

- 🕹️ **Online Scheduler (online_scheduler.py)**  
  Dynamically adjusts task utilization using real-time performance feedback.

- 🔋 **Energy Model (energy_model.py)**  
  Adds multi-objective optimization between energy and performance.

- 🧩 **GRU-Based Cost Predictor (GRU-Based Cost Predictor.py / predictor.py)**  
  Predicts future control costs for proactive scheduling using recurrent neural networks.

- 🧾 **Pseudocode — Online Dynamic Scheduler.txt**  
  Provides high-level algorithmic reference for understanding the scheduling logic.

---


