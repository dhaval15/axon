<!-- ScopeView.vue -->
<script setup lang="ts">
import type { Scope } from '../models/models'
import { defineProps } from 'vue'

const props = defineProps<{
	scope: Scope
	onClick: (scope: Scope) => void
}>()

function click() {
	props.onClick(props.scope)
}

</script>

<template>
		<a class="tile" href="#" :onclick="click">
				{{props.scope.label}}
		</a>
</template>

<style scoped>
	.tile {
		padding-top: 4px;
		padding-bottom: 4px;
		padding-left: 8px;
		padding-right: 8px;
		font-size: medium;
		font-weight: 500;
		color: rgba(0, 100, 200, 1);
		text-decoration: none;
	}
</style>
