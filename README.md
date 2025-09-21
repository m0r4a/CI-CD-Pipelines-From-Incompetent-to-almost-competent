# CI/CD Pipelines for GitHub Actions and GitLab CI/CD - From incompetent to almost close to be competent

This is my "mini" project where I will practice by creating 30 pipelines: 15 in GitHub Actions and 15 in GitLab CI/CD. The idea is to start with very basic and simple pipelines in GitHub and gradually increase the complexity level until switching to GitLab, where I attempt to approach it in a way that doesn't repeat the general and basic pipeline concepts but still "resets" the difficulty level.

This will README will be a tracker of my progress but you can check [the pipelines file](./pipelines.md) to read each pipeline's description.

> [!NOTE]
> Most of this is meant to be ran using [act](https://github.com/nektos/act)
> 
> A great resource for this project is [the official documentation](https://docs.github.com/en/actions) and [the  awesome list for GitHub actions](https://github.com/sdras/awesome-actions)
>
> If you use this repo's `.actrc` when you work on artifact's they will be stored in `./artifacts` by default see [this issue](https://github.com/nektos/act/issues/329) and `act help | grep artifact` for more details.

## GitHub Actions Pipelines

- [x] 1. Basic Pipeline (Python "Hello World")
- [x] 2. Unit Tests in Python
- [x] 3. Lint and Tests in Node.js/TypeScript
- [x] 4. Code Coverage in Python
- [x] 5. Multi-version Tests (Matrix)
- [x] 6. Multi-language Pipeline (Python + Go)
- [x] 7. Build and Publish Docker Image
- [ ] 8. Publish Package to PyPI
- [ ] 9. Publish Package to npm
- [ ] 10. Java Project Build and Tests (Maven/Gradle)
- [ ] 11. Multi-JDK Tests (Java Matrix)
- [ ] 12. Automatic GitHub Release Creation
- [ ] 13. GitHub Pages Deployment
- [ ] 14. Scheduled Pipeline (Cron)
- [ ] 15. Manual Approval Workflow

## GitLab CI/CD Pipelines

- [ ] 1. Basic Multi-stage Pipeline (build, test, deploy)
- [ ] 2. Cache and Artifacts Between Stages
- [ ] 3. Explicit Dependencies with needs
- [ ] 4. Multi-language Project in GitLab
- [ ] 5. Monorepo with Path Rules
- [ ] 6. Parent-Child Pipelines
- [ ] 7. Multi-project Pipeline
- [ ] 8. CI/CD Variables and Secrets
- [ ] 9. GitLab Pages Deployment
- [ ] 10. Code Analysis and Security
- [ ] 11. Build Docker and Use Container Registry
- [ ] 12. Basic Kubernetes Deployment
- [ ] 13. Helm Deployment to Kubernetes
- [ ] 14. Automated Release with Tags
- [ ] 15. Scheduled Pipeline (Schedules)
