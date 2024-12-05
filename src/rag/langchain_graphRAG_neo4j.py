# https://github.com/neo4j-labs/rdflib-neo4j
from langchain_community.graphs.rdf_graph import prefixes
from rdflib_neo4j import Neo4jStoreConfig, Neo4jStore, HANDLE_VOCAB_URI_STRATEGY
from rdflib import Graph


# set the configuration to connect to your Aura DB
AURA_DB_URI="neo4j+s://d1495246.databases.neo4j.io"
AURA_DB_USERNAME="neo4j"
AURA_DB_PWD="AdPR6laP452HN_rqyfeewSokzrTZeJFu_ahX4c5v3sw"

auth_data = {'uri': AURA_DB_URI,
             'database': "neo4j",
             'user': AURA_DB_USERNAME,
             'pwd': AURA_DB_PWD}

# Define your custom mappings & store config
config = Neo4jStoreConfig(auth_data=auth_data,
                          custom_prefixes=prefixes,
                          handle_vocab_uri_strategy=HANDLE_VOCAB_URI_STRATEGY.IGNORE,
                          batching=True)

#file_path = 'https://raw.githubusercontent.com/AbhijitVyas/Images/refs/heads/master/SOMA-HOME-TTL.owl'
# file_path = 'https://raw.githubusercontent.com/AbhijitVyas/Images/refs/heads/master/food_cutting.ttl'

# Create the RDF Graph, parse & ingest the data to Neo4j, and close the store(If the field batching is set to True in the Neo4jStoreConfig, remember to close the store to prevent the loss of any uncommitted records.)
neo4j_aura = Graph(store=Neo4jStore(config=config))
# Calling the parse method will implictly open the store
# neo4j_aura.parse(file_path, format="ttl")

# Import movie information

actions_query = """
LOAD CSV WITH HEADERS FROM 
'https://raw.githubusercontent.com/AbhijitVyas/Images/refs/heads/master/action_data.csv'
AS row
MERGE (m:Action {id:row.ActionId})
SET m.ActionSuccess = date(row.ActionSuccess),
    m.ActionType = row.ActionType,
    m.AgentName = row.AgentName,
    m.ObjectsParticipated = row.ObjectsParticipated
FOREACH (object in split(row.ObjectsParticipated, '|') | 
    MERGE (o:Object {name:trim(object)})
    MERGE (o)-[:PARTICIPATED_IN]->(m))
FOREACH (agent in split(row.AgentName, '|') | 
    MERGE (p:Person {name:trim(agent)})
    MERGE (m)-[:PERFORMED_BY]->(p))
"""

neo4j_aura.query(actions_query)
neo4j_aura.refresh_schema()
print(neo4j_aura.schema)

from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = GraphCypherQAChain.from_llm(graph=neo4j_aura, llm=llm, verbose=True)
response = chain.invoke({"query": "What was the cast of the Casino?"})
print(response)

# close the graph connection at the end
neo4j_aura.close(True)
