<script>
export default {
  emits: ["onSearch"],
	data () {
		return {
			query: ""
		}
	},
	methods: {
    search: function (event) {
      this.$emit("onSearch", this.query);
    }
  }
}
</script>

<template>
		<v-text-field 
			label="Enter Query" 
			variant="solo"
			class="search-box"
			v-model:value="query" 
			placeholder="Enter Query" />
</template>

<style scoped>
	.search-box {
		flex-grow: 1;
		font-size: large;
	}
	.container {
		display: flex;
		height: fit-content;
	}
</style>
