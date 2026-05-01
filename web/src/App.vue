<script setup lang="ts">
import { computed, ref } from 'vue'

const question = ref()
const response = ref()
const loading = ref(false)

const disabled = computed(() => {
  return !question.value?.length || loading.value
})

function submit() {
  loading.value = true
  fetch("http://localhost:8000/question", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question: question.value })
  })
  .then(res => res.json())
  .then(data => response.value = data)
  .catch(() => response.value = 'Error')
  .finally(() => {
    loading.value = false
  })
}
</script>

<template>
  <main>
    <textarea v-model="question" rows="4" placeholder="Escribe tu pregunta" :disabled="loading" />
    <button :disabled="disabled" @click="submit">Enviar</button>
    <p>{{ response }}</p>
  </main>
</template>

<style lang="css" scoped>
main {
  display: flex;
  flex-direction: column;

  height: 100dvh - 100px;
  margin-top: 100px;

  gap: 12px;
  align-items: center;
}

main > p, textarea {
  width: 50%;
}
main > p {
  white-space: pre-line;
}
main > textarea {
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 6px;
  resize: none;
}
</style>
