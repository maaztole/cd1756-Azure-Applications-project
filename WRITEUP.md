# Write-up Template

WRITEUP: VM vs. App Service Analysis

Introduction

The solution for this project could be hosted on Azure using Virtual Machines (VM) or App Service. The two alternatives have been assessed below on the parameters of cost, scalability, availability, and workflow. The assessment leads to choosing the App Service for deployment of this project.

1. Cost
Virtual Machine: The VM will be billed continuously irrespective of whether the application is serving traffic or not. There is no free tier for VMs and the lowest available tier will cost a certain amount per hour. In addition, there will be additional charges on account of OS disk, public IP, and outbound data transfer charges. There is no free tier for running a VM.

App Service: The App Service has a Free tier (F1), which incurs zero cost. This will serve the purpose of this application very well as the cost associated with other paid tiers is directly proportional to the additional compute and features and the minimum cost for hosting this application is $0. When deploying our sandbox subscription to App Service we hit a quota limit (Total VMs: 0) on a Basic App Service Plan in certain regions- this is a great illustration in practice of how the cost model works: any tier above Free tier hosts an actual VM behind the scenes and that is exactly what will incur a cost with a VM deployment.

Conclusion: App Service is the cheaper alternative for this project owing to the Free Tier offering.

2. Scalability

Virtual Machine: Scaling up of a VM involves sizing it up to a bigger instance (and hence a restart). Scaling out involves manually provisioning another VMs and then putting a load balancer in front of them. Scaling out is done manually and nothing else.

App Service: App Service provides both kinds of scaling and it can be achieved simply by changing tier/instance from the portal and can also be auto-scaled on metrics like CPU and request count

Conclusion: App Service is easier to scale because it is an inherent property of the platform.

3. Availability

Virtual Machine: Single VM is a single point of failure. High Availability requires creating an Availability Set or Availability Zone deployment, in addition to the load balancer. Responsibility for patching of OS, updating security, and managing the web server lies with the developer.
App Service: App Service has a published SLA. Automatic patching of the OS is provided and there is also automatic health monitoring/restarting of unhealthy instances. Even the Free tier takes care of everything except the application code.

Conclusion: Availability of the App Service is better because the platform will handle the OS layer.

4 Workflow

Virtual Machine: The deployment to a VM involves ssh-ing in, generation of ssh keys, installation of nginx/python/ODBC drivers, configuring reverse proxy manually, git pulling and restarting the app manually for every deployment All of the above steps have to be repeated for every deployment.

App Service: App Service's Deployment Center integrates with a GitHub repository and automatically sets up the CI/CD pipeline. On each commit in the main branch the application gets rebuilt and deployed automatically - there is no need for SSH access or configuration of server. For this particular project involving fixes in config.py and adding MSAL and logging code in views.py/_init__.py, we did a simple git push of our updates, which resulted in automatic deployment within a couple of minutes, which was evident from the GitHub actions tab and also the Azure App Service's Deployment Center logs.

Conclusion: App Service's CI/CD is faster and less prone to errors.

5. Choice & Justification

We are going to deploy the application on Azure App Service.

App Service has been chosen because the application does not involve any OS level customization or special networking requirements. It is just a Python Flask application which needs connectivity to SQL Database and Blob Storage, which is supported easily in the App Service using environment variables. The Free tier eliminates cost completely and GitHub Actions based CI/CD makes it easier to make the various changes that were required in this project config.py fix, MSAL authentication code, and application logging)

6. What Would Change This Decision

In case the application needs to support the following requirements a VM will be the better fit.

Requirement for root or OS level access: for example, installing system packages, running background daemons or services along with the web application or using a different runtime version not supported by the managed stacks of App Service.

Custom Networking Requirement: like requiring static outbound IP, custom configurations of VPN or Express Route, or detailed control over network stack provided by the managed networking of App Service. Hath traffic and need for optimization: at the high scale, a carefully right-sized and reserved instance VM or VM Scale Set can be more cost-effective than the correspondinst App Service Premium tier
Background tasks requirement: App Service is tuned for serving requests and responding, but an application that needs to perform some background tasks apart from request processing can be easier to manage on VM(or requires pairing with Azure Functions/WebJobs).
