import Vue from 'vue'
import Router from 'vue-router'
import VideosList from '@/components/VideosList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'VideosList',
      component: VideosList
    }
  ]
})
