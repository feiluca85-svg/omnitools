#!/usr/bin/env python3
"""
TokenGuard — Sentinel di Monitoraggio Consumi Token per OmniTools Lab
Analizza in tempo reale i log della sessione, calcola l'efficienza della cache
e stima l'impatto economico sull'abbonamento Google.
"""

import json
import os
import sys
from datetime import datetime, timezone

TRANSCRIPT_PATH = "/Users/ilalu/.gemini/antigravity/brain/085fd0d2-940b-492d-b908-81cdf27ff01b/.system_generated/logs/transcript.jsonl"

# Stime di costo standard per modelli frontier (es. Gemini 1.5/2.0 Pro)
# Input: $1.25 / 1M token (senza cache) | Cached: $0.30 / 1M token | Output: $5.00 / 1M token
PRICE_INPUT_1M = 1.25
PRICE_CACHED_1M = 0.3125
PRICE_OUTPUT_1M = 5.00
EUR_USD_RATE = 0.93

def format_tokens(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)

def analyze_session():
    if not os.path.exists(TRANSCRIPT_PATH):
        print(f"File log non trovato: {TRANSCRIPT_PATH}")
        sys.exit(1)

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    total_steps = 0
    total_input = 0
    total_cached = 0
    total_output = 0

    today_steps = 0
    today_input = 0
    today_cached = 0
    today_output = 0

    last_step_tokens = None

    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                if row.get("source") == "MODEL" and row.get("type") == "PLANNER_RESPONSE":
                    total_steps += 1
                    inp = row.get("input_tokens", 0)
                    cache = row.get("cache_read_tokens", 0)
                    out = row.get("output_tokens", 0)
                    created = row.get("created_at", "")

                    total_input += inp
                    total_cached += cache
                    total_output += out

                    last_step_tokens = {"input": inp, "cached": cache, "output": out}

                    if created.startswith(today_str):
                        today_steps += 1
                        today_input += inp
                        today_cached += cache
                        today_output += out
            except Exception:
                continue

    # Calcolo percentuali di risparmio tramite caching
    all_context_tokens = total_input + total_cached
    cache_ratio = (total_cached / all_context_tokens * 100) if all_context_tokens > 0 else 0

    # Stima costo equivalente standard API
    cost_input = (total_input / 1_000_000) * PRICE_INPUT_1M
    cost_cache = (total_cached / 1_000_000) * PRICE_CACHED_1M
    cost_output = (total_output / 1_000_000) * PRICE_OUTPUT_1M
    total_cost_usd = cost_input + cost_cache + cost_output
    total_cost_eur = total_cost_usd * EUR_USD_RATE

    # Costo se non ci fosse stata la cache (senza caching pagheresti full input su tutto!)
    cost_without_cache_usd = ((all_context_tokens / 1_000_000) * PRICE_INPUT_1M) + cost_output
    savings_usd = cost_without_cache_usd - total_cost_usd
    savings_eur = savings_usd * EUR_USD_RATE

    # Stampa Dashboard Sentinel
    cyan = "\033[96m"
    green = "\033[92m"
    yellow = "\033[93m"
    bold = "\033[1m"
    dim = "\033[2m"
    reset = "\033[0m"

    print("\n" + f"{cyan}╔════════════════════════════════════════════════════════════════════╗{reset}")
    print(f"{cyan}║{reset}  {bold}🛡️  TOKEN GUARD — SENTINEL DI MONITORAGGIO CONSUMI{reset}              {cyan}║{reset}")
    print(f"{cyan}║{reset}  {dim}OmniTools Lab Sentinel • Monitoraggio Sessione & Efficienza Cache{reset}  {cyan}║{reset}")
    print(f"{cyan}╠════════════════════════════════════════════════════════════════════╣{reset}")
    
    print(f"{cyan}║{reset}  {bold}📊 RIEPILOGO TOTALE SESSIONE{reset}                                      {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Azioni / Step del Modello:  {bold}{total_steps:,}{reset} step                       {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Token Input Nuovi:          {bold}{format_tokens(total_input)}{reset} ({total_input:,})             {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Token Letti da Cache:       {green}{bold}{format_tokens(total_cached)}{reset} ({total_cached:,})           {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Token Output Generati:      {bold}{format_tokens(total_output)}{reset} ({total_output:,})             {cyan}║{reset}")
    
    print(f"{cyan}╠════════════════════════════════════════════════════════════════════╣{reset}")
    print(f"{cyan}║{reset}  {bold}⚡ EFFICIENZA PROMPT CACHE GOOGLE{reset}                                  {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Indice di Caching:          {green}{bold}{cache_ratio:.1f}% DEI TOKEN IN CACHE{reset}         {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Risparmio Reale da Cache:   {green}{bold}≈ {savings_eur:.2f} € risparmiati{reset}             {cyan}║{reset}")
    
    print(f"{cyan}╠════════════════════════════════════════════════════════════════════╣{reset}")
    print(f"{cyan}║{reset}  {bold}📅 CONSUMO ODIERNO (Oggi, UTC){reset}                                    {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Step Oggi:                  {bold}{today_steps:,}{reset} step                         {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Input Oggi:                 {bold}{format_tokens(today_input)}{reset} ({today_input:,})             {cyan}║{reset}")
    print(f"{cyan}║{reset}  • In Cache Oggi:              {green}{bold}{format_tokens(today_cached)}{reset} ({today_cached:,})            {cyan}║{reset}")
    print(f"{cyan}║{reset}  • Output Oggi:                {bold}{format_tokens(today_output)}{reset} ({today_output:,})               {cyan}║{reset}")

    if last_step_tokens:
        print(f"{cyan}╠════════════════════════════════════════════════════════════════════╣{reset}")
        print(f"{cyan}║{reset}  {bold}⏱️  ULTIMA AZIONE ESEGUITA{reset}                                         {cyan}║{reset}")
        print(f"{cyan}║{reset}  • Input: {last_step_tokens['input']} | Cache: {last_step_tokens['cached']} | Output: {last_step_tokens['output']}                  {cyan}║{reset}")

    print(f"{cyan}╠════════════════════════════════════════════════════════════════════╣{reset}")
    status_label = f"{green}● OTTIMALE (95%+ Cache Hit){reset}" if cache_ratio > 90 else f"{yellow}● ATTENZIONE (Cache bassa){reset}"
    print(f"{cyan}║{reset}  Stato Salute Sessione: {status_label}                       {cyan}║{reset}")
    print(f"{cyan}╚════════════════════════════════════════════════════════════════════╝{reset}\n")

if __name__ == "__main__":
    analyze_session()
