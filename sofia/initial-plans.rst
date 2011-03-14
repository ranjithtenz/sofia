What should the core do?
------------------------

One of the main ways for Sofia to communicate is to propose a "task", or
problem to be solved. Various agents should respond with:

- their state, in ('asleep', 'starting', 'awake', 'stopping')
- their confidence that they will be able to perform the task
- an estimate of the "problem size", which should correlate positively with
  the amount of time/space it will take to perform the task
  - Or should this simply come from the number of bytes in the message?
- other tasks they will need solved before they can provide the answer
  (a chunker may depend on a tagging task, for example). They don't necessarily
  have to state the exact input they will give the sub-task.

Then it chooses some set of agents -- waking them up if necessary -- and asks
them for their solutions to the task.

Agents can return solutions, requests for other tasks, "complaints" (that they
consider the task erroneous), or indications that they have given up.

Sofia keeps estimates of the time and space required to wake up different
agents, the mapping from the problem size to the actual amount of time they
take, and the reliability of the responses they return. It also logs results to
MongoDB.

Some results are *assertions*, and should be stored permanently in ConceptDB
datasets. Other results are transient and should only be cached for a while.

Assertions are another form of communication. Sofia announces when new
assertions are created. Agents can respond to support the assertion, oppose it,
indicate that they would like to spend some time thinking about it, or indicate
that they would have an opinion if they were awake.

What does an agent do?
----------------------
An agent has two parts: one responsible for communication with Sofia, and one
responsible for actual computation.

The computation part can be "awake" or "asleep". The communication part makes
estimates about what the computation part will be able to do with various
information. Sofia will use these estimates to decide whether to wake up the
agent.

An agent can also request to be woken up independently, perhaps when the
database accumulates a significant amount of training data.
