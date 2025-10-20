import grpc
import folder_pb2, folder_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = folder_pb2_grpc.FolderServiceStub(channel)
    response = stub.ListFiles(folder_pb2.FolderRequest(path="."))
    print("Files:", response.filenames)
