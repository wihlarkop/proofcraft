# Jobs and Messaging

For each asynchronous flow, make the path observable:

producer/command -> durable state -> enqueue/publish -> consumer -> side effects -> acknowledgement.

State whether the message is a command/request or a fact/event. Define source of truth separately from transport. A broker carrying data does not automatically become the authoritative business store.
