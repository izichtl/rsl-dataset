# Small Language Models for Study Screening in Systematic Literature Reviews: SLM-as-a-Judge Approach

This repository contains the implementation of the research "Small Language Models for Study Screening in Systematic Literature Reviews: SLM-as-a-Judge Approach". The project explores the viability of using open-source Small Language Models (SLMs) to automate the screening phase of Systematic Literature Reviews (SLRs).

## Overview

The exponential growth of scientific publications makes manual screening in SLRs a labor-intensive and error-prone process. This project proposes an automated architecture named **SLM-as-a-Judge**, which simulates the methodological flow of human consensus and arbitration.

The system utilizes multiple artificial agents to apply inclusion and exclusion criteria to research papers. It employs a consensus mechanism with specific arbitrators to resolve conflicts, aiming to reduce human effort while maintaining methodological rigor.

## Methodology

The architecture follows a multi-stage pipeline:

### Primary Evaluation

Two distinct SLMs (Evaluators A and B) independently classify titles and abstracts based on predefined criteria.

- **Evaluator A**: Qwen3-4b-Instruct
- **Evaluator B**: gemma-3-4b-it

### Consensus and Arbitration

- **Consensus**: If both evaluators agree, the decision is maintained.
- **Arbitration**: In cases of divergence, a third specialized model (the Judge) reviews the conflicting decisions and justifications to issue a final verdict.
- **Judge Models**: Includes models like `GAIR/autoj-bilingual-6b` and `grounded-ai/phi3-hallucination-judge-merge`.

### SLM-as-a-Judge

The models function not just as text generators but as evaluators following strict logic chains.

## Key Features

- **Multi-Agent System**: Simulates a committee of reviewers to mitigate individual model bias.
- **High Recall Strategy**: Prioritizes minimizing false negatives to prevent the loss of relevant studies.
- **Open Source Focus**: Built using efficient, open-weight models rather than large proprietary APIs.
- **Automated Metrics**: Includes scripts for calculating Precision, Recall, F1-Score, and Kappa agreement coefficients against a Ground Truth.

## Dataset

The experiments were conducted using a corpus of **2,591 studies** related to Requirements Engineering in Agile Projects. This dataset includes a validated Ground Truth classification provided by domain experts.

## Results

The proposed architecture achieved a **Recall superior to 93%**, demonstrating its safety as a screening assistant. The system effectively filters out the majority of irrelevant studies, significantly reducing the workload for human researchers.

## Installation

The implementation is provided as a Jupyter Notebook designed to run in environments like Google Colab or a local Jupyter setup with GPU support (e.g., NVIDIA T4).

### Prerequisites

- Python environment with GPU support
- Hugging Face Account (for model access)
- Google Drive (optional, for saving processed outputs)

### Dependencies

Install the required Python packages:

```bash
pip install pandas numpy transformers accelerate sentence-transformers scikit-learn matplotlib
```

## Usage

1. **Setup Keys**: You must provide your Hugging Face User Access Token to download the models.
2. **Data Loading**: The notebook is configured to load the dataset directly from the repository.
3. **Pipeline Execution**:
   - Run the "Evaluator" cells to generate initial classifications.
   - Run the "Consensus/Judge" cells to resolve conflicts.
4. **Evaluation**: Execute the post-processing cells to generate performance metrics (Confusion Matrix, Recall, Precision).

## Reference

If you use this code or methodology, please cite the original report:

- **Title**: Small Language Models para a Triagem de Estudos em Revisões Sistemáticas da Literatura: Abordagem SLM-as-a-Judge
- **Author**: Ivan Zichtl Santos
- **Institution**: Instituto Federal de Educação, Ciência e Tecnologia da Paraíba (IFPB)

## License

This project is open-source. Please refer to the repository license file for usage terms.
