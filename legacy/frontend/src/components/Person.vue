<script setup>
import { defineProps, ref, computed } from 'vue';
import { RouterLink } from 'vue-router';

const props = defineProps({
    person: {
        type: Object,
        required: true
    }
});

// this file is for the cards on the home page
// Create a computed property for the image path
const imagePath = computed(() => {
    return props.person?.photo || '/assets/img/default.png'; // Fallback to default if photo is missing
});
</script>

<template>
    <div class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
        <RouterLink :to="'/staff/' + person.id" class="block">
            <div class="relative pb-[100%] group">
                <!-- Image container with fixed aspect ratio -->
                <img 
                    :src="imagePath" 
                    :alt="person.name.kanji" 
                    class="absolute inset-0 w-full h-full object-contain"
                    @error="$event.target.src = '/assets/img/default.png'"
                />
                
                <!-- Overlay that appears on hover -->
                <div class="absolute inset-0 bg-pink-200 bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center text-white">
                    <div class="text-center">
                        <h3 class="text-xl font-semibold mb-2">{{ person.name.kanji }}</h3>
                        <div class="border border-white inline-block px-4 py-1 mt-2">
                            <span class="text-sm tracking-wider">MORE</span>
                        </div>
                    </div>
                </div>
            </div>
        </RouterLink>
    </div>
</template>