Founder mode. Here's the take:

**The principle — each tool gets a lane and stays there.** The trap with this stack is using them interchangeably and losing track of what lives where. Assign one job per tool and resist mission creep.

**GitHub is the spine, not a tool.** Everything ends up there. Every project, every prototype, every doodle. Set up a consistent repo template (README, .env.example, deploy config, license) so spinning up #14 takes 30 seconds. GitHub Projects becomes your portfolio backlog. If it's not in GitHub, it doesn't exist.

Then assign roles:

**Claude Code → architect + craftsman.** Run it in your terminal against local repos for anything where structure matters: the clinical PWA, the 7-agent orchestration layer, anything in the Cowork OS. This is where you do the thinking — long-running, multi-file, opinionated work. Pair it with Claude chat for spec'ing things out before you touch code.

**ChatGPT Codex → parallel intern.** Cloud-based, async, runs while you do other things. Delegate well-scoped tasks: "add tests to this module," "implement X per this spec," "fix issue #47." It opens PRs against your GitHub repos. Perfect for your context-switched life — fire three tasks before clinic, review PRs at lunch. The unlock here is *delegation discipline*, not the tool itself.

**Replit → demo machine.** Anywhere you need to share a working prototype with someone non-technical (your dad on a Rai capital decision, a podcast guest, a patient testing a tool). One-click live URL. Don't build production here. Build show-and-tell here.

**Lovable → marketing surface, and only that.** Rai Orchards booking page, podcast site, the public "Rai" landing. Pixel-perfect, design-heavy, content-driven. Don't try to make Claude Code do what Lovable does in five minutes, and don't let Lovable creep into your tools layer.

**The handoff pattern:**
1. Spec in Claude chat — think it through, write the brief
2. Build in Claude Code OR delegate to Codex depending on whether you need to *think* or just *execute*
3. Ship to GitHub
4. Deploy to Cloudflare Pages (your roadmap already points here) or Replit depending on stakes
5. Front it with Lovable if a non-dev audience needs to find it

**What I'd actually do this month, given your roadmap:**
- Stand up a `rai-tools` GitHub org with sub-repos per tool. One template repo cloned for each.
- Move the clinical PWA to a real Cloudflare Pages deploy on a proper subdomain. It's the most credibility-generating asset you have and GitHub Pages undersells it.
- Pick one Codex task per day — well-scoped, fire-and-forget. Build the muscle of delegation, since that's the whole agentic-first thesis.
- Lock Lovable to the orchard site for now. Sprawl is the enemy.

**The real leverage isn't the tools — it's the meta-repo.** A single `rai/` index page on your domain that lists every tool with what it does, who it's for, and a link. *That's* the portfolio. The tools are inventory; the index is the asset, and it's also the thing your TikTok audience and any future investor/collaborator actually clicks on.

One honest note: $200/mo for ChatGPT Pro only earns its keep if you're running Codex multiple times a day. Track usage for a month — if Claude Code is doing 90% of the work, downgrade and reinvest the spend into a Claude Max seat or domain/infra.