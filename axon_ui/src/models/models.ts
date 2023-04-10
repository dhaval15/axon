export interface OrgRoam {
  nodes: AnyNode[]
  links: Link[]
  tags: string[]
	ghost: string[]
}

export interface Link {
  source: string
  sourceTitle: string
  dest: string
  destTitle: string
  inline?: string
  type: string
}

export type AnyNode = Node | GhostNode

export type GhostNode = {
  id: string
}

export type Node = {
  id: string
  file: string
  title: string
  level: number
  pos: number
  olp: string[] | null
  properties: {
    [key: string]: string | number
  }
  tags: string[]
	links: Link[]
	ghost?: boolean
}

export type Scope = {
	id: string
	label: string
	expr: string
}

export type GraphOptions = {
	width: number
	height: number
	nodeRelSize: number
}
