<script setup lang="ts">
import OrgDocumentView from '../components/OrgDocumentView.vue'
import { ref, reactive, computed, onMounted, defineProps} from 'vue'
import type { Node } from '../models/models'
import { useRoute } from 'vue-router';

const nodeId = ref<any>(useRoute().params.id)

</script>

<template>
  <main>
		<OrgDocumentView :nodeId="nodeId"/>
  </main>
</template>
