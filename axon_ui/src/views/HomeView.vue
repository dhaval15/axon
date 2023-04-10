<script setup lang="ts">
import NeuronView from '../components/NeuronView.vue'
import ScopeListView from '../components/ScopeListView.vue'
import TagListView from '../components/TagListView.vue'
import SearchBox from '../components/SearchBox.vue'
import type { OrgRoam, Node, Link, Scope} from '../models/models'
import { ref, reactive, computed, onMounted } from 'vue'
import { orgroamApi } from '../api/api'
import router from '../router';

interface State {
	nodes: Node[],
	tags: string[],
	drawer: boolean,
}

const scopes = ref([])
const state = reactive<State>({
	drawer: false,
	nodes: [],
	tags: [],
})

function toggleDrawer() {
	state.drawer = !state.drawer
}

function loadNeuron() {
	orgroamApi.nodes().then((nodes : Node[]) => {
		state.nodes = nodes
	})	
	orgroamApi.tags().then((tags : string[]) => {
		state.tags = tags
	})	
}

function onScopeClick (scope: Scope) {
	orgroamApi.expr(scope.expr).then((response : OrgRoam) => {
		//state.nodes = response.nodes
	})
}

function search (query: string) {
	orgroamApi.expr(query).then((response : OrgRoam) => {
		//state.nodes = response.nodes
	})
}

function onTagClick (tag: string) {
	orgroamApi.nodesWithTag(tag).then((response : Node[]) => {
		state.nodes = response
	})
}

function goToNetwork () {
	router.push({ 
		name: 'network',
	})
}


onMounted(() => {
	loadNeuron()
})

</script>

<template>
	<v-app class="app">
		<v-app-bar color="primary">
			<v-app-bar-nav-icon variant="text" @click.stop="toggleDrawer"/>
			<v-spacer/>
      <v-btn icon>
      	<v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon href="/#/network">
        <v-icon>mdi-graphql</v-icon>
      </v-btn>
		</v-app-bar>
		<v-navigation-drawer v-model="state.drawer">
			<v-list-item
    		key="home"
    		title="Home"
				:onclick="loadNeuron"/>
			<ScopeListView 
				:scopes="scopes" 
				:onScopeClick="onScopeClick"/>
			<TagListView 
				:tags="state.tags" 
				:onTagClick="onTagClick"/>
		</v-navigation-drawer>
		<v-main class="neuron">
    	<NeuronView :nodes="state.nodes"/>
		</v-main>
	</v-app>
</template>

<style scoped>
	.app {
		padding-top: 32px;
		padding-bottom: 32px;
	}
	.v-navigation-drawer__content::-webkit-scrollbar-track{
  	-webkit-box-shadow: inset 0 0 6px #5d5d5d;
  	background-color: #5d5d5d;
	}
	.v-navigation-drawer__content::-webkit-scrollbar{
  	width: 0px;
	}
	.v-navigation-drawer__content::-webkit-scrollbar-thumb{
  	-webkit-box-shadow: inset 0 0 6px #424242;
  	background-color: #424242;
	}
	.neuron {
		padding-left: 16px;
		padding-right: 16px;
	}
</style>
