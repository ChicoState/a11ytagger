.PHONY: help cluster-create cluster-delete cluster-restart up down logs clean

# Default target - show help
help:
	@echo "Available targets:"
	@echo "  cluster-create   - Create k3d cluster"
	@echo "  cluster-delete   - Delete k3d cluster"
	@echo "  cluster-restart  - Restart k3d cluster"
	@echo "  up               - Start Tilt (deploys everything)"
	@echo "  down             - Stop Tilt"
	@echo "  logs             - Show Tilt logs"
	@echo "  clean            - Delete cluster and clean up"

# Create k3d cluster
cluster-create:
	@echo "Creating k3d cluster..."
	k3d cluster create a11ytagger \
		--registry-create a11ytagger \
		--wait
	@echo "Cluster created successfully!"

# Delete k3d cluster
cluster-delete:
	@echo "Deleting k3d cluster..."
	k3d cluster delete a11ytagger
	@echo "Cluster deleted successfully!"

# Restart k3d cluster
cluster-restart: cluster-delete cluster-create

# Start Tilt (deploys everything)
up:
	tilt up

# Stop Tilt
down:
	tilt down

# Show Tilt logs
logs:
	tilt logs

# Clean up everything
clean: down cluster-delete
	@echo "Cleanup complete!"
