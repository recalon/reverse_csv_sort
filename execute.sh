docker build -t techtest .
docker run \
  --rm \
  --mount type=bind,source="$(pwd)/data/outputs",target=/tmp/reverse_string_sort/out \
  techtest
