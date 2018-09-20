<template>
    <div class="questions">
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <div v-if="question" class="form-group purple-border">
            <label for="script-input">{{ question.name }}</label>
            <p>{{ question.description }}</p>
            <pre>
                <textarea class="form-control" id="script-input" rows="20"></textarea>
            </pre>
        </div>
        <button v-on:click="compileScript" type="button" class="btn btn-primary">Opslaan</button>
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
                question: null,
                loading: null
            }
        },
        created () {
            this.fetchData()
        },
        methods: {
            fetchData () {
                this.loading = true
                this.loading = true
				instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa('max' + ':' + 'qwerty');
				const that = this
				instance.get('/questions/' + this.$route.params.id )
					.then(function (response) {
						console.log(response);
						that.question = response.data
						that.loading = false
					});
                // setTimeout(this.setTimeout, 1000)
            },
            setTimeout() {
                this.loading = false
                this.question = { 
                    id: 1,
                    name: "Los dit programmeer probleem op 1",
                    description: "Tel variable 'A' op bij 'B' en return de uitkomst",
                    answer: "3"
                }
            },
            compileScript() {
                const script = document.querySelector('#script-input').value
                var fn = Function(script)
                if(fn() == this.question.answer){
                    this.showResult(true)
                }else {
                    this.showResult(false)
                }
            },
            showResult(passed) {
                if(passed){
                    alert('Correcto');
                }else {
                    alert('Niet correcto');
                }
            }
        }
    }
</script>