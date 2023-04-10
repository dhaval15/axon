<!-- NeuronView.vue -->
<script setup lang="ts">
import OrgDocumentView from '../components/OrgDocumentView.vue'
import NodeTile from '../components/NodeTile.vue'
import type { Node, Link } from '../models/models'
import { defineProps, ref, reactive, computed, onMounted } from 'vue'

const props = defineProps<{
	nodes: Node[]
}>()
</script>

<template>
	<div v-for="node in props.nodes">
		<div class="padding">
  		<NodeTile :node="node"/>
		</div>
	</div>
</template>

<style scoped>
.padding {
	padding-top: 4px;
	padding-bottom: 4px;
}
</style>
