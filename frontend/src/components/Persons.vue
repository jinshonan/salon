<script setup>
// this is the background for showing the staff ON THE HOMEPAGE
import person from "./Person.vue";
import { reactive, defineProps, onMounted } from "vue";
import { RouterLink } from "vue-router";
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'  // beautify the loading process
import axios from "axios";  // http client for mock backend test

const state = reactive({  // using reactive instead of ref 
    persons: [],
    isLoading: true
})

// Add this import for your local JSON file
import personsData from '@/persons.json';

onMounted(async () => {
    try {
        // Option 1: Load from local JSON file
        state.persons = personsData.persons;
        
        // Option 2: Or load from an API endpoint if you prefer
        // const response = await axios.get('/api/persons');
        // state.persons = response.data.persons;
    } catch (error) {
        console.error('Failed to load stylists data:', error);
    } finally {
        state.isLoading = false;
    }
});

</script>

<template>
    <section class="bg-blue-50 px-4 py-10">
        <div class="container-xl lg:container m-auto"> 
            <h2 class="text-3xl font-bold text-blue-500 mb-6 text center">Stylists</h2>
            <!-- Show loading spinner while loading is true -->
            <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
                <PulseLoader />
            </div>

            <!-- Show staff when loading is done -->
            <div v-else class="grid grid-cols-1 md:grid-cols-4 gap-6">
                <person v-for="person in state.persons.slice(0, state.persons.length)" 
                :key="person.id" 
                :person="person" />  
            </div>
        </div>
    </section>
</template>