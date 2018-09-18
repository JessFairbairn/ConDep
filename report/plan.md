# Dissertation Plan

## Introduction

- [ ] Explanation of project + aims
- [ ] Explanation of structure

## Background

- [ ] NLP -> FOs, using argument roles

### Conceptual Dependencies

- [x] Introduce general concept
- Explain primitives
- Strengths
  - [X] Syntax independent
  - [x] Metaphor- fits with our 'metaphor' based understanding of the world
  - [ ] Possibility of applying ML
- Criticisms
  - [ ] Comments on possibly redundant primitives
  - [ ] Abandoning primitives altogether

## Implementation

### Primitives

- [X] Only using subset
  - [X] Redundant primitives?

### Natural language to Actions

- event into predicate argument
  - identify verb sense
  - [ ] apply nlp to work out various roles of each argument
  - find corresponding prim

- info from prim assigned to verb sense
  - affected_attribute, constraints
  - merging verb and prim definitions

- emit/eject example for different verbs with same primitive

- constraints (maybe)

### Actions to Natural Language

- Simulation reports events
- filtering primitives first then filtering verbs
  
### Physics Simulation

- [ ] Compound Entity
- [ ] Details about tracking various properties
- [ ] Spawning action events

### Predicate Argument Conclusions from CD

- [X] Theory/ templates for events
- [ ] Code

## Results

## Discussion

- [X] Expressing verbs as CDs- success
  - [X] Recognition- end conditions for experiments
- [ ] Extracting predicate-arg info from CDs- success?!

## Conclusion

### Future Work

- ML
  - Come up with an example ML may struggle with- e.g. where a scenario necessarily implies another event, but which isn't part of the definition
- Verify if the primitives are necessary and sufficient
- Testing in other domains