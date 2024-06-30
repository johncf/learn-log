# System Design Interview

Tackling the system design interview.

Do take a look at [general tips](./general.md) on problem solving first. (TLDR; make sure to consider different approaches and discuss its pros and cons, when choosing a design or component.)

## Basic Steps

1. Understand requirements and establish scope (5 minutes)
   - High-level objectives (use-cases)
   - Functional requirements (features)
   - Non-functional requirements (scale, latency, etc.)
1. Capacity estimation and constraints (2 minutes)
   - Assumptions (e.g. read-write ratio, daily active users)
   - Compute effective request rates to be handled
1. High-level design (10 minutes)
   - Design end-user APIs to meet functional requirements
   - Basic components of the system (load balancers, caching systems, DB, etc.)
   - List required services (e.g., application server, logging service, etc.)
   - Choices of each component are *not* explored (e.g. MySQL vs. MongoDB)
1. Low-level/component design (10 minutes)
   - Component specific APIs or internal design (e.g. database schema)
   - Analyze the need for DB indexing, DB replication, DB partitioning
   - Discuss caching options (e.g. CDN, database caching, client-side caching)
   - Do NOT discuss anything outside established scope
1. Understanding bottlenecks and improvements (5 minutes)
   - Issues that could happen with a component (e.g. a "celebrity" user)
   - Modifications that could resolve the issue
1. Evaluation and wrap-up (5 minutes)
   - Quick overview of the design and why it can handle the scale.

## Quick Tips

- Breaking the problem into sub-problems is a big part of the interview!
- Drive the conversation! Make sure to propose the design and suggest which part you could dive deeper into.
- Make absolutely sure to discuss trade-offs and alternatives!
- Try to find a part of the system that you're designing which you can draw from your previous experience, and discuss that in more detail (deep-dive).
- Feel free to let the interviewer know the parts that you're unsure of.
- Identify parts of the system that could be a bottleneck or a single-point-of-failure.

Sources: [Intro to Architecture and System Design Interviews](https://www.youtube.com/watch?v=ZgdS0EUmn70); [5 Common Mistakes to Avoid](https://www.youtube.com/watch?v=ySfpftMZnoU&list=PLTCrU9sGyburBw9wNOHebv9SjlE4Elv5a&index=29)

## Common Non-Functional Requirements

- Scalability: the ability of a system to handle a growing amount of work.
- Availability: the probability that a system is operational at a given time
  - Example: stay operational even with partial internal network failures
  - Strategies: load balancing, failover mechanisms (switching to backup systems on failure)
- Reliability: the probability that a system will produce correct outputs up to some given time
  - Example: recover from device failures or natural disasters
  - Strategies: built-in redundancies, replication, error monitoring
- Performance: throughput, latency
  - Strategies: horizontal and vertical scaling, data partitioning, caching
- Observability: the ability to collect data about programs' execution, modules' internal states, etc.
- Serviceability or Maintainability: the speed with which a system can be repaired or maintained

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

### Message Queues

- To decouple "processing" from "data producers".
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
- [Kafka design](https://kafka.apache.org/24/documentation.html#design)
- [RabbitMQ Queues](https://www.rabbitmq.com/docs/queues) and [Streams](https://www.rabbitmq.com/docs/streams)

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

### Distributed Data Processing

Spark is the successor to the previously hyped concept of "[MapReduce](https://en.wikipedia.org/wiki/MapReduce)". Spark can do "map", "reduce" and so much more! :)

See [this chapter](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch01.html) for an overview.

## Miscellaneous Topics

- [Consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing)
- [Count-min sketch](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch), a data structure that can serve as an approx. frequency table of events. This, combined with a min-heap, can be used to keep track of the top-k events (approx.) in a stream of data.

## References

- [Video from ByteByteGo](https://www.youtube.com/watch?v=i7twT3x5yv8)
- [The Twitter Problem](https://www.hiredintech.com/system-design/the-twitter-problem/)
- [Biggest Mistakes to Avoid](https://www.youtube.com/watch?v=4Q2fokImKfM)
- [Top K Problem (Heavy Hitters)](https://www.youtube.com/watch?v=kx-XDoPjoHw)
