<script setup>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'  // beautify the loading process?
import BackButton from '@/components/BackButton.vue';
import { useRoute, RouterLink, useRouter } from "vue-router";
import { reactive, defineProps, onMounted } from "vue";
import { useToast } from 'vue-toastification';
import axios from "axios";  // http client for mock backend test
import personsData from '@/persons.json';

const route = useRoute();
const router = useRouter();
const toast = useToast();

const state = reactive({
    person: {},
    isLoading: true
})

onMounted(() => {
    console.log("Loaded personsData:", personsData); // Debugging
    
    if (personsData && Array.isArray(personsData.persons)) {
        const person = personsData.persons.find(person => person.id === route.params.id);
        if (person) {
            state.person = person;
        } else {
            console.error("Not found for ID:", route.params.id);
        }
    } else {
        console.error("personsData.persons is not an array or undefined:", personsData);
    }
    state.isLoading = false;
});

</script>

<template>
    <BackButton /> 
    <section v-if="!state.isLoading" class="flex flex-col md:flex-row items-center bg-blue-50 p-10 rounded-lg shadow-lg">
        <img 
        :src="state.person.photo || '/assets/img/default.png'" 
        :alt="state.person.name" class="w-64 h-64 object-cover rounded-lg shadow-md mb-6 md:mb-0 md:mr-6">
        <div class="text-center md:text-left">
            <h1 class="text-3xl font-bold">{{ state.person.name.kanji }}</h1>
            <h2 class="text-lg font-semibold text-gray-700">{{ state.person.title }}</h2>
            <p class="mt-4 text-gray-600">{{ state.person.description }}</p>
            <div class="mt-6">
                <RouterLink :to="`/booking/${state.person.id}`" class="bg-blue-500 text-white px-6 py-2 rounded-lg shadow hover:bg-pink-500 transition">
                    このスタイリストで予約
                </RouterLink>
            </div>
        </div>
    </section>

    <div v-else class="text-center text-gray-500 py-6">
        <PulseLoader />
    </div>
</template>