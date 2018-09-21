<template>
    <div class="create-quiz">
        <div class="row justify-content-center">
            <div class="col col-lg-8">
                <div class="card">
                    <div class="card-header">
                        Edit your quiz
                    </div>
                    <div class="card-body">
                        <form>
                            <div class="form-group">
                                <label for="exampleInputEmail1">Name</label>
                                <input type="text" class="form-control" v-bind:value="quiz.name" id="exampleInputEmail1" aria-describedby="emailHelp">
                            </div>
                            <button type="submit" class="btn btn-primary edit-quiz-btn">Submit</button>
                        </form>
                    </div>
                    <table v-if="quiz" class="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Name</th>
                                <th scope="col">description</th>
                                <th scope="col">answer</th>
                                <th scope="col">Edit</th>
                                <th scope="col">Remove</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="question in quiz.questions" :key="question.id">
                                <th scope="row">{{ question.id }}</th>
                                <td>{{ question.name }}</td>
                                <td>{{ question.description }}</td>
                                <td>{{ question.answer }}</td>
                                <td><router-link :to="{ name: 'quiz', params: { id: quiz.id}}">Here</router-link></td>
                                <td><a href="#" class="remove-question">Here</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                </br>
                <div class="card">
                    <div class="card-header">
                        Add new question
                    </div>
                    <div class="card-body">
                        <form>
                            <div class="form-group new-question-form">
                                <label for="exampleInputEmail1">Question Name</label>
                                <input type="text" class="form-control new-question" placeholder="Question Name" id="newQuestionNameInput" aria-describedby="emailHelp">
                            </div>
                            <div class="form-group new-question-form">
                                <label for="exampleInputEmail1">Question Description</label>
                                <input type="text" class="form-control new-question" placeholder="Question Description" id="newQuestionDescriptionInput" aria-describedby="emailHelp">
                            </div>
                            <div class="form-group new-question-form">
                                <label for="exampleInputEmail1">Answer</label>
                                <input type="text" class="form-control new-question" placeholder="Answer" id="newQuestionAnswerInput" aria-describedby="emailHelp">
                            </div>
                            <button type="submit" class="btn btn-primary add-question-btn">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const axios = require("axios");
const instance = axios.create({
  baseURL: "http://localhost:5000/"
});
export default {
  data() {
    return {
      loading: false,
        inputName: null,
        inputDescription: null,
        inputAnswer: null,
      quiz: {
        // id: 1,
        // name: "quiz 1",
        // user: { first_name: "menno", last_name: "prinzhorn" },
        // questions: [
        //     { id: 1, name: "Los dit programmeer probleem op 1", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3, answers: { id: 1, user_id: 1, question_id: 1, input: "<test>"} },
        //     { id: 2, name: "Los dit programmeer probleem op 2", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3 },
        //     { id: 3, name: "Los dit programmeer probleem op 3", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3 },
        //     { id: 4, name: "Los dit programmeer probleem op 4", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3 }
        // ]
      }
    };
  },
  created() {
    this.fetchData();
  },
  mounted() {
    this.setEventListeners();
  },
  methods: {
    fetchData() {
      const axios = require("axios");
      instance.defaults.headers.common["Authorization"] =
        "Basic " + btoa("max" + ":" + "qwerty");
      const that = this;
      instance
        .get("/quizzes/" + this.$route.params.id)
        .then(function(response) {
          console.log(response);
          that.quiz = response.data;
          that.loading = false;
        });
    },
    setTimeout() {
      this.loading = false;
    },
    setEventListeners() {
      const submitBtn = document.querySelector(".edit-quiz-btn");
      const deleteBtn = document.querySelector(".remove-question");
      const addQBtn = document.querySelector(".add-question-btn");
      if (submitBtn) {
        submitBtn.addEventListener("click", () => {
          this.editQuiz();
        });
      }
      if (deleteBtn) {
        deleteBtn.addEventListener("click", () => {
          this.removeQuestion();
        });
      }
      if (addQBtn) {
        addQBtn.addEventListener("click", () => {
            this.inputName = document.getElementById('newQuestionNameInput').value;
            this.inputDescription = document.getElementById('newQuestionDescriptionInput').value;
            this.inputAnswer = document.getElementById('newQuestionAnswerInput').value;

          this.addQuestion();
        });
      }
    },
    addQuestion(){
        instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa('max' + ':' + 'qwerty');
        const that = this
        instance.post('/questions', {
            name: this.inputName,
            description: this.inputDescription,
            answer: this.inputAnswer,
            quiz_id: this.$route.params.id
        } )
            .then(function (response) {
                console.log(response);
                // that.user = response.data
                // that.loading = false
            });
        // alert('Vraag aangemaakt');
        // this.$router.push({ name: 'quizzes'})
    },
    editQuiz() {
      //doe api call
      alert("Quiz aangepast");
      this.$router.push({ name: "quizzes" });
    },
    removeQuestion() {
      //doe api call
      alert("Question removed");
      this.$router.push({ name: "quizzes" });
    }
  }
};
</script>