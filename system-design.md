# System Design

Tackling the system design interview.

## Basic Steps

1. Understand requirements and establish scope (5 minutes)
   - High-level objectives (use-cases)
   - Functional requirements (features)
   - Non-functional requirements (scale, latency, etc.)
   - Technical constraints
1. Capacity estimation and constraints (2 minutes)
   - Assumptions (e.g. read-write ratio)
   - Compute effective requests rates to be handled
1. High-level design (10 minutes)
   - Basic components of the system (load balancers, caching systems, DB, etc.)
   - List required services
   - Choices of each component are *not* explored (e.g. MySQL vs. MongoDB)
   - Design end-user APIs to meet functional requirements
1. Component design (10 minutes)
   - Component specific APIs or internal design (e.g. database schema)
   - Analyze the need for database replication, database partitioning + map-reduce for aggregation
   - Discuss caching options (e.g. CDN, database caching, in-memory caching)
   - Do NOT discuss anything outside established scope
1. Understanding bottlenecks and improvements (5 minutes)
   - Issues that could happen with a component (e.g. a "celebrity" user)
   - Modifications that could resolve the issue
1. Evaluation and wrap-up (5 minutes)
   - Quick overview of the design and why it can handle the scale.

Sources:
- [Video from ByteByteGo](https://www.youtube.com/watch?v=i7twT3x5yv8)
- [Cheat sheet in the wild](https://gist.github.com/vasanthk/485d1c25737e8e72759f)
