# System Design Interview

Tackling the system design interview.

Do take a look at [general tips](./general.md) on problem solving first. (TLDR; make sure to consider different approaches and discuss its pros and cons, when choosing a design or component.)

Evaluated primarily on 3 aspects:
- Problem navigation: understanding and deconstruction of the problem; proper time-management
- Solution design: how well-rounded the solution is; address functional _and_ non-functional requirements
- Technical communication: how well the ideas are conveyed; show evidence of deeper-knowledge

## Basic Steps

1. Understand requirements and establish scope (3-4 minutes)
   - High-level objectives (use-cases)
   - Functional requirements (features)
   - Non-functional requirements (scale, latency, etc.)
1. Capacity estimation and constraints (2-3 minutes)
   - Assumptions (e.g. read-write ratio, daily active users) (validate these with the interviewer)
   - Compute effective request rates to be handled
1. High-level design (7-8 minutes)
   - Basic components of the system (load balancers, caching systems, DB, etc.)
   - Basic database design (with rough table schemas)
   - List required services (e.g., gateway server, logging service, etc.)
   - _Note:_ API design is usually not required (but confirm with the interviewer)
1. Low-level component design: deep-dive (12-15 minutes)
   - The interviewer may want to drill down on a specific component or part of the design
   - Adjust the design to resolve possible bottlenecks (e.g. spikes in traffic, "celebrity" users)
   - Analyze the need for DB indexing, DB replication, DB partitioning
   - Explore caching options (e.g. CDN, database caching, client-side caching)
   - Do NOT discuss anything outside established scope
1. Evaluation and wrap-up (2-3 minutes)
   - A quick overview of the design and why it can handle the scale.
   - Example: a step-by-step walk-through of what happens when a client issues a particular request.

## Quick Tips

