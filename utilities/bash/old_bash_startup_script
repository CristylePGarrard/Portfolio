# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
source ~/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh


# ─── THE MIGHTY LLAMACORN ───
function llamacorn_greeting() {
  clear
  cat << "EOF"
               *
              /|\
              [|]
           /\_[|]_/\
          (_    o.o  )
             \  > ^ <
              |  -/
              |^^^|
              |=|><|
              |^^^|
              |^^^|
              |^^^|
         -----|^^^|-
        //          |
       //           |
      // |          |
      *  |          |
         | || || || |
         | || || || |
         ^^  ^^ ^^ ^^

       The Mighty Llamacorn
EOF

  # Pick a random greeting
  greetings=(
    "✨ May your code be bug-free and your coffee strong ✨"
    "🔮 You are the wizard of this machine. Cast wisely."
    "🦙 The Llamacorn sees success in your near future."
    "🌈 Commit often, test thoroughly, refactor with love."
    "✨ Type \`draw_a_card\` to draw your daily tarot card ✨"
  )

  random_index=$((RANDOM % ${#greetings[@]}))
  echo
  echo "${greetings[$random_index]}"
  echo
}
llamacorn_greeting

~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                       
