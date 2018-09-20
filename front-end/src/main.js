import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }
const User = { templates: '<div>user</div>' }

const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar },
  { path: 'user/:id', component: User }
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

const app = new Vue({
  router,
  render: h => h(App)
}).$mount('#app')