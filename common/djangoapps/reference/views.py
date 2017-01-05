#from django.shortcuts import render
from edxmako.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from reference.models import ReferenceInfo
from django.forms import ModelForm
from django.shortcuts import get_list_or_404, get_object_or_404
import requests
import json
from requests.exceptions import ConnectionError, MissingSchema

'''
class ReferencesList(ListView):
    """
    Should return reference list.
    """
    model = ReferenceInfo
    template_name = 'reference/referenceinfo_list.html'

class ReferenceCreate(CreateView):
    """
    Should create the reference.
    """
    model = ReferenceInfo
    template_name = 'reference/referenceinfo_form.html'
    success_url = reverse_lazy('reference_list')
    fields = ['ref_name', 'ref_type', 'ref_link', 'ref_status']


class ReferenceUpdate(UpdateView):
    """
    Should update the reference.
    """
    model = ReferenceInfo
    template_name = 'reference/referenceinfo_form.html'
    success_url = reverse_lazy('reference_list')
    fields = ['ref_name', 'ref_type', 'ref_link', 'ref_status']


class ReferenceDelete(DeleteView):
    """
    Should delete the reference.
    """
    model = ReferenceInfo
    template_name = 'reference/referenceinfo_confirm_delete.html'
    success_url = reverse_lazy('reference_list')
    fields = ['ref_name', 'ref_type', 'ref_link', 'ref_status']

'''


class ReferenceForm(ModelForm):
    class Meta:
        model = ReferenceInfo
        fields = ['ref_name', 'ref_type', 'ref_link', 'ref_status', 'ref_desc']


def reference_list(request, template_name='references/referenceinfo_list.html'):
    references = ReferenceInfo.objects.all()
    data = []

    for i, dt in enumerate(references):
        ref_dict = {}
        ref_dict['ref_name'] = dt.ref_name
        ref_dict['ref_type'] = dt.ref_type
        ref_dict['ref_link'] = dt.ref_link
        ref_dict['ref_status'] = dt.ref_status
        ref_dict['ref_desc'] = dt.ref_desc
        ref_dict['id'] = dt.id
        data.append(ref_dict)
    return render_to_response(template_name, {'data':data})

def reference_create(request, template_name='references/referenceinfo_form.html'):
    """
    Should create references.
    """
    form = ReferenceForm(request.POST or None)
    if request.method == "GET": 
        return render_to_response(template_name, {'form':form})
    try:
        if form.data.get('ref_link'):
            try:
                response = requests.get(form.data.get('ref_link'))
                if response.status_code == 200:
                    if form.is_valid():
                        form.save()
                        return HttpResponse(json.dumps({"success": 'true', 'msg':'Reference created successfully!!!'}))
                    else:
                        return HttpResponse(json.dumps({"success": 'failed'}))
                else:
                    return HttpResponse(json.dumps({"success": 'failed', 'msg':'Reference link is not valid!!!'}))
            except ConnectionError:
                return HttpResponse(json.dumps({"success": 'failed', 'msg': 'deadlink'}))
            except MissingSchema:
                return HttpResponse(json.dumps({"success": 'failed', 'msg': 'Invalid URL'}))
        else:
            return HttpResponse(json.dumps({"success": 'failed', 'msg':'Please input a valid link.'}))
    except:
        return HttpResponse(json.dumps({"success": 'failed', 'msg':'Internal Serever Error!!!'}))


def reference_update(request, pk, template_name='references/referenceupdate.html'):
    """
    Should update references.
    """
    reference = get_object_or_404(ReferenceInfo, pk=pk)
    form = ReferenceForm(request.POST or None, instance=reference)
    if request.method == "GET":
        return render_to_response(template_name, {'form':form, 'pk':pk})
    try:
        if form.data.get('ref_link'):
            try:
                response = requests.get(form.data.get('ref_link'))
                if response.status_code == 200:
                    if form.is_valid():
                        form.save()
                        return HttpResponse(json.dumps({"success": 'true', 'msg':'Reference updated successfully!!!'}))
                    else:
                        return HttpResponse(json.dumps({"success": 'failed'}))
                else:
                    return HttpResponse(json.dumps({"success": 'failed', 'msg':'Reference link is not valid!!!'}))
            except ConnectionError:
                return HttpResponse(json.dumps({"success": 'failed', 'msg': 'deadlink'}))
            except MissingSchema:
                return HttpResponse(json.dumps({"success": 'failed', 'msg': 'Invalid URL'}))
        else:
            return HttpResponse(json.dumps({"success": 'failed', 'msg':'Please input a valid link.'}))
    except:
         return HttpResponse(json.dumps({"success": 'failed', 'msg':'Internal Serever Error!!!'}))



def reference_delete(request, pk, template_name='references/referenceinfo_confirm_delete.html'):
    """
    Should remove references.
    """
    reference = get_object_or_404(ReferenceInfo, pk=pk)
    try:
        if request.method=='POST':
            reference.delete()
            return HttpResponseRedirect(reverse_lazy('reference_list'))
    except:
        print "Exception occured during delete!!!!"

    return render_to_response(template_name, {'object':reference, 'pk':pk})
