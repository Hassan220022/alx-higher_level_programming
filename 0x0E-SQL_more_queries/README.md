# SQL More Queries Project

## Overview

This project focuses on deepening SQL skills with advanced queries in MySQL. Topics include creating users, managing privileges, understanding key constraints, and utilizing JOIN and UNION operations.

## Learning Objectives

- Create and manage users and their privileges on a MySQL server.
- Understand and implement PRIMARY and FOREIGN KEYs.
- Utilize SQL constraints like NOT NULL and UNIQUE.
- Retrieve data from multiple tables using advanced JOIN operations.
- Explore subqueries, UNIONs, and how to handle multiple joins.

## Requirements

- All SQL files should end with a newline.
- SQL queries must include comments describing the task.
- Use uppercase for SQL keywords.
- Each file should start with a comment about the task.
- MySQL 8.0 on Ubuntu 20.04 LTS is used for all scripts.

## Installation

Install MySQL on Ubuntu 20.04:

```

sudo apt update
sudo apt install mysql-server

```

## Usage

Scripts can be executed on a MySQL server like so:

```

cat script.sql | mysql -u root -p

```

## Files

- `0-privileges.sql`: List all privileges for specified users.
- `1-create_user.sql`: Create a MySQL user with all privileges.
- Further files follow the pattern set for specific SQL tasks.

## Author

ALX Software Engineering Programme
