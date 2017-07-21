# MicroFrameworks vs Mongo

This is a very simple benchmark to compare speed response using Flask, Sanic and Express.

All output is saved in `benchmark_hello_world.txt` and `benchmark_data.txt`

All benchark was maded using this command

```
wrk -d 10 -c 100 -t 12 --timeout 8 http://localhost:8000
```

Replacing with appropiated port
