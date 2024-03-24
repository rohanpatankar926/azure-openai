install azure cli
1.generate a k8s cluster with azure
2.generate the rbac role with azure
command-->az ad sp create-for-rbac --name "yourApp" --role contributor \
                            --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} \
                            --json-auth

3.create a namespace in k8s cluster
4.change the name of all the 


commands to run in k8s cluster
1.sudo kubectl create namespace azure-ml
2.sudo kubectl create secret docker-registry azure-ml-secret --docker-server=DOCKER_REGISTRY_SERVER --docker-username=DOCKER_USER --docker-password=DOCKER_PASSWORD --docker-email=DOCKER_EMAIL -n azure-ml
