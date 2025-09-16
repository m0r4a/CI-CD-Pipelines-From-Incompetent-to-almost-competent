# CI/CD Pipelines for GitHub Actions and GitLab CI/CD - From incompetent to almost close to be competent

This is my "mini" project where I will practice by creating 30 pipelines: 15 in GitHub Actions and 15 in GitLab CI/CD. The idea is to start with very basic and simple pipelines in GitHub and gradually increase the complexity level until switching to GitLab, where I attempt to approach it in a way that doesn't repeat the general and basic pipeline concepts but still "resets" the difficulty level.

## GitHub Actions Pipelines

### 1. Basic Pipeline (Python "Hello World")
Workflow that triggers on push to any branch and executes a trivial Python script (e.g., print "Hello World").

**Tasks:** Clone repository, configure Python (`actions/setup-python`), execute script or simple test.

**Learning:** Basic GitHub Actions YAML syntax, `on: push` events, using `actions/checkout@vX` to get code, and simple job commands.

### 2. Unit Tests in Python
Pipeline that runs unit tests on a small library with pytest when pushing or creating a pull request.

**Tasks:** Checkout, install dependencies (`pip install -r requirements.txt`), execute pytest to run tests.

**Learning:** Configure Python environments in Actions, pass arguments to commands, visualize test results and report failures.

### 3. Lint and Tests in Node.js/TypeScript
Workflow for a Node.js (or TypeScript) project that runs a linter (e.g., ESLint) and then executes its test suite (e.g., with Jest) on push or PR.

**Tasks:** Setup Node.js (`actions/setup-node@vX`), install packages (`npm ci`), run `npm run lint` and `npm test`.

**Learning:** Configure Node environment in Actions, use cache (`actions/cache@vX` for `node_modules/` if desired), integrate linters and view their output.

### 4. Code Coverage in Python
Similar to the test pipeline, but also generates a coverage report with coverage.py. The pipeline should store the report (artifact) or upload it to a service like Codecov.

**Tasks:** Run tests with coverage (`coverage run`), generate report (`coverage xml` or similar), use `actions/upload-artifact` to save results, configure secret token for Codecov (optional).

**Learning:** Using artifacts in Actions to share files, managing secrets (e.g., `$GH_TOKEN`), and integration with external code analysis tools.

### 5. Multi-version Tests (Matrix)
Pipeline that uses GitHub Actions' matrix strategy to run Node or Python tests across multiple interpreter or OS versions (e.g., Node 14, 16, and 18).

**Tasks:** Define a `strategy: matrix:` block with versions (e.g., Node or Python), so GitHub Actions executes a job simultaneously for each combination. Repeat installation/test steps in each generated job.

**Learning:** The matrix strategy allows running jobs in parallel for different configurations without duplicating the workflow. This lets you verify your project works in different environments (operating systems, language versions, etc.).

### 6. Multi-language Pipeline (Python + Go)
A workflow with at least two parallel jobs: one to test a small Python project and another to compile/test a Go project.

**Tasks:** Job "python_test": configure Python and install dependencies, execute pytest. Job "go_build": configure Go (`actions/setup-go@vX`), run `go test` or `go build`.

**Learning:** Execute simultaneous jobs for different languages, combine different sets of steps, explore how each job uses its own runner and base image.

### 7. Build and Publish Docker Image
Pipeline that builds a Docker image from a Dockerfile and publishes it to Docker Hub (or another registry) when pushing to the main branch.

**Tasks:** Login to Docker Registry using a secret (e.g., username/password in GitHub Secrets), use `docker/build-push-action` to build the image and push to registry.

**Learning:** Interact with external services in CI, configure official Docker actions, manage secure credentials, and generate container artifacts.

### 8. Publish Package to PyPI
Pipeline that automates publishing a Python library to PyPI when creating a new tag or release.

**Tasks:** Detect tag/release event (`on: push` with `tags:` or `on: release`), build package (`python setup.py sdist bdist_wheel`), use official `pypa/gh-action-pypi-publish` action with PyPI token stored in Secrets.

**Learning:** Automate releases, work with tag and version events, manage access tokens for package repositories.

### 9. Publish Package to npm
Similarly, create a pipeline that builds and publishes a Node package to npm when tagging a version in GitHub.

**Tasks:** Configure `actions/setup-node` with npm authentication (`NODE_AUTH_TOKEN`), run `npm ci` and `npm publish`.

**Learning:** JavaScript package publication flow, semantic version control, using secrets for authentication.

### 10. Java Project Build and Tests (Maven/Gradle)
Pipeline for a simple Java application that compiles code (using Maven or Gradle) and runs unit tests.

**Tasks:** Checkout, configure Java (`actions/setup-java@vX`), run `mvn test` or `gradle test`.

