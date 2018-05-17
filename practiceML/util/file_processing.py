import os


def derived_filename(filename, prefix='', extension='.txt'):
    """ 
    Derive a new filename based on the given one.
    
    >>> derived_filename('file.csv', prefix='my_', extension='.new')
    my_file.new
    """
    return prefix + os.path.splitext(filename)[0] + extension


def process_file(source_name, target_name, process_content):
    with open(source_name) as source:
        result = process_content(source)
    with open(target_name, 'w') as target:
        target.write(result)
        target.flush()


def process_all_files(source_dir, target_dir, prefix, extension, process_content):

    assert source_dir != ''
    assert target_dir != ''
    assert source_dir != target_dir
    
    problems = []
    
    for filename in os.listdir(source_dir):
        
        source_name = os.path.join(source_dir, filename)
        target_name = os.path.join(target_dir, derived_filename(filename, prefix, extension))
        
        try:
            process_file(source_name, target_name, process_content)
        except Exception as exception:
            problems.append((filename, exception))
            continue
    
    return problems