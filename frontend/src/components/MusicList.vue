<template>
    <v-table>
      <thead>
        <tr>
          <th class="text-left">Id</th>
          <th class="text-left">Artist</th>
          <th class="text-left">Title</th>
          <th class="text-left">Album</th>
          <th class="text-left">Path</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="info in store.infoList" :key="info.id">
          <td>{{ info.Id }}</td>
          <td>{{ info.Artist }}</td>
          <td>{{ info.Title }}</td>
          <td>{{ info.Album }}</td>
          <td>{{ info.Path }}</td>
        </tr>
      </tbody>
    </v-table>
</template>

<script setup>
import { useInfoStore } from "@/store/info-store";

const store = useInfoStore();
store.fetchInfoAll();
console.log(store.infoList)
</script>

<style></style>
