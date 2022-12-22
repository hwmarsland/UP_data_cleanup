import pandas as pd
import sys

def data_clean_up(filename):
    raw_data = pd.read_excel(filename, index_col = 0)

    edited_data = raw_data.copy()
    edited_data = edited_data.replace('--', '—', regex=True)
    edited_data = edited_data.replace('@-', '–', regex=True)
    edited_data = edited_data.replace('###', '<i>', regex=True)
    edited_data = edited_data.replace('##', '<i>', regex=True)
    edited_data = edited_data.replace(' # ', '</i> ', regex=True)
    edited_data = edited_data.replace(' #,', '</i>,', regex=True)
    edited_data = edited_data.replace(' #.', '</i>.', regex=True)
    edited_data = edited_data.replace(' #—', '</i>—', regex=True)
    edited_data = edited_data.replace(' #', '-+-+-', regex=True)
    edited_data = edited_data.replace('#', '</i>', regex=True)
    edited_data = edited_data.replace('-+-+-', ' #', regex=True)
    edited_data = edited_data.replace('â€”', '--', regex=True)
    edited_data = edited_data.replace('â€“', '--', regex=True)
    edited_data = edited_data.replace('â€¦', ' . . . ', regex=True)
    edited_data = edited_data.replace('‘', '\'', regex=True)
    edited_data = edited_data.replace('’', '\'', regex=True)
    edited_data = edited_data.replace('“', '"', regex=True)
    edited_data = edited_data.replace('”', '"', regex=True)
    edited_data = edited_data.replace('<!—', '<!--', regex=True)
    edited_data = edited_data.replace('—>', '-->', regex=True)
    
    writer = pd.ExcelWriter(str(filename)+' edited-data.xlsx', engine='xlsxwriter')
    edited_data.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    
    print("Finished")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python data_clean_up_v1_5.py <filename>')
    
    else:
        data_clean_up(sys.argv[1])
