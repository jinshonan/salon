<script setup>
// this page is the background for the jobcards
import JobListing from "./JobListing.vue";
// import jobData from "@/jobs.json";  // refactored to fetch that from a server
// import { ref, defineProps, onMounted } from "vue";  // use ref instead of reactive
import { reactive, defineProps, onMounted } from "vue";
import { RouterLink } from "vue-router";
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'  // beautify the loading process
import axios from "axios";  // http client for mock backend test

defineProps({
    limit: Number,
    showButton: {
        type: Boolean,
        default: false,
    }
});

// const jobs = ref([]);  this is refactored to reactive

const state = reactive({  // using reactive instead of ref (no idea why)
    jobs: [],
    isLoading: true
})

onMounted(async () => {
    try {
        const response = await axios.get('/api/jobs');  // holy shit I added jobs there
        state.jobs = response.data;
    } catch (error) {
        console.error('Error fetching jobs', error);
    } finally {
        state.isLoading = false;
    }
})

// const jobs = ref(jobData.jobs);  // different from the tutorial. not jobData
// console.log(jobs.value);
</script>

<template>
    <section class="bg-blue-50 px-4 py-10">
        <div class="container-xl lg:container m-auto">
            <h2 class="text-3xl font-bold text-blue-500 mb-6 text center">スタッフ一覧</h2>
            <!-- Show loading spinner while loading is true -->
            <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
                <PulseLoader />
            </div>

            <!-- Show listings when loading is done -->
            <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <JobListing v-for="job in state.jobs.slice(0, limit || state.jobs.length)" 
                :key="job.id" 
                :job="job" />  
            </div>
        </div>
    </section>
    <section v-if="showButton" class="m-auto max-w-lg my-10 px-6">
      <RouterLink
        to="/jobs"
        class="block bg-black text-white text-center py-4 px-6 rounded-xl hover:bg-gray-700"
        >View All Jobs</RouterLink
      >
    </section>
</template>