Task Management API

A small HTTP API for managing tasks.

What it does

The service provides a simple list of tasks and health information.

Available endpoints:

GET / - returns information about the API

GET /healthz - checks if the service is running

GET /tasks - returns the list of tasks

Requirements

Python 3

Bash

How to run

Run the service with:

./scripts/run.sh

The service uses the PORT environment variable.

If PORT is not set, it uses port 8080.

Example:

PORT=8080 ./scripts/run.sh

How to test

Run:

./scripts/test.sh

The test script runs 3 tests and prints:

TESTS: 3/3

Project structure

Task-Management-API/
├── src/
│   └── server.py
├── tests/
│   └── test_server.py
├── scripts/
│   ├── run.sh
│   └── test.sh
├── .gitignore
└── README.md

Port

The default port is 8080.

The application binds to 0.0.0.0 and can use a different port through the PORT environment variable.