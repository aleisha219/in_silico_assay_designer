from django.shortcuts import render
from .forms import AssayInputForm
from .ai_engine import interpret_goal
from .bio_engine import analyze_sequence

def input_view(request):
    form = AssayInputForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        target = form.cleaned_data['target']
        goal = form.cleaned_data['goal']
        suggestion = interpret_goal(goal)
        bio = analyze_sequence(target)
        context.update({'suggestion': suggestion, 'bio': bio})
        return render(request, 'core/result.html', context)
    return render(request, 'core/input_form.html', context)
