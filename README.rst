So this is our grandiose idea to turn Open Mind Common Sense back into what it
was meant to be: an ensemble method of loosely-linked AI techniques.

Thoughts so far:

- Write the core in Python 3 if possible. This prevents us from
  depending on too many modules... which I see as kind of a plus.

- Store information about the ensemble in MongoDB.
  - incremental CORONA over MongoDB to determine reliability

- No particular requirement that ensemble code should be in Python. It should
  just run, and do reasonable JSON I/O.
  - Probably over STOMP. With some approximation to JSON-RPC.

