# SussLLM: Simulated User Search Sessions with Large Language Models


Source code for our paper :  
***SussLLM: Simulated User Search Sessions with Large Language Models***


<div align="center" style="margin: 10px 0 30px; padding: 20px;">

### 🚧 Repository Update In Progress 🚧

We are currently refactoring the repository to enhance its usability. Soon, you will be able to <strong>Install SussLLM via <code>pip install suss-llm</code></strong> and <strong>Utilize enhanced command-line functionality for easier access and operation</strong>.

### 🚨 Upcoming Release Alert 🚨
**SussData**, the comprehensive dataset generated by SussLLM, will be **soon published on Zenodo** for public access and research use. 

</div>

## Overview

SussLLM is a Python-based simulation framework designed to model user search behavior using advanced large language models (LLMs). It generates realistic user profiles and search sessions to better understand and analyze how users interact with search engines.








### 🚨 Upcoming Release Alert 🚨
**SussData**, the comprehensive dataset generated by SussLLM, will be **soon published on Zenodo** for public access and research use. Stay tuned!


## Quick Start

### Structure

```
sussllm/
│
├── sussllm/                              # Main package directory
│   ├── __init__.py                       # Initialization script
│   ├── profiles.py                       # User profile construction
│   ├── simulation.py                     # Simulation process management
│   ├── interaction.py                    # User interaction simulation
│   ├── reasoning.py                      # LLM reasoning and action decision module
│   ├── dataset.py                        # Dataset construction and management
│   ├── train.py                          # Training the models
│   ├── search/interfaces                 # Search interfaces and indexing
│   │   ├── __init__.py
│   │   ├── lucene/                       # Lucene indexing and BM25 search
│   │   ├── bing_search_engine.py         # Bing API search
│   │   └── google_search_engine.py       # Google API search
│   ├── utils/                            # Utility functions and classes
│   │   ├── __init__.py
│   │   ├── logger.py                     # Logging utility
│   │   ├── evaluation_metrics.py         # Evaluation utility
│   │   └── helpers.py                    # Helper functions
│   ├── llm_agent/                        # LLM-agents acting as users
│   ├── user_profile/                     # User profile simulation
│   │   ├── behavioral/                   # User profile simulation using Behavioral-oriented approach
│   │   └── component/                    # User profile simulation using Component-oriented approach
│
├── scripts/                              # Scripts for running simulations and analyses
│   ├── run_simulation.py                 # Script to run simulations
│   └── evaluate_model.py                 # Evaluation script for IR tasks
│
├── models/                               # Directory for ML models
│   ├── bm25_baseline.py                 
│   └── ranking_model.py
│
├── datasets/                             # Directory for storing datasets
│   ├── aol/                
│   └── trec/
│
├── simulations/                          # Simulation output for User profiles and sessions
│   ├── sussdata/                
│   └── user_profiles/
│
├── pyproject.toml                        # Poetry package and dependency management
└── README.md                             # Project overview and usage instructions
```



## Features

- **User Profile Simulation**: Generate detailed user profiles based on behavioral and component-oriented attributes.
- **Search Session Simulation**: Simulate dynamic search sessions including queries, clicks, and decisions.
- **Reasoning with LLMs**: Integrate large language models to enhance simulation realism by generating user reasoning and decision-making processes.
- **Dataset Management**: Handle and manipulate datasets of simulated search sessions and real-world data.
- **Extensible**: Easily extendable for various simulation scenarios and different LLMs.

## Prerequisites

- Python 3.8 or higher
- Poetry for dependency management

## Configuration

Set your own API keys in the environment variables:
```bash
export OPENAI_API_KEY='your-openai-api-key'
export BING_API_KEY='your-bing-api-key' 
```

## Installation

First, clone the repository:

```bash
git clone https://github.com/saberzerhoudi/suss-llm.git
cd sussllm
```

Install the project dependencies using Poetry:

```bash
poetry install
```

## Usage

### Running Simulations

To run simulations, use the `run_simulation.py` script:

```bash
poetry run python scripts/run_simulation.py
```

This script generates user profiles, simulates their search sessions, and logs the output.

### Evaluating Models

To evaluate your IR models with the simulated data, use the `evaluate_model.py` script:

```bash
poetry run python scripts/evaluate_model.py
```

Ensure you have a trained model and a dataset path set correctly in the script.