**Learning:** Integrate Java projects in Actions, view build reports, explore differences in Java execution vs scripting.

### 11. Multi-JDK Tests (Java Matrix)
Extends the previous Java pipeline by adding a matrix strategy to test across multiple Java versions (e.g., 8, 11, and 17).

**Tasks:** Define a matrix with JDK versions, repeat build/test steps for each JDK.

**Learning:** Expand matrix for a project requiring compatibility with multiple Java versions, consolidating the matrix concept.

### 12. Automatic GitHub Release Creation
Workflow that, when pushing to main or creating a tag, compiles the project and creates a GitHub Release with generated binary artifacts (e.g., Go executables or Java JARs).

**Tasks:** Detect event (push to main or tags), compile artifacts, use `actions/create-release` and `actions/upload-release-asset` to generate a Release and upload associated files.

**Learning:** Automate the final delivery process, connect the pipeline with GitHub version management and deploy production-ready artifacts.

### 13. GitHub Pages Deployment
Pipeline to generate and deploy a static site to GitHub Pages every time you push to the main branch. For example, using MkDocs, Hugo, or any static generator.

**Tasks:** Install generator (Python, Go, Node, etc.), build site to HTML, use `peaceiris/actions-gh-pages` (or similar) to publish to gh-pages branch.

**Learning:** Automatically publish documentation, use artifacts as static pages, and leverage native Pages integration.

### 14. Scheduled Pipeline (Cron)
Workflow that runs on a fixed schedule (e.g., once a day or week) for maintenance tasks or regular tests.

**Tasks:** Configure `on: schedule` section with cron expression, for example to run nightly tests, security analysis, or report generation.

**Learning:** Trigger time-based pipelines, understand scheduled events in GitHub Actions.

### 15. Manual Approval Workflow
Pipeline where a deployment job requires manual approval before executing. This is achieved through protected environments.

**Tasks:** Define an environment in the repo (e.g., Production) with required approval; in the workflow, assign the final job to that environment. After build and test, the pipeline waits for approval in GitHub interface before deploying.

**Learning:** Control pipeline permissions, introduce human reviews, and use GitHub Actions environments for deployment jobs.

---

## GitLab CI/CD Pipelines

In GitLab CI/CD, pipelines are defined in a `.gitlab-ci.yml` file using YAML keywords. They consist of jobs grouped into stages that execute in sequential order. For example, a `build` stage executes before `test`, and within each stage, jobs run in parallel. Pipelines can be triggered automatically on events like push, merge request, or on a programmed schedule. Building on these fundamentals and assuming prior knowledge from GitHub pipelines, here are 15 more advanced ideas for GitLab CI/CD:

### 1. Basic Multi-stage Pipeline (build, test, deploy)
A simple pipeline with three stages.

**Tasks:** In `build`, compile or prepare the project (e.g., execute `go build` or `mvn package`). In `test`, run unit tests. In `deploy`, perform a simulated deployment or publish artifacts (e.g., a success message).

**Learning:** Define `stages: [build, test, deploy]`, understand sequential stage execution, and how progression to the next stage only occurs if all previous jobs succeed.

### 2. Cache and Artifacts Between Stages
Pipeline that uses `cache:` for accelerators and `artifacts:` to share files.

**Tasks:** In `build`, generate dependencies (e.g., front-end build or download libraries) and store cache of dependency directory. Also, save compiled artifacts. In `test`, recover those artifacts (dependencies or executable) and execute them.

**Learning:** Reduce execution times using cache (e.g., Maven, npm, pip), and share results (binaries, packages) between stages using artifacts.

### 3. Explicit Dependencies with needs
Pipeline that optimizes flow using the `needs` keyword. For example, having two test jobs where one depends on the other.

**Tasks:** Create jobs in the same `test` stage and use `needs: ['job1']` so one job waits for artifacts from another.

**Learning:** Accelerate pipeline by allowing some jobs to trigger as soon as their dependencies are ready (instead of waiting for the entire stage to complete).

### 4. Multi-language Project in GitLab
Similar to multi-language in GitHub, define several parallel jobs for different languages in the same pipeline.

**Tasks:** Define separate jobs, e.g., `py_tests`, `go_build`, `js_lint`, each with its appropriate Docker image (`image: python:3.9`, `image: golang:1.17`, `image: node:14`, etc.).

**Learning:** Execute multiple environments simultaneously, see how GitLab assigns runners according to image, and combine independent results.

### 5. Monorepo with Path Rules
Pipeline for repositories with multiple services/folders. Use rules (`rules: changes`) to execute jobs only if specific files change.

**Tasks:** For example, define a `backend` job that only runs if there are changes in `backend/`, and another `frontend` if `frontend/` changes. Each job uses `rules: changes:` to filter.

