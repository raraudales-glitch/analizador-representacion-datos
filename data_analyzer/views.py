from django.shortcuts import render
from .forms import NumberAnalyzerForm, TextAnalyzerForm

def index_view(request):
    num_form = NumberAnalyzerForm(request.POST or None, prefix='num')
    text_form = TextAnalyzerForm(request.POST or None, prefix='text')
    
    num_result = None
    text_results = None

    if 'num_submit' in request.POST and num_form.is_valid():
        dec = num_form.cleaned_data['decimal_val']
        
        bin_raw = bin(dec)[2:]
        bit_length = len(bin_raw)
        byte_limit = ((bit_length + 7) // 8) * 8
        if byte_limit == 0:
            byte_limit = 8
        bin_padded = bin_raw.zfill(byte_limit)
        bytes_needed = byte_limit // 8

        num_result = {
            'decimal': dec,
            'binario': bin_padded,
            'octal': oct(dec)[2:],
            'hexadecimal': hex(dec)[2:].upper(),
            'bits_significativos': bit_length,
            'bytes_necesarios': bytes_needed
        }

    if 'text_submit' in request.POST and text_form.is_valid():
        text = text_form.cleaned_data['text_input']
        text_results = []
        for char in text:
            code_point = ord(char)
            utf8_bytes = char.encode('utf-8')
            text_results.append({
                'char': char,
                'decimal': code_point,
                'unicode_point': f"U+{code_point:04X}",
                'hexadecimal': hex(code_point)[2:].upper(),
                'utf8_bytes': ' '.join([f"0x{b:02X}" for b in utf8_bytes])
            })

    context = {
        'num_form': num_form,
        'text_form': text_form,
        'num_result': num_result,
        'text_results': text_results,
    }
    return render(request, 'data_analyzer/index.html', context)