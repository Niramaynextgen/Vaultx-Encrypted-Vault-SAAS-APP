from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VaultItem, VaultFile

@login_required
def dashboard(request):
    vault_items = VaultItem.objects.filter(user=request.user)
    # Decrypt for display
    items = []
    for item in vault_items:
        items.append({
            'id':       item.id,
            'title':    item.title,
            'username': item.get_username(),
            'password': item.get_password(),
            'notes':    item.get_notes(),
            'created_at': item.created_at,
            'files':    item.files.all(),
        })
    return render(request, "vault/dashboard.html", {"items": items})

@login_required
def add_item(request):
    if request.method == "POST":
        item = VaultItem(user=request.user, title=request.POST.get("title"))
        item.set_username(request.POST.get("username", ""))
        item.set_password(request.POST.get("password", ""))
        item.set_notes(request.POST.get("content", ""))
        item.save()

        # Handle multiple file uploads
        for f in request.FILES.getlist("attachments"):
            ext = f.name.rsplit('.', 1)[-1].lower()
            VaultFile.objects.create(
                vault_item=item,
                file=f,
                filename=f.name,
                file_type=ext
            )
        return redirect("dashboard")
    return render(request, "vault/add_item.html")

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(VaultItem, id=item_id, user=request.user)
    if request.method == "POST":
        item.title = request.POST.get("title")
        item.set_username(request.POST.get("username", ""))
        item.set_password(request.POST.get("password", ""))
        item.set_notes(request.POST.get("content", ""))
        item.save()

        for f in request.FILES.getlist("attachments"):
            ext = f.name.rsplit('.', 1)[-1].lower()
            VaultFile.objects.create(
                vault_item=item,
                file=f,
                filename=f.name,
                file_type=ext
            )
        return redirect("dashboard")

    # Pass decrypted values to pre-fill the form
    context = {
        'item': item,
        'username': item.get_username(),
        'password': item.get_password(),
        'notes':    item.get_notes(),
        'files':    item.files.all(),
    }
    return render(request, "vault/edit_item.html", context)

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(VaultItem, id=item_id, user=request.user)
    if request.method == "POST":
        item.delete()
    return redirect("dashboard")

@login_required
def delete_file(request, file_id):
    vfile = get_object_or_404(VaultFile, id=file_id, vault_item__user=request.user)
    if request.method == "POST":
        vfile.file.delete()  # delete from disk
        vfile.delete()
    return redirect("dashboard")