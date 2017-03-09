#!/bin/bash

export GOPATH=`pwd`

go get github.com/golang/protobuf/protoc-gen-go/
go get github.com/grpc-ecosystem/grpc-gateway/
export PATH=`pwd`/bin:$PATH
pushd schema
protoc -I./ -I../src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis --go_out=Mgoogle/protobuf/struct.proto=github.com/golang/protobuf/ptypes/struct,\
Mgoogle/api/annotations.proto=github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/google/api:../client/go ophion.proto
popd