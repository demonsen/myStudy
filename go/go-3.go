package main

import (
     "fmt"
     "math"
     "os"
     //"syscall"
)

func fib(n int) int{
    if n < 2 {
        return n
    }
    return fib(n-1) + fib(n-2)
}

func main() {
    var i = [5]int {1,2,3,4,5}
    fmt.Println(len(i),i)
    for j:=0; j<len(i); j++ {
        fmt.Println(i[j])
    }
    fmt.Println(1.69*1.7)
    a := 16.0
    b := 2.0
    c := a*b
    
    fmt.Printf("%f, %.2f\n",c, math.Sqrt(a))
    fmt.Println(fib(5))
    //syscall.Stat()
    fmt.Println(os.Stat("go-4"))
}
