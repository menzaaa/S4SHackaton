<template>
	<div class="user">
		<div class="loading" v-if="loading">
			Loading...
		</div>
		<div v-if="error" class="error">
			{{ error }}
		</div>	
		<div class="row justify-content-center">
            <div class="col col-lg-8">
                <div v-if="user" class="card">
                    <div class="card-header">
						{{ user.first_name }} {{ user.last_name }}
					</div>
					<div class="card-block">
						<h4 class="card-title">About</h4>
						<p class="card-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
					</div>
					<div class="card-footer text-muted">
						Last active: 2 days ago
					</div>
                </div>
            </div>
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