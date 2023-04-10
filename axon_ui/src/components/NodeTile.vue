<!-- NodeTile.vue -->
<script setup lang="ts">
import router from '../router';
import type { Node } from '../models/models'
import { defineProps } from 'vue'

const props = defineProps<{
	node: Node
}>()

function openNode() {
	router.push({ 
		name: 'document', 
		params: {
			id: props.node.id,
		},
	})
}
</script>

<template>
		<a class="node-tile" :onclick="openNode">
				{{props.node.title}}
		</a>
</template>

<style scoped>
	.node-tile {
		padding-top: 4px;
		padding-bottom: 4px;
		padding-left: 8px;
		padding-right: 8px;
		font-size: x-large;
		font-weight: 400;
		color: rgba(0, 100, 200, 1);
		text-decoration: none;
	}
</style>
