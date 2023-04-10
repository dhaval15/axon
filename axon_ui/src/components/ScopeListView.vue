<!-- ScopeListView.vue -->
<script setup lang="ts">
import ScopeView from '../components/ScopeView.vue'
import { defineProps} from 'vue'
import type { Scope } from '../models/models'

const props = defineProps<{
  scopes: Scope[]
  onScopeClick: (scope: Scope) => void
}>()

</script>

<template>
	<div v-for="scope in props.scopes">
		<div class="padding">
  		<ScopeView :scope="scope" :onClick="props.onScopeClick"/>
		</div>
	</div>
</template>

<style scoped>
.padding {
	padding-top: 4px;
	padding-bottom: 4px;
}
</style>
