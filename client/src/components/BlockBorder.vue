<script setup>
import { computed } from "vue"

const props = defineProps({
    color: {
        type: String,
        required: true
    },

    radius: {
        type: String,
        required: true
    },
    padding: {
        type: String
    }
})

const colors = {
    grey: "#69696950",
    blue: "#4a84f8",
    none: "transparent"
}

const style = computed(() => {
    return {
        background: "linear-gradient(to right bottom, " + colors[props.color] + " 0%, rgba(0, 0, 0, 0) 100%)",
        borderRadius: props.radius + "px",
        padding: props.padding ? props.padding + "px" : "1px"
    }
})
</script>

<template>
    <div :style="style" class="border">
        <slot />
    </div>
</template>

<style lang="scss" scoped>
.border {
    z-index: -1;
    border: none;
}
</style>
