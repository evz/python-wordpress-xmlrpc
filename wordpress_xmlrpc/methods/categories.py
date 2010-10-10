from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressCategory, WordPressTag

class GetCategories(AuthenticatedMethod):
	method_name = 'wp.getCategories'
	results_class = WordPressCategory

class NewCategory(AuthenticatedMethod):
	method_name = 'wp.newCategory'
	method_args = ('category',)

class DeleteCategory(AuthenticatedMethod):
	method_name = 'wp.deleteCategory'
	method_args = ('category_id',)

class SuggestCategories(AuthenticatedMethod):
	method_name = 'wp.suggestCategories'
	method_args = ('category', 'max_results')

class GetPostCategories(AuthParamsOffsetMixin, AuthenticatedMethod):
	method_name = 'mt.getPostCategories'
	method_args = ('post_id',)
	results_class = WordPressCategory

class SetPostCategories(AuthParamsOffsetMixin, AuthenticatedMethod):
	method_name = 'mt.setPostCategories'
	method_args = ('post_id', 'categories',)

class GetTags(AuthenticatedMethod):
	method_name = 'wp.getTags'
	results_class = WordPressTag