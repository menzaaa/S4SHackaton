<template>
    <div class="login">
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <div v-if="login" class="form-group purple-border">
            <h1>Login</h1>
            <pre>
                <input type="text" name="username" v-model="input.username" placeholder="Gebruikersnaam" />
                <input type="password" name="password" v-model="input.password" placeholder="Wachtwoord" />   
            </pre>
        </div>
        <button v-on:click="login" type="button" class="btn btn-primary">Log in</button>
    </div>
</template>
<script>
    import axios from 'axios';

    const instance = axios.create({
        baseURL: 'http://localhost:5000/'
    })
    export default {
        data () {
            return {
                input: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            login(){
                if(this.input.username != "" & this.input.password != ""){
                    instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa(this.input.username + ':' + this.input.password);
                    const that = this;
                    instance.get('/login')
                        .then(function (response) {
                            console.log(response);
                            if(response.status >= 200 && response.status < 300) {
                                that.$emit('authenticated', true, response.data);
                                that.$router.replace({name: "users"});
                            }

                        });
                        console.log(this.$current_user);
                }
            }
        }
    }
</script>