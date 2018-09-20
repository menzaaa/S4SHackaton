<template>
    <div class="user">
        <!-- <script src="https://unpkg.com/axios/dist/axios.min.js"></script> -->
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <h2>Users</h2>
        <table v-if="users" class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">username</th>
                    <th scope="col">profile</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in users" :key="user.id">
                    <th scope="row">{{ user.id }}</th>
                    <td>{{ user.first_name }}</td>
                    <td>{{ user.last_name }}</td>
                    <td><router-link :to="{ name: 'user', params: { id: user.id}}">Profile</router-link></td>
                </tr>
            </tbody>
        </table>
    <router-view></router-view>
    </div>
</template>

<script>
    const axios = require('axios')
    const instance = axios.create({
        baseURL: 'http://localhost:5000/'
    })
    export default {
        data () {
            return {
                users: null,
                loading: false,
                data: null
            }
        },
        created () {
            this.fetchData()
        },
        methods: {
            fetchData () {
                this.loading = true
                const axios = require('axios')
                instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa('test' + ':' + 'test');
                const that = this
                instance.get('/users')
                    .then(function (response) {
                        console.log(response);
                        that.users = response.data
                        that.loading = false
                    });
            },
            setTimeout() {
                this.loading = false
                this.users = [
                    { id: 1, first_name: "Robert", last_name: "Kleef" },
                    { id: 2, first_name: "Menno", last_name: "Prinzhorn" },
                    { id: 3, first_name: "Max", last_name: "van hasselt" },
                ]
            }
        },
    }
</script>