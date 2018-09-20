<template>
	<div class="user">
		<div class="loading" v-if="loading">
			Loading...
		</div>
		<div v-if="error" class="error">
			{{ error }}
		</div>
		<h2>User {{ $route.params.id }}</h2>
		<div class="test" v-if="user">
			<p>{{ user.first_name }} | {{ user.last_name}}</p>
		</div>
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
				loading: false,
				data: null,
				error: null,
				user: null
			}
		},
		created () {
			// fetch the data when the view is created and the data is
			// already being observed
			this.fetchData()
		},
		methods: {
			fetchData () {
				this.error = this.post = null
				this.loading = true
				const axios = require('axios')
				instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa('max' + ':' + 'qwerty');
				const that = this
				instance.get('/users/' + this.$route.params.id )
					.then(function (response) {
						console.log(response);
						that.user = response.data
						that.loading = false
					});
			},
			setTimeout() {
				this.loading = false
				this.user = {
					first_name: "robert",
					last_name: "kleef"
				}
			}
		}
	}
</script>