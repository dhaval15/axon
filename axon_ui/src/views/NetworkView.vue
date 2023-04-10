<script setup lang="ts">
import router from '../router';
import type { GraphOptions, OrgRoam, Node, Link} from '../models/models'
import { ref, reactive,  computed, onMounted } from 'vue'
import { orgroamApi } from '../api/api'
import type { ZoomProps, GraphProps } from '../models/graph-props'
// @ts-ignore
const d3promise = import('d3-force-3d')

interface State {
	orgroam?: OrgRoam
	options: GraphOptions
}

const state = reactive<State>({
	options: {
		width: 600,
		height: 400,
		nodeRelSize: 8,
	},
})

const graph = ref()

onMounted(() => {
    orgroamApi.orgroam()
      .then((response: OrgRoam) => {
				state.orgroam = {
					 nodes : response.nodes,
					 links : response.links.filter((link: Link) => link.type == 'id'),
					 tags : response.tags,
					 ghost: response.ghost,
				}
			})
})

function updatePhysics() {
	d3promise.then((d3) => {
		let fg = graph.value!
		fg.d3Force('x', d3.forceX().strength(0.3))
		fg.d3Force('y', d3.forceY().strength(0.3))
    fg.d3Force('center', d3.forceCenter().strength(0.2))
  	fg.d3Force('link').strength(0.3)
    fg.d3Force('link').iterations(1)
    fg.d3Force('charge').strength(-700)
    fg.d3Force('collide', d3.forceCollide().radius(20))
    fg.zoomToFit(5, 100)
	})
}

function nodeLabel(node: Node) {
	return node.title
}

function nodeVal(node: Node) {
	return 4
}

function onNodeClick(node: Node) {
	router.push({ 
		name: 'document', 
		params: {
			id: node.id,
		},
	})
}

function search(query: string) {
	orgroamApi.expr(query).then((response: OrgRoam) => (state.orgroam = response))
}

const graphProps = computed<GraphProps>(() => {
	return buildGraphProps(state.orgroam!)
})

const ops = reactive({
	scale: 1
})


function buildGraphProps(response: OrgRoam) : GraphProps {
		return {
			graphData: response,
			width: 800,
			height: 600,
			backgroundColor: 'white',
			warmupTicks: 100,
			onZoom: (props: ZoomProps) => {
				ops.scale = props.k
			},
		  nodeColor: (node: Node) => {
				if(node.ghost) 
					return "orange"
				else
					return "red"
			},
			nodeRelSize: 4,
			nodeVal: (node: Node) => {
				return 4 / Math.pow(ops.scale, 1.2)
			},
			nodeLabel: (node: Node) => {
				if(node.ghost)
					return 'Let\'s create a new one'
				else
					return node.title
			},
			nodeCanvasObject: (node: Node, ctx: any, globalScale: any) => {},
			nodeCanvasObjectMode: () => 'after',
			linkDirectionalParticles: true,
			linkDirectionalArrowLength: 1,
			linkDirectionalArrowRelPos: 0.5,
			linkDirectionalArrowColor: 'red',
			linkColor: (link: Link) => {
				return "orange"
			},
			linkWidth: (link: Link) => {
				return 2
			},
			linkDirectionalParticleWidth: 4,
			d3AlphaDecay: 0.05,
			d3AlphaMin: 0,
			d3VelocityDecay: 0.25,
			onNodeClick: (node: Node, event: any) => {},
			onNodeHover: (node: Node) => {
				
			},
			onNodeRightClick: (node: Node, event: any) => {},
			onNodeDrag: (node: Node) => {},
			onNodeDragEnd: () => {},
		}
}

</script>

<template>
  <main>
		<v-btn :onclick="updatePhysics" variant="outlined">
			<v-icon>
				mdi-home
			</v-icon>
		</v-btn>
		<div>
			<VueForceGraph2D 
				ref="graph"
				v-if="state.orgroam!=null"
				linkTarget="dest"
				v-bind="graphProps"/>
		</div>
  </main>
</template>

<style scoped>
	div {
		padding-top: 32px;
		padding-bottom: 32px;
	}
</style>
