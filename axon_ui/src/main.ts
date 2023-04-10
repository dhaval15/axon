import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import '@mdi/font/css/materialdesignicons.css'

const vuetify = createVuetify({
  components,
  directives,
	icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    }
  },
})

import './assets/main.css'
import { VueForceGraph2D, VueForceGraph3D, VueForceGraphVR, VueForceGraphAR, GraphContextMenu } from 'vue-force-graph';

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.use(VueForceGraph3D)
app.use(VueForceGraph2D)

app.mount('#app')
