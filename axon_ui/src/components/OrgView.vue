<!-- OrgView.vue -->
<script setup lang="ts">
import { ref, reactive, computed, onMounted, defineProps} from 'vue'
import { processor } from '../utils/org-html'

const props = defineProps<{
		content: string
		justify: boolean
		outline: boolean
		onReview: (selection: string) => string
}>()

interface State {
	htmlContent?: string
}

const state = reactive<State>({})

const contentClass = computed(() => {
	const classes : string[] = ['org-content']
	if (props.outline){
		classes.push('outline')
	}
	if (props.justify){
		classes.push('justify')
	}
	return  classes.join(' ')
})

onMounted(() => {
	processor
		.process(props.content)
		.then(data => (state.htmlContent = data.value));
})

function onContextMenu(e: any) {
	let selection = window.getSelection();
	if(selection!=null && selection!.rangeCount > 0){
		e.preventDefault();
		let content = props.onReview(selection!.toString());
	processor
		.process(content)
		.then(data => (state.htmlContent = data.value));
	}
}
</script>

<template class="container" >
		<div @contextmenu="onContextMenu" :class="contentClass" v-html="state.htmlContent"/>
</template>

<style scoped>
.container {
	padding: 16px;
}

.button {
	margin-right: 8px;
}

.org-content >>> p {
	font-size: large;
	padding-bottom: 4px;
}

.org-content >>> review {
	background-color: orange;
  position:relative; 
}

.org-content >>> review:hover:before {
  display:block;
}

.org-content >>> review:before {
	content: attr(feedback); /* here's the magic */
  position: absolute;
  top: 100%;
  transform: translateY(-50%);
  left: 100%;
  margin-left: 16px; /* and add a small left margin */
  width: 200px;
  padding: 4px;
  border-radius: 12px;
  background: orange;
	foreground: black;
  color: #fff;
  text-align: center;
  display:none;
}

.org-content.justify >>> p {
	text-align: justify;
}

.org-content >>> ol {
	padding-left: 32px;
}

.org-content >>> ul {
	padding-left: 32px;
}

.org-content >>> li::marker {
	font-size: medium;
}

.outline >>> .bullet-headline:not(h1){
	font-size: large;
	font-weight: 600;
}

.outline >>> h1 {
	font-size: x-large;
}

.outline >>> [class^="section-"] {
	padding-left: 24px;
}

.outline >>> .bullet-headline:before {
	content: ' ◦ ';
	top: 6px;
	font-size: xx-large;
}

.outline >>> [class^="section-"]:before {
	content: '';
  width: 0;
  height: 100%;
  position: absolute;
  border: 1px solid rgba(0,0,0,0.05);
  top: 0px;
  left: 6px;
}

.center {
  border: 5px solid;
  display: flex;
  justify-content: center;
}
</style>
