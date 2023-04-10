import axios from 'axios'
import type {OrgRoam, Link, Node} from '../models/models'

class OrgRoamApi {
	baseUrl : string;

	constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

	orgroam() : Promise<OrgRoam> {
		return axios.get(`${this.baseUrl}`)
			.then((response) => {
				let ghostNodes = response.data.ghost.map((id: string) => ({ id: id }))
				Array.prototype.push.apply(response.data.nodes, ghostNodes)
				return response.data
		})
	}

	nodes() : Promise<Node[]> {
		return axios.get(`${this.baseUrl}/nodes`)
			.then((response) => {
				return response.data
		})
	}


	nodeWithId(id: string) : Promise<Node> {
		return axios.get(`${this.baseUrl}/nodes/${id}`)
			.then((response) => {
				return response.data
		})
	}

	tags() : Promise<string[]> {
		return axios.get(`${this.baseUrl}/tags`)
			.then((response) => {
				return response.data
		})
	}

	expr(query: string): Promise<OrgRoam> {
		return axios
			.get(`${this.baseUrl}/expr`, {
				params: {'q' : query}
			}).then((response) => {
				return response.data
			})
	}

	nodesWithTag(tag: string): Promise<Node[]> {
    return axios.get(`${this.baseUrl}/nodes?tag=${tag}`)
			.then(response => {
					return response.data
			})
	}

	links(id: string): Promise<Link[]> {
    return axios.get(`${this.baseUrl}/links?id=${id}`)
			.then(response => {
					return response.data
			})
	}

	read(id: string): Promise<string> {
    return axios
      .get(`${this.baseUrl}/read/${id}`)
  		.then((response) => {
				return response.data
			})
	}

	review(id: string, selection: string, feedback: string): Promise<any> {
		return axios
			.post(`${this.baseUrl}/review`, {
				id: id,
				selection: selection,
				feedback: feedback,
			})
  		.then((response) => {
				return response.data
			})
	}
}

export const orgroamApi = new OrgRoamApi('/orgroam')
