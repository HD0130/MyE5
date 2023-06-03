from Bio import SeqIO
from Bio.SeqUtils import GC

# 读取FASTQ文件
def read_fastq(file_path):
    sequences = []
    qualities = []
    for record in SeqIO.parse(file_path, 'fastq'):
        sequences.append(str(record.seq))
        qualities.append(record.letter_annotations['phred_quality'])
    return sequences, qualities

# 进行质量控制
def perform_quality_control(sequences, qualities, min_length, min_quality):
    filtered_sequences = []
    for seq, qual in zip(sequences, qualities):
        if len(seq) >= min_length and min(qual) >= min_quality:
            filtered_sequences.append(seq)
    return filtered_sequences

# 计算GC含量
def compute_gc_content(sequences):
    gc_contents = []
    for seq in sequences:
        gc_contents.append(GC(seq))
    return gc_contents

# 主函数
def main():
    # 读取FASTQ文件
    sequences, qualities = read_fastq('input.fastq')

    # 进行质量控制
    min_length = 100
    min_quality = 20
    filtered_sequences = perform_quality_control(sequences, qualities, min_length, min_quality)

    # 计算GC含量
    gc_contents = compute_gc_content(filtered_sequences)

    # 输出结果
    for seq, gc_content in zip(filtered_sequences, gc_contents):
        print('Sequence: {}'.format(seq))
        print('GC Content: {:.2f}%'.format(gc_content))

if __name__ == '__main__':
    main()
