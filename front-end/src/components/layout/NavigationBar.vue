<template>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
	<a class="navbar-brand" href="#">So you think you can program</a>
	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
		<span class="navbar-toggler-icon"></span>
	</button>
	<div class="collapse navbar-collapse" id="navbarNav">
		<ul class="navbar-nav">
			<li class="nav-item active">
				<router-link :to="{ name: 'users'}" class="nav-link">Users <span class="sr-only">(current)</span></router-link>
			</li>
			<li class="nav-item active">
				<router-link :to="{ name: 'quizzes'}" class="nav-link">Quizzes</router-link>
			</li>
		</ul>
	</div>
	</nav>
</template>