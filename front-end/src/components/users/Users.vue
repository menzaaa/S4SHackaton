<template>
    <div class="user">
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <h2>Users</h2>
        <table v-if="users" class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">First</th>
                    <th scope="col">Last</th>
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
                setTimeout(this.setTimeout, 1000)
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