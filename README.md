# AI Agent with neo4j

Installation requirements:

A knowledge graph is constructed form the movies collected from https://www.themoviedb.org/
Further details on the graph used in this project can be found here: https://github.com/neo4j-graph-examples/recommendations

```commandline
conda create -n aiagent -y python=3.10.0 && conda activate aiagent 
pip install -r requirements.txt
```

Run the agent by executing the following command:

```shell
streamlit run chatbot.py
```

### UI
![Chatbot UI](https://github.com/rashad101/AIAgent_with_neo4j/blob/main/aiagent-neo4j.png)

### Credit:
- Adapted from neo4j GraphAcademy
