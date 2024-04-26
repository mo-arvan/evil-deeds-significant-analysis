

```bash
docker build -t evil-deeds -f artifacts/dockerfile .

docker run -it --rm  -v $(pwd):/workspace evil-deeds bash 
```


