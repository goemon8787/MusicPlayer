<template>
  <v-bottom-sheet inset>
    <template v-slot:activator="{ props }">
      <div class="text-center">
        <v-btn
          v-bind="props"
          color="red"
          size="x-large"
          text="Click Me"
        ></v-btn>
      </div>
    </template>

    <v-sheet>
      <v-progress-linear model-value="50"></v-progress-linear>

      <v-list>
        <v-list-item>
          <v-list-item-title>The Walker</v-list-item-title>
          <v-list-item-subtitle>Fitz & The Trantrums</v-list-item-subtitle>
          <template v-slot:append>
            <v-btn icon="mdi-rewind" variant="text"></v-btn>

            <v-btn
              :class="{ 'mx-5': display.mdAndUp }"
              :icon="pauseStatus"
              variant="text"
              @click="playOrPause"
            ></v-btn>

            <v-btn
              :class="{ 'me-3': display.mdAndUp }"
              class="ms-0"
              icon="mdi-fast-forward"
              variant="text"
            ></v-btn>
          </template>
        </v-list-item>
        <v-list-item>
          <v-list-item-title>Current Time: {{ currentTime }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-sheet>
  </v-bottom-sheet>
</template>

<script setup>
import music from "@/assets/sample-data/ゆいかおり/LUCKY DUCKY!!/LUCKY DUCKY!!.flac";
import { watch, ref, onMounted } from "vue";
import { useDisplay } from "vuetify";

const playing = ref(false);
const display = useDisplay();
const audioPlayer = ref(new Audio(music));

const playOrPause = () => {
  if (playing.value) {
    audioPlayer.value.pause();
    playing.value = false;
  } else {
    audioPlayer.value.play();
    playing.value = true;
  }
};

const pauseStatus = ref("mdi-play");

const currentTime = ref(0);

const updateCurrentTime = () => {
  currentTime.value = audioPlayer.value.currentTime;
};

watch(playing, (newPlaying) => {
  pauseStatus.value = newPlaying ? "mdi-pause" : "mdi-play";
});

onMounted(() => {
  audioPlayer.value.addEventListener("timeupdate", updateCurrentTime);
});
</script>

<script>
export default {
  computed: {
    display() {
      return this.$vuetify.display;
    },
  },
};
</script>
