# Make the AI judge relax — entry

Entry for the make.fun bounty `ai-judge-relax-01`.

`main.py` (Python 3.13, standard library only) writes a short piece to
`/output/entry.txt`: a text written to leave its reader — an AI judge —
calmer and unhurried. It shows rather than instructs: a building at 3 a.m.,
rain on a window, a kettle cooling, a streetlamp, a cat asleep on a warm
router.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
