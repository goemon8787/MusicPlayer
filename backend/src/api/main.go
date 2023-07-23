package main

import (
	"github.com/gin-gonic/gin"

	"api/controller"
)

func main() {
	router := gin.Default()

	router.GET("/", controller.Hello)

	router.GET("/info", controller.GetInfoAll)
	// router.GET("/albums/:id", getInfoById)

	router.Run(":8080")
}
