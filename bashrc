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

