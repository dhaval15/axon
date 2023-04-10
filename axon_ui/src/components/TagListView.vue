<script setup lang="ts">
import TagView from '../components/TagView.vue'
import { defineProps} from 'vue'

const props = defineProps<{
  tags: string[]
  onTagClick: (tag: string) => void
}>()

</script>

<template>
	<v-list lines="one" variant="plain">
		<v-list-item
    	v-for="tag in props.tags"
    	:key="tag"
    	:title="tag"
			:onclick="() => props.onTagClick(tag)"/>
	</v-list>
</template>

<style scoped>
.padding {
	padding-top: 4px;
	padding-bottom: 4px;
}
</style>
