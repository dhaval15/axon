<!-- NodeLinskRefView.vue -->
<script>
import axios from 'axios'
//import { LinkRef } from '../models.d.ts'

export default {
	props: ['from', 'to']
}
</script>

<template>
	<h1> Links </h1>
	<h2> From </h2>
	<div v-for="ref in this.from">
		<a class="link-ref" :href="ref.id">
				{{ref.title}}
		</a>
	</div>
	<h2> To </h2>
	<div v-for="ref in this.to">
		<a class="link-ref" :href="ref.id">
				{{ref.title}}
		</a>
	</div>
</template>

<style scoped>
	.link-ref {
		padding-top: 4px;
		padding-bottom: 4px;
		padding-left: 8px;
		padding-right: 8px;
		font-size: large;
		font-weight: 500;
		color: rgba(0, 100, 200, 1);
		text-decoration: none;
	}
</style>
