# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.core import serializers

from post.models import Post, Comment
# Create your views here.

class PostView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(PostView, self).dispatch(request, *args, **kwargs)

	def get(self, request, post_pk):
		post = get_object_or_404(Post, id=post_pk)
		data = serializers.serialize("json", [post])
		return HttpResponse(data, content_type='application/json')

	def delete(self, request, post_pk):
		post = get_object_or_404(Post, id=post_pk)
		post.delete()
		data = serializers.serialize("json", [post])
		return HttpResponse(data, content_type="application/json")

class PostsView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(PostsView, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		posts = Post.objects.all()
		data = serializers.serialize("json", posts)
		return HttpResponse(data, content_type='application/json')

	def post(self, request):
		body = json.loads(request.body)

		post = Post(
			title=body["title"], 
			author=body["author"], 
			content=body["content"])
		post.save()

		data = serializers.serialize("json", [post])

		return HttpResponse(data, content_type="application/json")

class CommentView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(CommentView, self).dispatch(request, *args, **kwargs)

	def get(self, request, comment_pk):
		comment = get_object_or_404(Comment, id=comment_pk)
		data = serializers.serialize("json", [comment])
		return HttpResponse(data, content_type='application/json')

	def delete(self, request, comment_pk):
		comment = get_object_or_404(Comment, id=comment_pk)
		comment.delete()
		data = serializers.serialize("json", [comment])
		return HttpResponse(data, content_type="application/json")

class CommentsView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(CommentsView, self).dispatch(request, *args, **kwargs)

	def get(self, request, post_pk):
		post = get_object_or_404(Post, id=post_pk)
		comments = post.comments.all()
		data = serializers.serialize("json", comments)
		return HttpResponse(data, content_type='application/json')

	def post(self, request, post_pk):
		post = get_object_or_404(Post, id=post_pk)
		body = json.loads(request.body)
		comment = post.comments.create(
			author=body["author"], 
			content=body["content"])

		comment.save()
		
		data = serializers.serialize("json", [comment])
		return HttpResponse(data, content_type="application/json")
