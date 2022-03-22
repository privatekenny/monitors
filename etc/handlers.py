import gzip
import os

# https://stackoverflow.com/a/8468041
class GZipRotator:
    def __call__(self, source, dest):
        os.rename(source, dest)
        with open(dest, 'rb') as f_in:
            f_out = gzip.open("%s.gz" % dest, 'wb')
            f_out.writelines(f_in)
            f_out.close()
            f_in.close()
        os.remove(dest)


