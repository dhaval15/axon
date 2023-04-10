<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps<{
	open: boolean
}>()

</script>

<template>
<Teleport to="body">
  <div v-if="props.open" class="modal">
    <slot name="container"/>
  </div>
</Teleport>
</template>

<style>
.modal {
  position: fixed;
  z-index: 999;
	background: rgb(255, 250, 248);
  top: 40%;
  left: 50%;
	padding: 32px;
  width: 400px;
  margin-left: -150px;
	border-radius: 8px;
	box-shadow: 10px 10px 12px rgba(0,0,0,0.5);
}
</style>
