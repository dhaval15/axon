<script setup lang="ts">
import axios from 'axios'
import router from '../router';
import OrgView from '../components/OrgView.vue'
import NodeLinksRefView from '../components/NodeLinksRefView.vue'
import type { Node, Link } from '../models/models'
import { orgroamApi } from '../api/api'
import type { TextSelection } from '../utils/review'
import { fetchSelectedContent, findSelections, insertReviews } from '../utils/review'
import { ref, reactive, computed, onMounted, defineProps} from 'vue'
import ModalContainer from './ModalContainer.vue'

const props = defineProps<{nodeId: string}>()

interface State {
	content?: string
	node?: Node
	from?: Link[]
	to?: Link[]
	outline: boolean
	justify: boolean
	selections?: TextSelection[]
}

const state = reactive<State>({
	outline: true,
	justify: true,
})

const title = computed<string>(() => state.node?.title ?? 'What a cool name?')

function toggleOutline() {
	state.outline = !state.outline
}

function toggleJustify() {
	state.justify = !state.justify
}

onMounted(() => {
	orgroamApi.read(props.nodeId).then((content: string) => (state.content = content))
	orgroamApi.nodeWithId(props.nodeId).then((node: Node) => {
		state.node = node 
	})
	orgroamApi.links(props.nodeId).then((links: Link[]) => {
		state.from = links.filter((link) => link.dest == props.nodeId)
		state.to = links.filter((link) => link.source == props.nodeId)
	})
})

function onReview(selection: string): string {
	state.selections = findSelections(state.content!, selection, ['\n', ' '])
	let reviews = state.selections.map((s) => {
		return {
			start: s.start,
			end: s.end,
			text: 'Hello world',
			feedback: 'Here we are again',
		}
	})
	return insertReviews(state.content!, reviews)
}

</script>

<template >
		<ModalContainer :open="state.selections!=null">
			<template #container>
				<ul v-for="selection in state.selections">
					{{fetchSelectedContent(state.content!, selection)}}
				</ul>
			</template>
		</ModalContainer>
		<div class="container">
			<v-btn 
				class="button" 
				variant="outlined" 
				icon="mdi-home" 
				href="/#"/> 
			<h1> 
				{{ title }}
			</h1>
			<div v-if="state.node!=null">
				<div v-for="tag in state.node.tags">
					{{tag}}
				</div>
			</div>
			<v-btn 
				class="button" 
				variant="outlined" 
				:icon="state.outline ? 'mdi-format-list-bulleted' : 'mdi-text-long'"
				:onclick="toggleOutline"/>
			<v-btn 
				class="button" 
				variant="outlined" 
				:icon="state.justify ? 'mdi-format-align-justify' : 'mdi-format-align-left'"
				:onclick="toggleJustify"/>
			<OrgView 
				:content="state.content" 
				v-if="state.content != null"
				:outline="state.outline"
				:justify="state.justify"
				:onReview="onReview"/>
			<NodeLinksRefView 
				v-if="state.from!=null && state.to!=null"
				:from="state.from" 
				:to="state.to"/>
	</div>
</template>

<style scoped>
h1 {
	color: rgba(220,120,50, 0.7);
	padding-bottom: 16px;
}
.container {
	padding: 32px;
}
.document-main {
	padding-right: 32px;
}
.document-sidebar {
}
.document-sidebar:before {	
	content: '';
  width: 0;
  height: 100%;
  position: absolute;
  border: 1px solid rgba(0,0,0,0.05);
  top: 0px;
}
</style>
