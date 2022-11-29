# Build all containers
build:
	docker-compose build

# Run all containers
up:
	docker-compose up

# Build and run all containers
run: build up

# Stop and remove all running containers
stop:
	docker-compose down