package main

import (
    "foo"
    "math/rand"
    "fmt"
    "time"
)

func main() {
    foo.Foo1()
    a := "a112233"
    rand.Seed(time.Now().UnixNano())
    for i:=0; i<20;i++ {
        fmt.Print(rand.Intn(100) ," ")
        fmt.Print(a)
    }

}
