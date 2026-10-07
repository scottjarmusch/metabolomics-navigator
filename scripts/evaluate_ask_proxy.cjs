// Editorial baseline: run real browser searches without adjusting expected outcomes.
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..'),fixture=JSON.parse(fs.readFileSync(path.join(root,'docs/ask-proxy-query-set-2026-10-07.json'),'utf8'));
(async()=>{const browser=await chromium.launch({headless:true,channel:process.env.BROWSER_CHANNEL || 'msedge'});try{
 const page=await browser.newPage(),errors=[],answers=[];page.on('pageerror',e=>errors.push(e.message));
 await page.route('http://preview/**',async r=>{let f=path.join(root,'dist',new URL(r.request().url()).pathname.replace('/metabolomics-navigator-alpha/',''));if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');await r.fulfill(fs.existsSync(f)?{path:f}:{status:404,body:'missing'});});
 await page.goto('http://preview/metabolomics-navigator-alpha/ask/');
 for(const q of fixture.queries){await page.locator('#ask-query').fill(q.query);await page.locator('#ask-search-button').click();
  const strategies=await page.locator('.ask-strategy-card:visible h3 a').evaluateAll(es=>es.map(e=>({slug:new URL(e.href).pathname.split('/').filter(Boolean).at(-1),name:e.textContent.trim()})));
  const tools=await page.locator('[data-ask-tool]:visible').evaluateAll(es=>es.map(e=>e.dataset.slug));
  const response=(await page.locator('#ask-result-count').textContent()).trim(),guidance=(await page.locator('#ask-guide-message').textContent()).trim();
  const actions=await page.locator('[data-guide-action]:visible').evaluateAll(es=>es.map(e=>e.dataset.guideAction));
  let pass=false,reason='';
  switch(q.expected_route){
   case 'strategy':pass=strategies.slice(0,3).some(s=>s.slug===q.expected_strategy);reason='Expected Strategy in first three';break;
   case 'comparison_guidance':pass=!strategies.length&&actions.includes('statistics')&&/comparison|Compare processed|bulk.sample/i.test(response+' '+guidance);reason='Comparison guidance and statistical exploration, no specialist cards';break;
   case 'clarification':pass=!strategies.length&&actions.includes('learn')&&/study guide|clarify|scientific aim/i.test(response+' '+guidance);reason='Beginner clarification with learning route, no method cards';break;
   case 'constraint':pass=!strategies.length&&/missing input|exclusion/i.test(response);reason='Missing-input constraint, no method cards';break;
   case 'scope':pass=!strategies.length&&/outside scope/i.test(response);reason='Recognize explicit NMR-only intent';break;
   case 'tool':pass=tools.includes(q.expected_tool);reason='Named tool resolved; compatibility still requires review';break;
   case 'statistics':pass=!strategies.length&&actions.includes('statistics');reason='Local statistics route, no method cards';break;
  }
  answers.push({...q,response,guidance,strategies,tools,actions,passed:pass,criterion:reason});
 }
 if(errors.length)throw new Error(errors.join('\n'));
 const failed=answers.filter(a=>!a.passed);fs.writeFileSync(path.join(root,process.argv[2] || 'docs/ask-proxy-baseline-2026-10-07.json'),JSON.stringify({source_commit:require('child_process').execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'}).trim(),controller_sha256:require('crypto').createHash('sha256').update(fs.readFileSync(path.join(root,'dist/assets/ask.js'))).digest('hex'),queries:answers.length,passed:answers.length-failed.length,failed:failed.length,browser_errors:errors,results:answers},null,2));
 console.log(JSON.stringify({total:answers.length,passed:answers.length-failed.length,failed:failed.map(a=>({id:a.id,query:a.query,response:a.response,top:a.strategies[0]?.name||null}))},null,2));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});
