import type { OrgRoam, Node, Link } from './models'

export type ZoomProps = {
	k: number
	x: number
	y: number
}

export type GraphProps = {
    graphData: OrgRoam
    width: number
    height: number
    backgroundColor: string
    warmupTicks: number
    onZoom: (props: ZoomProps) => void,
    nodeColor: (node: Node) => string
    nodeRelSize: number
    nodeVal: (node: Node) => number
    nodeLabel: (node: Node) => string
    nodeCanvasObject: (node :Node, ctx: any, globalScale: any) => void
    nodeCanvasObjectMode: () => string
    linkDirectionalParticles: boolean
    linkDirectionalArrowLength?: number
    linkDirectionalArrowRelPos: number
    linkDirectionalArrowColor: string
		linkColor: (link: Link) => string
    linkWidth: (link: Link) => number
    linkDirectionalParticleWidth: number
    d3AlphaDecay: number
    d3AlphaMin: number
    d3VelocityDecay: number
    onNodeClick: (node: Node, event: any) => any
    onNodeHover: (node: Node) => void
    onNodeRightClick: (node: Node, event: any) => any
    onNodeDrag: (node: Node) => void
    onNodeDragEnd: () => void
}

