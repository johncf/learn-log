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
1. Low-level/component design (10 minutes)
   - Component specific APIs or internal design (e.g. database schema)
   - Analyze the need for DB indexing, DB replication, DB partitioning + map-reduce for aggregation
   - Discuss caching options (e.g. CDN, database caching, client-side caching)
   - Do NOT discuss anything outside established scope
1. Understanding bottlenecks and improvements (5 minutes)
   - Issues that could happen with a component (e.g. a "celebrity" user)
   - Modifications that could resolve the issue
1. Evaluation and wrap-up (5 minutes)
   - Quick overview of the design and why it can handle the scale.

## Key Topics

- Availability: the probability that a system is operational at a given time
  - Example: stay operational even with partial internal network failures
  - Strategies: load balancing, failover mechanisms (switching to backup systems on failure)
- Reliability: the probability that a system will produce correct outputs up to some given time
  - Example: recover from device failures or natural disasters
  - Strategies: built-in redundancies, replication, error monitoring
- Performance: throughput, latency
  - Strategies: horizontal and vertical scaling, data partitioning, caching
- Concurrency: locking, consistency
- Serviceability or Maintainability: the speed with which a system can be repaired or maintained

## Key Questions to Keep in Mind

- What's the estimated size of the data? (Or are we starting from scratch, and have a growth phase?)
- How is the data consumed by end users? (Streaming vs. downloading)
- How often will data be accessed by users? (Request rate, bandwidth usage)
- Are there parts of data that are read-heavy or write-heavy?
- Which parts of data will need strict consistency? Is eventual consistency enough?
- Will there be bursts of requests due to popularity spikes? (Queues could be used to manage spikes)

## References

- [Video from ByteByteGo](https://www.youtube.com/watch?v=i7twT3x5yv8)
- [Cheat sheet in the wild](https://gist.github.com/vasanthk/485d1c25737e8e72759f)
