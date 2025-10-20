import grpc
from concurrent import futures
import folder_pb2, folder_pb2_grpc
import os

class FolderServiceServicer(folder_pb2_grpc.FolderServiceServicer):
    def ListFiles(self, request, context):
        files = os.listdir(request.path)
        return folder_pb2.FolderResponse(filenames=files)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
folder_pb2_grpc.add_FolderServiceServicer_to_server(FolderServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
