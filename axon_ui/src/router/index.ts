import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DocumentView from '../views/DocumentView.vue'
import NetworkView from '../views/NetworkView.vue'

const BASE_URL = 'https://neuron.dhaval.cloud'

const router = createRouter({
	history: createWebHashHistory(BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/network',
      name: 'network',
      component: NetworkView
    },
    {
      path: '/document/:id',
      name: 'document',
      component: DocumentView
    },
  ]
})

export default router
