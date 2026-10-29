# CNIT-381 — Weekly Labs
Weekly labs for CNIT 381.
## Week 1
Created the repository, configured Git, cloned it locally, and made my first commit.
## Week 2
Practiced team Git collaboration using VS Code and Git commands: feature branches, commits, pushes, pull requests code review, squash merging, and resolving a merge conflict while building the UW-Stout CNIT Cybersecurity Technology Hub.
## Week 3 
Containerized a duplicate-IP checker with Docker and published the image to Docker Hub.
## Week 4 
Built a network config pipeline: an intent file plus a generator, containerized, 
with CI/CD that regenerates and validates the configs on every change. 
## Week 5
Called the GitHub REST API from Python to read my repo and create an issue.
## Week 6: IP Plan Check Pipeline 
**What I built:** A Python checker for our IP address plan, packaged in Docker, run by GitHub Actions on every push, that opens a GitHub issue through the API when the plan has errors.
**Repo:** https://github.com/NateSD2/ip-plan-check
## Week 8: OSPF by Hand, Then Automated 
What I did: configured OSPF manually, ran a provided playbook that automated it, and wrote my own playbook to back up the configs. What I learned is how Ansible can automate network configurations on multiple routers using a playbook. I also learned how to us ios_config to configure routers and back up their running configurations to files, making networks management more efficient.