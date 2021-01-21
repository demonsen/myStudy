# go



## 目录结构
```
/work/go/src
├── foo
│   └── foo.go
└── main
    └── main.go
```
export GOPATH=/work/go/

```
cat foo/foo.go 

package foo
import "fmt" 
# 函数开头一定要大写
func Foo1() { 
     fmt.Println("Fool1 ----")
}
```


```
cat main/main.go 

package main
import "foo"

func main() {
    foo.Foo1()
}

```
