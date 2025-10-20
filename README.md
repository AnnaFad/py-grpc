# py-grpc

installation requirements: ```pip3 install grpcio grpcio-tools ```

converting proto file: ``` python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. folder.proto ```
