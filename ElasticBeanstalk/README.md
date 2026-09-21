# PHP Application on AWS Elastic Beanstalk

A versioned PHP sample application prepared for **AWS Elastic Beanstalk** deployment and deployment-strategy practice.

The repository keeps the four application versions used in the lab:

- **v1** — initial Elastic Beanstalk application
- **v2** — application update
- **v3** — application update used with Rolling deployment
- **v4** — application update used with Rolling with Additional Batch

The application also demonstrates:

- scheduled requests through `cron.yaml`
- application logging under `/tmp`
- Elastic Beanstalk log collection through `.ebextensions/logging.config`
- application-version changes
- environment capacity changes
- All at Once, Rolling, and Rolling with Additional Batch deployment strategies

## Repository Structure

```text
.
├── application-versions/
│   ├── php-v1/
│   │   ├── .ebextensions/
│   │   │   └── logging.config
│   │   ├── cron.yaml
│   │   ├── index.php
│   │   ├── scheduled.php
│   │   ├── styles.css
│   │   ├── logo_aws_reduced.gif
│   │   └── EBSampleApp-PHP.iml
│   ├── php-v2/
│   ├── php-v3/
│   └── php-v4/
├── docs/
│   └── DEPLOYMENT-GUIDE.md
├── scripts/
│   └── package-version.sh
├── .gitignore
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Application Flow

```text
Browser
   |
   v
AWS Elastic Beanstalk
   |
   +---- PHP application
   |       |
   |       +---- index.php
   |       +---- scheduled.php
   |
   +---- Scheduled task
   |       |
   |       +---- cron.yaml
   |
   +---- Application logs
           |
           +---- /tmp/sample-app.log
           |
           +---- .ebextensions/logging.config
```

## Versioning Strategy

The repository intentionally stores each deployment version separately so that the deployment lab can demonstrate how the application changes over time.

| Version | Purpose |
|---|---|
| `php-v1` | Initial application |
| `php-v2` | Application update to version 2 |
| `php-v3` | Application update to version 3 |
| `php-v4` | Application update to version 4 |

The visible application version is reflected by the page title/message in each version.

## Creating an Elastic Beanstalk Source Bundle

Elastic Beanstalk expects the application files at the **root of the uploaded source bundle**.

Use the helper script:

```bash
chmod +x scripts/package-version.sh

./scripts/package-version.sh php-v1
./scripts/package-version.sh php-v2
./scripts/package-version.sh php-v3
./scripts/package-version.sh php-v4
```

This creates:

```text
dist/
├── mysampleapp-source-v1.zip
├── mysampleapp-source-v2.zip
├── mysampleapp-source-v3.zip
└── mysampleapp-source-v4.zip
```

Each generated ZIP contains the corresponding PHP application directly at its root.

## Deployment Lab

The complete step-by-step Elastic Beanstalk workflow is documented in:

[`docs/DEPLOYMENT-GUIDE.md`](docs/DEPLOYMENT-GUIDE.md)

The guide covers:

1. Launching the application
2. Uploading version 1
3. Updating to version 2 with **All at Once**
4. Increasing environment capacity
5. Updating to version 3 with **Rolling**
6. Updating to version 4 with **Rolling with Additional Batch**
7. Monitoring application versions and environment health
8. Terminating the environment
9. Restoring the terminated environment
10. Deleting the application

## Important Configuration

The original lab configuration uses:

```text
Platform:
PHP 8.3 running on 64bit Amazon Linux 2023

Application:
MySampleApp

Environment:
MySampleApp-env

Initial deployment:
mysampleapp-source-v1
```

The lab also uses:

```text
Service Role:
Create and use new service role

EC2 instance profile:
aws-elasticbeanstalk-ec2-role
```

with the policies specified in the deployment guide.

## Scheduled Task

`cron.yaml` configures a task that calls:

```text
/scheduled.php
```

once per minute:

```yaml
version: 1
cron:
  - name: "task1"
    url: "/scheduled.php"
    schedule: "*/1 * * * *"
```

The scheduled endpoint records task information in:

```text
/tmp/sample-app.log
```

## Application Logging

The `.ebextensions/logging.config` file configures Elastic Beanstalk to collect:

```text
/tmp/sample-app*
```

for bundled logs and:

```text
/tmp/sample-app.log
```

for tail logs.

This makes the log activity visible through Elastic Beanstalk's logging features.

## Local Validation

PHP syntax can be checked with:

```bash
php -l application-versions/php-v1/index.php
php -l application-versions/php-v1/scheduled.php
```

Repeat for v2, v3 and v4.

## Scope

This repository is primarily an **AWS Elastic Beanstalk deployment and learning project**. It is intentionally focused on application deployment, versioning, scheduled tasks, logging, capacity, and deployment strategies rather than being a production-ready PHP framework application.

## Author

**Ramazan Agac**

GitHub: https://github.com/ramznagc
