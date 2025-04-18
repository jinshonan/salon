import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import JobsView from '@/views/JobsView.vue';
import NotFoundView from '@/views/NotFoundView.vue';
import JobView from '@/views/JobView.vue';
import AddJobView from '@/views/AddJobView.vue';
import EditJobView from '@/views/EditJobView.vue';
import StaffView from '@/views/StaffView.vue';
import PersonView from '@/views/PersonView.vue';
import BookingView from '@/views/BookingView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/staff',
            name: 'staff',
            component: StaffView,
        },
        {
            path: '/staff/:id',
            name: 'person',
            component: PersonView,
        },
        {
            path: '/booking/:id',
            name: 'booking',
            component: BookingView,
        },
        {
            path: '/jobs',
            name: 'jobs',
            component: JobsView,
        },
        {
            path: '/jobs/:id',
            name: 'job',
            component: JobView,
        },
        {
            path: '/jobs/add',
            name: 'add-job',
            component: AddJobView,
        },
        {
            path: '/jobs/edit/:id',
            name: 'edit-job',
            component: EditJobView,
        },
        {
            path: '/:catchAll(.*)',
            name: 'not-found',
            component: NotFoundView,
        },
        // Add a catch-all route to handle unexpected paths
        // HomeView weren't rendering so I had to trouble shoot
        // {
        //     path: '/:pathMatch(.*)*',
        //     name: 'NotFound',
        //     component: HomeView // Or create a 404 page component
        // }
    ]
});

export default router;