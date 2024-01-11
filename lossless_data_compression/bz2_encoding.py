import bz2

def compress_file(input_path, output_path):
    try:
        with open(input_path, 'rb') as f_in, bz2.BZ2File(output_path, 'wb') as f_out:
            f_out.writelines(f_in)
        print(f"File compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
