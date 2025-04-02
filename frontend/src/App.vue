<!-- <script setup>
 import Navbar from './components/Navbar.vue';
 import { RouterView } from 'vue-router';
</script>

<template>
  <Navbar />
  <RouterView />
</template> -->


<!-- HomeView weren't rendering so I had to trouble shoot and below is the version by Claude -->
<script setup>
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <Navbar />
  <RouterView />
  <Footer />
  <!-- <div id="app">
    // seems that there is no need to put it in a div
    <RouterView />
  </div> -->
</template>