## Software Engineering

### Software Development Lifecycle

1. Exploration phase:
   - Brainstorm ideas, set goals, identify risks
   - Functional specifications: project and scope; use-cases and non-goals; assumptions, risks and feasibility; possible solutions and requirements; defining milestones, etc.
   - Data exploration; quick prototyping etc.
1. Design phase: use case diagram, API design, API sequence diagrams, class diagrams, database design etc.
1. Implementation phase: parallel implementation of various parts, with unit tests
1. Quality check phase: writing extensive integration tests, verification
1. Deployment phase: ensure proper monitoring, updateability, backups, revertibility etc.

Different project management aproaches:

- **Waterfall model**: go through each phase, one at a time, in-detail. Slow deliveries, and may not keep up with changing requirements.
- **Agile model**: very short design phase; prototyping and implementation may happen simultaneously; short quality check phase. Fast deliveries, but possibly more maintenance cost due to higher chances of bugs and inflexible design decisions
- **Iterative model**: divide the project into several small deliverable milestones. Faster deliveries and user feedback opportunities. May need clever simplifications; may not always be possible to design a small deliverable for each step.
- **Spiral model**: similar to iterative model?

### Machine Learning Project Lifecycle

Source: [Intro to ML in Production](https://www.coursera.org/learn/introduction-to-machine-learning-in-production)

1. Scoping: define the project and constraints
   - Constraints: realtime or batched, cloud or edge/browser, compute resources, latency, privacy
1. Data: define, explore, collect
   - Define inputs and targets; establish rules to minimize inconsistencies
   - Explore usability of publicly available datasets
   - Collect, label and organize
1. Modeling: baseline, select, train, evaluate
   - Define various useful metrics for evaluation (e.g.: F-score)
   - Establish baseline performance
     - Human Level Performance (HLP) for unstructured data (image, audio, natural language)
     - Performance of a quick prototype (using a small model, or a public model), or older model
   - When selecting a model, ensure model is powerful enough
     - Train to over-fit the model on a small subset of data
   - Error analysis
     - Try to give meaningful context "tags" for the mistakes
     - Compare with baseline performance for each tag
     - Estimate model uncertainty (confidence); how to calibrate confidence?
   - Iterate with changes to models, hyperparameters, dataset, data augmentation, feature-set, etc.
     - Have good experiment tracking (MLOps) system with:
       - Replicability/reproducibility (hyperparameters, dataset metadata, code/library versions etc.)
       - Results, error analysis, and summary metrics
       - Resource monitoring
1. Deployment: deploy, then monitor & maintain
   - Shadow-mode (parallel) deployment, Canary (gradual ramp-up) deployment
   - Monitoring:
     - software metrics (memory, compute, latency etc.)
     - input metrics (input length, fraction of missing values, image brightness)
     - output metrics (fraction of missing values, is null/empty/error)
     - user behavior (rerunning, switching to manual mode etc.)
     - set thresholds for notifications/alarms (for detecting drifts etc.)
