# Research Foundation

## 1. Introduction

AURA was developed in response to a real-world problem observed in
educational and public environments: children with Autism Spectrum
Disorder (ASD) or sensory processing differences often experience
episodes of sensory overload that temporarily impair their ability
to communicate verbally.

This document outlines the theoretical and scientific foundation
that guided the system design of AURA.

---

## 2. Autism Spectrum Disorder & Communication Challenges

According to the Diagnostic and Statistical Manual of Mental Disorders
(DSM-5-TR), Autism Spectrum Disorder is characterized by:

- Persistent difficulties in social communication
- Restricted or repetitive patterns of behavior
- Differences in sensory processing

Many individuals with ASD experience:
- Hypersensitivity to sound, light, or touch
- Difficulty filtering environmental stimuli
- Increased stress response in unpredictable environments

During high-stress moments, executive functioning may decrease.
Speech production may temporarily become inaccessible.
This is not unwillingness — it is neurological overload.

This temporary mutism significantly increases:
- Anxiety
- Frustration
- Risk of escalation
- Misinterpretation by adults

Therefore, alternative communication pathways are critical.

---

## 3. Sensory Overload & Fight-or-Flight Response

Sensory overload activates the body's stress system.
When stimuli exceed processing capacity, the nervous system may
shift into a fight-or-flight state.

In this state:
- Heart rate increases
- Cortisol levels rise
- Cognitive flexibility decreases
- Verbal reasoning declines

High-level executive tasks (like navigating menus or searching
through icons) become difficult or impossible.

Any assistive device intended for crisis use must account for
this neurophysiological shift.

---

## 4. Cognitive Load Theory

Cognitive Load Theory explains that working memory capacity
is limited.

When stress increases, effective working memory capacity decreases.

Touchscreen AAC systems typically require:
- Visual scanning
- Icon recognition
- Sequential navigation
- Multi-step selection

These processes demand working memory and attentional control.

Mechanical single-action buttons significantly reduce:
- Decision steps
- Visual dependency
- Motor precision demands

By mapping one button directly to one emotional state,
AURA reduces cognitive load to a single physical action.

This design choice is directly informed by cognitive load principles.

---

## 5. Augmentative & Alternative Communication (AAC)

AAC systems support individuals who cannot rely on verbal speech.

AAC methods include:
- Low-tech (PECS cards)
- High-tech (tablets, speech-generating devices)
- Hybrid systems

Research by Mirenda (2003) emphasizes that AAC systems
must be functional, accessible, and context-appropriate.

In crisis scenarios:
- Speed is more important than complexity
- Reliability is more important than customization
- Simplicity is more important than feature richness

AURA was designed as a crisis-optimized AAC tool,
not as a full replacement for structured AAC therapy.

---

## 6. Co-Regulation Theory

Emotional regulation in children often requires external support.

Co-regulation refers to the process where a trusted system
or adult helps stabilize emotional state through:

- Predictability
- Sensory grounding
- Calm signaling

AURA integrates co-regulation by:
1. Allowing the child to signal their state
2. Immediately providing calming audio feedback
3. Informing adults how to respond appropriately

Thus, AURA is not only a communication device,
but also a regulatory support system.

---

## 7. Tactile Interface Justification

Why physical buttons?

Research in sensory processing suggests that tactile feedback can:
- Provide grounding input
- Increase predictability
- Reduce visual dependency
- Support self-regulation behaviors

Additionally:
- Buttons work without looking
- Buttons work during panic
- Buttons provide physical confirmation of activation

Touchscreens lack physical feedback and may increase sensory stress.

---

## 8. Embedded Systems Considerations

Assistive systems must also be technically reliable.

AURA integrates principles from embedded systems engineering:

- Deterministic input mapping
- Low-latency response
- Memory management optimization
- Fault tolerance (GPIO cleanup)
- Controlled boot process (Headless Linux)

Hybrid RAM Cache architecture was designed to prevent
Linux OOM (Out Of Memory) crashes — ensuring reliability
during repeated activation.

In assistive technology, system stability is an ethical requirement.

---

## 9. Ethical Design Principles

The project follows key ethical design principles:

- Dignity-preserving form factor (integrated backpack)
- No stigmatizing visual labeling
- Non-invasive data collection (current version)
- Low-risk electrical configuration
- Supervised usage framework

Technology must adapt to the user —
the user should not adapt to technology.

---

## 10. Limitations of Current Research Scope

This project is an engineering prototype.
Limitations include:

- No clinical trials
- No biometric data validation
- No long-term user studies
- No regulatory certification

Future research should involve:
- Behavioral outcome measurement
- Controlled pilot testing
- Collaboration with therapists
- Usability studies in school environments

---

## 11. References

American Psychiatric Association. (2022).
Diagnostic and Statistical Manual of Mental Disorders (5th ed., text rev.).

Mirenda, P. (2003).
Toward functional augmentative and alternative communication for students with autism.
Language, Speech, and Hearing Services in Schools.

Ayres, A. J. (1972).
Sensory Integration and Learning Disorders.

Embedded Systems Design Principles – General Engineering References.