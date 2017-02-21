package main

import (
	pb "./user"
	"fmt"
        "os"
        "strings"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"gopkg.in/mgo.v2"
	"gopkg.in/mgo.v2/bson"
	"log"
	"net"
)

const (
	port = ":50051"
)

type server struct {
	c *mgo.Collection
}

func (s *server) AddUser(ctx context.Context, in *pb.User) (*pb.Status, error) {
	fmt.Printf("Inserting : ", *in)
	err := s.c.Insert(&in)
	if err != nil {
		return &pb.Status{State: pb.Status_FAILED, Message: "failed!"}, nil
	}
	return &pb.Status{State: pb.Status_SUCCESSFUL, Message: "Successull!"}, nil
}

func (s *server) DeleteUser(ctx context.Context, in *pb.User_Name) (*pb.Status, error) {
	err := s.c.Remove(bson.M{"name": in.Name})
	if err != nil {
		return &pb.Status{State: pb.Status_FAILED, Message: "failed!"}, nil
	}
	return &pb.Status{State: pb.Status_SUCCESSFUL, Message: "Successull!"}, nil
}

func (s *server) GetUsers(ctx context.Context, in *pb.UserList) (*pb.Users, error) {
	result := pb.Users{}
	err := s.c.Find(bson.M{}).All(&result.UserList)
	if err != nil {
		fmt.Println(err)
		return &result, nil
	}
	fmt.Println("record:", result)
	return &result, nil
}

func (s *server) GetUser(ctx context.Context, in *pb.User_Name) (*pb.User, error) {
	result := pb.User{}
	fmt.Println(*in)
	err := s.c.Find(bson.M{"name": in.Name}).One(&result)
	if err != nil {
		fmt.Println(err)
		return &result, nil
	}
	fmt.Println("record:", result)
	return &result, nil
}

func (s *server) UpdateUser(ctx context.Context, in *pb.User) (*pb.Status, error) {
	err := s.c.Update(bson.M{"name": in.Name}, &in)
	if err != nil {
		return &pb.Status{State: pb.Status_FAILED, Message: "failed!"}, nil
	}
	return &pb.Status{State: pb.Status_SUCCESSFUL, Message: "Successull!"}, nil
}

func main() {
        db_ip := os.Args[1]
        db_ip = strings.Replace(db_ip, "tcp://", "", 1)
	fmt.Printf("Helloworld %s:27017", db_ip)
        log.Print("Log everything" + db_ip)
	session, err := mgo.Dial(db_ip)
	if err != nil {
		panic(err)
	}
	defer session.Close()
	session.SetMode(mgo.Monotonic, true)

	collection := session.DB("micro").C("Users")

	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	// Creates a new gRPC server
	s := grpc.NewServer()
	pb.RegisterUserdbServer(s, &server{c: collection})
	s.Serve(lis)
}
