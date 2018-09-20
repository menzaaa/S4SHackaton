<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <router-link to="/foo">Go to Foo</router-link><br>
    <router-link to="/bar">Go to Bar</router-link><br><br>

    <router-link to="/user/foo">/user/foo</router-link><br>
    <router-link to="/user/bar">/user/bar</router-link>
    
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
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

a {
  color: #42b983;
}
</style>
