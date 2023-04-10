export type TextSelection = {
	start: number
	end: number
}

export type Review = {
	start: number
	end: number
	text: string
	feedback: string
}

export function fetchSelectedContent(content: string, selection: TextSelection){
	var cWords = content.split(/(\s+)/);
	return cWords.slice(selection.start, selection.end)
		.join(' ')
		.replace(/\s+/g, ' ')
		.trim()
}

export function insertReviews(content: string, reviews: Review[]){
	var cWords = content.split(/(\s+)/);
	for(var review of reviews) {
		prependToIndex(cWords, review.start, ` [[review:${review.feedback}][`)
		appendToIndex(cWords, review.end - 1, `]] `)
	}
	return cWords.join('');
}

function prependToIndex(stringArray: string[], index: number, text: string) {
		let original = stringArray[index]
		stringArray.splice(index, 1, `${text}${original}`)
}

function appendToIndex(stringArray: string[], index: number, text: string) {
		let original = stringArray[index]
		stringArray.splice(index, 1, `${original}${text}`)
}

export function findSelections(content: string, text: string, ignores: string[]) : TextSelection[] {
	var selections : TextSelection[] = []
	var cWords = content.split(/(\s+)/);
	let sWords = text.split(/(\s+)/).filter((e) => e.trim().length > 0);
	let word = sWords[0];
	var i = 0
	for (let i=0; i < cWords.length; i++) {
		let c = cWords[i];
		if (c.endsWith(word)){
			let index  = startsWith(cWords.slice(i), sWords, ignores)
			if (index == -1){
				continue
			}
			let selection = {
				start: i,
				end: i + index,
			}
			selections.push(selection)
			i = i + index + 1
		}
	}
	return selections
}

function startsWith(cWords: string[], sWords: string[], ignores: string[])
	: number {
	var i = 1
	var index = 1
	let length = sWords.length
	while(index < length){
		var c = cWords[i].trim();
		let s = sWords[index];
		if (index == length - 1 && c.startsWith(s)){
			i++
			index++
			continue
		}
		if (c == s) {
			i++
			index++
			continue
		}
		if(c == ''){
			c = ' '
		}
		if (ignores.indexOf(c) > -1) {
			i++
			continue
		}
		index = -1
		break
	}
	if (index == -1)
		return -1
	return i
}
