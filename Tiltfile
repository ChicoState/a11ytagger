# Tiltfile for a11ytagger local development

# Deploy using kustomize
k8s_yaml(kustomize('./manifests'))

# Build backend Docker image with live updates
docker_build(
    'a11ytagger-backend',
    context='./backend',
    dockerfile='./backend/Dockerfile',
    live_update=[
        sync('./backend/server', '/app/server'),
        sync('./backend/a11ytagger', '/app/a11ytagger'),
        run(
            'uv pip install -r requirements.txt',
            trigger=['./backend/requirements.txt', './backend/pyproject.toml']
        ),
    ],
)

# Build frontend Docker image
docker_build(
    'a11ytagger-frontend',
    context='./frontend',
    dockerfile='./frontend/Dockerfile',
)

# Configure backend service
k8s_resource(
    'backend',
    port_forwards='3000:3000',
    labels=['backend'],
)

# Configure frontend service  
k8s_resource(
    'frontend',
    port_forwards='8080:80',
    labels=['frontend'],
)

# Set resource limits
update_settings(max_parallel_updates=2)
