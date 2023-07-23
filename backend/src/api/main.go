package main

import (
	"github.com/gin-gonic/gin"
	"github.com/gin-contrib/cors"
	"api/controller"
)

func main() {
	router := gin.Default()

	router.Use(cors.Default())

	router.GET("/", controller.Hello)

	router.GET("/info", controller.GetInfoAll)
	// router.GET("/albums/:id", getInfoById)

	router.Run(":8080")
}
