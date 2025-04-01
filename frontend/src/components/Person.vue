<script setup>
import { defineProps, ref, computed } from 'vue';
import { RouterLink } from 'vue-router';

const props = defineProps({
    person: Object
})

// Create a computed property for the image path
const imagePath = computed(() => {
    // For Vite, we need to use dynamic imports for assets
    try {
        // Remove the 'src/' prefix from the path
        const path = props.person?.photo?.replace('src/', '') || '';
        return new URL(`../../${path}`, import.meta.url).href;
    } catch (error) {
        console.error('Error loading image:', error);
        return '/images/default-avatar.jpg';
    }
});

</script>

<!-- <template>
    <div class="bg-white rounded-xl shadow-md relative">
        <RouterLink :to="'/staff/' + person.id"></RouterLink>
    </div>
</template> -->

<template>
    <div class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
        <RouterLink :to="'/staff/' + person.id" class="block">
            <div class="relative pb-[75%]">
                <!-- Image container with fixed aspect ratio -->
                <img 
                    :src="imagePath" 
                    :alt="person.name" 
                    class="absolute inset-0 w-full h-full object-cover"
                    @error="$event.target.src = '/images/default-avatar.jpg'"
                />
            </div>
            <div class="p-4">
                <h3 class="text-xl font-semibold text-blue-700">{{ person.name }}</h3>
                <p v-if="person.specialty" class="text-gray-600 mt-1">{{ person.specialty }}</p>
                <p v-if="person.description" class="text-gray-500 mt-2 line-clamp-2">{{ person.description }}</p>
                <div class="mt-3 flex justify-between items-center">
                    <span class="text-blue-500 font-medium">View Profile</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                    </svg>
                </div>
            </div>
        </RouterLink>
    </div>
</template>