# User Profile Construction

## Overview
To simulate users' search behaviors effectively, it's essential to create diverse and detailed user profiles. These profiles encompass various aspects of online interactions, capturing both static and dynamic components of user behavior.

## Behavioral-oriented User Profile
Based on prior research, we've designed a profile structure with five main attributes:

- **Temporal Patterns**: Categorized into short, medium, and long durations based on user interaction logs.
- **Search Query Analysis**: Identifies query reformulation patterns, such as spelling corrections and synonym usage.
- **Clickstream Data**: Tracks user navigation paths, categorizing behaviors into patterns like direct hits and iterative refinement.
- **Use of Advanced Search Features**: Classifies users based on their usage of operators, filters, or specialized search domains.
- **Interest**: Dynamically categorized, initially defining broad categories that are further refined with GPT-4.

Attribute values are defined using data analysis and hybrid generation techniques.

## Component-oriented User Profile
Leveraging the SimIIR framework, this profile structure incorporates components reflecting dynamic user interactions in web search:

- **Querying Component**: Analyzes query patterns to define querying behavior.
- **Snippet and Document Components**: Classify attractiveness or relevancy based on varying criteria.
- **Stopping Component**: Implements stopping rules to accurately simulate when users cease their search.
- **Loggers**: Record detailed logs of user interactions, providing search context.

User profiles are constructed using Real Data-based and Hybrid generation approaches, combining large-scale user data and predefined attribute values by human analysts and GPT-4.

## User Search Construction
Utilizing the profile construction method, we employ LLM-based agents to simulate user behavior in search engine settings. Agents maintain awareness of their state, formulate queries, assimilate returned information, and click on relevant web pages. They assess whether their information needs are met to determine the continuation or conclusion of a session.

### SussLLM's Approach
SussLLM enhances the accuracy of generated actions using the ReAct method, expanding the action space to include reasoning and action steps. It uses a task-specific prompt for each round of interaction, guiding the LLM to perform reasoning tasks and generate stops, queries, clicks, and observations based on the updated context.

### Interaction Sequence
The interaction sequence involves alternating queries, clicks, and a session stop action, divided into rounds comprising the decision to query, click, and stop actions.

### Prompts and Templates
For different prompting approaches, we create templates to ensure stable and controlled agent outputs. These templates are available in our repository.

### Sequential Behaviors
Each user exhibits sequential behaviors in a search session, interacting with search engines using ChatGPT.
