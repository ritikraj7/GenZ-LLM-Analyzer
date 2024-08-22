import streamlit as st
import time
st.set_page_config(
    page_title="GenZ-LLM Analyzer",
    page_icon="🔬",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/abhibambhaniya/GenZ-LLM-Analyzer/issues',
        'Report a bug': "https://github.com/abhibambhaniya/GenZ-LLM-Analyzer/issues",
        'About': "https://github.com/abhibambhaniya/GenZ-LLM-Analyzer/blob/main/README.md"
    }
)
st.sidebar.info("If this app helps you, consider giving it a star! [⭐️](https://github.com/abhibambhaniya/GenZ-LLM-Analyzer)")

st.write("# Welcome to GenZ-LLM Analyzer! 👋")

st.markdown(
    """
Contents:
  - [Overview](#overview)
  - [Installation](#installation)
  - [Example](#Examples)
  - [Parallelism Scheme](#parallelism-scheme)
  - [Communication](#communication)
  - [Data Types](#data-types)
  - [TODOs](#todos)
  - [Citation](#citation)
  - [Useful Links](#useful-links)

## Overview

GenZ to designed to simplify the relationship between the hardware platform used for serving Large Language Models(LLMs) and inference serving metrics like latency and memory.

Running an LLM on hardware has three key component.
- Model : The LLM model architecture and corresponding parameters like number of layers, layer dimension etc.
- Usecase : Size of the Input queries, expected size of output query, and number of parallel beams generated.
- Optimization : There are various different optimizations that can be used to improve the LLM performance on a given hardware platform.
  - Quantization (Reducing the data precision)
  - Batching (Batching multiple similar sized queries to improve the throughput)
  - Parallelization ( Choosing specific parallelization strategies can help improve the performance of the LLM).
  - Operator Fusion ( FlashAttention/FLAT are techniques used to fuse multiple kernels together to speedup certain kernels.)


Given the specified LLM, Hardware Platform(GPU/CPU/Accelerator), data type, and parallelism configurations, genz can generate the latency and memory usage estimations.

GenZ can help answer various system-level choice-making questions, including,  
- how should the deployment platform change for LLM use cases for Q/A chatbots for customer services agents versus legal document summarization in attorney's offices? 
- how can the platform configurations be tweaked to maintain the same level of performance when deploying LLaMA2-70B instead of LLaMA2-7B?
- What will be the performance compromise if we do not change the serving platform?

GenZ can help computer architects understand trends which can help in designing the next generation of AI platforms by navigating the interplay between various HW characteristics and LLM inference performance based on models and compute demand. 
- if each node's total HBM bandwidth increases/decreases by 10\%, what would the impact on inference latency be? 
- By how much should the chip-to-chip communication network be improved? 

## Parallelism Scheme
GenZ supports Tensor Parallelism (TP), Pipeline Parallelism (PP) accross large platforms with multiple NPUs.


## Communication
Tensor Parallelism requires `ring allreduce`. Pipeline Parallelism requires a single hop node-to-node message passing.


## Data Types
Data types are expressed with the number of bits, We have the following data types are modeled for now.

| Data Type | Bits |
|:---------:|:----:|
|    FP32   |  32  |
|    BF16   |  16  |
|  INT8/FP8 |   8  |
|  INT4/FP4 |   4  |
|    INT2   |   2  |

## TODOs
Check the TODOs below for what's next and stay tuned! Any contributions or feedback are highly welcome!

- [ ] Add Expert parallelism and Sequence parallelism
- [ ] Support LoRA
- [ ] Add different kind of quantization for weights/KV/activations.

## Appreciation and Citation
"""
)

github_button = """
If a project helps you, please give it a star! [⭐️](https://github.com/abhibambhaniya/GenZ-LLM-Analyzer)
"""
st.markdown(github_button, unsafe_allow_html=True)

st.markdown(
    """
If you use GenZ in your [paper](https://arxiv.org/abs/2406.01698), please cite:

```
@misc{bambhaniya2024demystifying,
      title={Demystifying Platform Requirements for Diverse LLM Inference Use Cases},
      author={Abhimanyu Bambhaniya and Ritik Raj and Geonhwa Jeong and Souvik Kundu and Sudarshan Srinivasan and Midhilesh Elavazhagan and Madhu Kumar and Tushar Krishna},
      year={2024},
      eprint={2406.01698},
      archivePrefix={arXiv},
      primaryClass={cs.AR}
}
```
"""
)


st.session_state.models = [
        'meta-llama/Llama-2-7B',
        'meta-llama/Meta-Llama-3.1-8B',
        'meta-llama/Llama-2-13B',
        'meta-llama/Llama-2-70B',
        'meta-llama/Meta-Llama-3.1-405B',
        'google/gemma-2B',
        'google/gemma-7B',
        'google/gemma-2-9B',
        'google/gemma-2-27B',
        'mistralai/mistral-7B',
        'mistralai/Mixtral-8x7B',
        'microsoft/phi3mini',
        'microsoft/phi3small',
        'microsoft/phi3medium',
        'databricks/dbrx-base',
        'xai-org/grok-1',
        'openai/gpt-3',
        'openai/gpt-4',
        'facebook/opt-125m',
        'facebook/opt-350m',
        'facebook/opt-1.3b',
        'facebook/opt-175b',
        ]

st.session_state.systems = ['A100_40GB_GPU', 'A100_80GB_GPU', 'H100_GPU','GH200_GPU', 'TPUv4','TPUv5e', 'MI300X', 'Gaudi3', 'Custom']
