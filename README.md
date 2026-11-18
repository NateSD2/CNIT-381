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
## Week 9: 
Build a Network and Automated It End to End 
What I built: a CML topology (2 routers, a switch, and an Ubuntu control node), bootstrapped the devices by hand, then used Ansible to configure loopbacks, EIGRP, a login banner, and to back up all device. 
What I learned: I learned how to build and configure a multi-device network using Cisco Modeling Labs and automate network configurations using Ansible. I gained experience with YAML playbooks, inventory files, SSH connectivity, and Cisco IOS modules. I also learned how to automate repetitive tasks such as configuring loopback interfaces, enabling EIGRP routing, applying login banners, and backing up device configurations.
## Week 10: Ansible on a CSR with the DEVASC VM 
What I did: moved from CML to the DEVASC VM and a CSR1000v, set up the hosts inventory and ansible.cfg, backed up the config, and configured IPv6. What I learned: I learned how to use Ansible to automate network configuration on a physical style Cisco router using the DEVASC VM. I also learned how to create an inventory file, configure Ansible settings, back up router configurations, and use automation to configure IPv6 and deploy.
## Week 11 AI Network Agent Web App
What I built:
I built a Streamlit web application on my CML Ubuntu node with two pages: an AI Network Agent that can inspect and configure R1, R2, and SW1 using plain-English requests, and a Live Network Dashboard that displays interface status pulled directly from the devices.
What I learned:
I learned how an MCP tool server, an AI model, and a web application work together. The MCP server provides tools that allow the AI agent to interact with the network devices. The application sends the user's request along with the available tools to Anthropic's AI model, which determines which tools to call and what arguments to use. The agent then executes those tools and returns the results. I also learned how Streamlit creates the web interface with separate pages for the Network Agent and Live Dashboard. The dashboard works differently from the agent because it skips the AI entirely and uses Netmiko to connect directly to the devices and retrieve their live interface information.