- Don't be afraid to ask questions to improve clarity and define a practically limited scope.
- Separate out different logical components (e.g. "upload service" and "download service") even if they _can_ be served by a single monolith server.
- **Steer the conversation** to highlight your strengths and experience! Let the interviewer know which part is most interesting to you and would like to focus on (get buy-in).
- Feel free to admit your weaknesses (the parts that you're unsure of).
- Try to state non-functional requirements as specific trade-offs (e.g., "for low latency feed retrieval, a few minutes of staleness is okay"), instead of being overly broad (e.g., "system should have low latency").
- Make absolutely sure to **discuss trade-offs** and alternatives for each of your choices!
- Be proactive in discussing failure possibilities in every component of the system so as to avoid single-points-of-failures.
- Be mindful of the time spent gathering requirements, capacity estimation and high-level design.
  - After gathering high-level details, only drill down to specifics if necessary for a design decision.
  - You need to spare ample time for the deep-dive, so that you can showcase your expertise.
- During the deep-dive, if the interviewer introduces a change in requirements or constraints (e.g., larger scale), be open to rethink major parts of the architecture.

Sources:
- [Intro to Architecture and System Design Interviews (video)](https://www.youtube.com/watch?v=ZgdS0EUmn70)
- [5 Common Mistakes to Avoid (video)](https://www.youtube.com/watch?v=ySfpftMZnoU&list=PLTCrU9sGyburBw9wNOHebv9SjlE4Elv5a&index=29)
- [System Design Requirements Gathering](https://www.hellointerview.com/blog/system-design-requirements)

## Non-Functional Concepts

- Scalability: the ability of a system to handle a growing amount of work.
  - Example goal: provide high throughput and low latency even during usage spikes
  - Strategies: more servers + load balancing, data partitioning, caching
- Availability: the probability that a system is operational at a given time
  - Example goal: stay operational even with partial internal network failures
  - Strategies: DNS-based load balancing, failover mechanisms (switching to backup systems on failure)
- Reliability: the probability that a system will produce correct outputs up to some given time
  - Example goal: avoid loss of data due to device failures or natural disasters
  - Strategies: built-in redundancies, replication, regular back-ups, error monitoring
- Observability: the ability to collect data about programs' execution, modules' internal states, etc.
  - Example goal: monitor servers under high load/stress so as to route traffic away
- Serviceability or Maintainability: the speed with which a system can be repaired or maintained
  - Example goal: minimize or avoid downtime when upgrading a component

See [list of system quality attributes](https://en.wikipedia.org/wiki/List_of_system_quality_attributes) for a more complete list.

## Key Questions to Keep in Mind

- What's the estimated size of the data? (Or are we starting from scratch, and have a growth phase?)
- How is the data consumed by end users? (Streaming vs. downloading)
- How often will data be accessed by users? (Request rate, bandwidth usage)
- Are there parts of data that are read-heavy or write-heavy?
- Which parts of data will need strict consistency? Is eventual consistency enough?
- Will there be bursts of requests due to popularity spikes? (Queues could be used to manage spikes)

## Key Components Explained

Basics: [Lecture on Web Scalability by David Malan](https://www.youtube.com/watch?v=-W9F__D3oY4)

### Load Balancers

Helps with horizontal scaling, by distributing traffic across multiple servers of the same kind.

- Could be placed between user and web server, web server and internal services or databases.
- Algorithms used for balancing: static ("round robin", "IP hash"), dynamic ("least connection", "least response time", "resource-based"), and their weighted variants.
- Implementations: "DNS-based LB", "Hardware LB", "Software LB"

### Proxy Servers

A server sitting between the client and server that may do one or more of the following:

- Filter requests
- Log requests
- Transform requests
- Batch requests
- Cache responses

### Caching

- May exist at all levels in architecture.
- A short-lived copy that is faster to access than the original source.
- Cache eviction: Removal of a cached entry to make space for another.
- Cache invalidation: marking a cache entry as stale/invalid due to the original source having changed.
- Cache consistency: probability of getting stale data.
- Example use-case: Content Delivery Network (CDN) for caching static data (e.g., photos or videos).
- Example use-case: Database cache (e.g., using Memcached) to speed-up certain database read-queries.

#### Cache Invalidation Strategies

- *Write through cache*: Writes go through the cache, succeeding only if writes to both the source and the cache succeed.
  - High write latency, high cache consistency _and_ low read latency due to fewer cache misses.
- *Write around cache*: Writes go directly to the source.
  - Low write latency, low cache consistency _or_ high read latency due to higher cache misses.
- *Write back cache*: Writes only done to the cache, and cache syncs to the source later.
  - Low write latency, low read latency, high cache consistency, but increased risk of data loss.

#### Cache Eviction Policies

- Least Recently Used (LRU): The least recently accessed entry gets evicted.
- First In First Out (FIFO): The least recently added entry gets evicted.
- Random Replacement (RR): Randomly discards an entry.
- [S3-FIFO](https://s3fifo.com/): A 2023 algorithm that uses 3 FIFO queues, and is more efficient and scalable than LRU.
- [SIEVE](https://sievecache.com/): A 2024 algorithm that's authored by the same group from S3-FIFO.
- Least Frequently Uesd (LFU): The one with lowest access count gets evicted. Rarely used as is due to issues.
- Most Recently Used (MRU): The most recently accessed gets evicted! Only useful in niche scenarios.
- Last In First Out (LIFO): The most recently added gets evicted! Only useful in scenarios where MRU is useful.

### Queues and Streams

- To decouple "processing" from "data producers", "processing" fault tolerance (retryability).
  - Note1: If you just want decoupling but not fault tolerance (i.e., losing some data when a processing node crashes is okay), then you can simply use an internal load balancer.
  - Note2: A distributed data stream (Kafka or Kinesis) should be used when each message needs to go to multiple clients, and/or reading older messages is beneficial (publisher-subscriber model). Be careful about designing topics and partition in a way that can scale up.
  - Note3: A message queue should be used when a single message goes to a single consumer (FIFO queue model).
- Use-case: logging to a message stream, with a pub-sub model.
- Use-case: activity and operational monitoring (page views, searches, etc.) for analytics and reporting.
- Use-case: stream processing or data-pipeline orchestration.
- Use-case: posting a tweet on Twitter -- would be hard to update all followers' feeds instantly. So queue it up for eventual update.
- Kafka is a scalable and fault-tolerant message broker.
  - It uses persistent logs efficiently to achieve high-performance.
  - Topics can be partitioned and each consumer in a consumer-group gets mapped to a single partition (ideally, one-to-one) for scaling.
  - Consumers "commit" their offset manually. If the consumer fails and restarts, this commit can be inspected to recover from. Messages can be replayed arbitrarily.
  - Requires pull-based consumers.
- RabbitMQ's "Classic Queue" is an in-memory message broker (with a focus on message-ordering like in a FIFO queue). However, recent versions introduced "Quorum Queues" and "Streams" which use persistent logs and Raft for fault-tolerance and consistency in a distributed setup.
  - Uses an ACK-based retry-logic, managed by RabbitMQ.
  - Prefers push-based consumers. Can configure limits to control the number of un-ACK-ed messages to prevent overwhelming a consumer.
  - "Streams" also support partitioning for better horizontal scalability, without ordering guarantees.
  - "Quorum Queues" can be given a replication factor to be fault-tolerant. Scaling up the cluster size beyond the replication factor will see an improvement in throughput only when there are many independent queues. See [this article](https://www.rabbitmq.com/blog/2020/06/18/cluster-sizing-and-other-considerations#how-does-redundancy-affect-sizing) for more details.

Further reading:
- [Kafka design](https://kafka.apache.org/24/documentation.html#design) (official docs)
- [RabbitMQ Queues](https://www.rabbitmq.com/docs/queues) and [Streams](https://www.rabbitmq.com/docs/streams) (official docs)
- [Kafka 101](https://highscalability.com/untitled-2/)

### Databases

- [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem): choose 2 out of "Consistency", "Availability" and "Partition Tolerance".
- Most traditional SQL databases are Consistent and Available, and also provide [ACID](https://en.wikipedia.org/wiki/ACID) guarantees.
- Many distributed databases are also ACID-compliant. They choose "Consistency" over "Availability".
- Distributed databases that use [Eventual Consistency](https://en.wikipedia.org/wiki/Eventual_consistency) as their consistency model choose "Availability" over "Consistency".
- Defining good indexes improve read/search performance, but reduce write-performance.
- Horizontal partitioning (sharding): distributing different rows across multiple instances.
  - Used to distribute the compute-workload.
  - Indexes also need to be partitioned.
- Vertical partitioning: distributing different columns across multiple instances.
  - Used to group columns based on their access patterns (read or write-heavy).
- Types of databases:
  - Key-value stores. Example: Redis
  - Document stores. Example: MongoDB, CouchDB
  - Wide-column stores. Example: Cassandra, HBase, BigTable
  - Graph databases. Example: Neo4j
- A [data warehouse](https://www.coursera.org/articles/data-warehouse) is a scalable service/solution built on top of some database(s), that provides data analysis capabilities. Example: Google BigQuery, Amazon RedShift

Interesting articles:
- [When to (and not) use Cassandra](https://towardsdatascience.com/when-to-use-cassandra-and-when-to-steer-clear-72b7f2cede76)
- [Cassandra vs. MongoDB](https://aws.amazon.com/compare/the-difference-between-cassandra-and-mongodb/)
- [Scaling Postgres Horizontally](https://stackoverflow.com/a/34840217/2849934)
- [How to implement sharding in PostgreSQL](https://www.squash.io/tutorial-on-database-sharding-in-postgresql/)

### Distributed Data Processing

Spark is the successor to the previously hyped concept of "[MapReduce](https://en.wikipedia.org/wiki/MapReduce)". Spark can do "map", "reduce" and so much more! :)

See [this chapter](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch01.html) for an overview.

## Miscellaneous Topics

- [Consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing), a technique to map inputs to a set of slots, where new slots can be added or existing slots removed with minimal changes to the input-mapping.
- [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter), a probabilistic data structure to test whether an element is a member of a set, where false positives are possible but false negatives are not.
- [Count-min sketch](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch), a probabilistic data structure that can serve as an approximate frequency table of events. This, combined with a min-heap, can be used to keep track of the top-k events (approx.) in a stream of data.
- [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog), an approximate algorithm for estimating the number of distinct elements in a large collection (or stream).

## References

- [General Advice from ByteByteGo](https://www.youtube.com/watch?v=o-k7h2G3Gco)
- [A step-by-step guide from ByteByteGo](https://www.youtube.com/watch?v=i7twT3x5yv8)
- [An example design from ByteByteGo](https://www.youtube.com/watch?v=M4lR_Va97cQ) (note that the trade-offs and reasoning discussion is very important during the interview)
- [The System Design Primer](https://github.com/donnemartin/system-design-primer)
- [The Twitter Problem](https://www.hiredintech.com/system-design/the-twitter-problem/)
- [Biggest Mistakes to Avoid](https://www.youtube.com/watch?v=4Q2fokImKfM)
- [Top K Problem (Heavy Hitters)](https://www.youtube.com/watch?v=kx-XDoPjoHw)
- [More questions to practice](https://www.educative.io/blog/meta-system-design-interview)
