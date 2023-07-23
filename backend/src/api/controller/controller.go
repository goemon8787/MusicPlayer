package controller

import (
	"api/database"
	"net/http"

	"github.com/gin-gonic/gin"
)

func Hello(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"message": "hello world",
	})
}

func GetInfoAll(c *gin.Context) {
	infoList, err := database.GetInfoAll()
	if err != nil {
		panic("In controller.GetInfoAll")
	}
	c.JSON(http.StatusOK, infoList)
}
