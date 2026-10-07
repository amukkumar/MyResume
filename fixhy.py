import sys,re
try:
    import pikepdf
except ImportError:
    sys.exit("nopikepdf")
src,dst=sys.argv[1:3]
pdf=pikepdf.open(src); n=0
for obj in pdf.objects:
    if isinstance(obj,pikepdf.Stream) and obj.get('/Type') is None:
        try: d=obj.read_bytes()
        except Exception: continue
        if b'beginbfchar' in d or b'beginbfrange' in d:
            new=re.sub(rb'<2010>',b'<002D>',d)
            if new!=d: n+=d.count(b'<2010>'); obj.write(new)
pdf.save(dst); print('patched',n)
