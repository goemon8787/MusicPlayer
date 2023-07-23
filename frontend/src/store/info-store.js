// Utilities
import { ref } from 'vue';
import { defineStore } from "pinia";

export const useInfoStore = defineStore("info", () => {
    const infoList = ref([])
    const error = ref(null)
    const loading = ref(false)

    const fetchInfoAll = async () => {
      infoList.value = [];
      loading.value = true;
      const response = await fetch("http://localhost:8080/info");
      if (response.ok) {
        infoList.value = await response.json();
      } else {
        error.value =`fetch error in info-store: ${response.status}`
        console.warn(error.value);
      }
      loading.value = false
    }

    return {
      infoList,
      error,
      loading,
      fetchInfoAll,
    }
  }
)
