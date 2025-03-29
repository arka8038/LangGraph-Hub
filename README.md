# LangGraph-Hub   
A beginner-friendly repo to learn **LangGraph** through real projects!  

## Overview  
This repository is designed to help beginners understand and experiment with **LangGraph**, a framework for building structured AI workflows. It contains step-by-step Jupyter notebooks:  

1. **1_basic_graph.ipynb** – Learn the core structure and execution flow of LangGraph.  
2. **2_langgraph_Chatbot.ipynb** – Build an interactive AI chatbot using LangGraph and Groq LLM.  
3. **3_langgraph_routing.ipynb** – Implement intelligent tool routing for dynamic AI workflows.
4. **4_langgraph_custom_tool_agents.ipynb** -  Create modular AI agents with custom tool selection and execution.

## Setup Instructions  

### Option 1: Using Conda (Recommended)  
If you have **environment.yml**, you can set up the environment with:  

```bash
conda env create -f environment.yml
conda activate langgraph-env
```

### Option 2: Using pip  
If you prefer **requirements.txt**, you can install dependencies using:  

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Notebooks  
1. Start Jupyter Notebook:  
   ```bash
   jupyter notebook
   ```
2. Open the notebook you want to explore and run the cells!

## **LangGraph Debugging Guide**  

### **📌 How to Debug and Visualize the Graph**  

To see the real flow of the graph in LangGraph, follow these steps:  

1️⃣ **Navigate to the Debugging Folder**  
```bash
cd debugging
```

2️⃣ **Start the LangGraph Dev Server**  
```bash
langgraph dev
```

3️⃣ **Open LangGraph Studio**  
Once the server starts, open the following link in your browser:  
🔗 **[LangGraph Studio](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)**  

This allows you to:  
✅ **Visualize the execution flow**  
✅ **Debug nodes step-by-step**  
✅ **Inspect inputs, outputs, and errors in real-time**  

### **⚠️ Troubleshooting**
- If `langgraph dev` fails with a missing file error, ensure all required Python files exist inside the `debugging` folder.
- If the server is slow, try restarting with:  
  ```bash
  langgraph dev --reload
  ```
- If dependencies are missing, install them inside your Conda environment:  
  ```bash
  conda activate llms
  pip install -r requirements.txt
  ```

## Contribute & Learn  
If this helps you, drop a ⭐ on the repo and let me know what you’d like to learn next!  
