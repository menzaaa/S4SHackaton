<template>
  <div id="app">
    <router-view class="navigation" name="navigation"></router-view>
    <router-view class="main" name="main"></router-view>
    <router-view @authenticated="setAuthenticated"></router-view>
    <router-view @logout="logout"></router-view>
    <router-view @current_user="getCurrentUser"></router-view>
  </div>
</template>

<script>

export default {
  name: 'app',
  data () {
    return {
      msg: 'So you think you can program',
      authenticated: false,
      current: null
    }
  },
  mounted(){
    if(!this.authenticated) {
      this.$router.replace({name: "login"});
    }
  },
  methods: {
    setAuthenticated(status, user) {
      this.authenticated = status;
      this.current_user = user;
    },
    logout(){
      this.authenticated = false;
      this.$router.replace({name: "login"});
    },
    getCurrentUser(){
      return this.current_user;
    },
  },
  watch: {
      '$route': function () {
        console.log('route watcher: ' + this.$route.path)
      }
    },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}
</style>
