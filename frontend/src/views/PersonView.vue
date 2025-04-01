<script setup>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'  // beautify the loading process?
import BackButton from '@/components/BackButton.vue';
import { useRoute, RouterLink, useRouter } from "vue-router";
import { reactive, defineProps, onMounted } from "vue";
import { useToast } from 'vue-toastification';
import axios from "axios";  // http client for mock backend test

const route = useRoute();
const router = useRouter();
const toast = useToast();

const jobId = route.params.id;

const state = reactive({
    job: {},
    isLoading: true
})

</script>

<template>
    <BackButton /> 
    <section v-if="!state.isLoading" class="bg-blue-50">
      <div class="container m-auto py-10 px-6">
        <div class="grid grid-cols-1 md:grid-cols-70/30 w-full gap-6">
          <main>
            <div
              class="bg-white p-6 rounded-lg shadow-md text-center md:text-left"
            >
              <div class="text-gray-500 mb-4">{{ state.job.type }}</div>
              <h1 class="text-3xl font-bold mb-4">{{ state.job.title }}</h1>
              <div
                class="text-gray-500 mb-4 flex align-middle justify-center md:justify-start"
              >
                <i
                  class="pi pi-map-marker text-xl text-orange-700 mr-2"
                ></i>
                <p class="text-orange-700">{{ state.job.location }}</p>
              </div>
            </div>

            <div class="bg-white p-6 rounded-lg shadow-md mt-6">
              <h3 class="text-blue-800 text-lg font-bold mb-6">
                Job Description
              </h3>

              <p class="mb-4">
                {{ state.job.description }}
              </p>

              <h3 class="text-blue-800 text-lg font-bold mb-2">Salary</h3>

              <p class="mb-4">{{ state.job.salary }} / Year</p>
            </div>
          </main>

          <!-- Sidebar -->
          <aside>
            <!-- Company Info -->
            <div class="bg-white p-6 rounded-lg shadow-md">
              <h3 class="text-xl font-bold mb-6">Company Info</h3>

              <h2 class="text-2xl">{{ state.job.company.name }}</h2>

              <p class="my-2">
                {{ state.job.company.description }}
              </p>

              <hr class="my-4" />

              <h3 class="text-xl">Contact Email:</h3>

              <p class="my-2 bg-blue-100 p-2 font-bold">
                {{ state.job.company.contactEmail }}
              </p>

              <h3 class="text-xl">Contact Phone:</h3>

              <p class="my-2 bg-blue-100 p-2 font-bold">{{ state.job.company.contactPhone }}</p>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <div v-else class="text-center text-gray-500 py-6">
        <PulseLoader />
    </div>
</template>