# Characteristics of Agentic AI

### Autonomy

It refers to the ability to make decisions and take actions on its own

### Goal Oriented

Goals act as compass for autonomy, they come with constraints and stored in core memory.

### Planning

Dividing the goals into smaller steps and then decide, what is the best path

Steps :-

1. Generating multiple candidate plans
2. Evaluate each plan
3. Select the best plan

### Reasoning

It is a process through which agentic ai system interprets information, draws conclusions and makes decisions.

eg -> Decision making, HITL handling, Err handling

### Adaptability

Ability to modify its tasks or strategies.

### Context Awareness

Ability to understand and utilize relevant info from the ongoing task.

    Types of context

1. The original goal
2. Progress till now
3. Env state
4. Tool responses
5. User specific preferences
6. Policy of guardrails

# Components of AI Agent

### Brain

### Orchestrator

### Tools

### Memory

### Supervisor

# Some points

### State -> 

It is a typedDict stored for future inference

### Reducer -> 


# LangGraph Execution Model

### Graph Definition

State schema

Nodes 

Edges

### Compilation

.compile()

### Invocation

.invoke(initioal_state)

### Super-steps begin

Execution proceeds in rounds

All active nodes run in parallel

Each returns an update (message) to the state

### Message Passing and Node Activation

The messages are passed to downstream nodes via edges.

Nodes that recieve messages become active for the next round.

### Halting Condition

Execution stops when:

    No nodes are active and

    No messages are in transit