**Learning:** Dynamic pipelines based on context, avoid running unnecessary tasks, and practice advanced conditions in `.gitlab-ci.yml`.

### 6. Parent-Child Pipelines
Divide a complex pipeline into sub-pipelines.

**Tasks:** Create a job in the main pipeline that uses `trigger:` or `include:` to trigger one or more child pipelines (defined in other YAML files). For example, the job `trigger: child-pipeline.yml`.

**Learning:** Modularize pipeline, delegate parts to sub-workflows (child pipelines), useful in large projects or monorepos.

### 7. Multi-project Pipeline
Orchestrate pipelines across multiple repositories.

**Tasks:** Configure the pipeline so that, upon successful completion, it uses `trigger: project: my-group/other-project` to launch a pipeline in another repo.

**Learning:** Integration between projects, GitLab multi-project pipelines, coordinate deliveries between different components.

### 8. CI/CD Variables and Secrets
Pipeline that makes intensive use of protected variables.

**Tasks:** Define variables in GitLab (e.g., `AWS_ACCESS_KEY`, `DOCKER_PASSWORD`) with `masked` and `protected`. Use them in jobs to deploy, publish to registry, or interact with APIs.

**Learning:** Secure credential management, differentiate environment variables and pipeline variables, and how to hide sensitive information.

### 9. GitLab Pages Deployment
Pipeline that builds a static site and deploys it with Pages.

**Tasks:** In `build` stage, generate HTML files (using static tools). Then create the special `pages` job, which must store the public directory as an artifact (e.g., `public/`). GitLab will automatically publish those artifacts at `https://<user>.gitlab.io/<project>`.

**Learning:** Learn the special `pages` job, GitLab Pages configuration and URL addresses, and see how Pages consumes generated artifacts.

### 10. Code Analysis and Security
Integrate automatic code scanning.

**Tasks:** Use GitLab's integrated scanners (e.g., adding `sast` and `container_scanning` jobs from Auto DevOps template), or run tools like ESLint or SonarQube and export reports.

**Learning:** Ensure code quality and security in CI, understand SAST/DAST reports, and configure additional jobs in the pipeline.

### 11. Build Docker and Use Container Registry
Pipeline that builds a Docker image and uploads it to GitLab's Container Registry.

**Tasks:** Use the official Docker image (`docker:latest`) or similar, do `docker login` using `$CI_REGISTRY_USER` and `$CI_REGISTRY_PASSWORD`, then `docker build` and `docker push registry.gitlab.com/your-namespace/your-project:tag`.

**Learning:** Use GitLab's integrated private registry, authentication with internal CI variables, and the difference between `image:` (for the job) and built containers/artifacts.

### 12. Basic Kubernetes Deployment
Pipeline that builds containers and deploys them to a Kubernetes cluster.

**Tasks:** In previous stages, compile and push Docker image to registry. Then, in `deploy` stage, use a `kubectl` image or include kubectl in the job to apply deployment YAML files to the cluster (need to configure cluster credentials, e.g., `KUBECONFIG` or use GitLab's Kubernetes integration).

**Learning:** Basic CI/CD concepts to Kubernetes: handle access credentials, apply YAML manifests, and understand continuous deployment to clusters (first pipeline with K8s).

### 13. Helm Deployment to Kubernetes
Pipeline that uses Helm to package and deploy an application to K8s.

**Tasks:** Store a Helm Chart in the repo. In the pipeline, use an image with Helm (e.g., `alpine/helm`), and run `helm repo add`, `helm upgrade --install` commands pointing to your cluster.

**Learning:** Advanced application management in K8s using Helm, package releases and parameterize deployments (second pipeline with K8s).

### 14. Automated Release with Tags
Pipeline that triggers with a Git tag (specifying `only: - tags`) and generates a GitLab Release with artifacts.

**Tasks:** Configure pipeline for `only: [tags]`, compile artifacts (binaries, packages, etc.), and use GitLab API or a job with `curl` to create a Release associated with the tag, uploading generated artifacts.

**Learning:** Similar to GitHub release, here you learn about versioning (Git TAGS), and GitLab's Releases functionality.

### 15. Scheduled Pipeline (Schedules)
Example of pipeline that runs periodically in GitLab.

**Tasks:** While schedules are configured in GitLab's interface (Project > CI/CD > Schedules), the pipeline itself can include regular jobs, for example a `nightly_build` job that checks status or performs backup.

**Learning:** Automatic periodic maintenance and testing through GitLab's CI/CD Schedules, preparing your pipeline to run without intervention according to a cron schedule.

> [!NOTE]
> Most of this is almost fully AI generated, the important part are the pipelines in question.
