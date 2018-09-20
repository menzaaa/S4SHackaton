import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'
import VueRouter from 'vue-router'
//test?
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

//components
import Users from './components/users/Users.vue'
import User from './components/users/User.vue'
import NavigationBar from './components/layout/NavigationBar.vue'
import Quizzes from './components/quizzes/Quizzes.vue'
import Quiz from './components/quizzes/Quiz.vue'
import CreateQuiz from './components/quizzes/Create.vue'
import Question from './components/questions/Questions.vue';
import Login from './components/login/Login.vue';

Vue.use(VueRouter)
Vue.use(BootstrapVue)

Vue.prototype.$current_user = null;

const UserProfile = { template: '<div>profile</div>' }
const UserPosts   = { template: '<div>posts</div>'}

const routes = [
  {
    path: '/',
    redirect: {
      name:'login'
    }
  },
  {
    path: '/users',
    name: 'users',
    components: {
      navigation: NavigationBar,
      main: Users,
    },
  },
  {
    path: '/login',
    name: 'login',
    components: {
      navigation: null,
      main: Login
    }
  },
  { 
    path: '/user/:id',
    components: {
      navigation: NavigationBar,
      main: User,
    },
    name: 'user',
    children: [
      {
        path: 'profile',
        component: UserProfile
      },
      {
        path: 'posts',
        component: UserPosts
      }
    ]
  },
  {
    path: '/quizzes',
    name: 'quizzes',
    components: {
      navigation: NavigationBar,
      main: Quizzes
    }
  },
  {
    path: '/quizzes/:id',
    name: 'quiz',
    components: {
      navigation: NavigationBar,
      main: Quiz
    }
  },
  {
    path: '/quizzes/create',
    name: 'quiz.create',
    components: {
      navigation: NavigationBar,
      main: CreateQuiz
    }
  },
  {
    path: '/questions/:id',
    name: 'questions',
    components: {
      navigation: NavigationBar,
      main: Question
    }
  }
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

const app = new Vue({
  router,
  render: h => h(App)
}).$mount('#app')