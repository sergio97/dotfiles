# My stuff
export EDITOR=vim

function parse_git_dirty {
  output=$(git status --porcelain 2> /dev/null)
  echo "$output" | grep -q -e "^ *D" && echo -n "-"
  echo "$output" | grep -q -e "^ *M" -e "^ *R" && echo -n "*"
  echo "$output" | grep -q -e "^ *A" && echo -n "+"
}
function parse_git_stash {
  [[ $(git stash list 2> /dev/null | tail -n1) != "" ]] && echo "^"
}
function parse_git_branch {
  git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/ (\1$(parse_git_dirty)$(parse_git_stash))/"
}

export PS1='${debian_chroot:+($debian_chroot)}\u:\w$(parse_git_branch)\$ '

# Docker-related stuff
alias dstop="docker ps -q | xargs docker stop"
alias dps="docker ps -q | head -n1"
alias dx='docker exec -it $(dps) /bin/bash'

# git stuff
alias rmb='git remote prune origin && git branch | grep -v -e "master" -e "*"| xargs -L 1 git branch -d'
alias glog='git log --graph --color --decorate'
alias com='git checkout master'
alias gl='git pull --ff-only'

# Misc stuff
alias count_files_in_dirs='for x in $(ls); do echo ${x}: $(find "${x}" -type f | wc -l); done'
alias rm_nodemodules='find . -maxdepth 2 -name "node_modules" -type d -exec rm -rf "{}" \;'
alias valt='vagrant halt'
