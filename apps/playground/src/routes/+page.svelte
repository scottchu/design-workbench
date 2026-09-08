<script>
  let { data } = $props();
</script>
<svelte:head><title>Design Workbench · Playground</title></svelte:head>
<main>
  <p class="eyebrow">DESIGN WORKBENCH · LOCAL</p>
  <h1>Playground</h1>
  <p class="intro">開啟專案既有的互動工具。模型與參數邏輯由原專案提供。</p>
  {#if data.problem}<p role="alert">Registration unavailable: {data.problem}</p>{/if}
  {#if !data.simulators.length && !data.problem}<p>尚未登錄專案頁面。</p>{/if}
  <div class="list">{#each data.simulators as sim}{#if sim.available}<a class="card" href={'/simulators/' + sim.id}><span class="tag">EXTERNAL PROJECT</span><h2>{sim.title}</h2><p>{sim.description}</p><span class="open">開啟專案頁面 →</span><small>Source {sim.source.revision.slice(0,12)}</small></a>{:else}<article class="card unavailable"><span class="tag">UNAVAILABLE</span><h2>{sim.title}</h2><p>{sim.reason}</p><small>修復此項目的來源或登錄後重新整理；其他頁面仍可使用。</small></article>{/if}{/each}</div>
</main>
<style>:global(body){margin:0;background:#f4f5f2;color:#202820;font-family:system-ui,sans-serif}main{max-width:1100px;margin:0 auto;padding:64px 32px}.eyebrow,.tag{font-size:12px;letter-spacing:.14em;color:#526e5b}h1{font-size:48px;margin:12px 0}.intro{font-size:18px;color:#647068}.list{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:36px}.card{display:block;padding:28px;border:1px solid #d5ded3;border-radius:16px;background:white;color:inherit;text-decoration:none}.card:hover{border-color:#517a55}.card p{line-height:1.6;color:#647068}.open{display:block;margin:24px 0 12px;color:#315d3c;font-weight:650}small{color:#737c74}</style>
