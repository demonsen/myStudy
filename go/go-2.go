package main
import "fmt"

func main(){
    a,b := 1,3
    var c = a + b
    d := [] int {1,2,3,4,5}
    var e *int
    var f **int
    fmt.Println("hello.")
    fmt.Println(c)
    for i := 0; i <= 4; i++ {
        fmt.Print(d[i],"---\n")
    }
    e = &a
    f = &e
    fmt.Printf("a=%d,&a=%x,e=%x,*e=%d,&e=%x\n",a,&a,e,*e,&e)
    fmt.Printf("f=%x,**f=%d\n",f,**f)
    for i := 1; i <= 9; i++ {
        for j := 1; j <= 9; j++ {
            if j >= i {
                fmt.Printf(" %d*%d=%2d ",i,j,i*j)
            } else {
                fmt.Print("        ")
            }
        }
        fmt.Println()
    }
}
