# Claude Code Roadmap

## 

# File Path Mentions (@)

File path mentions, triggered by typing the `@` symbol followed by a filename or folder, allow you to manually point the AI toward specific parts of your codebase. This creates a direct reference that prioritizes those files in the current conversation, ensuring the assistant analyzes the exact code you are interested in without having to search your entire project first. It supports autocomplete, so as you type after the @ symbol, a list of matching files appears, allowing you to quickly select the correct path and add it to the conversation context.

Visit the following resources to learn more:

- [@official@Quick commands](https://code.claude.com/docs/en/interactive-mode#built-in-commands)
- [@official@CLAUDE.md imports](https://code.claude.com/docs/en/memory#claude-md-imports)
- [@article@Referencing Files and Resources in Claude Code | Developing with AI Tools | Steve Kinney](https://stevekinney.com/courses/ai-development/referencing-files-in-claude-code)

## 

# Multiline input ()

Multiline input allows you to format complex instructions across several lines without immediately sending the prompt to the AI. The fastest way to create multiline input is by typing `\` followed by `Enter`. This works in all terminals by default and tells the system to treat the next line as a continuation of the current one. However, depending on your terminal and configuration, alternative methods may be available.

Visit the following resources to learn more:

- [@official@Multiline input](https://code.claude.com/docs/en/interactive-mode#multiline-input)
- [@official@Line breaks](http://code.claude.com/docs/en/terminal-config#line-breaks)

## 

# Bash Mode (!)

Bash Mode (triggered by prefixing your input with an exclamation mark !) is a powerful feature that allows you to execute shell commands directly on your machine without involving the Claude Code's reasoning or consuming any tokens. While the AI assistant normally uses the "Bash tool" to run commands on your behalf (which costs money and takes time for the model to "think"), Bash Mode is your direct line to the terminal.

Visit the following resources to learn more:

- [@official@Bash mode with ! prefix](https://code.claude.com/docs/en/interactive-mode#bash-mode-with-prefix)
- [@article@Claude Code and Bash Scripts | Developing with AI Tools | Steve Kinney](https://stevekinney.com/courses/ai-development/claude-code-and-bash-scripts)

## Add Dir

# claude --add-dir

The `claude --add-dir` command is a startup flag that allows you to include extra folders in your working session before the interface even opens. By providing one or more directory paths when you launch the tool (for example, `claude --add-dir ../library --add-dir ./docs`), you grant the assistant permission to read and modify files in those external locations alongside your current project. This is particularly useful for cross-repository tasks, such as updating a shared library and its dependent application simultaneously, as it ensures the AI has a unified view of all relevant codebases from the very first prompt.

## Agent Team

# Agent Team

Agent Teams are an experimental multi-agent orchestration feature in Claude Code that allows you to coordinate multiple AI instances working in parallel on a single project. Agent Teams function as a collaborative network where a designated Team Lead manages a shared task list and delegates work to Teammates who can message each other directly to share findings or debate solutions.

Visit the following resources to learn more:

- [@official@Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)
- [@official@Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)
- [@article@How to Set Up Claude Code Agent Teams (Full Walkthrough + What Actually Changed)](https://www.reddit.com/r/ClaudeCode/comments/1qz8tyy/how_to_set_up_claude_code_agent_teams_full/)
- [@video@Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](https://www.youtube.com/watch?v=-1K_ZWDKpU0)

## Agents

# /agents

The `/agents` command is a specialized management interface used to create, configure, and orchestrate sub-agents within your Claude Code environment. This command transitions from a single-assistant model to a multi-agent workflow, allowing you to delegate specific types of work—like security auditing, unit testing, or architectural planning—to "specialists" that have their own isolated context windows and tailored system prompts.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Create custom subagents](https://code.claude.com/docs/en/sub-agents#use-the-agents-command)
- [@official@Agents flag format](https://code.claude.com/docs/en/cli-reference)
- [@video@Claude Code NEW Sub Agents in 7 Minutes](https://www.youtube.com/watch?v=DNGxMX7ym44)

## Api Usage

# API Usage

Claude Console authentication uses a pay-as-you-go model where the tool connects directly to the Anthropic API using a personal API key rather than a flat-rate monthly subscription. To set this up, you must first create an account at the Claude Console, generate a secret API key, and ensure you have a balance of credits in your account. This mode is ideal for power users or developers who prefer to pay only for the specific amount of data (or tokens) processed during their coding sessions. Because this connection communicates directly with the API, it also allows you to choose specific model versions and provides more granular control over your billing and usage thresholds.

Visit the following resources to learn more:

- [@official@Claude Console](https://platform.claude.com/)
- [@official@Claude Code Analytics API](https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api)
- [@article@Claude Pricing Explained: Subscription Plans & API Costs](https://intuitionlabs.ai/articles/claude-pricing-plans-api-costs)
- [@article@Claude, Claude API, and Claude Code: What's the Difference?](https://eval.16x.engineer/blog/claude-vs-claude-api-vs-claude-code)

## Be Mindful Of Extensions

# Be mindful of extensions

Carefully managing extensions, such as MCP servers, skills, and subagents, is vital because every active integration consumes a portion of Claude’s finite context window, and excessive "context pollution" can lead to degraded reasoning or higher operational costs.

Visit the following resources to learn more:

- [@article@The Hidden Cost of MCP Servers (And When They're Worth It)](https://mariogiancini.com/the-hidden-cost-of-mcp-servers-and-when-theyre-worth-it)
- [@article@Claude Skills are awesome, maybe a bigger deal than MCP](https://simonw.substack.com/p/claude-skills-are-awesome-maybe-a)

## Channels

# Channels

Claude Code channels are MCP server plugins that push messages, alerts, and webhooks into your running Claude Code session, allowing Claude to react to events while you're away from the terminal. Channels enable two-way communication through platforms like Telegram, Discord, and iMessage. You install them as plugins, configure credentials, and pair your account so Claude can receive and respond to messages in real-time. Unlike web sessions that spawn fresh instances, events arrive in your already-open session, making channels ideal for always-on setups where you run Claude in a background process.

Visit the following resources to learn more:

- [@official@Push events into a running session with channels](https://code.claude.com/docs/en/channels)
- [@official@Channels reference](https://code.claude.com/docs/en/channels-reference)
- [@video@Claude Code Channels in 8 Minutes](https://www.youtube.com/watch?v=QZXaAc80OL0)

## Claude   Add Dir

# claude --add-dir

The `claude --add-dir` command is a startup flag that allows you to include extra folders in your working session before the interface even opens. By providing one or more directory paths when you launch the tool (for example, `claude --add-dir ../library --add-dir ./docs`), you grant the assistant permission to read and modify files in those external locations alongside your current project. This is particularly useful for cross-repository tasks, such as updating a shared library and its dependent application simultaneously, as it ensures the AI has a unified view of all relevant codebases from the very first prompt.

## Claude  C

# claude -c

The `claude -c` command (short for --continue) is a CLI flag used to instantly reopen the most recent conversation session in your current directory. Instead of starting a fresh chat with a clean context, this command restores the previous conversation history, allowing you to pick up exactly where you left off without having to re-explain your project’s state or repeat previous instructions.

Visit the following resources to learn more:

- [@official@CLI commands](https://code.claude.com/docs/en/cli-reference#cli-commands)
- [@official@Resume previous conversations](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)

## Claude  P

# claude -p

The `claude -p` command (short for --print) activates Print Mode, which runs Claude Code as a non-interactive, single-use utility rather than a continuous chat session. When you use this flag, you provide a prompt directly in the command line; Claude then executes its agentic loop—researching, editing files, or running commands as needed—and exits immediately once the task is complete. This mode is designed primarily for automation and scripting, allowing you to integrate Claude's reasoning into CI/CD pipelines, shell scripts, or "one-liners".

Visit the following resources to learn more:

- [@official@CLI commands](https://code.claude.com/docs/en/cli-reference#cli-commands)
- [@official@Run Claude Code programmatically](https://code.claude.com/docs/en/headless)
- [@video@Building headless automation with Claude Code | Code w/ Claude](https://www.youtube.com/watch?v=dRsjO-88nBs)

## Claude  R

# claude -r

The `claude -r` command (short for --resume) allows you to restart a specific past conversation by providing its unique Session ID. Unlike the `-c` flag, which automatically opens the very last session you had, `-r` gives you the precision to jump back to any session from your history, ensuring you can continue a specific line of work without losing context or previous tool outputs. If you run the command without an ID—simply typing `claude --resume` —it opens an interactive session picker where you can scroll through a list of recent conversations, see their titles, and choose the one you want to reactivate.

Visit the following resources to learn more:

- [@official@CLI commands](https://code.claude.com/docs/en/cli-reference#cli-commands)
- [@official@Resume or fork sessions](https://code.claude.com/docs/en/how-claude-code-works#resume-or-fork-sessions)

## Claude Cli

# Claude CLI

Claude Code CLI is a command-line tool that acts as an agentic AI coding partner by interacting directly with your local files and terminal. To set it up, you first need an active Claude subscription or an Anthropic Console account. Once installed, navigate to your project folder, type `claude` to start a session, and follow the prompts to log in via your browser.

Visit the following resources to learn more:

- [@official@Getting Started with Claude Code](https://code.claude.com/docs/en/quickstart)
- [@official@Optimize your terminal setup](https://code.claude.com/docs/en/terminal-config)

## Claude Code Security

# Claude Code Security

Claude Code Security is a new feature built into Claude Code that scans your codebase for security vulnerabilities and suggests fixes for your team to review. Every finding goes through a verification process before it reaches you, with severity ratings so you know what to fix first. Nothing gets changed automatically; Claude suggests the fix, but a human always approves it. It is currently available as a limited research preview for Enterprise and Team customers, with free access for open-source maintainers.

Visit the following resources to learn more:

- [@official@Making frontier cybersecurity capabilities available to defenders](https://www.anthropic.com/news/claude-code-security)
- [@article@Evaluating and mitigating the growing risk of LLM-discovered 0-days](https://red.anthropic.com/2026/zero-days/)

## Claude Query

# claude "query"

The `claude "query"` command allows you to start the Claude Code interactive REPL (Read-Eval-Print Loop) with an initial instruction already provided. By passing a string as an argument directly after the `claude` command, the assistant will immediately begin processing that request—such as "explain this project" or "fix the lint errors"—the moment the interface loads. This method is more efficient than opening the tool first and typing your request manually, as it combines the startup and the initial task into a single step while still keeping the session open for further conversation and follow-up actions.

Visit the following resources to learn more:

- [@official@CLI commands](https://code.claude.com/docs/en/cli-reference)

## Claude Workflow

# Claude Workflow

The Claude Code workflow operates as a continuous agentic loop where the AI moves through four primary phases: Explore, Plan, Implement, and Verify. It begins by indexing your local codebase and reading persistent instructions from your [CLAUDE.md](http://CLAUDE.md) file to align with your project's specific standards. When you issue a prompt, Claude uses its suite of built-in tools to research the files (Explore), proposes a detailed step-by-step strategy for the change (Plan), and—upon your approval—executes the modifications using file-editing and shell tools (Implement). The cycle concludes by running your defined test suites or linters (Verify) to ensure no regressions were introduced, often utilizing MCP servers to sync the final results with external platforms like GitHub or Jira.

Visit the following resources to learn more:

- [@official@How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works)
- [@official@Common workflows](https://code.claude.com/docs/en/common-workflows)
- [@article@My Best Workflow for Working with Claude Code : r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1m3pol4/my_best_workflow_for_working_with_claude_code/)
- [@video@Claude Code Workflows That Will 10x Your Productivity](https://www.youtube.com/watch?v=yZvDo_n12ns)
- [@video@The greatest Claude Code workflow ever (10x your speed)](https://www.youtube.com/watch?v=WdD6uD_kupY)

## Claude

# claude command

The `claude` command is the primary entry point used to launch the Claude Code interface from your terminal. When you type this command within a project directory, it initializes the agentic environment, indexes your local files, and establishes a secure connection to the AI model so you can begin issuing natural language instructions. It also supports various flags to customize Claude Code’s behavior.

Visit the following resources to learn more:

- [@official@CLI commands](https://code.claude.com/docs/en/cli-reference#cli-commands)

## Claudemd

# CLAUDE.md

`CLAUDE.md` is a configuration file placed in a project's root directory that provides the AI assistant with specific rules, project context, and custom instructions for that particular codebase. It acts as a set of persistent guidelines that the AI reads at the start of every session to ensure its code suggestions align with your project's coding standards, tech stack, and architectural patterns.

Visit the following resources to learn more:

- [@official@Write an effective CLAUDE.md](https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md)
- [@article@The Complete Guide to CLAUDE.md](https://www.builder.io/blog/claude-md-guide)
- [@article@Writing a good CLAUDE.md | HumanLayer Blog](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [@video@Claude Code Tutorial #2 - CLAUDE.md Files & /init - YouTube](https://www.youtube.com/watch?v=i_OHQH4-M2Y)

## Claudemd

# CLAUDE.md

[CLAUDE.md](http://CLAUDE.md) is a project-specific markdown file that acts as the "persistent memory" and onboarding manual for Claude Code, ensuring the AI adheres to your unique development standards across every session. Since Claude begins each new interaction with a blank context, this file is automatically read at launch to provide essential project "WHY, WHAT, and HOW".

Visit the following resources to learn more:

- [@official@Manage Claude's memory](https://code.claude.com/docs/en/memory#manage-claudes-memory)
- [@article@The Complete Guide to CLAUDE.md](https://www.builder.io/blog/claude-md-guide)
- [@article@What is the point of CLAUDE.md? : r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1nokaln/what_is_the_point_of_claudemd/)
- [@video@How to Use CLAUDE.md in Claude Code in 5 Minutes](https://www.youtube.com/watch?v=h7QJL2_gEXA)
- [@video@CLAUDE.md & /init](https://www.youtube.com/watch?v=i_OHQH4-M2Y&list=PL4cUxeGkcC9g4YJeBqChhFJwKQ9TRiivY)

## Clear

# /clear

The `/clear` command is a utility tool that removes all previous messages, tool outputs, and file contents from the active conversation history. It wipes the current context, allowing you to start a fresh dialogue with the AI without exiting the application or losing your current working directory settings. This is particularly useful for reducing token costs and preventing "context drift," where the AI might become confused by old instructions or irrelevant code snippets from a previous task.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@article@Claude Code Context Guide: Master CLAUDE.md & /clear](https://www.arsturn.com/blog/beyond-prompting-a-guide-to-managing-context-in-claude-code)
- [@article@In claude code, what is the difference between doing /clear and starting a new chat? : r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1myr717/in_claude_code_what_is_the_difference_between/)

## Code Intelligence

# Code Intelligence Plugin

Code Intelligence plugins extend the CLI's native search capabilities by integrating with the Language Server Protocol (LSP), granting Claude the same "IDE-level" awareness found in modern editors.

Visit the following resources to learn more:

- [@official@Code intelligence](https://code.claude.com/docs/en/discover-plugins#code-intelligence)
- [@official@LSP server](https://code.claude.com/docs/en/plugins-reference#lsp-servers)
- [@article@Language Server Protocol](https://microsoft.github.io/language-server-protocol/)

## Common Usecases

# Common Usecases

Claude Code can be used for a wide range of professional software development tasks, from legacy system modernization and large-scale refactoring to rapid prototyping for startups. Organizations use it to navigate and modernize massive codebases containing millions of lines of code, while data science teams employ it to convert exploratory research from notebooks into production-ready data pipelines. In daily engineering workflows, it is frequently applied to automate unit testing, diagnose complex bugs using stack traces, and manage dependency upgrades across entire repositories. Additionally, it has become a powerful tool for infrastructure automation, where DevOps teams use it to manage Kubernetes clusters, configure monitoring systems, and build CI/CD pipelines through natural language instructions.

Visit the following resources to learn more:

- [@official@What you can do](https://code.claude.com/docs/en/overview#what-you-can-do)
- [@official@Common workflows](https://code.claude.com/docs/en/common-workflows)
- [@article@20+ Real Use Cases That Prove Claude Code Is a Game-Changer](https://medium.com/@agencyai/20-real-use-cases-that-prove-claude-code-is-a-game-changer-46ceefaf19ed)
- [@video@8 Insane Claude Code Use Cases (code anything!)](https://www.youtube.com/watch?v=akIHv-n--io)

## Community Tools

# Community Tools

Community tools extend Claude Code's capabilities by integrating it with external platforms via the Model Context Protocol (MCP) and specialized plugins. These integrations allow the assistant to interact directly with services like GitHub for managing pull requests, Slack for sending project updates, and Jira or Linear for tracking issues. Beyond official offerings, the community has developed numerous third-party extensions, which can be easily added via the `/plugin` command.

Visit the following resources to learn more:

- [@official@Conductor](https://docs.conductor.build/)
- [@article@A Hands-On Review of Conductor, an AI Parallel Runner App](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/)

## Compact

# /compact

The `/compact` command is a context management tool designed to optimize your session's memory when the context window begins to fill up. Instead of completely wiping your history like `/clear`, `/compact` instructs Claude to generate a concise summary of the key decisions, code changes, and project state established so far. It then replaces the bulky, line-by-line conversation history with this summarized version, effectively "compressing" the tokens used while preserving the essential knowledge the AI needs to continue the task.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@article@What Actually Happens When You Run /compact in Claude Code](https://dev.to/rigby_/what-actually-happens-when-you-run-compact-in-claude-code-3kl9)
- [@video@3 Ways to Fix Claude Code's Context](https://www.youtube.com/watch?v=yBLwsBKPYSw)

## Config

# /config

The `/config` command is the central management tool for customizing your Claude Code experience and fine-tuning how the assistant interacts with your system. Running this command opens an interactive menu—or allows for direct terminal arguments—to modify global and project-specific settings such as default models, theme preferences, and permission levels.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Claude Code settings](https://code.claude.com/docs/en/settings)

## Connecting Tools With Mcp

# Connecting Tools with MCP

Model Context Protocol (MCP) transforms Claude Code from a local file editor into a connected agent capable of interacting with your entire tech stack, from Jira tickets to live databases. Acting like a "USB-C port for AI," MCP provides a standardized bridge that allows Claude to discover and execute external functions without requiring custom-coded integrations for every service.

Visit the following resources to learn more:

- [@course@Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics)
- [@official@Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
- [@article@What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [@video@Claude Code MCP: How to Add MCP Servers (Complete Guide)](https://www.youtube.com/watch?v=DfWHX7kszQI)
- [@video@Claude Code Tutorial #7 - MCP Servers](https://www.youtube.com/watch?v=X7lgIa6guKg)

## Context

# /context

The `/context` command is a diagnostic tool that provides a technical breakdown of how the model's context window is currently allocated, using a colored grid. While commands like `/usage` show you the "how much," `/context` shows you the "what." It lists every file, conversation turn, and tool result currently being held in the AI's active memory, allowing you to see exactly which resources are consuming tokens.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@article@Monitor Token Usage with the /context Command](https://wmedia.es/en/tips/claude-code-context-command-token-usage)
- [@video@3 Ways to Fix Claude Code's Context](https://www.youtube.com/watch?v=yBLwsBKPYSw)

## Context

# Context

A context window is the total amount of information a model can hold in its active memory at one time, including your conversation history, the files it has read, and the results of any terminal commands it has executed. It functions like a temporary workspace where every word and symbol (counted as tokens) fills up a limited capacity. As this window fills, Claude Code may begin to "forget" earlier details or become less accurate, which is why managing context through commands like `/compact` is essential to keep responses sharp and costs under control.

Visit the following resources to learn more:

- [@official@The context window](https://code.claude.com/docs/en/how-claude-code-works#the-context-window)
- [@official@How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [@article@What is a context window? | IBM](https://www.ibm.com/think/topics/context-window)
- [@video@Claude Code’s Memory Problem (Solved in 12 Minutes) - YouTube](https://www.youtube.com/watch?v=c0g_wYux6X4&t=39s)
- [@video@3 Ways to Fix Claude Code's Context - YouTube](https://www.youtube.com/watch?v=yBLwsBKPYSw)

## Cost

# /cost

The `/cost` command is a financial monitoring tool that provides a real-time snapshot of the monetary expenses and token usage for your active session. While the `/usage` command focuses on how much of your context window is occupied, /cost translates that activity into USD amounts, showing you exactly how much your current conversation has cost based on your API pricing tier.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Using the /cost command](https://code.claude.com/docs/en/costs)

## Creating Skills

# Creating Custom Skills

To create a custom skill in Claude Code, you must establish a new folder within the `.claude/skills/` directory containing a `SKILL.md` file that defines the skill's identity and logic. This file begins with a YAML frontmatter block containing a unique `name` and a detailed `description`, which Claude uses as a trigger to "know" when to activate the skill, and can include an optional `disable-model-invocation: true` flag if you want the skill to run as a manual, deterministic workflow rather than an autonomous one.

Visit the following resources to learn more:

- [@course@Agent Skills with Anthropic](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- [@official@Extend Claude with skills](https://code.claude.com/docs/en/skills#extend-claude-with-skills)
- [@official@How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [@article@Build Your First Claude Code Agent Skill: A Simple Project Memory System That Saves Hours](https://pub.spillwave.com/build-your-first-claude-code-skill-a-simple-project-memory-system-that-saves-hours-1d13f21aff9e)
- [@video@Claude Code Skills & skills.sh - Crash Course](https://www.youtube.com/watch?v=rcRS8-7OgBo)

## Creating Subagents

# Creating Subagents

To create a Subagent in Claude Code, you must define a specialized assistant within a Markdown file located in the `.claude/agents/` directory, using YAML frontmatter to specify its `name`, `description`, `model`, and a restricted set of `tools`.

Visit the following resources to learn more:

- [@official@Create custom subagents](https://code.claude.com/docs/en/sub-agents)
- [@article@Building with Claude Code Subagents (My Beloved Minions)](https://medium.com/@ooi_yee_fei/building-with-claude-code-subagents-my-beloved-minions-b5a9a4318ba5)
- [@video@Claude Code Tutorial #8 - Subagents](https://www.youtube.com/watch?v=Phr7vBx9yFQ)
- [@video@Master Claude Code Sub‑Agents in 10 Minutes](https://www.youtube.com/watch?v=mEt-i8FunG8)

## Ctrlc

# Ctrl+C

`Ctrl+C` is a keyboard shortcut that immediately sends an interrupt signal to the Claude Code terminal to stop its current activity. It is primarily used to halt a long-running process, such as an accidental infinite loop in your code, a search that is taking too long, or a lengthy model response that you realized was going in the wrong direction. This provides a manual "kill switch" that is essential for maintaining control over the agent's actions and preventing the unnecessary consumption of tokens and time.

Visit the following resources to learn more:

- [@official@Interactive mode - Claude Code Docs](https://code.claude.com/docs/en/interactive-mode)
- [@article@How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)

## Ctrlr

# Ctrl+R

`Ctrl+R` is a terminal shortcut that opens the command history search, allowing you to quickly find and reuse previous prompts or terminal commands you have typed during your session. Instead of manually retyping complex instructions or scrolling back through hundreds of lines of output, you can press `Ctrl+R` and start typing a few letters to filter your recent activity until the correct entry is highlighted. Once you find the desired command, you can press `Enter` to run it immediately or use the arrow keys to edit the text before execution.

Visit the following resources to learn more:

- [@official@Interactive mode - Claude Code Docs](https://code.claude.com/docs/en/interactive-mode)
- [@official@Reverse search with Ctrl+R](https://code.claude.com/docs/en/interactive-mode#reverse-search-with-ctrl+r)
- [@article@Ctrl+R: Stop Retyping That Perfect Prompt You Wrote Last Week - DEV Community](https://dev.to/rajeshroyal/ctrlr-stop-retyping-that-perfect-prompt-you-wrote-last-week-19ae)

## Customize Status Line

# Customize Status Line

Claude Code allows you to personalize your terminal environment by customizing the status line, which is the persistent information bar at the bottom of the interface. You can keep essential data like real-time session costs or context usage percentages visible at all times, helping you manage your budget and "context rot" without manually running diagnostic commands.

Visit the following resources to learn more:

- [@official@Customize Status Line](https://code.claude.com/docs/en/statusline)
- [@video@Your Claude Code Terminal Should Look Like This](https://www.youtube.com/watch?v=fiZfVTsPy-w)
- [@video@Claude Code StatusLine Explained (Free Script Generator)](https://www.youtube.com/watch?v=PB9_Q2tfe90)

## Desktop App

# Claude Code Desktop

Claude Code desktop is a software application that allows an AI assistant to interact directly with your local files and development tools through a graphical interface. It functions as an agentic coding partner that can read your codebase, edit files, and execute terminal commands to help build features or fix bugs in real time.

Visit the following resources to learn more:

- [@official@Claude Code on desktop](https://code.claude.com/docs/en/desktop)
- [@article@I Discovered Claude Code Desktop: The (New) Way to Build Faster Than Your Terminal](https://medium.com/@joe.njenga/i-discovered-claude-code-desktop-the-new-way-to-build-faster-than-your-terminal-1679aa6ce790)
- [@video@Claude Code on desktop](https://www.youtube.com/watch?v=zrcCS9oHjtI)
- [@video@Claude Code for Desktop is the BEST way to build apps with AI EVER](https://www.youtube.com/watch?v=pZ2N7CJFbBk)

## Doctor

# /doctor

The `/doctor` command is a diagnostic utility used to troubleshoot and verify the health of your Claude Code installation and its environment. When executed, it runs a series of automated checks to ensure that your authentication tokens are valid, your network connection to the Anthropic servers is stable, and all required system dependencies—like Git and Node.js—are correctly configured. If the tool detects an issue, such as a missing binary or an expired session, it provides a detailed error report and suggested steps to resolve the problem immediately.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@article@Claude Code Installation Guide: Using irm Script, npm Setup, and https://claude.ai/install.ps1 Script](https://vibecodingwithfred.com/blog/claude-code-installation-guide/)

## Editor Extensions

# CLaude Code in Code Editor

IDE extensions allow you to use Claude Code directly within popular development environments like Visual Studio Code and the JetBrains family (including IntelliJ IDEA, PyCharm, and WebStorm). These extensions provide a graphical sidebar and inline diff viewers, enabling you to review proposed code changes side-by-side with your existing files. By integrating with the IDE, Claude gains automatic awareness of your active workspace, current file selection, and even terminal error messages, which eliminates the need to manually copy and paste context.

Visit the following resources to learn more:

- [@official@Use Claude Code in VS Code](https://code.claude.com/docs/en/vs-code)
- [@official@JetBrains IDEs - Claude Code Docs](https://code.claude.com/docs/en/jetbrains)
- [@article@Introducing Claude Agent in JetBrains IDEs](https://blog.jetbrains.com/ai/2025/09/introducing-claude-agent-in-jetbrains-ides/)
- [@video@How to Install Claude Code in VS Code in 3 Minutes](https://www.youtube.com/watch?v=ph5DRCX_g6s)
- [@video@Introducing Claude Agent in JetBrains IDEs](https://www.youtube.com/watch?v=k3XsDxMYCHQ)

## Esc  Esc

# Esc + Esc

Double-tapping the `Esc` key in Claude Code activates the Rewind feature, which serves as a temporal navigation system for both your conversation history and your code state. When triggered, it opens an interactive menu that allows you to jump back to any previous prompt in the session, effectively acting as a "undo" button for AI-driven development. You can choose to restore only the conversation (useful for refining instructions without losing current file edits), restore only the code (to revert specific file changes while keeping the chat context), or restore both to a verified checkpoint. This shortcut is particularly valuable for experimental coding because it automatically creates local checkpoints before every change, allowing you to quickly discard an entire branch of reasoning or a failed implementation without manually restoring individual files or managing Git commits.

Visit the following resources to learn more:

- [@official@Interactive mode - Claude Code Docs](https://code.claude.com/docs/en/interactive-mode#reverse-search-with-ctrl+r)
- [@official@Checkpointing - Claude Code Docs](https://code.claude.com/docs/en/checkpointing)
- [@article@Your Time Machine for Code: Double Esc to Rewind When Things Go Wrong - DEV Community](https://dev.to/rajeshroyal/your-time-machine-for-code-double-esc-to-rewind-when-things-go-wrong-53pa)

## Esc

# Esc Command

The `Esc` key is a navigation shortcut used to exit current menus, cancel active inputs, or clear the command line. If you are in the middle of typing a long prompt and want to start over, pressing Esc will wipe the input field clean, and if you have a dropdown menu or a multi-select list open—such as when choosing files to add to context—it will close that menu without making a selection. This shortcut provides a quick way to reset your immediate interface state without interrupting the underlying AI process or closing the terminal session entirely.

Visit the following resources to learn more:

- [@official@Interactive mode - Claude Code Docs](https://code.claude.com/docs/en/interactive-mode)

## Exit

# /exit

The `/exit` command is a built-in utility used to safely terminate your current Claude Code session and return you to your standard terminal prompt. Unlike force-quitting the application, using this command ensures that the system performs a clean shutdown, which includes saving your conversation history and updating any local session metadata so that you can resume your work later using the `claude -c` flag.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)

## Export

# /export

The `/export` command is a data utility that allows you to save your entire current conversation history into a single file on your local machine. This command generates a Markdown-formatted document containing all your prompts, the AI's responses, and the results of any code changes or terminal commands executed during the session. It is designed for documentation and knowledge sharing, enabling you to archive successful debugging sessions, create project reports, or share a complex implementation logic with teammates who do not have access to your local terminal history.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@article@1.0.44 has new /export command : r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1lw5r1l/1044_has_new_export_command/)

## Git Worktrees

# Git Worktrees

Using Git worktrees with Claude Code is a powerful scaling technique that allows you to run multiple independent AI sessions in parallel without the overhead of context switching or the risk of file-edit collisions. This workflow is highly efficient for "fanning out" tasks: you can supervise several separate worktrees simultaneously, leveraging prompt caching across them for shared codebase context, and simply delete the worktree folder once the branch is merged to keep your environment clean.

Visit the following resources to learn more:

- [@official@Run parallel Claude Code sessions with Git worktrees](https://code.claude.com/docs/en/worktrees)
- [@article@Using Git Worktrees for Parallel AI Development](https://stevekinney.com/courses/ai-development/git-worktrees)
- [@video@Git Worktrees: The secret sauce to Claude Code!](https://www.youtube.com/watch?v=up91rbPEdVc)

## Haiku

# Haiku

Claude Haiku is the fastest and most cost-effective model in the Claude family, specifically engineered for high-speed, high-volume tasks that require near-instant responsiveness. It provides a compact but powerful solution for real-time applications like customer service chatbots, rapid data extraction, and moderating large content streams where low latency is critical.

Visit the following resources to learn more:

- [@official@Introducing Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5)
- [@official@Claude Haiku 4.5](https://www.anthropic.com/claude/haiku)
- [@video@Introducing Claude Haiku 4.5](https://www.youtube.com/watch?v=ccQSHQ3VGIc)
- [@video@Anthropic’s Claude Haiku 4.5 in 6 Minutes](https://www.youtube.com/watch?v=jC_rX86O1Q8)

## Headless Mode

# Headless mode

Headless mode in Claude Code, enabled by the `-p` (or `--print`) flag, transforms the interactive terminal assistant into a programmable Unix-style utility designed for automation and CI/CD pipelines.

Visit the following resources to learn more:

- [@official@Run Claude Code programmatically](https://code.claude.com/docs/en/headless)
- [@article@Headless Mode: Unleash AI in Your CI/CD Pipeline](https://dev.to/rajeshroyal/headless-mode-unleash-ai-in-your-cicd-pipeline-1imm)
- [@video@Building headless automation with Claude Code | Code w/ Claude](https://www.youtube.com/watch?v=dRsjO-88nBs)

## Help

# /help

The `/help` command is an interactive directory that provides a comprehensive list of all available slash commands, keyboard shortcuts, and system features. When you type it, Claude Code displays a searchable guide that explains how to use tools such as context management, file mentions, and permission modes. It is designed to be a quick-access manual that helps you discover advanced functionality or refresh your memory of syntax without leaving your terminal or consulting external documentation.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@video@Claude Code Tutorial #6 - Slash Commands](https://www.youtube.com/watch?v=52KBhQqqHuc&t=1s)

## Hook Events  Matchers

# Hook Events & Matchers

In Claude Code, Hook Events represent the specific lifecycle moments when custom logic can be triggered, while Matchers act as the regex-based filters that determine which specific actions within those moments should fire the hook.

Visit the following resources to learn more:

- [@official@Hook Events](https://code.claude.com/docs/en/hooks#hook-events)
- [@official@Event Matchers](https://code.claude.com/docs/en/hooks#matcher-patterns)
- [@article@Hooks: Automating Event Reactions](https://angelo-lima.fr/en/claude-code-hooks/)

## Hook Inputs  Outputs

# Hook Inputs & Outputs

Hooks communicate via a standardized JSON interface: Inputs are passed to the hook via `stdin`, and Outputs are returned via `stdout` to influence the agent's next move. The input payload typically includes a `context` object containing session metadata and event-specific data, such as the `tool` name and its arguments (e.g., the exact code being written or command being run). To respond, your hook must return a JSON object.

Visit the following resources to learn more:

- [@official@Hook Inputs & Outputs](https://code.claude.com/docs/en/hooks#hook-input-and-output)

## Hook Types

# Hook Types

In Claude Code, you can configure three distinct handler types for your hooks—Command, Prompt, and Agent—depending on whether you need a script, an AI "judgement call," or a specialized researcher to validate actions. Command hooks (`type: "command"`) are deterministic shell scripts that execute standard commands (like `npm run lint`) and use exit codes to either approve the action or block it with an error message. Prompt hooks (`type: "prompt"`) use a lightweight Claude model for single-turn evaluation, where the model analyzes the context (e.g., "Is this commit message descriptive?") and returns a simple JSON yes/no decision. Finally, Agent hooks (`type: "agent"`) are the most sophisticated, spawning a multi-turn subagent with tool access (like `Read` or `Grep`) to conduct deep, autonomous verification before deciding if the main agent should proceed.

Visit the following resources to learn more:

- [@official@Hook Types](https://code.claude.com/docs/en/hooks)
- [@official@Prompt-based hooks](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks)
- [@official@Agent-based hooks](https://code.claude.com/docs/en/hooks-guide#agent-based-hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)

## Hooks

# Hooks

Hooks are automated triggers that execute specific scripts or commands at key points in the AI's workflow, such as before or after the assistant performs a task. These hooks allow developers to enforce project standards and ensure system reliability without manual intervention, much like Git hooks but designed for an AI-driven development cycle.

Visit the following resources to learn more:

- [@official@Automate workflows with hooks - Claude Code Docs](https://code.claude.com/docs/en/hooks-guide)
- [@article@Automate Your AI Workflows with Claude Code Hooks | Butler's Log](https://blog.gitbutler.com/automate-your-ai-workflows-with-claude-code-hooks)
- [@video@How Claude Code Hooks Save Me HOURS Daily](https://www.youtube.com/watch?v=Q4gsvJvRjCU)
- [@video@Claude Code hooks are Officially Awesome](https://www.youtube.com/watch?v=eFjqogpmNkQ)

## Hooks

# /hooks

The `/hooks` command opens an interactive management menu for configuring automated workflows that trigger at specific points in the Claude Code lifecycle. While features like `CLAUDE.md` provide "soft" instructions, hooks offer deterministic control, ensuring that specific shell commands or AI evaluations run every single time a certain event occurs—such as formatting code after an edit or sending a notification when Claude needs your attention.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Hooks reference](https://code.claude.com/docs/en/hooks)
- [@official@The /hooks menu](https://code.claude.com/docs/en/hooks#the-hooks-menu)

## Hooks

# Hooks

Hooks are automated triggers that execute specific scripts or commands at key points in the AI's workflow, such as before or after the assistant performs a task. These hooks allow developers to enforce project standards and ensure system reliability without manual intervention, much like Git hooks but designed for an AI-driven development cycle.

Visit the following resources to learn more:

- [@official@Automate workflows with hooks - Claude Code Docs](https://code.claude.com/docs/en/hooks-guide)
- [@article@Automate Your AI Workflows with Claude Code Hooks | Butler's Log](https://blog.gitbutler.com/automate-your-ai-workflows-with-claude-code-hooks)
- [@video@How Claude Code Hooks Save Me HOURS Daily](https://www.youtube.com/watch?v=Q4gsvJvRjCU)
- [@video@Claude Code hooks are Officially Awesome](https://www.youtube.com/watch?v=eFjqogpmNkQ)

## How To Structure

# How to Structure CLAUDE.md

To write an effective [CLAUDE.md](http://CLAUDE.md), you should treat it as a concise, persistent "source of truth" that provides Claude with the project-specific context it cannot infer from the code alone. The file should be kept short and human-readable, focusing on non-obvious information like unique bash commands for building and testing, repository-specific code styles, and architectural decisions.

Visit the following resources to learn more:

- [@official@Write an effective CLAUDE.md](https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md)
- [@article@How to structure your CLAUDE.md file](https://www.builder.io/blog/claude-md-guide)
- [@article@How we structure our CLAUDE.md file (and why) : r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1mecx5t/how_we_structure_our_claudemd_file_and_why/)
- [@article@# Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

## Init

# /init

The `/init` command is the initialization utility used to set up Claude Code for a specific project directory. When you run this command, it creates a [CLAUDE.md](http://CLAUDE.md) file in your current folder. This file serves as the "foundation" for the assistant, allowing you to define project-specific coding standards, build commands, and test suites that Claude will automatically reference in every future session within that repository.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Write an effective CLAUDE.md](https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md)
- [@article@Build your own /init command like Claude Code](https://kau.sh/blog/build-ai-init-command/)

## Introduction

# What is Claude Code?

Claude Code is an AI-powered coding tool developed by Anthropic that operates directly in the terminal. Unlike traditional autocomplete tools, Claude Code functions as an autonomous agent capable of understanding entire codebases, executing multi-step tasks, and maintaining context across complex projects. By understanding the entire codebase, Claude Code helps simplify workflows, making it a powerful tool for software development.

Visit the following resources to learn more:

- [@course@Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- [@course@Claude Code 101](https://anthropic.skilljar.com/claude-code-101)
- [@official@Claude Code overview](https://code.claude.com/docs/en/overview)
- [@official@How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)

## Locations

# Locations of CLAUDE.md

Claude Code manages instructions through a hierarchical memory system that layers context based on the directory structure of your project. At the start of every session, Claude recursively searches from your current working directory up to the root, automatically loading global preferences from `~/.claude/CLAUDE.md` and shared team standards from the project root's `CLAUDE.md`. Claude also supports progressive disclosure via subdirectory [CLAUDE.md](http://CLAUDE.md) files.

Visit the following resources to learn more:

- [@official@Write an effective CLAUDE.md](https://code.claude.com/docs/en/best-practices)
- [@official@Determine memory type](https://code.claude.com/docs/en/memory#determine-memory-type)
- [@article@The Complete Guide to CLAUDE.md](https://www.builder.io/blog/claude-md-guide)

## Manage Context

# Manage Context

Active management of the context window is the single most effective way to ensure reliable model performance and predictable operational costs, as Claude Code is billed based on the total number of tokens processed in each turn. Because the tool re-reads the entire conversation history with every new message to maintain state, unmanaged sessions can quickly balloon in size, leading to "context rot" where the model loses track of early instructions or struggles with "lost-in-the-middle" accuracy degradation.

Visit the following resources to learn more:

- [@official@Manage costs effectively](https://code.claude.com/docs/en/costs#reduce-token-usage)

## Manage Sessions

# Manage Sessions

Claude Code manages sessions through a persistent, local architecture where every interaction is stored in a unique session file, allowing you to resume work using terminal flags like `claude --continue` (for the most recent thread) or `claude --resume` (to open an interactive picker of past conversations). While each new session initializes with a fresh context window to optimize token usage and avoid irrelevance, Claude automatically snapshots affected files before any modification, enabling you to use the `/rewind` command to revert both code and conversation history to a previous "checkpoint."

Visit the following resources to learn more:

- [@official@Work with sessions](https://code.claude.com/docs/en/how-claude-code-works#work-with-sessions)
- [@article@Claude Code Session Management | Developing with AI Tools | Steve Kinney](https://stevekinney.com/courses/ai-development/claude-code-session-management)

## Mcp

# MCP

The Model Context Protocol (MCP) is an open-source standard that enables a Claude Code to connect securely to a vast ecosystem of external tools, databases, and third-party services. By acting like a "universal connector" for AI, MCP allows you to extend the Claude Code's core capabilities beyond simple file editing, giving it the power to interact with APIs like GitHub to manage pull requests, query live databases such as PostgreSQL or Snowflake, and much more.

Visit the following resources to learn more:

- [@course@Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol)
- [@course@Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics)
- [@official@Connect Claude Code to tools via MCP - Claude Code Docs](https://code.claude.com/docs/en/mcp)
- [@article@What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [@video@Claude Code Tutorial #7 - MCP Servers](https://www.youtube.com/watch?v=X7lgIa6guKg)

## Mcp

# /mcp

The `/mcp` command is the integration hub for the Model Context Protocol, an open standard that connects Claude Code to external data sources and third-party tools. While you use the terminal command `claude mcp add` to install a new server, the `/mcp` slash command is used inside the session to manage those connections, authorize permissions, and view the specific capabilities (tools) available to the AI.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)

## Memory

# /memory

The `/memory` command is a knowledge management tool used to create and manage persistent information that survives across different Claude Code sessions. Unlike the `/compact` command, which only optimizes the current conversation's temporary window, `/memory` interacts with permanent storage—primarily your project's [CLAUDE.md](http://CLAUDE.md) file and a hidden auto-memory directory. When you run this command, it typically opens your system's default text editor, allowing you to manually refine the coding standards, architectural decisions, and project-specific patterns that Claude should "remember" every time you launch the tool in that directory.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Manage Claude's memory](https://code.claude.com/docs/en/memory#directly-edit-memories-with-memory)

## Mobile Channels

# Channels

To use Claude Code with mobile apps through channels, you install a pre-built channel plugin for your messaging platform, like Telegram, Discord, or iMessage. The plugin runs locally on your computer and polls the platform's API for new messages. When someone sends you a message on the mobile app, the plugin receives it and forwards it to Claude Code, which can then read and respond. You configure the plugin in your MCP config file, and Claude Code spawns it automatically. The plugin acts as a bridge between the mobile app and Claude Code, so you can chat with Claude through your phone without exposing any URLs to the internet.

Visit the following resources to learn more:

- [@official@Push events into a running session with channels](https://code.claude.com/docs/en/channels)
- [@official@Channels reference](https://code.claude.com/docs/en/channels-reference)
- [@video@Claude Code Channels in 8 Minutes](https://www.youtube.com/watch?v=QZXaAc80OL0)

## Model Configuration

# Model Configuration

Claude Code offers a highly flexible model configuration hierarchy that allows you to balance speed, cost, and reasoning depth across different tasks. You can switch models instantly during an active session using the `/model` command, specify a model at startup with the `--model` flag, or set a permanent default in your `~/.claude/settings.json` file using the `model` key. The system supports semantic aliases like sonnet (default for daily coding), haiku (fast and efficient), and opus (high-reasoning for complex architecture), as well as a specialized `opusplan` mode that intelligently uses Opus for strategic planning before automatically switching to Sonnet for the actual code implementation. Furthermore, you can fine-tune performance on supported models by adjusting the `effortLevel` (low, medium, or high), which controls how much "thinking time" Claude allocates to solving difficult logic puzzles versus generating rapid responses.

Visit the following resources to learn more:

- [@official@Model configuration](https://code.claude.com/docs/en/model-config#model-configuration)
- [@article@A complete guide to model configuration in Claude Code](https://www.eesel.ai/blog/model-configuration-claude-code)

## Model

# /model

The `/model` command is a switcher utility that allows you to change which large language model (LLM) is powering your current session without restarting the application. This is particularly useful for cost-performance optimization; you can use a high-intelligence model like Claude Sonnet for complex architectural planning and then switch to a faster, cheaper model like Claude Haiku for repetitive tasks like writing boilerplate code or unit tests.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Model configuration](https://code.claude.com/docs/en/model-config#setting-your-model)

## Models

# Claude Code Models

Claude Code is powered by three distinct models—Opus, Sonnet, and Haiku— each optimized for a specific role within the development lifecycle. **Claude Opus** is the "deep thinker" and primary architect, used for complex reasoning, high-level system design, and surgical bug fixes in large codebases. **Claude Sonnet** serves as the versatile "balanced builder," providing a high-speed middle ground for daily tasks like implementing feature logic, writing boilerplate, and managing state across multiple files. **Claude Haiku** is the "fast-response specialist," designed for near-instant execution of lightweight tasks, such as generating rapid UI prototypes, drafting commit messages, or acting as parallel sub-agents to scan logs and run quick checks.

Visit the following resources to learn more:

- [@official@Models](https://code.claude.com/docs/en/how-claude-code-works#models)
- [@official@Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [@official@Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- [@article@A practical guide to Claude Code model selection](https://www.eesel.ai/blog/claude-code-model-selection)

## Modes

# Modes

Permission modes are settings that control the level of autonomy the AI has when interacting with your computer. By default, the system operates in Default Mode, where it must ask for your approval before it edits any files or executes shell commands. You can cycle through other levels of authority, such as Accept-Edits Mode, which allows the AI to modify files automatically while still prompting you for terminal commands, or Plan Mode, which restricts the AI to read-only tools so it can research and outline a strategy without making any actual changes. For advanced workflows, specialized states like Delegate Mode exist to limit a "lead" agent to coordinating other sub-agents, while the high-risk Bypass-Permissions Mode removes all approval prompts entirely for use in secure, isolated environments.

Visit the following resources to learn more:

- [@official@Configure permissions](https://code.claude.com/docs/en/permissions)
- [@article@A complete guide to Claude Code permissions](https://www.eesel.ai/blog/claude-code-permissions)
- [@video@Claude Code Tutorial #4 - Tools & Permissions](https://www.youtube.com/watch?v=TU0ZcDFq0e0)

## Opus

# Opus

Claude Opus is the most advanced and capable large language model in the Claude family, designed specifically for high-level reasoning and complex problem-solving. It functions as a "deep thinking" engine that can handle vast amounts of information and follow intricate instructions with a high degree of accuracy and nuance.

Visit the following resources to learn more:

- [@official@Claude Opus 4.6 \ Anthropic](https://www.anthropic.com/claude/opus)
- [@official@What's new in Claude 4.6 - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)
- [@video@Introducing Claude Opus 4.6](https://www.youtube.com/watch?v=dPn3GBI8lII)
- [@video@Claude Opus 4.6: The Biggest AI Jump I've Covered--It's Not Close. (Here's What You Need to Know)](https://www.youtube.com/watch?v=JKk77rzOL34)

## Opusplan

# Opusplan

`opusplan` is a specialized command alias for Claude Code that combines the high-level reasoning of the most advanced model with the speed and efficiency of a faster one to optimize complex development tasks. When you initiate a session using `claude opusplan`, the tool uses Claude Opus to analyze your request, explore the codebase, and draft a comprehensive technical strategy, ensuring that the initial logic and architectural decisions are as accurate as possible.

Visit the following resources to learn more:

- [@official@opusplan model setting](https://code.claude.com/docs/en/model-config#opusplan-model-setting)
- [@video@Claude Code Opus Plan Mode // 1M Context // Testing ++](https://www.youtube.com/watch?v=I2aAkp7q_uY)

## Output Styles

# Output Styles

Claude Code allows you to switch between different output styles to adapt the agent’s persona and verbosity to your specific needs, effectively modifying its core system prompt. Beyond the standard coding mode, you can use built-in styles like Explanatory, which provides educational insights into implementation choices, or Learning, a collaborative mode where Claude places `TODO(human)` markers to encourage hands-on contribution.

Visit the following resources to learn more:

- [@official@Output styles](https://code.claude.com/docs/en/output-styles#output-styles)
- [@article@Share your Claude Code output styles](https://www.reddit.com/r/ClaudeAI/comments/1mqp4g4/share_your_claude_code_output_styles/)
- [@article@A practical guide to output styles in Claude Code](https://www.eesel.ai/blog/output-styles-claude-code)
- [@video@New Claude Code Output Styles Are HUGE](https://www.youtube.com/watch?v=IokDmpuXTrQ)

## Permission Modes

# Permission Modes

Claude Code features several permission modes that define the balance between autonomy and safety during your session, ranging from Plan mode, which restricts Claude to a read-only state for exploration and strategy without any tool execution, to BypassPermissions mode (often called "YOLO mode"), which grants the AI full autonomy to run any command or edit any file without interruption.

Visit the following resources to learn more:

- [@official@Permission modes](https://code.claude.com/docs/en/permissions#permission-modes)
- [@article@A complete guide to Claude Code permissions](https://www.eesel.ai/blog/claude-code-permissions)
- [@article@3 Things You Must Know About /permissions in Claude Code](https://wmedia.es/en/tips/claude-code-permissions-3-key-concepts)
- [@article@Claude Code on Loop: The Ultimate YOLO Mode](https://mfyz.com/claude-code-on-loop-autonomous-ai-coding/)
- [@video@Claude Code Tutorial #4 - Tools & Permissions](https://www.youtube.com/watch?v=TU0ZcDFq0e0)

## Permissions

# /permissions

The `/permissions` command is a security management interface that allows you to view and adjust the rules governing what Claude can and cannot do on your machine. By default, Claude Code operates with a "human-in-the-loop" philosophy, meaning it asks for your approval before performing any action that could affect your system—such as modifying a file or running a terminal command. The `/permissions` command allows you to grant "permanent" trust to specific tools or commands, reducing the number of interruptions during your workflow.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Manage permissions](https://code.claude.com/docs/en/permissions)

## Plan Mode

# Plan Mode

Plan Mode is a strictly read-only permission state that allows Claude to analyze your codebase, research dependencies, and draft a step-by-step implementation strategy without the risk of modifying any files or executing state-changing commands.

Visit the following resources to learn more:

- [@official@How to use Plan Mode](https://code.claude.com/docs/en/common-workflows#how-to-use-plan-mode)
- [@official@Explore first, then plan, then code](https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code)
- [@article@What Actually Is Claude Code’s Plan Mode?](https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/)
- [@article@Claude Code Plan Mode | Developing with AI Tools | Steve Kinney](https://stevekinney.com/courses/ai-development/claude-code-plan-mode)
- [@video@I was an AI skeptic. Then I tried plan mode](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=70s)
- [@video@How I Use Claude Code Plan Mode: 3 Examples](https://www.youtube.com/watch?v=altX5elI-1k)

## Plan

# /plan

Plan Mode is a read-only environment that allows the AI to research, analyze, and outline a multi-step strategy for a task without making any actual changes to your files or executing state-altering commands. When you enter this mode—either by typing `/plan` or pressing `Shift+Tab`—the assistant focuses on gathering context and identifying dependencies to create a detailed implementation document. This serves as a safety gate where you can review and edit the proposed approach (using `Ctrl+G` to open the plan file) before giving the final approval to transition into an execution mode to apply the changes.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Use Plan Mode for safe code analysis](https://code.claude.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis)
- [@article@What Actually Is Claude Code’s Plan Mode?](https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/)

## Plugins

# Plugins

Claude Code plugins are shareable packages that bundle multiple customizations, including slash commands, specialized agents, skills, hooks, and Model Context Protocol (MCP) servers, into a single installable unit. They serve as a standardized way to distribute complex AI workflows across different projects or within an engineering team, ensuring that every developer has access to the same tools and coding standards.

Visit the following resources to learn more:

- [@official@Discover and install prebuilt plugins through marketplaces - Claude Code Docs](https://code.claude.com/docs/en/discover-plugins)
- [@official@Plugins](https://claude.com/plugins)
- [@opensource@plugins](https://github.com/anthropics/claude-code/tree/main/plugins)
- [@article@Claude Code Now Has SUPERPOWERS! (plugin)](https://www.youtube.com/watch?v=vfVQP2AbUHo)
- [@article@Claude Code Plugins Just Changed My Workflow Forever](https://www.youtube.com/watch?v=-KusSduAP1A)

## Plugins

# Plugins

Claude Code plugins are shareable packages that bundle multiple customizations, including slash commands, specialized agents, skills, hooks, and Model Context Protocol (MCP) servers, into a single installable unit. They serve as a standardized way to distribute complex AI workflows across different projects or within an engineering team, ensuring that every developer has access to the same tools and coding standards.

Visit the following resources to learn more:

- [@official@Discover and install prebuilt plugins through marketplaces - Claude Code Docs](https://code.claude.com/docs/en/discover-plugins)
- [@official@Plugins](https://claude.com/plugins)
- [@opensource@plugins](https://github.com/anthropics/claude-code/tree/main/plugins)
- [@video@Claude Code Now Has SUPERPOWERS! (plugin)](https://www.youtube.com/watch?v=vfVQP2AbUHo)

## Posttooluse

# PostToolUse

The `PostToolUse` hook is a reactive lifecycle event that triggers immediately after a tool (like Bash, Write, Edit, or a custom MCP tool) completes its execution. While the `PreToolUse` hook acts as a guard to block actions, the `PostToolUse` hook is designed for automation, cleanup, and quality control—ensuring that every action Claude takes adheres to your project's standards.

Visit the following resources to learn more:

- [@official@Hooks reference](https://code.claude.com/docs/en/hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)

## Pretooluse

# PreToolUse

The `PreToolUse` hook is a validation gate that executes immediately after Claude decides to use a tool (like writing a file or running a shell command) but before that tool actually runs. It is primarily used for security, policy enforcement, and input sanitization, acting as a final check to ensure the AI's proposed action is safe and correct.

Visit the following resources to learn more:

- [@official@Hooks reference](https://code.claude.com/docs/en/hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)
- [@article@Secure Your Claude Skills with Custom PreToolUse Hooks](https://egghead.io/secure-your-claude-skills-with-custom-pre-tool-use-hooks~dhqko)

## Prompt Caching

# Prompt Caching

Prompt caching in Claude Code is a performance-optimizing feature that stores the frequently used "prefixes" of your conversations—such as your entire codebase state, system instructions, and tool definitions—so they don't have to be reprocessed from scratch with every new message. In an agentic environment where Claude often re-reads your files multiple times to maintain context, caching acts as a "checkpoint" system: while the initial write to the cache carries a slight premium, every subsequent interaction that reuses that prefix receives a 90% discount on input tokens and up to an 85% reduction in latency. Claude Code handles this automatically by placing "cache breakpoints" at strategic points in the prompt (like after your [CLAUDE.md](http://CLAUDE.md) and project structure), ensuring that even as your conversation grows, the "static" foundation of your project remains instantly accessible and cost-effective.

## Reduce Token Usage

# Prompt Caching

Prompt caching in Claude Code is a performance-optimizing feature that stores the frequently used "prefixes" of your conversations—such as your entire codebase state, system instructions, and tool definitions—so they don't have to be reprocessed from scratch with every new message. In an agentic environment where Claude often re-reads your files multiple times to maintain context, caching acts as a "checkpoint" system: while the initial write to the cache carries a slight premium, every subsequent interaction that reuses that prefix receives a 90% discount on input tokens and up to an 85% reduction in latency. Claude Code handles this automatically by placing "cache breakpoints" at strategic points in the prompt (like after your CLAUDE.md and project structure), ensuring that even as your conversation grows, the "static" foundation of your project remains instantly accessible and cost-effective.

## Resume

# Resume Conversations

To resume a conversation in Claude Code, you can use the terminal command `claude --continue` (or `-c`) to instantly pick up the most recent session in your current directory, or `claude --resume` (or `-r`) to open an interactive session picker. This picker allows you to browse past conversations and select one using your arrow keys and the Enter key. If you know a specific session ID, you can bypass the menu by running `claude --resume <session_id>`. Once inside a session, you can also use the `/resume` slash command to switch between conversations without exiting the tool.

Visit the following resources to learn more:

- [@official@Resume previous conversations](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)
- [@official@Resume conversations](https://code.claude.com/docs/en/best-practices#resume-conversations)

## Rewind

# /rewind

The `/rewind` command is a history management tool that allows you to undo recent turns in your conversation. When executed, it removes the most recent prompt and response from the active context, effectively "winding back" the session to a previous state. This is particularly useful if the AI misunderstood a complex instruction or if a code generation task went in the wrong direction, as it allows you to re-issue the command with better clarity without the baggage of the failed attempt cluttering the model's memory or inflating your token usage.

Visit the following resources to learn more:

- [@official@Built-in commadns](https://code.claude.com/docs/en/interactive-mode)
- [@official@Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [@article@Rewind Changes Instantly with Checkpoints](https://wmedia.es/en/tips/rewind-changes-instantly-with-checkpoints)

## Rewind

# Rewind Conversations

To rewind a conversation in Claude Code, you can use the `/rewind` slash command or the `Esc + Esc` keyboard shortcut to open the interactive checkpoint menu. This feature leverages the tool's automatic snapshotting, which creates a restore point for every user prompt and file modification throughout your session.

Visit the following resources to learn more:

- [@official@Rewind and summarize](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)
- [@official@Rewind with checkpoints](https://code.claude.com/docs/en/best-practices#rewind-with-checkpoints)
- [@article@Claude Code Checkpoints: 5 Patterns for Disaster Recovery | Medium](https://alirezarezvani.medium.com/claude-code-rewind-5-patterns-after-a-3-hour-disaster-a9de9bce0372)

## Scaling Claude

# Scaling Claude Code

Claude Code offers several ways to parallelize work across multiple agents or sessions: subagents, agent view, agent teams, and worktrees. Subagents are delegated workers that handle a side task within their own context and return a summary, keeping the main conversation clean. Agent view lets you dispatch independent sessions to the background and monitor them from a single screen. Agent teams coordinate multiple sessions through a shared task list and inter-agent messaging, managed by a lead agent. Worktrees isolate parallel sessions into separate git checkouts so they never conflict over the same files.

Visit the following resources to learn more:

- [@official@Run agents in parallel](https://code.claude.com/docs/en/agents)
- [@official@Agent view](https://code.claude.com/docs/en/agent-view)

## Scheduling Jobs

# Scheduling Jobs

Scheduled tasks let you run prompts automatically on a schedule in Claude Code. You can use the `/loop` command to repeat a prompt at regular intervals (like every 5 minutes or every 2 hours) while your session is open. You can also set one-time reminders for specific times. The tasks run in the background and stop when you close Claude Code. If you need tasks to keep running after you close the program, you should use Cloud or Desktop scheduled tasks instead.

Visit the following resources to learn more:

- [@official@Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
- [@official@Schedule tasks on the web](https://code.claude.com/docs/en/web-scheduled-tasks)
- [@article@Claude Code Loop vs Scheduled Tasks: Which Should You Use?](https://www.mindstudio.ai/blog/claude-code-loop-vs-scheduled-tasks)
- [@video@Claude Code Scheduled Tasks Are Insane](https://www.youtube.com/watch?v=U_cDKkDvPAQ)

## Security Best Practices

# Security Best Practices

Security is the most critical pillar of using Claude Code because giving an AI agent the ability to execute terminal commands and modify files creates a powerful "intern with root access" who is susceptible to prompt injection and data exfiltration.

Visit the following resources to learn more:

- [@official@Security](https://code.claude.com/docs/en/security#security)
- [@official@Sandboxing](https://code.claude.com/docs/en/sandboxing)
- [@official@Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing)
- [@article@A deep dive into security for Claude Code in 2025](https://www.eesel.ai/blog/security-claude-code)

## Sessionend

# SessionEnd

The `SessionEnd` hook is a teardown lifecycle event that triggers when you exit Claude Code or terminate a session. While `SessionStart` is for preparation, `SessionEnd` is your dedicated window for cleanup, archiving, and final reporting. It ensures that your environment is left in a clean state and that any important session metrics are captured before the process fully closes.

Visit the following resources to learn more:

- [@official@Hooks reference](https://code.claude.com/docs/en/hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)
- [@article@Claude Code Session Hooks: Make Every Session Start Smart (and End Clean)](https://medium.com/@CodeCoup/claude-code-session-hooks-make-every-session-start-smart-and-end-clean-e505e6914d45)

## Sessionstart

# SessionStart

The `SessionStart` hook is an initialization lifecycle event that triggers at the very beginning of a Claude Code interaction. Unlike other hooks that react to specific user prompts or file edits, `SessionStart` is designed to bootstrap your environment and inject high-priority context before the first prompt is even processed.

Visit the following resources to learn more:

- [@official@Hooks reference](https://code.claude.com/docs/en/hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)
- [@article@Claude Code Session Hooks: Make Every Session Start Smart (and End Clean)](https://medium.com/@CodeCoup/claude-code-session-hooks-make-every-session-start-smart-and-end-clean-e505e6914d45)

## Setting Up Claude

# Setting up Claude Code

To set up Claude Code, you first install the CLI tool through your terminal using a single command tailored to your operating system. For macOS, Linux, or WSL, you run `curl -fsSL https://claude.ai/install.sh | bash`, while Windows users can use PowerShell to run `irm https://claude.ai/install.ps1 | iex`. Once the installation is complete, you navigate to any code project directory and type `claude`, which will trigger a one-time login process where you authenticate using your Claude account or an Anthropic Console API key. After logging in, the tool is ready to use immediately.

Visit the following resources to learn more:

- [@official@Getting started with Claude Code](https://code.claude.com/docs/en/quickstart)

## Shifttab

# Shift+Tab

`Shift+Tab` is a navigation shortcut that allows you to cycle through different permission modes to control how much autonomy the AI assistant has over your computer. These modes act as a security dial, ranging from Default Mode, where the assistant must ask for your approval before making any file edits or running terminal commands, to Auto-Accept Mode, which grants it the power to modify files automatically while still prompting for shell commands. Additionally, the cycle includes Plan Mode, a specialized read-only state that restricts the assistant to searching and analyzing your codebase without the ability to change any files or execute code. By toggling these modes on the fly, you can switch from a highly controlled "safety-first" workflow for critical system files to a high-speed, autonomous mode for repetitive tasks like styling or unit testing.

Visit the following resources to learn more:

- [@official@Interactive mode - Claude Code Docs](https://code.claude.com/docs/en/interactive-mode)
- [@article@Claude Code Plan Mode | Developing with AI Tools | Steve Kinney](https://stevekinney.com/courses/ai-development/claude-code-plan-mode)

## Skill Best Practices

# Skill Best Practices

When configuring Claude Code skills, the primary best practice is to optimize for discoverability and context efficiency by using precise YAML frontmatter and "lazy loading." Your skill's `description` should act as a clear semantic trigger, using specific keywords that help Claude identify exactly when to activate the expert instructions without bloating the context window of every conversation. Structure the `SKILL.md` with a narrow, modular focus rather than creating a "Swiss Army Knife" skill; if a workflow has non-negotiable side effects, use `disable-model-invocation: true` to ensure it only runs when manually triggered via a slash command. Additionally, leverage argument placeholders (like `$ARGUMENTS`) to make your skills reusable across different files, and store them in the project’s `.claude/skills/` directory so they are version-controlled and shared with your team. Finally, keep skill instructions deterministic by providing step-by-step tool sequences, which ensures Claude follows your project’s "golden path" for complex tasks like deployments or security audits.

## Skill Scope

# Skill Best Practices

When configuring Claude Code skills, the primary best practice is to optimize for discoverability and context efficiency by using precise YAML frontmatter and "lazy loading." Your skill's `description` should act as a clear semantic trigger, using specific keywords that help Claude identify exactly when to activate the expert instructions without bloating the context window of every conversation. Structure the `SKILL.md` with a narrow, modular focus rather than creating a "Swiss Army Knife" skill; if a workflow has non-negotiable side effects, use `disable-model-invocation: true` to ensure it only runs when manually triggered via a slash command. Additionally, leverage argument placeholders (like `$ARGUMENTS`) to make your skills reusable across different files, and store them in the project’s `.claude/skills/` directory so they are version-controlled and shared with your team. Finally, keep skill instructions deterministic by providing step-by-step tool sequences, which ensures Claude follows your project’s "golden path" for complex tasks like deployments or security audits.

## Skills For Mcp

# Skills for MCP

Skills act as structured, reusable knowledge packages that dramatically improve how Claude interacts with MCP (Model Context Protocol) servers by giving it precise, context-aware instructions for specific tools and workflows. Rather than relying on Claude to infer how to use a given MCP server from scratch each time, skills provide curated guidance that helps Claude make smarter, more reliable decisions when invoking tools, chaining calls, and interpreting results.

Visit the following resources to learn more:

- [@official@The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en)
- [@opensource@Anthropic Skills Guide](https://github.com/darraghh1/my-claude-setup/blob/main/docs/research/anthropic-skills-guide.md)
- [@article@Claude Skills Library](https://mcpservers.org/claude-skills)

## Skills

# Skills

In Claude Code, Skills are self-contained folders of "expert knowledge" and repeatable workflows that Claude loads dynamically into its context only when the task requires it. Each skill is anchored by a `SKILL.md` file containing YAML frontmatter, which helps Claude identify the skill's purpose without bloating the context window, and a body of specific instructions

Visit the following resources to learn more:

- [@course@Agent Skills with Anthropic](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- [@course@Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills)
- [@official@Extend Claude with skills](https://code.claude.com/docs/en/skills#extend-claude-with-skills)
- [@official@The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en)
- [@video@Claude Code Skills & skills.sh - Crash Course](https://www.youtube.com/watch?v=rcRS8-7OgBo)

## Skills

# Skills

Claude Code skills are modular packages of instructions, scripts, and assets that teach the AI assistant how to perform specific, repeatable workflows. Each skill is stored in a dedicated folder containing a mandatory [SKILL.md](http://SKILL.md) file, which uses YAML frontmatter to define its name and a description that the AI uses to automatically discover and load the skill when relevant.

Visit the following resources to learn more:

- [@course@Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills)
- [@course@Agent Skills with Anthropic](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- [@official@Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [@official@The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en)
- [@video@Claude Code Skills & skills.sh - Crash Course](https://www.youtube.com/watch?v=rcRS8-7OgBo)

## Slash Commands

# Slash Commands (/)

Slash commands are the steering wheel of Claude Code. They allow you to execute meta-actions, manage your session, and configure the environment without needing to write a natural language request. By typing a forward slash / at the start of your prompt, you gain access to a suite of utility tools that help you control costs, manage context, and extend functionality. These commands are processed locally and do not involve the AI's reasoning engine until necessary, making them instant and efficient

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode#built-in-commands)
- [@article@How to Use Claude Code: A Guide to Slash Commands, Agents, Skills, and Plug-ins](https://www.producttalk.org/how-to-use-claude-code-features/)
- [@article@Claude Code Tutorial #6 - Slash Commands](https://www.youtube.com/watch?v=52KBhQqqHuc)

## Sonnet

# Sonnet

Claude Sonnet is a high-performance large language model that strikes an ideal balance between advanced reasoning intelligence and rapid processing speed. It serves as the versatile "workhorse" of the Claude family, capable of handling complex programming tasks, such as multi-file refactoring and autonomous debugging, while operating significantly faster and more cost-effectively than the top-tier Opus model.

Visit the following resources to learn more:

- [@official@Introducing Claude Sonnet 4.5 \ Anthropic](https://www.anthropic.com/news/claude-sonnet-4-5)
- [@official@Claude Sonnet 4.5 \ Anthropic](https://www.anthropic.com/claude/sonnet)
- [@video@Sonnet 4.5 is the best coding model in the world](https://www.youtube.com/watch?v=uZBjVeyiYkk)

## Status

# /status & /statusline

The `/status` command is an interactive dashboard that provides a comprehensive overview of your current session's health and system configuration. Unlike the `/statusline` command, which places a permanent information bar at the bottom of your terminal, `/status` opens a temporary, tabbed interface that displays detailed metrics such as your Claude Code version, the specific AI model in use, active account details, and real-time usage limits. It is designed for one-off checks to verify connection stability or to monitor your daily and weekly token quotas before starting a large coding task.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)
- [@official@Customize your status line](https://code.claude.com/docs/en/statusline)
- [@video@Your Claude Code Terminal Should Look Like This](https://www.youtube.com/watch?v=fiZfVTsPy-w)
- [@video@Claude Code StatusLine Explained (Free Script Generator)](https://www.youtube.com/watch?v=PB9_Q2tfe90)

## Stop

# Stop

The `Stop` hook is a final-stage lifecycle event that triggers when Claude Code believes it has finished its entire response and is about to return control to the user. Unlike `PostToolUse`, which fires after every single file edit or command, the `Stop` hook only runs once at the very end of the interaction "turn."

Visit the following resources to learn more:

- [@official@Hooks reference](https://code.claude.com/docs/en/hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)

## Subagents

# Subagents

Subagents are specialized AI assistants that function as independent "team members" to handle focused tasks on behalf of the main agent. Each subagent operates within its own isolated context window, meaning it starts with a clean slate and does not clutter your primary conversation with large amounts of intermediate research or technical logs.

Visit the following resources to learn more:

- [@official@Create custom subagents](https://code.claude.com/docs/en/sub-agents)
- [@article@Claude Code Subagents: Complete Guide to Multi-Agent Architecture](https://wmedia.es/en/writing/claude-code-subagents-guide-ai)
- [@article@Building with Claude Code Subagents (My Beloved Minions) | by Yee Fei | Medium](https://medium.com/@ooi_yee_fei/building-with-claude-code-subagents-my-beloved-minions-b5a9a4318ba5)
- [@article@99% of Developers Haven’t Seen Claude Code Sub Agents (It Changes Everything)](https://medium.com/vibe-coding/99-of-developers-havent-seen-claude-code-sub-agents-it-changes-everything-c8b80ed79b97)
- [@video@Claude Code NEW Sub Agents in 7 Minutes](https://www.youtube.com/watch?v=DNGxMX7ym44&pp=ygUVY2xhdWRlIGNvZGUgc3ViYWdlbnRz)
- [@video@Claude Code Tutorial #8 - Subagents](https://www.youtube.com/watch?v=Phr7vBx9yFQ)

## Subagents

# Subagents

Subagents are specialized AI assistants that function as independent "team members" to handle focused tasks on behalf of the main agent. Each subagent operates within its own isolated context window, meaning it starts with a clean slate and does not clutter your primary conversation with large amounts of intermediate research or technical logs. They are typically defined by a markdown file in the `.claude/agents/` directory, where you specify their unique system prompt, expertise, and restricted tool access.

Visit the following resources to learn more:

- [@course@Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)
- [@official@Create custom subagents - Claude Code Docs](https://code.claude.com/docs/en/sub-agents)
- [@video@Stop Using Claude Code Like This (Use Sub-Agents Instead) -](https://www.youtube.com/watch?v=P60LqQg1RH8)
- [@video@Claude Code NEW Sub Agents in 7 Minutes](https://www.youtube.com/watch?v=DNGxMX7ym44)
- [@video@Claude Code Tutorial #8 - Subagents](https://www.youtube.com/watch?v=Phr7vBx9yFQ)

## Subscription

# Subscription Options

Subscription options for Claude Code allow users to authenticate and access its features. Individuals with a Claude Pro or Claude Max subscription can link their account for free Claude Code usage. For teams and larger organizations, Team and Enterprise plans offer higher usage limits, enhanced security features like SSO and audit logs, and deeper integration capabilities.

Visit the following resources to learn more:

- [@official@Log in to your account](https://code.claude.com/docs/en/quickstart#step-2-log-in-to-your-account)
- [@official@Subscription & Pricing](https://claude.com/pricing)
- [@official@Choosing a Claude plan](https://support.claude.com/en/articles/11049762-choosing-a-claude-plan)
- [@article@Claude Pricing Explained: Subscription Plans & API Costs](https://intuitionlabs.ai/articles/claude-pricing-plans-api-costs)

## Thinking Modes  Effort

# Thinking modes & Effort

Using thinking modes and adjusting effort levels in Claude Code is essential for balancing deep reasoning with operational efficiency. Furthermore, you can fine-tune Claude's cognitive energy using the effort parameter (available through the /model command).

Visit the following resources to learn more:

- [@official@Adjust effort level](https://code.claude.com/docs/en/model-config#adjust-ef)
- [@official@Adjust extended thinking](https://code.claude.com/docs/en/costs#adjust-extended-thinking)
- [@official@Effort](https://platform.claude.com/docs/en/build-with-claude/effort)
- [@official@Speed up responses with fast mode](https://code.claude.com/docs/en/fast-mode)

## Tools

# Tools

Tools are specialized functions that allow the AI assistant to perform actions on your computer rather than just generating text. These functions are categorized into client-side tools that interact with your local environment, such as `Bash` for running terminal commands, `Read` and `Edit` for file manipulation, and `Glob` or `Grep` for searching codebases, and server-side tools like `WebSearch` for fetching real-time information from the internet.

Visit the following resources to learn more:

- [@official@Tools](https://code.claude.com/docs/en/how-claude-code-works#tools)
- [@official@Tools available to Claude](https://code.claude.com/docs/en/settings#tools-available-to-claude)
- [@official@Introducing advanced tool use on the Claude Developer Platform \ Anthropic](https://www.anthropic.com/engineering/advanced-tool-use)
- [@article@Claude Code Built-in Tools Reference | vtrivedy](https://www.vtrivedy.com/posts/claudecode-tools-reference/)

## Tunnels

# MCP Tunnels

MCP Tunnels let you connect Claude to MCP servers running inside your private network without opening inbound firewall ports or exposing services to the public internet. Traffic flows over an outbound-only encrypted connection, meaning your internal tools and data sources stay fully private while still being accessible to Claude. This makes it practical to build agents that interact with internal databases, APIs, or services that you would never expose publicly.

Visit the following resources to learn more:

- [@official@MCP Tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)
- [@video@How to connect enterprise MCP servers to Claude via Anthropic MCP Tunnels](https://www.youtube.com/watch?v=DlCP7PKN-dU)

## Understand Claude Pricing

# Understand Claude Pricing

Claude Code offers a flexible, dual-path pricing model designed to accommodate both individual power users and high-scale enterprise teams. You can access the tool through a fixed-rate subscription (such as the Pro or Max plans), which provides a generous recurring allocation of messages shared across the web interface and the terminal, making costs predictable for daily development. Alternatively, you can use a pay-as-you-go API model, where you are billed based on the total number of "tokens" (small units of text) processed in each interaction.

Visit the following resources to learn more:

- [@official@Pricing](https://claude.com/pricing)
- [@official@Pricing in detail](https://platform.claude.com/docs/en/about-claude/pricing)
- [@article@Claude Pricing Explained: Subscription Plans & API Costs](https://intuitionlabs.ai/articles/claude-pricing-plans-api-costs)

## Usage Best Practices

# Usage Best Practices

Effective utilization of Claude Code involves adopting key strategies for optimal performance and long-term efficiency. This begins with a "Plan First, Implement Second" approach, especially for complex tasks, utilizing Plan Mode to allow Claude to create a plan before altering the source code. Maintaining a `CLAUDE.md` file as a project's central knowledge repository with relevant information, such as build commands and style guides, is crucial. Context management, through regular use of the /compact command and new conversations for separate tasks, helps mitigate performance degradation. Finally, automating routine processes, like generating Git commits with `claude commit` or setting up hooks, ensures efficiency and consistency throughout the development lifecycle.

Visit the following resources to learn more:

- [@official@Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices#best-practices-for-claude-code)
- [@article@Vibe Coding Best Practices: How To Get Consistent Results](https://roadmap.sh/vibe-coding/best-practices)
- [@article@What are your "best practices" for Claude Code? : r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1nris9w/what_are_your_best_practices_for_claude_code/)
- [@article@How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)
- [@video@Claude Code Workflows That Will 10x Your Productivity](https://www.youtube.com/watch?v=yZvDo_n12ns&t=145s)
- [@video@Claude Code - 47 PRO TIPS in 9 minutes](https://www.youtube.com/watch?v=TiNpzxoBPz0)

## Usage

# /usage

The `/usage` command is a specialized diagnostic tool designed specifically for users on Claude Pro or Claude Max subscription plans. Since these plans have unified limits, the command provides a real-time status report of your remaining capacity instead of monetary costs.

Visit the following resources to learn more:

- [@official@Built-in commands](https://code.claude.com/docs/en/interactive-mode)

## Use Compact And Clear

# Use /compact and /clear

Regularly using `/compact` and `/clear` is the most effective way to prevent "context rot" and manage spiraling API costs while working with Claude Code. Using `/compact` allows you to summarize long research or debugging threads into a lean set of key findings, effectively "zipping" the conversation so you can continue without losing essential progress. In contrast, `/clear` is vital when switching to an unrelated task; it wipes the current history to provide a clean slate.

## Use Compact Regularly

# Use /compact and /clear

Regularly using `/compact` and `/clear` is the most effective way to prevent "context rot" and manage spiraling API costs while working with Claude Code. Because Claude re-processes your entire conversation history with every new message, a session that has accumulated thousands of lines of terminal output and file diffs will eventually become expensive, slow, and prone to "forgetting" early instructions. Using `/compact` allows you to summarize long research or debugging threads into a lean set of key findings, effectively "zipping" the conversation so you can continue without losing essential progress. In contrast, `/clear` is vital when switching to an unrelated task; it wipes the current history to provide a clean slate.

## Use Subagents And Hooks

# Use subagents and hooks

Subagents and Hooks are powerful architectural tools that manage the context window by practicing "selective attention," ensuring the main conversation stays lean while specialized tasks remain high-precision. Subagents act as isolated "expert bubbles" that run in their own independent context windows with restricted toolsets, while Hooks provide a deterministic way to inject or prune context at key lifecycle moments.

Visit the following resources to learn more:

- [@official@Claude Code Subagents: Complete Guide to Multi-Agent Architecture](https://wmedia.es/en/writing/claude-code-subagents-guide-ai)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)
- [@article@Delegate verbose operations to subagents](https://code.claude.com/docs/en/costs#delegate-verbose-operations-to-subagents)

## Userpromptsubmit

# UserPromptSubmit

The `UserPromptSubmit` hook is an interception mechanism that fires the moment you press Enter on a prompt, but before the text is actually sent to the Claude model. It is the most powerful tool for prompt engineering automation, allowing you to programmatically rewrite, validate, or enhance your instructions on the fly.

Visit the following resources to learn more:

- [@official@Hooks reference](https://code.claude.com/docs/en/hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)
- [@article@Rewrite Prompts on the Fly with UserPromptSubmit Hooks](https://egghead.io/lessons/rewrite-prompts-on-the-fly-with-user-prompt-submit-hooks~76rrt)

## Using Claude Code

# Using Claude Code

Claude Code is a sophisticated agentic tool that provides significant power through its ability to execute commands and edit files, but it requires a disciplined approach to prevent security risks and runaway costs.

Visit the following resources to learn more:

- [@course@AI Capabilities and Limitations](https://anthropic.skilljar.com/ai-capabilities-and-limitations)
- [@official@Best Practices for Claude Code - Claude Code Docs](https://code.claude.com/docs/en/best-practices)
- [@official@Prompting best practices - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [@article@Vibe coding tutorial: Build your first app with Claude Code](https://roadmap.sh/vibe-coding/tutorial)
- [@article@How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)
- [@video@How I use Claude Code (Meta Staff Engineer Tips) - YouTube](https://www.youtube.com/watch?v=mZzhfPle9QU)
- [@video@My top 6 tips & ways of using Claude Code efficiently - YouTube](https://www.youtube.com/watch?v=WwdIYp5fuxY)

## Ways To Use Claude

# Ways to Use Claude Code

Claude Code offers multiple interfaces to cater to diverse development workflows. These include a Command Line Interface (CLI) for automation and scripting, editor code extensions (like VS Code, JetBrains IDEs) providing a graphical sidebar with inline code diffs, and a standalone Desktop Application for managing complex projects. Each interface leverages the same agentic engine for researching, writing, and executing code, providing options for different development styles. The CLI is accessible via shell scripts for macOS, Linux, and WSL, and through PowerShell for Windows.

Visit the following resources to learn more:

- [@course@Claude 101](https://anthropic.skilljar.com/claude-101)
- [@official@Use Claude Code everywhere](https://code.claude.com/docs/en/overview#use-claude-code-everywhere)

## What Is A Coding Agent

# Coding Agent

A coding agent is an AI-powered software entity designed to autonomously write, test, and debug code to solve specific programming tasks or complete software development projects. It uses various AI techniques, like large language models and reinforcement learning, to understand requirements, generate code snippets, identify errors, and iterate on its solutions to achieve the desired outcome.

Visit the following resources to learn more:

- [@article@Visit the Dedicated AI Agents Roadmap](https://roadmap.sh/ai-agents)
- [@article@What are AI agents?](https://www.ibm.com/think/topics/ai-agents)
- [@article@What are AI agents? Definition, examples, and types | Google Cloud](https://cloud.google.com/discover/what-are-ai-agents)
- [@video@AI Agents, Clearly Explained](https://www.youtube.com/watch?v=FwOTs4UxQS4)

## What Is Agentic Loop

# Agentic Loop

An agentic loop is a computational pattern where an agent continuously interacts with its environment through a cycle of perception, planning, and action. The agent observes its surroundings, decides on a course of action based on its goals and current state, executes that action, and then observes the results to inform its next decision. This iterative process allows the agent to learn, adapt, and pursue its objectives in a dynamic and potentially unpredictable environment.

Visit the following resources to learn more:

- [@official@Claude Code Agentic Loop](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop)
- [@article@What is an Agent Loop?](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure)
- [@article@Let's Build your Own Agentic Loop](https://www.reddit.com/r/AI_Agents/comments/1js1xjz/lets_build_our_own_agentic_loop_running_in_our/)
- [@video@What is Agentic RAG?](https://www.youtube.com/watch?v=0z9_MhcYvcY)

## What Is Vibe Coding

# Vibe Coding

Vibe coding is a modern software development approach in which developers use AI agents and large language models (LLMs) to generate, build, and iterate on applications via natural language prompts, rather than writing code manually. Coined by Andrej Karpathy, this method focuses on the "vibe" or overall intent of the application, often involving rapid prototyping and minimal manual code review, making software development more accessible and faster.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Vibe Coding Roadmap](https://roadmap.sh/vibe-coding)
- [@article@What is vibe coding?](https://www.ibm.com/think/topics/vibe-coding)
- [@video@What Is Vibe Coding? Building Software with Agentic AI](https://www.youtube.com/watch?v=Y68FF_nUSWE)
- [@video@What is Vibe Coding?](https://www.youtube.com/watch?v=5OWurmg41tI)
