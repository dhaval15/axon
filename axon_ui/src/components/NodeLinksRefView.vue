<script setup lang="ts">
import { defineProps} from 'vue'
import type { Link } from '../models/models'

const props = defineProps<{
	from: Link[]
	to: Link[]
}>()

</script>

<template>
	<h1> Links </h1>
	<h2> From </h2>
	<div v-for="ref in props.from">
		<a class="link-ref" :href="ref.source">
				{{ref.sourceTitle}}
		</a>
	</div>
	<h2> To </h2>
	<div v-for="ref in props.to">
		<a class="link-ref" :href="ref.dest">
				{{ref.destTitle ?? ref.inline}}
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
