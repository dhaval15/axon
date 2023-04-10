import { unified } from 'unified'
import parse from 'uniorg-parse'
import uniorg2rehype from 'uniorg-rehype'
import stringify from 'rehype-stringify'
import {visit} from 'unist-util-visit'

function flatMap(ast, fn) {
  return transform(ast, 0, null)[0]

  function transform(node, index, parent) {
    if (node.children) {
      var out = []
      for (var i = 0, n = node.children.length; i < n; i++) {
        var xs = transform(node.children[i], i, node)
        if (xs) {
          for (var j = 0, m = xs.length; j < m; j++) {
            out.push(xs[j])
          }
        }
      }
      node.children = out
    }

    return fn(node, index, parent)
  }
}

function remodelUI() {
  return (tree) => {
    flatMap(tree, node => {
  		if (node.type == 'element' 
				&& node.tagName == 'section'
				&& ['h1', 'h2', 'h3', 'h4', 'h5'].includes(node.children[0].tagName)) {
					const heading = node.children.shift()
					heading.properties["className"] = "bullet-headline collapsible"
					heading.value = '◦ ' + heading.value;
    			return [
						heading,
						node,
    			]
  		}
			if(node.tagName == 'a') {
				if(node.properties['href'].startsWith('id:')) {
					node.properties['href'] = node.properties['href'].replace('id:', '');
				}
				if(node.properties['href'].startsWith('review:')) {
					node.tagName = 'review'
					node.properties['feedback'] = node.properties['href'].slice(7)
					node.properties['href'] = null
				}
    		return [node]
			}
  		// No change
  		return [node]
		})
  }
}

function infuseNaiveUI() {
  return (tree) => {
    visit(tree, 'element', (node) => {
			if (node.tagName == "section") {
				const level = node.properties['className'][0].replace("section-level-", "");
			}
			if (node.tagName == "h1") {
				node.children[0].value = '◦ ' + node.children[0].value;
			}
			if (node.tagName == "code") {
				//node.properties['style'] = "background-color:red"
			}
    })
  }
}

export const processor = unified().use(parse)
										.use(uniorg2rehype, {useSections: true})
										.use(remodelUI)
										.use(stringify);
