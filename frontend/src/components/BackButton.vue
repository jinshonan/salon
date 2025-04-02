<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <section>
      <div class="container m-auto py-6 px-6">
        <RouterLink
          to="/staff"
          class="text-blue-500 hover:text-blue-600 flex items-center"
        >
          <i class="pi pi-arrow-circle-left mr-3"></i> Back
        </RouterLink>
      </div>
    </section>
</template>