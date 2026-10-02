import asyncio,glob
from playwright.async_api import async_playwright
EXE=glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=EXE)
        pg=await b.new_page(viewport={'width':1400,'height':900},device_scale_factor=1.6)
        await pg.goto('http://localhost:8899/lab/tree/pass2_wet.ipynb?reset',wait_until='networkidle')
        await pg.wait_for_selector('.jp-Notebook .jp-Cell',timeout=60000); await pg.wait_for_timeout(4000)
        await pg.wait_for_timeout(2000)
        try: await pg.locator('.jp-toast-button',has_text='No').first.click(timeout=4000)
        except Exception as e: print('popup',e)
        await pg.evaluate("()=>document.querySelectorAll('.Toastify').forEach(e=>e.remove())")
        await pg.keyboard.press('Control+b'); await pg.wait_for_timeout(800)
        await pg.screenshot(path='/tmp/claude-0/jl/shots/A_top.png')
        # Phase 6 output: scroll so the output area of cell 44 starts at the top
        await pg.evaluate("""()=>{const c=document.querySelectorAll('.jp-Notebook .jp-Cell')[44];
            c.scrollIntoView({block:'start'});}""")
        await pg.wait_for_timeout(1200)
        await pg.evaluate("""()=>{const c=document.querySelectorAll('.jp-Notebook .jp-Cell')[44];
            const pre=[...c.querySelectorAll('.jp-OutputArea-output pre')].find(p=>p.textContent.includes('done in 160s'));
            pre.scrollIntoView({block:'start'}); const s=document.querySelector('.jp-WindowedPanel-outer'); s.scrollBy(0,-120);}""")
        await pg.wait_for_timeout(1500)
        await pg.screenshot(path='/tmp/claude-0/jl/shots/B_p6.png')
        await b.close()
asyncio.run(main())
