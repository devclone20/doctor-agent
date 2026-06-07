# Openclaw Roadmap

## Adding Daemon

# Adding Daemon

A daemon is a background process that runs continuously without needing a terminal window open. Configuring Open Claw as a daemon ensures it starts automatically and keeps running even after you log out or restart your machine.

Visit the following resources to learn more:

- [@article@Run OpenClaw 24/7: Complete Setup Guide for Local, AWS & Ubuntu (2026)](https://dextralabs.com/blog/how-to-run-openclaw/)

## Adding First Channel

# Adding First Channel

After setting up your model provider, the next step is connecting a communication channel, in other words, the platform where you will actually talk to your agent. Telegram is recommended as the fastest channel to get started with.

Visit the following resources to learn more:

- [@official@Channels](https://docs.openclaw.ai/channels)

## Agent Loop

# Agent Loop

When Open Claw receives a message, it runs a full agent loop rather than returning a single response. The loop validates the message, resolves the model, assembles the system prompt from skills and context files, and then sends everything to the model for inference. If the model decides to call a tool, like running a command, reading a file, or searching the web, the loop executes it, feeds the result back to the model, and continues until no more tool calls are needed and a final reply is ready. If the session gets too long for the context window, compaction kicks in automatically before retrying.

Visit the following resources to learn more:

- [@article@Agent Loop](https://docs.openclaw.ai/concepts/agent-loop)

## Agents

# Agents

An agent in Open Claw is a fully isolated unit with its own workspace folder containing its personality and configuration files, its own state directory that holds auth profiles and the model registry, and its own session store that keeps the full conversation history separate from every other agent. Because auth profiles are scoped per-agent, credentials for one agent are never automatically shared with another, which means you can run a personal agent on your WhatsApp number and a work agent on a separate account on the same Gateway without any risk of their sessions, memories, or API keys crossing over.

Visit the following resources to learn more:

- [@official@Agent Runtime](https://docs.openclaw.ai/concepts/agent)
- [@opensource@🦞 Awesome OpenClaw Agents](https://github.com/mergisi/awesome-openclaw-agents)

## Agentsmd

# AGENTS.md

[AGENTS.md](http://AGENTS.md) describes the agents available in your workspace, their roles, and how they relate to each other. It is used when running multiple agents to clarify who does what.

Visit the following resources to learn more:

- [@official@Default AGENTS.md](https://docs.openclaw.ai/reference/AGENTS.default#default-agents-md)
- [@official@AGENTS.md Template](https://docs.openclaw.ai/reference/templates/AGENTS)

## Allowlist

# /allowlist

`/allowlist` lists, adds, or removes entries from the sender allowlist that controls who can interact with the agent. Add and remove operations require `commands.config: true` to be set in your configuration.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)
- [@official@Allowlists (DM + groups) - terminology](https://docs.openclaw.ai/gateway/security#allowlists-dm-+-groups-terminology)

## Anthropic

# Anthropic

Anthropic is the company behind the Claude family of models. Connecting Open Claw to Anthropic lets you use Claude as your agent's underlying model, which is well-suited for reasoning, writing, and tool use.

Visit the following resources to learn more:

- [@official@Anthropic Provider](https://docs.openclaw.ai/providers/anthropic)
- [@official@Using anthropic Models](https://docs.openclaw.ai/providers/anthropic)
- [@video@Anthropic just blocked OpenClaw. Here’s what you need to do immediately](https://www.youtube.com/watch?v=cNALFf9R4t4)

## Antropic

# Anthropic

Anthropic is the company behind the Claude family of models. Connecting Open Claw to Anthropic lets you use Claude as your agent's underlying model, which is well-suited for reasoning, writing, and tool use.

Visit the following resources to learn more:

- [@official@Anthropic Provider](https://docs.openclaw.ai/providers/anthropic)
- [@official@Using anthropic Models](https://docs.openclaw.ai/providers/anthropic)
- [@video@Anthropic just blocked OpenClaw. Here’s what you need to do immediately](https://www.youtube.com/watch?v=cNALFf9R4t4)

## Auth  Model Providers

# Auth & Model Providers

This section covers how to connect Open Claw to AI model providers like Anthropic, OpenAI, Gemini, or Ollama by entering your API credentials. The model provider is what powers the agent's intelligence.

Visit the following resources to learn more:

- [@official@Provider Directory](https://docs.openclaw.ai/providers)
- [@official@Provider Quickstart](https://docs.openclaw.ai/providers/models)
- [@article@OpenClaw Model Selection & API Providers](https://www.meta-intelligence.tech/en/insight-openclaw-model-guide)

## Automating Tasks

# Automating Tasks

Open Claw supports several mechanisms for running tasks automatically, including hooks, webhooks, heartbeats, and cron jobs, so your agent can act without waiting for a human to send a message.

Visit the following resources to learn more:

- [@official@Automation Overview](https://docs.openclaw.ai/automation)
- [@video@OpenClaw (Clawdbot) use cases: 9 automations + 4 wild builds that actually work](https://www.youtube.com/watch?v=52kOmSQGt_E)

## Backup Create

# openclaw backup create

`openclaw backup create` generates a snapshot of your Open Claw configuration and memory files so you can restore your setup if something goes wrong.

Visit the following resources to learn more:

- [@official@backup](https://docs.openclaw.ai/cli/backup#backup)

## Bind The Gateway To Localhost Not 0000 And Secure Ports 18789 And 18793

# Bind the Gateway to Localhost

Binding to localhost means the gateway only accepts connections from the same machine, not from the open internet. You can then use a reverse proxy or Tailscale to selectively expose it.

Visit the following resources to learn more:

- [@official@Gateway Runbook](https://docs.openclaw.ai/gateway)
- [@official@Tailscale](https://docs.openclaw.ai/gateway/tailscale)

## Channels Add   Channel

# openclaw channels add --channel

`openclaw channels add --channel` adds a new communication channel to your Open Claw setup, specifying which platform to connect.

Visit the following resources to learn more:

- [@official@Add / remove accounts](https://docs.openclaw.ai/cli/channels#add-/-remove-accounts)

## Channels List

# openclaw channels list

`openclaw channels list` displays all the communication channels currently connected to your Open Claw gateway, along with their status.

Visit the following resources to learn more:

- [@official@Common Commands](https://docs.openclaw.ai/cli/channels#add-/-remove-accounts)

## Channels Login

# openclaw channels login

`openclaw channels login` initiates the authentication flow for a specific channel, allowing Open Claw to connect to it on your behalf.

Visit the following resources to learn more:

- [@official@Login / logout (interactive)](https://docs.openclaw.ai/cli/channels#add-/-remove-accounts)

## Channels Remove   Channel

# openclaw channels remove --channel

`openclaw channels remove --channel` disconnects and removes a channel from your Open Claw configuration.

Visit the following resources to learn more:

- [@official@Add / remove accounts](https://docs.openclaw.ai/cli/channels#add-/-remove-accounts)

## Channels Status   Probe

# openclaw channels status --probe

`openclaw channels status --probe` actively checks the connection status of your channels by probing them, rather than just reporting cached status.

Visit the following resources to learn more:

- [@official@Status / capabilities / resolve / logs](https://docs.openclaw.ai/cli/channels#status-/-capabilities-/-resolve-/-logs)

## Channels

# Channels

Channels are the messaging platforms through which users interact with Open Claw, and each one connects to the single Gateway process that routes incoming messages to the right agent and sends replies back. Every channel runs simultaneously on the same Gateway, so you can be connected to Telegram, WhatsApp, Discord, and Slack all at once without running separate processes. Text is supported across all channels, but richer features like reactions, media, message editing, and group behavior vary depending on what each platform's API supports

Visit the following resources to learn more:

- [@official@Chat Channels](https://docs.openclaw.ai/channels)

## Compact

# /compact

`/compact` is a text-only command that compresses or summarizes the current conversation context to free up space in the context window without losing essential information. You can optionally pass instructions to guide how the compaction is done.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)
- [@official@Compaction](https://docs.openclaw.ai/concepts/compaction)

## Config

# /config

`/config` reads and writes your on-disk `openclaw.json` configuration file directly from chat. It is disabled by default and requires `commands.config: true` in your config to enable. It supports `show`, `get`, `set`, and `unset` subcommands and is owner-only.

Visit the following resources to learn more:

- [@official@Config updates](https://docs.openclaw.ai/tools/slash-commands#config-updates)
- [@official@Gateway Configuration](https://docs.openclaw.ai/gateway/configuration)

## Context Window

# Context Window

The context window is the amount of conversation history, instructions, and tool results the AI model can see at once when generating a response. Open Claw manages this carefully through a context engine and compaction system so long-running agents don't exceed the model's limits.

Visit the following resources to learn more:

- [@official@Context](https://docs.openclaw.ai/concepts/context)
- [@official@Context Engine](https://docs.openclaw.ai/concepts/context-engine)
- [@article@OpenClaw Memory Masterclass: The complete guide to agent memory that survives • VelvetShark](https://velvetshark.com/openclaw-memory-masterclass)

## Context

# /context

`/context` explains what context the agent is currently working with. You can use `/context list` for a summary, `/context detail` for a breakdown of per-file, per-tool, per-skill, and system prompt sizes, or `/context json` for machine-readable output.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands#command-list)

## Creating Plugins

# Creating Plugins

You can build your own plugins to add custom functionality to Open Claw, such as integrating a new service or adding a new type of tool the agent can call.

Visit the following resources to learn more:

- [@official@Building Plugins](https://docs.openclaw.ai/plugins/building-plugins)

## Creating Skills

# Creating Skills

You can write your own skills by creating a `SKILL.md` file with instructions and placing it in your workspace's `skills/` folder. This lets you teach the agent new behaviors tailored to your specific needs.

Visit the following resources to learn more:

- [@official@Creating Skills](https://docs.openclaw.ai/tools/creating-skills)
- [@video@Create Unlimited OpenClaw Skills | Full Tutorial (Upstage Studio Skill)](https://www.youtube.com/watch?v=aYsPTu7VzEs)

## Cron Add

# openclaw cron add

`openclaw cron add` registers a new scheduled task, letting you define what the agent should do and when it should trigger automatically.

Visit the following resources to learn more:

- [@official@Scheduled Tasks](https://docs.openclaw.ai/automation/cron-jobs)
- [@official@Cron](https://docs.openclaw.ai/cli/index#cron)

## Cron Jobs

# Cron Jobs

Cron jobs are scheduled tasks that run at specific times or intervals. They allow you to automate recurring actions like summaries, cleanups, or reports without any human prompt.

Visit the following resources to learn more:

- [@official@Scheduled Tasks](https://docs.openclaw.ai/automation/cron-jobs)
- [@video@OpenClaw Cron Jobs vs Heartbeat Explained](https://www.youtube.com/watch?v=KtNZ1twkc7o)

## Cron List

# openclaw cron list

`openclaw cron list` shows all the scheduled tasks currently registered in Open Claw along with their schedules and status.

Visit the following resources to learn more:

- [@official@Scheduled Tasks](https://docs.openclaw.ai/automation/cron-jobs)
- [@official@Cron](https://docs.openclaw.ai/cli/index#cron)

## Dedicated Hardware

# Dedicated Hardware

Running Open Claw on dedicated hardware means using a physical device like a Raspberry Pi or Mac Mini that runs continuously in your home or office. This gives you full control and low ongoing costs with no monthly cloud fees.

Visit the following resources to learn more:

- [@article@How to Install OpenClaw: A Complete Setup Guide](https://roadmap.sh/openclaw/installation-guide)
- [@article@OpenClaw: The complete guide to building, training, and living with your personal AI agent](https://www.lennysnewsletter.com/p/openclaw-the-complete-guide-to-building?hide_intro_popup=true)

## Deploy On An Isolated Vps Vm Or Dedicated Device Not You Pc

# Deploy on an Isolated VPS, VM, or Dedicated Device

Running Open Claw on a dedicated, isolated machine rather than your personal computer limits the blast radius if something goes wrong and keeps your agent separate from your sensitive personal data.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)
- [@official@Remote Access](https://docs.openclaw.ai/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent)
- [@video@How to Secure OpenClaw - Complete Security Guide with Private Models](https://www.youtube.com/watch?v=jPslceOAbv0)

## Deploy On An Isolated Vps Vm Or Dedicated Device Not Your Pc

# Deploy on an Isolated VPS, VM, or Dedicated Device

Running Open Claw on a dedicated, isolated machine rather than your personal computer limits the blast radius if something goes wrong and keeps your agent separate from your sensitive personal data.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)
- [@official@Remote Access](https://docs.openclaw.ai/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent)
- [@article@OpenClaw Security: 12 Best Practices Our Experts Recommend](https://roadmap.sh/openclaw/security-best-practices)
- [@video@How to Secure OpenClaw - Complete Security Guide with Private Models](https://www.youtube.com/watch?v=jPslceOAbv0)

## Discord

# Discord

Discord is a chat platform popular in gaming and developer communities. Open Claw connects to it via the Discord Bot API and Gateway, supporting servers, channels, and DMs.

Visit the following resources to learn more:

- [@official@Discord Channel](https://docs.openclaw.ai/channels/discord)
- [@video@Set Up OpenClaw + Discord Fast (Step-by-Step)](https://www.youtube.com/watch?v=uy_wmsEwW6U)

## Docker

# Docker / Isolated Install

Docker lets you run Open Claw inside a container, an isolated environment that keeps it separate from the rest of your system. This makes installation cleaner, reduces conflicts with other software, and makes it easier to remove or update later.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Docker Roadmap](https://roadmap.sh/docker)
- [@official@Docker Install](https://docs.openclaw.ai/install/docker)
- [@article@Use OpenClaw to Make a Personal AI Assistant](https://towardsdatascience.com/use-openclaw-to-make-a-personal-ai-assistant/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- [@video@How To Install and Setup OpenClaw With Docker | OpenClaw AI Docker Setup | Clawdbot, Moltbot](https://www.youtube.com/watch?v=Ql4nm0FW_MA)

## Doctor   Deep

# openclaw doctor --deep

`openclaw doctor --deep` is an extended version of `openclaw doctor` that performs a more thorough diagnostic check, scanning system services for extra gateway installs and deeper configuration issues that the standard check might miss. You can add the `--yes` flag to automatically accept any prompts without manual input, which is useful for running the command in a headless or

Visit the following resources to learn more:

- [@official@Doctor](https://docs.openclaw.ai/gateway/doctor)
- [@official@doctor](https://docs.openclaw.ai/cli/doctor)

## Doctor

# openclaw doctor

The `openclaw doctor` command checks your Open Claw installation for common configuration problems and misconfigurations. It is the first thing to run when something is not working as expected.

Visit the following resources to learn more:

- [@official@Doctor](https://docs.openclaw.ai/gateway/doctor)
- [@official@doctor](https://docs.openclaw.ai/cli/doctor)

## Enable Device Pairing And Maintain A Minimal Sender Allowlist

# Enable Device Pairing and Maintain a Minimal Sender Allowlist

Device pairing ensures only verified devices can talk to your agent. Keeping the allowlist minimal means only the people or systems you explicitly trust can send it messages.

Visit the following resources to learn more:

- [@official@Pairing](https://docs.openclaw.ai/channels/pairing#pairing)
- [@official@Allowlists (DM + groups) - terminology](https://docs.openclaw.ai/gateway/security/index#allowlists-dm-+-groups-terminology)

## Event Types

# Event Types

Open Claw hooks support a range of event types, including command events like `/new` and `/reset`, session events like compaction, agent bootstrap events, gateway startup events, and message received and sent events.

Visit the following resources to learn more:

- [@official@Event Types](https://docs.openclaw.ai/automation/hooks#event-types)

## Fast

# /fast

`/fast` is a directive that toggles fast mode for the current session. It takes `on`, `off`, or `status` as arguments. Fast mode maps to different provider-level behaviors depending on your model — for example, `service_tier=priority` on OpenAI or `service_tier=auto` on Anthropic. Omitting the argument shows the current effective fast-mode state.

Visit the following resources to learn more:

- [@official@Fast mode (/fast)](https://docs.openclaw.ai/tools/thinking#fast-mode-/fast)
- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)

## Gateway Settings

# Gateway Settings

Gateway settings control how the Open Claw server behaves, including the port it listens on, authentication tokens, and which interfaces it binds to. These settings are critical for both functionality and security.

Visit the following resources to learn more:

- [@official@Gateway Configuration](https://docs.openclaw.ai/gateway/configuration)

## Gateway Start  Stop  Restart

# openclaw gateway start | stop | restart

`openclaw gateway start`, `openclaw gateway stop`, and `openclaw gateway restart` control the lifecycle of the Open Claw gateway process, starting it up, shutting it down, or restarting it after a configuration change.

Visit the following resources to learn more:

- [@official@Gateway Runbook](https://docs.openclaw.ai/gateway)
- [@official@Manage the Gateway service](https://docs.openclaw.ai/cli/gateway#manage-the-gateway-service)

## Gateway

# openclaw gateway

`openclaw gateway` is the main command for interacting with the gateway process. It is the entry point for all gateway-related operations from the command line.

Visit the following resources to learn more:

- [@official@Gateway Runbook](https://docs.openclaw.ai/gateway)
- [@official@gateway](https://docs.openclaw.ai/cli/gateway#gateway)

## Gateway

# Gateway

The Gateway is the single always-on process that handles routing, the control plane, and all channel connections. It runs on a single multiplexed port that serves the WebSocket control and RPC interface, HTTP APIs, the Control UI, and hooks. By default, it binds to localhost and requires an auth token before accepting any connections.

Visit the following resources to learn more:

- [@official@Gateway Runbook](https://docs.openclaw.ai/gateway)
- [@article@OpenClaw Gateway: Setup, Start/Stop Commands & Remote Mode](https://www.meta-intelligence.tech/en/insight-openclaw-gateway)

## Gemini

# Gemini

Gemini is Google's family of AI models. Open Claw supports Gemini as an alternative model provider, giving you access to Google's AI infrastructure for powering your agents.

Visit the following resources to learn more:

- [@official@Google (Gemini) Provider](https://docs.openclaw.ai/providers/google)
- [@video@Gemini 3.1 Pro + OpenClaw Tested!](https://www.youtube.com/watch?v=es16_Icm_PM)

## Heartbeatmd

# HEARTBEAT.md

[HEARTBEAT.md](http://HEARTBEAT.md) is a workspace configuration file where you define what the agent should do during each heartbeat cycle — essentially a set of instructions for proactive, time-based behavior.

Visit the following resources to learn more:

- [@official@HEARTBEAT.md](https://docs.openclaw.ai/gateway/heartbeat#heartbeat-md-optional)
- [@official@HEARTBEAT.md Template](https://docs.openclaw.ai/reference/templates/HEARTBEAT)

## Heartbeats

# Heartbeats

Heartbeats are periodic signals the Gateway emits on a regular interval. They can be used to confirm the agent is alive and to trigger recurring background tasks without any human input.

Visit the following resources to learn more:

- [@official@Scheduled Tasks (Cron) vs Heartbeat](https://docs.openclaw.ai/automation#scheduled-tasks-cron-vs-heartbeat)
- [@official@Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- [@video@OpenClaw Cron Jobs vs Heartbeat Explained](https://www.youtube.com/watch?v=KtNZ1twkc7o)

## Help

# /help

`/help` displays a list of available slash commands and a brief description of what each one does. It also works as an inline shortcut, meaning it can be embedded in a normal message and will be stripped before the model sees the rest of the text.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)

## Hook Structure

# Hook Structure

Each hook is a directory containing a `HOOK.md` file with metadata and a `handler.ts` file with the logic to run. The metadata defines which events to listen for and what requirements the hook needs to be eligible.

Visit the following resources to learn more:

- [@official@Hook Structure](https://docs.openclaw.ai/automation/hooks#hook-structure)

## Hooks

# Hooks

Hooks are small scripts that run inside the Gateway when specific agent events fire, like `/new`, `/reset`, `/stop`, or lifecycle events. They are automatically discovered from directories and can be inspected with `openclaw hooks`.

Visit the following resources to learn more:

- [@official@Hooks](https://docs.openclaw.ai/automation/hooks)

## How Open Clawworks

# How OpenClaw Works

Open Claw runs a single long-lived Gateway that owns all messaging surfaces and exposes a typed WebSocket API for control-plane clients like the macOS app, CLI, and web UI. When a message arrives, the Gateway routes it to the appropriate agent, which then runs through a full loop of context assembly, model inference, and tool execution before streaming a reply back.

Visit the following resources to learn more:

- [@official@OpenClaw Overview](https://docs.openclaw.ai/)
- [@official@Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [@article@OpenClaw Architecture, Explained: How It Works](https://ppaolo.substack.com/p/openclaw-system-architecture-overview)
- [@video@How OpenClaw Works: The Architecture Behind the 'Magic'](https://www.youtube.com/watch?v=CAbrRTu5xcw&t=75s)

## How Openclaw Works

# How OpenClaw Works

Open Claw runs a single long-lived Gateway that owns all messaging surfaces and exposes a typed WebSocket API for control-plane clients like the macOS app, CLI, and web UI. When a message arrives, the Gateway routes it to the appropriate agent, which then runs through a full loop of context assembly, model inference, and tool execution before streaming a reply back.

Visit the following resources to learn more:

- [@official@OpenClaw Overview](https://docs.openclaw.ai/)
- [@official@Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [@article@OpenClaw Architecture, Explained: How It Works](https://ppaolo.substack.com/p/openclaw-system-architecture-overview)
- [@video@How OpenClaw Works: The Architecture Behind the 'Magic'](https://www.youtube.com/watch?v=CAbrRTu5xcw&t=75s)

## Imessage

# iMessage

iMessage is Apple's built-in messaging system. The recommended way to connect it to Open Claw is via BlueBubbles, a macOS server that provides a full-featured REST API for iMessage integration.

Visit the following resources to learn more:

- [@official@BlueBubbles Channel](https://docs.openclaw.ai/channels/bluebubbles)
- [@article@OpenClaw SMS and iMessage setup guide (Twilio, BlueBubbles, imsg)](https://lumadock.com/tutorials/openclaw-sms-imessage-setup-guide)

## Installation

# Installation

Installation covers the steps to get Open Claw onto your chosen environment. It requires a recent version of Node.js, an API key from your chosen model provider, and takes around five minutes. The core install command is `npm install -g openclaw@latest`, after which you run openclaw onboard to connect your first model and channel. Always check the official documentation for the current Node.js version requirements before installing, as these may change between releases.

Visit the following resources to learn more:

- [@official@Getting Started](https://docs.openclaw.ai/start/getting-started)

## Installing From Clawhub

# Installing from ClawHub

ClawHub is a community repository of pre-built skills. You can browse and install skills from ClawHub directly, saving time compared to building them from scratch.

Visit the following resources to learn more:

- [@official@ClawHub](https://clawhub.ai/)
- [@official@What is ClawHub?](https://docs.openclaw.ai/tools/clawhub)

## Installing Plugins

# Installing Plugins

Plugins are installed via `openclaw plugins install` followed by the package name or path. Once installed, they become available to all agents in your workspace.

Visit the following resources to learn more:

- [@official@Install and Configure](https://docs.openclaw.ai/tools/plugin)

## Interval  Active Hours

# Interval & Active Hours

You can configure how often heartbeats fire and restrict them to certain hours of the day, so your agent only runs automated tasks during times you define as active.

Visit the following resources to learn more:

- [@official@Heartbeat](https://docs.openclaw.ai/gateway/heartbeat#heartbeat-gateway)

## Introduction

# Introduction

Open Claw is a self-hosted AI agent gateway that connects your messaging apps to AI models you control. You run a single Gateway process on your own machine or server, and it becomes the bridge between platforms like Telegram, WhatsApp, Discord, Slack, Signal, and more, and an always-available AI assistant. It is MIT-licensed, open source, and designed for developers and power users who want a personal AI they can message from anywhere without giving up control of their data.

Visit the following resources to learn more:

- [@official@Open Claw Docs](https://docs.openclaw.ai/)
- [@article@What Is OpenClaw? The Open-Source AI Agent That Actually Does Things](https://www.mindstudio.ai/blog/what-is-openclaw-ai-agent)
- [@video@The wild rise of OpenClaw...](https://www.youtube.com/watch?v=ssYt09bCgUY)

## Local Machine

# Local Machine

Running Open Claw on your local machine means installing it directly on your personal computer. This is the quickest way to get started and is good for experimentation, though it comes with limitations around uptime and accessibility from outside your network.

Visit the following resources to learn more:

- [@official@Getting Started](https://docs.openclaw.ai/start/getting-started)
- [@article@How to Install OpenClaw: A Complete Setup Guide](https://roadmap.sh/openclaw/installation-guide)
- [@video@OpenClaw Full Tutorial for Beginners – How to Set Up and Use OpenClaw (ClawdBot / MoltBot)](https://www.youtube.com/watch?v=n1sfrc-RjyM)

## Mac Mini

# Mac Mini

A Mac Mini is a compact desktop computer that works well as a home server for Open Claw. It is more powerful than a Raspberry Pi and runs macOS, which may simplify setup for Mac users.

Visit the following resources to learn more:

- [@video@How to set up OpenClaw on Mac mini (full tutorial)](https://www.youtube.com/watch?v=dKRJQeGIj_E)
- [@video@OpenClaw Installation Guide: The Setup That Actually Works!](https://www.youtube.com/watch?v=9xnWCeLhRow)

## Managing  Disabling Jobs

# Managing & Disabling Jobs

You can list, pause, and delete cron jobs from the command line, giving you control over which scheduled tasks are active at any given time.

Visit the following resources to learn more:

- [@official@Managing jobs](https://docs.openclaw.ai/automation/cron-jobs#managing-jobs)

## Mcp

# /mcp

`/mcp` manages OpenClaw-managed MCP server definitions from chat. It is disabled by default and requires `commands.mcp: true` to enable. It supports `show`, `get`, `set`, and `unset` subcommands and is owner-only

Visit the following resources to learn more:

- [@official@MCP Updates](https://docs.openclaw.ai/tools/slash-commands#mcp-updates)
- [@official@mcp](https://docs.openclaw.ai/cli/mcp#mcp)

## Mcp

# MCP

MCP (Model Context Protocol) is an open standard for connecting AI models to external tools and data sources. Open Claw supports MCP, allowing your agent to call tools from any MCP-compatible server.

Visit the following resources to learn more:

- [@official@mcp](https://docs.openclaw.ai/cli/mcp#mcp)
- [@article@How to Set Up OpenClaw MCP Server](https://fast.io/resources/openclaw-mcp-setup/)

## Memory Index   All

# openclaw memory index

`openclaw memory index` rebuilds the search index for all memory files, ensuring the agent can efficiently retrieve relevant information from its stored memories.

Visit the following resources to learn more:

- [@official@Memory overview](https://docs.openclaw.ai/concepts/memory#memory-overview)
- [@official@memory](https://docs.openclaw.ai/cli/index#memory)

## Memory Search Query

# openclaw memory search "query"

`openclaw memory search "query"` lets you search through the agent's stored memories using a keyword or phrase, useful for checking what the agent has remembered about past conversations or preferences.

Visit the following resources to learn more:

- [@official@Memory](https://docs.openclaw.ai/cli/index#memory)

## Memory System

# Memory System

The memory system allows Open Claw agents to remember information across conversations. Instead of starting fresh every time, agents can store and retrieve facts, past interactions, or user preferences from structured memory files in the workspace. Open Claw also includes a compaction system that automatically summarizes older conversation history when a session grows too long, preserving the essential information while freeing up space for new exchanges.

Visit the following resources to learn more:

- [@official@Memory](https://docs.openclaw.ai/concepts/memory)
- [@official@Compaction](https://docs.openclaw.ai/concepts/compaction)

## Memorymd

# MEMORY.md

[MEMORY.md](http://MEMORY.md) is a persistent file where the agent stores important facts it has learned over time. It is regularly updated so the agent can recall relevant information in future conversations.

Visit the following resources to learn more:

- [@official@Memory Overview](https://docs.openclaw.ai/concepts/memory#memory-overview)
- [@official@MEMORY.md - Your Long-Term Memory](https://docs.openclaw.ai/reference/templates/AGENTS#-memory-md-your-long-term-memory)

## Memoryyyyy Mm Ddmd

# memory/YYYY-MM-DD.md

These are dated memory log files that store a record of what happened on a specific day. They give the agent a chronological history that it can reference when needed, and are created automatically by the session-memory hook.

Visit the following resources to learn more:

- [@official@Memory Overview](https://docs.openclaw.ai/concepts/memory)

## Model

# /model

`/model` is a directive that lets you switch the AI model the agent is currently using. You can pass a number from the model picker, a full `provider/model` string, or use `/model list` to see available options.

Visit the following resources to learn more:

- [@official@Model selection (/model)](https://docs.openclaw.ai/tools/slash-commands#model-selection-/model)

## Models Auth Add

# openclaw models auth add

`openclaw models auth add` is the interactive auth helper. It can launch a provider auth flow (OAuth/API key) or guide you into manual token paste, depending on the provider you choose.

Visit the following resources to learn more:

- [@official@Model Providers](https://docs.openclaw.ai/concepts/model-providers#model-providers)
- [@official@Auth Providers](https://docs.openclaw.ai/cli/models#auth-profiles)

## Models Auth Setup Token

# openclaw models auth setup-token

`openclaw models auth setup-token` stores the authentication token for a model provider, allowing Open Claw to make authenticated API calls on your behalf. It is part of the broader `models auth` command group, which also includes `add`, `login`, and `paste-token`.

Visit the following resources to learn more:

- [@official@Model Providers](https://docs.openclaw.ai/concepts/model-providers#model-providers)
- [@official@Auth Providers](https://docs.openclaw.ai/cli/models#auth-profiles)

## Models List  Set  Status

# openclaw models list | set | status

`openclaw models list`, `openclaw models set`, and `openclaw models status` let you view the AI models available in your setup, switch between them, and check which one is currently active.

Visit the following resources to learn more:

- [@official@model list](https://docs.openclaw.ai/concepts/models#models-list)
- [@official@models status](https://docs.openclaw.ai/concepts/models#models-status)
- [@official@Common commands](https://docs.openclaw.ai/concepts/models?search=openclaw+models+set)

## Multi Agents

# Multi-Agents

Multi-agent mode lets you run several specialized agents in the same Open Claw gateway, each with its own workspace, auth profiles, and session store. They can operate independently or be coordinated through routing rules and shared memory.

Visit the following resources to learn more:

- [@official@Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent)
- [@official@Sub-Agents](https://docs.openclaw.ai/tools/subagents)

## Never Hardcode Api Keys  Use Environment Variables

# Never Hardcode API Keys

API keys stored directly in code or config files can be accidentally exposed through logs, version control, or error messages. Always use environment variables or a secrets manager instead.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)

## Never Trust External Content Emails Web Pages To Prevent Prompt Injection

# Never Trust External Content to Prevent Prompt Injection

Prompt injection is an attack where malicious text in an email, webpage, or file tricks the agent into taking unintended actions. Treating all external content as untrusted input is a core security principle in Open Claw.

Visit the following resources to learn more:

- [@official@Threat Model](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS)

## New

# /new

`/new` starts a fresh conversation with the agent, clearing the current context so you are beginning from a clean slate. It also triggers the session-memory hook to save the previous session before resetting. You can optionally pass a model name after `/new` to start the session with a specific model.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)

## Ollama

# Ollama

Ollama is a tool that lets you run open-source AI models locally on your own hardware, making it a natural fit for Open Claw setups where privacy, cost, or offline availability are a priority. It shines most in dedicated hardware setups like a Mac Mini or a capable home server, where you have enough RAM and processing power to run a model comfortably. However, low-powered devices like a Raspberry Pi will likely struggle with most models.

Visit the following resources to learn more:

- [@official@Ollama Provider](https://docs.openclaw.ai/providers/ollama)

## Onboard

# openclaw onboard

`openclaw onboard` walks you through the initial setup process interactively, helping you connect your model provider and first channel step by step.

Visit the following resources to learn more:

- [@official@Onboarding: CLI](https://docs.openclaw.ai/start/wizard)
- [@official@onboard](https://docs.openclaw.ai/cli/onboard)

## Onboarding

# Onboarding

Onboarding is the guided first-run process that walks you through connecting your first AI model provider and communication channel so your agent is ready to receive and respond to messages. You can run it with `openclaw onboard`.

Visit the following resources to learn more:

- [@official@Onboarding Overview](https://docs.openclaw.ai/start/onboarding-overview)
- [@official@Onboarding CLI](https://docs.openclaw.ai/start/wizard)

## Openai

# OpenAI

OpenAI provides access to models like GPT-4o. Open Claw can use these models as the AI brain behind your agent by configuring your OpenAI API key in the model provider settings.

Visit the following resources to learn more:

- [@official@OpenAI Provider](https://docs.openclaw.ai/providers/openai)
- [@official@Using OpenAI Models](https://docs.openclaw.ai/providers/openai)

## Openclaw Vs Claude Code

# OpenClaw vs Claude Code

Claude Code is Anthropic's official CLI tool for AI-assisted coding, tightly integrated with Claude models and designed for developer workflows. OpenClaw is a community-built alternative that runs independently, supports a wide range of AI providers beyond Anthropic, and extends beyond coding to general agent automation across messaging platforms.

Visit the following resources to learn more:

- [@official@Open Claw vs Claude Code](https://docs.openclaw.ai/help/faq#what-are-the-advantages-vs-claude-code-for-web-development)
- [@article@OpenClaw vs Claude explained simply in 8 minutes](https://www.mindstudio.ai/blog/what-is-openclaw-ai-agent)
- [@video@OpenClaw vs Claude explained simply in 8 minutes](https://www.youtube.com/watch?v=b773XfpS7fw)

## Other Workspace Files

# Other Workspace Files

Open Claw recognizes several other special markdown files that are automatically injected into the agent's context at startup. [BOOT.md](http://BOOT.md) contains instructions that the agent runs once when the Gateway starts. [TOOLS.md](http://TOOLS.md) describes the tools available to the agent and how they should be used. [IDENTITY.md](http://IDENTITY.md) is an alternative or complement to [SOUL.md](http://SOUL.md) for defining the agent's persona. [BOOTSTRAP.md](http://BOOTSTRAP.md) is a general-purpose file for injecting additional context into every session. On top of these recognized filenames, you can also add any other markdown files to your workspace, such as project notes, reference documents, or custom instructions for specific tasks.

Visit the following resources to learn more:

- [@official@Agent Workspace](https://docs.openclaw.ai/concepts/agent-workspace)
- [@article@AI Agents 003 — OpenClaw Workspace Files Explained: SOUL.md, AGENTS.md, HEARTBEAT.md and More](https://capodieci.medium.com/ai-agents-003-openclaw-workspace-files-explained-soul-md-agents-md-heartbeat-md-and-more-5bdfbee4827a)

## Pick A Provider

# VPS & Cloud Providers

Open Claw runs on any VPS or cloud server that supports Node.js, so you are not locked into a specific provider. The official docs include setup guides for several popular options, including DigitalOcean, Render, Hetzner, [Fly.io](http://Fly.io), Google Cloud Platform, Azure, and exe.dev, each with different trade-offs around pricing, location, and ease of setup

Visit the following resources to learn more:

- [@official@Hosting and Deployment](https://docs.openclaw.ai/install#hosting-and-deployment)
- [@article@Best VPS hosts for OpenClaw ?](https://www.reddit.com/r/VPS/comments/1reuehc/best_vps_hosts_for_openclaw/#:~:text=Comments%20Section,a%20script%20for%20the%20setup)
- [@video@Run OpenClaw for $0/Month — 5 Free VPS That Actually Work in 2026](https://www.youtube.com/watch?v=EfmIl0_Naj8)

## Plugins

# /plugins

`/plugins` lets you inspect discovered plugins and toggle their enablement from chat. It is disabled by default and requires `commands.plugins: true` to enable. It supports `list`, `show`, `install`, `enable`, and `disable` subcommands. Write operations are owner-only. Alias: `/plugin`.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)
- [@official@Install and Configure](https://docs.openclaw.ai/tools/plugin)

## Plugins

# Plugins

Plugins are packages that can register any combination of capabilities: channels, model providers, tools, skills, speech, image generation, and more. Some are bundled with Open Claw, and others are published by the community on npm.

Visit the following resources to learn more:

- [@official@Tools and Plugins](https://docs.openclaw.ai/tools)
- [@official@Plugins](https://docs.openclaw.ai/tools/plugin)
- [@video@Create OpenClaw AI Plugin for Extra Features and Skills | Step-by-Step Guide for Beginners](https://www.youtube.com/watch?v=baHEUzqatK4)

## Proactive Core

# Proactive Core

The proactive core is what allows Open Claw agents to act on their own initiative rather than just responding to messages. Using heartbeats, cron jobs, and standing orders, the agent can run tasks on a schedule or trigger automatically based on conditions you define.

Visit the following resources to learn more:

- [@official@Automation & Tasks](https://docs.openclaw.ai/automation)
- [@article@How OpenClaw Works: Understanding AI Agents Through a Real Architecture](https://bibek-poudel.medium.com/how-openclaw-works-understanding-ai-agents-through-a-real-architecture-5d59cc7a4764)

## Rasberry Pi

# Raspberry Pi

A Raspberry Pi is a small, low-cost single-board computer that can run Open Claw 24/7 with minimal power consumption. It is a popular self-hosting choice for hobbyists who want a home server.

Visit the following resources to learn more:

- [@official@Raspberry Pi Hosting](https://docs.openclaw.ai/install/raspberry-pi#raspberry-pi)
- [@video@OpenClaw on Raspberry Pi 5: Full Setup Guide + AI Agent Demo (Step-by-Step)](https://www.youtube.com/watch?v=NqY0wF4YKXo)
- [@video@OpenClaw on Raspberry Pi](https://www.youtube.com/watch?v=fMtQy9msLz0)

## Raspberry Pi

# Raspberry Pi

A Raspberry Pi is a small, low-cost single-board computer that can run Open Claw 24/7 with minimal power consumption. It is a popular self-hosting choice for hobbyists who want a home server.

Visit the following resources to learn more:

- [@official@Raspberry Pi Hosting](https://docs.openclaw.ai/install/raspberry-pi#raspberry-pi)
- [@video@OpenClaw on Raspberry Pi 5: Full Setup Guide + AI Agent Demo (Step-by-Step)](https://www.youtube.com/watch?v=NqY0wF4YKXo)
- [@video@OpenClaw on Raspberry Pi](https://www.youtube.com/watch?v=fMtQy9msLz0)

## Reasoning

# /reasoning

`/reasoning` is a directive that enables or disables extended reasoning mode. It takes `on`, `off`, or `stream` as arguments. When set to `on`, the agent sends a separate message prefixed with `Reasoning:` before its final reply. `stream` enables Telegram draft streaming only. Alias: `/reason`.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)
- [@official@Reasoning visibility (/reasoning)](https://docs.openclaw.ai/tools/thinking#reasoning-visibility-%2Freasoning)

## Reset

# /reset

`/reset` resets the agent's current state, clearing any ongoing task or context and returning it to its idle state. Like `/new`, it triggers the session-memory hook before resetting.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)

## Rotate All Credentials Immediately If A Breach Is Suspected

# Rotate All Credentials Immediately if a Breach is Suspected

If you think your setup has been compromised, changing all API keys, tokens, and passwords immediately limits how long an attacker can maintain access.

## Routing Rules

# Routing Rules

Routing rules determine which agent handles which incoming messages. Open Claw uses a deterministic, most-specific-wins system: peer matches beat channel-wide rules, which beat the fallback default agent.

Visit the following resources to learn more:

- [@official@Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent)
- [@official@Channel Routing](https://docs.openclaw.ai/channels/channel-routing)

## Run Openclaw As A Non Root User

# Run OpenClaw as a Non-Root User

Running as a non-root user means that even if the agent is compromised, an attacker cannot gain full system access. It is a basic but important layer of defense for any production setup.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)

## Run Openclaw Security Audit   Deep After Every Config Change

# Run openclaw security audit --deep After Every Config Change

Every configuration change is an opportunity to accidentally introduce a vulnerability. Running a deep security audit after changes catches problems before they become incidents.

Visit the following resources to learn more:

- [@official@Quick check: openclaw security audit](https://docs.openclaw.ai/gateway/security/index#quick-check-openclaw-security-audit)
- [@official@Formal Verification (Security Models)](https://docs.openclaw.ai/security/formal-verification)

## Securing Webhooks

# Securing Webhooks

The Webhooks plugin ensures that each route is protected by shared-secret authentication, rate limiting, request size guards, and in-flight request limiting. Use a strong unique secret per route, store it as a SecretRef rather than inline plaintext, and bind each route to the narrowest session that fits the workflow. If a secret cannot be resolved at startup, the plugin skips that route and logs a warning instead of exposing a broken endpoint.

Visit the following resources to learn more:

- [@official@Webhooks Plugin](https://docs.openclaw.ai/plugins/webhooks)

## Security Audit

# openclaw security audit

`openclaw security audit` scans your Open Claw setup for potential security vulnerabilities such as exposed ports, weak tokens, or insecure configurations. You can also run `openclaw security audit --deep` for a live Gateway probe, or openclaw `security audit --fix` to automatically tighten safe defaults.

Visit the following resources to learn more:

- [@official@Quick check: openclaw security audit](https://docs.openclaw.ai/gateway/security#quick-check-openclaw-security-audit)
- [@official@security](https://docs.openclaw.ai/cli/security)
- [@article@OpenClaw Security: 12 Best Practices Our Experts Recommend](https://roadmap.sh/openclaw/security-best-practices)

## Security Best Practices

# Security Best Practices

When running Open Claw locally, bind the Gateway to localhost only so it is never exposed directly to the internet, set a strong, randomly generated auth token, and never hardcode API keys in config files — use environment variables instead. Run the process as a non-root user, keep your sender allowlist minimal, and enable device pairing so unknown devices cannot connect. Be cautious about prompt injection since the agent can read external content like emails and web pages. Run `openclaw security audit --deep` after any configuration change, keep Open Claw updated regularly, and rotate all credentials immediately if you suspect a breach.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)
- [@official@Threat Model](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS)
- [@article@OpenClaw Security: 12 Best Practices Our Experts Recommend](https://roadmap.sh/openclaw/security-best-practices)
- [@video@DO NOT use a VPS for OpenClaw (major warning)](https://www.youtube.com/watch?v=ev4iiGXlnh0)

## Security Best Practices

# Security Best Practices

Use a local machine setup only for single-user personal use. Bind the Gateway to localhost so it is never exposed to the internet, set a strong randomly generated auth token, and store all API keys in environment variables rather than config files. Run Open Claw as a non-root user, keep your sender allowlist to just yourself, and enable device pairing so unknown devices cannot connect. Run `openclaw security audit --deep` after any configuration change and keep Open Claw updated regularly.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)
- [@official@Gateway Runbook](https://docs.openclaw.ai/gateway)
- [@article@OpenClaw Security: 12 Best Practices Our Experts Recommend](https://roadmap.sh/openclaw/security-best-practices)

## Security Risks

# Security Risks (Skills)

Installing third-party skills carries risk since a skill can define instructions or tool access that could be misused. It is important to review skills from external sources before installing them.

Visit the following resources to learn more:

- [@official@Security and moderation](https://docs.openclaw.ai/tools/clawhub#security-and-moderation)
- [@article@OpenClaw Security: 12 Best Practices Our Experts Recommend](https://roadmap.sh/openclaw/security-best-practices)

## Security Risks

# Security Risks (Plugins)

Plugins run at a deeper level than skills and can have significant access to your system. Open Claw installs plugin dependencies with `--ignore-scripts` to reduce risk, but you should still only install plugins from trusted sources.

Visit the following resources to learn more:

- [@official@Install and Configure](https://docs.openclaw.ai/tools/plugin)
- [@official@Threat Model](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS)
- [@article@OpenClaw Security: 12 Best Practices Our Experts Recommend](https://roadmap.sh/openclaw/security-best-practices)

## Sessions

# Sessions

A session is the conversation context tied to a specific agent and chat source. Direct messages share one session by default, but you can isolate each sender into their own context, strongly recommended if more than one person can message your agent. All session state is owned by the Gateway and maintained automatically through pruning and entry caps to keep the store bounded over time.

Visit the following resources to learn more:

- [@official@Session Management](https://docs.openclaw.ai/concepts/session)
- [@official@Session Pruning](https://docs.openclaw.ai/concepts/session-pruning)
- [@article@OpenClaw Session Management Explained](https://www.dench.com/blog/openclaw-session-management)

## Set A Strong Gateway Auth Token Before Exposing Any Service

# Set a Strong Gateway Auth Token

The auth token is the password that protects your gateway from unauthorized access. It should be long, random, and unique and never shared or committed to version control.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)

## Setting Up Openclaw

# Setting up Open Claw

Setting up Open Claw involves installing the package via npm, running the onboarding wizard to connect your AI model provider and first communication channel, and optionally installing the Gateway as a background daemon so it starts automatically.

Visit the following resources to learn more:

- [@official@Getting Started](https://docs.openclaw.ai/start/getting-started)
- [@official@Onboarding Overview](https://docs.openclaw.ai/start/onboarding-overview)
- [@article@How to Install OpenClaw: A Complete Setup Guide](https://roadmap.sh/openclaw/installation-guide)
- [@video@OpenClaw Full Tutorial for Beginners – How to Set Up and Use OpenClaw (ClawdBot / MoltBot)](https://www.youtube.com/watch?v=n1sfrc-RjyM)

## Signal

# Signal

Signal is an end-to-end encrypted messaging app. Open Claw connects to it via signal-cli, making it a strong option for users who prioritize privacy in their communications with the agent.

Visit the following resources to learn more:

- [@official@Signal Channel](https://docs.openclaw.ai/channels/signal)
- [@video@OpenClaw Signal Setup - How To Connect Signal With OpenClaw (Signal integration)](https://www.youtube.com/watch?v=fbdT7akVm2I)

## Skills

# Skills

Skills are modular capability packages that extend what your agent can do. Each skill is a markdown file injected into the system prompt that gives the agent context and guidance for using specific tools or following specific workflows.

Visit the following resources to learn more:

- [@official@Skills](https://docs.openclaw.ai/tools/skills)
- [@official@Skills Config](https://docs.openclaw.ai/tools/skills-config)
- [@article@What are OpenClaw Skills? A 2026 Developer’s Guide](https://www.digitalocean.com/resources/articles/what-are-openclaw-skills)
- [@video@Everything You Need to Know About OpenClaw Skills (Beginner to Pro)](https://www.youtube.com/watch?v=kvTYp6uB_zQ)

## Skills

# Skills

OpenClaw uses AgentSkills-compatible skill folders to teach the agent how to use tools. A skill is a markdown file injected into the system prompt that gives the agent context, constraints, and step-by-step guidance for using tools effectively. Skills live in your workspace, in shared folders, or ship inside plugins.

Visit the following resources to learn more:

- [@official@Skills](https://docs.openclaw.ai/tools/skills)
- [@official@Agent Skills](https://agentskills.io/home)
- [@article@What are OpenClaw Skills? A 2026 Developer’s Guide | DigitalOcean](https://www.digitalocean.com/resources/articles/what-are-openclaw-skills)

## Slack

# Slack

Slack is a team communication platform. Open Claw connects to it via the Bolt SDK as a workspace app, making it useful for team-based automation and internal tooling.

Visit the following resources to learn more:

- [@official@Slack Channel](https://docs.openclaw.ai/channels/slack)
- [@video@Connect OpenClaw to Slack in 5 Minutes](https://www.youtube.com/watch?v=gOUbJA9YFiE)

## Soulmd

# SOUL.md

[SOUL.md](http://SOUL.md) is the file where you define the agent's personality, tone, and core behavioral guidelines. Think of it as the agent's character sheet. It shapes how it communicates and makes decisions across all conversations.

Visit the following resources to learn more:

- [@official@SOUL.md Personality Guide](https://docs.openclaw.ai/concepts/soul#soul-md-personality-guide)
- [@official@SOUL.md Template](https://docs.openclaw.ai/reference/templates/SOUL#soul-md-template)

## Start In Read Only Mode And Widen Permissions Deliberately

# Start in Read-Only Mode and Widen Permissions Deliberately

Starting with minimal permissions and only expanding them as needed is a safer approach than granting broad access upfront. Open Claw supports tool allow and deny lists per agent to help enforce this.

Visit the following resources to learn more:

- [@official@Security](https://docs.openclaw.ai/gateway/security)
- [@official@Sandboxing](https://docs.openclaw.ai/gateway/sandboxing)

## Status

# /status

`/status` asks the agent to report its current state, including active tasks, connected channels, and any pending operations. It also shows provider usage and quota for the current model provider when usage tracking is enabled.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)

## Stop

# /stop

`/stop` interrupts the agent if it is currently in the middle of a task or loop, bringing it to a halt immediately. It targets the active chat session directly so it can abort the current run.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)

## Telegram

# Telegram

Telegram is a messaging app that supports bots via a straightforward API. It is one of the easiest channels to connect to Open Claw and is recommended as the first channel for new users.

Visit the following resources to learn more:

- [@official@Telegram Channel](https://docs.openclaw.ai/channels/telegram)
- [@article@How to Set Up OpenClaw with Telegram (So Your AI Can Text You Back)](https://blog.mohitnagaraj.in/blog/202602/openclaw-telegram-setup)
- [@video@How to Connect OpenClaw to Telegram (Step-by-Step)](https://www.youtube.com/watch?v=U4wxi3tt7JU)

## Think

# /think

`/think` is a directive that sets the agent's thinking level before responding. It takes `off`, `minimal`, `low`, `medium`, `high`, or `xhigh` as arguments. Higher levels make the agent reason more deeply before giving a final answer, which is useful for complex or ambiguous tasks. Aliases: `/thinking`, `/t`.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)
- [@official@Thinking Levels](https://docs.openclaw.ai/tools/thinking)

## Update Openclaw Regularly Many Security Fixes Ship In Patch Releases

# Update OpenClaw Regularly

Open Claw releases often include security patches. Staying up to date ensures you are not running with known vulnerabilities that have already been fixed upstream.

## Usage Best Practices

# Usage Best Practices

To get the most out of Open Claw, run `openclaw doctor` regularly to catch configuration drift early, and always run openclaw `security audit --deep` after any config change. Keep your workspace files like [SOUL.md](http://SOUL.md), [USER.md](http://USER.md), and [MEMORY.md](http://MEMORY.md) up to date so the agent always has accurate context about who you are and how you want it to behave. Use `/new` at the start of a new topic rather than letting a single session grow indefinitely, which keeps the context window clean and triggers the session-memory hook to save what was discussed. Start with a minimal tool allowlist and only expand permissions when you have a specific need, and prefer Tailscale over open ports for any remote access to keep your Gateway secure without extra complexity.

Visit the following resources to learn more:

- [@official@CLI Reference](https://docs.openclaw.ai/cli)
- [@article@Vibe Coding Best Practices: How To Get Consistent Results](https://roadmap.sh/vibe-coding/best-practices)
- [@article@OpenClaw Cheatsheet](https://moltfounders.com/openclaw-mega-cheatsheet)

## Usage

# /usage

`/usage` controls the per-response usage footer appended to normal replies. It takes `off`, `tokens`, `full`, or `cost` as arguments. `/usage cost` prints a local cost summary from your Open Claw session logs rather than appending it to each reply.

Visit the following resources to learn more:

- [@official@Slash Commands](https://docs.openclaw.ai/tools/slash-commands)

## Use Cases

# Use Cases

Open Claw can be used for a wide range of tasks: you can connect it to your messaging apps to have it read and respond to messages on your behalf, set up scheduled jobs using cron and heartbeats to run recurring tasks like daily summaries or file cleanups without any human input, process incoming data from webhooks by extracting and acting on information automatically, manage and update files and documentation in your workspace, chain multiple actions together in a single agent loop to complete multi-step workflows from start to finish, and even run several specialized agents in parallel with routing rules and shared memory so each one handles a different domain while staying coordinated with the others.

Visit the following resources to learn more:

- [@official@Showcase - OpenClaw](https://docs.openclaw.ai/start/showcase)
- [@opensource@awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/README.md)
- [@video@OpenClaw Use Cases that are actually helpful...](https://www.youtube.com/watch?v=Q7r--i9lLck)

## Usermd

# USER.md

[USER.md](http://USER.md) contains information about you: your preferences, context, and anything you want the agent to know about you by default. The agent reads this to personalize its responses.

Visit the following resources to learn more:

- [@official@USER Template](https://docs.openclaw.ai/reference/templates/USER#user-md-about-your-human)

## Vpscloud

# VPS/Cloud

Running Open Claw on a VPS or cloud platform gives you a machine that is always online and accessible from anywhere. This is the most common production setup and is recommended over running on a local machine for anything beyond experimentation.

Visit the following resources to learn more:

- [@official@Remote Access](https://docs.openclaw.ai/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent)
- [@article@How to Install OpenClaw: A Complete Setup Guide](https://roadmap.sh/openclaw/installation-guide)
- [@article@Self-Host OpenClaw on a Free VPS — Step by Step](https://cognio.so/clawdbot/self-hosting)
- [@video@OpenClaw Tutorial for Beginners - Full Setup Guide](https://www.youtube.com/watch?v=WDHgibiZ9S8)

## Webhooks

# Webhooks

Webhooks allow external services to send HTTP requests to Open Claw to trigger agent actions. This is how you can connect third-party tools like GitHub or custom apps to your agent.

Visit the following resources to learn more:

- [@official@Webhooks](https://docs.openclaw.ai/automation/cron-jobs#webhooks)
- [@article@OpenClaw webhooks explained: A complete guide](https://lumadock.com/tutorials/openclaw-webhooks-explained)

## Whatsapp

# WhatsApp

WhatsApp is the most popular channel in Open Claw. It connects via the Baileys library and requires a QR code pairing step to link your account to the Gateway.

Visit the following resources to learn more:

- [@official@WhatsApp Channel](https://docs.openclaw.ai/channels/whatsapp)
- [@video@Connect OpenClaw to WhatsApp in 5 Minutes](https://www.youtube.com/watch?v=cQ6diPGtwAY)

## Why And Why Not

# Why and Why not?

A local machine is the right choice if you are just getting started, experimenting with Open Claw, or running it as a personal assistant for yourself only. It requires no ongoing costs, no remote infrastructure to manage, and lets you get up and running in minutes. It is not a good fit if you need your agent to be available 24/7, reachable from outside your home network, or capable of receiving webhooks from external services, since your agent goes offline whenever your machine is off or asleep and most home networks block incoming traffic by default.

Visit the following resources to learn more:

- [@official@Getting Started](https://docs.openclaw.ai/start/getting-started)
- [@video@The only OpenClaw tutorial you’ll ever need (March 2026 edition)](https://www.youtube.com/watch?v=CxErCGVo-oo)

## Why And Why Not

# Limitations

Running Open Claw on dedicated hardware like a Raspberry Pi or Mac Mini gives you full control and no ongoing cloud fees, but the hardware itself is a constraint. Low-powered devices like a Raspberry Pi may struggle with memory-intensive tasks or multiple simultaneous agent sessions, and any hardware failure means your agent goes offline until you physically fix or replace the device. You are also still dependent on your home internet connection for external access, which may be unreliable, have changing IP addresses, or block incoming traffic by default.

Visit the following resources to learn more:

- [@official@Remote Access](https://docs.openclaw.ai/gateway/remote)
- [@video@OpenClaw Tutorial for Beginners: How to Use & Set up OpenClaw (ClawdBot)](https://www.youtube.com/watch?v=CxErCGVo-oo)

## Why And Why Not

# When to Use a VPS or Cloud Server

A VPS or cloud server is the right choice if you need your agent to be always online, reachable from anywhere, and capable of receiving webhooks from external services. It is the most common production setup and works well for personal assistants, team automation, and any workflow that requires continuous availability. It is not a good fit if you want to avoid recurring costs, prefer to keep everything on hardware you physically own, or want to run local models via Ollama without paying for a powerful enough remote machine.

Visit the following resources to learn more:

- [@official@Remote Access](https://docs.openclaw.ai/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent)
- [@video@DO NOT use a VPS for OpenClaw (major warning)](https://www.youtube.com/watch?v=ev4iiGXlnh0)

## Workspace Settings

# Workspace Settings

Workspace settings define the environment your agent operates in, including its identity, behavioral guidelines, and what it knows about you. These are stored in a set of markdown configuration files in your project directory.

Visit the following resources to learn more:

- [@official@Agent Workspace](https://docs.openclaw.ai/concepts/agent-workspace)
- [@article@How to Build and Secure a Personal AI Agent with OpenClaw](https://www.freecodecamp.org/news/how-to-build-and-secure-a-personal-ai-agent-with-openclaw/#heading-step-2-write-the-agents-operating-manual)
- [@article@AI Agents 003 — OpenClaw Workspace Files Explained: SOUL.md, AGENTS.md, HEARTBEAT.md and More](https://capodieci.medium.com/ai-agents-003-openclaw-workspace-files-explained-soul-md-agents-md-heartbeat-md-and-more-5bdfbee4827a)
- [@video@OpenClaw Workspace Files Tutorial (AI Agent's Brain)](https://www.youtube.com/watch?v=XhtjVvlOO3U)
