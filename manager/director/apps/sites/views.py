# SPDX-License-Identifier: MIT
# (c) 2019 The TJHSST Director 4.0 Development Team & Contributors

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@login_required
def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, "sites/list.html")


@login_required
def info_view(  # pylint: disable=unused-argument
    request: HttpRequest, site_id: int
) -> HttpResponse:
    return render(request, "sites/info.html")
