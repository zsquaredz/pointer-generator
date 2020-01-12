import os

def combine(dir, fileName):
    files = os.listdir(dir)
    files.sort()
    with open(fileName, 'w') as s:
        for file in files:
            summary = ''
            with open(dir+file, 'r') as f:
                line = f.readline()
                while line:
                    summary += line.strip()
                    summary += ' '
                    line = f.readline()
            s.write(summary.strip()+'\n')

if __name__ == '__main__':
    # combine output
    combine('/disk/ocean/zheng/pointer-generator/logs/pretrained_model_tf1.2.1/decode_test_400maxenc_4beam_35mindec_100maxdec_ckpt-238410/decoded/',
            'decoded.txt')

    # combine reference
    combine('/disk/ocean/zheng/pointer-generator/logs/pretrained_model_tf1.2.1/decode_test_400maxenc_4beam_35mindec_100maxdec_ckpt-238410/reference/',
            'reference.txt')