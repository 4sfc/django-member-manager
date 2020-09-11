"""PublishedListFilterTest class"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from member_manager.filters.published import PublishedListFilter
from member_manager.models.page import Page


class PublishedListFilterTest(TestCase):
    """Test PublishedListFilter"""

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='fbar', email='fb@example.com')
        Page.objects.bulk_create([
            Page(title='Title 1', slug='title-1', content='Content of page 1',
                 public=True, published=timezone.now(), created_by=user,
                 modified_by=user),
            Page(title='Title 2', slug='title-2', content='Content of page 2',
                 public=False, published=timezone.now(), created_by=user,
                 modified_by=user),
            Page(title='Title 3', slug='title-3', content='Content of page 3',
                 public=True, published=timezone.now(), created_by=user,
                 modified_by=user),
            Page(title='Title 4', slug='title-4', content='Content of page 4',
                 public=True, created_by=user, modified_by=user),
            Page(title='Title 5', slug='title-5', content='Content of page 5',
                 public=False, created_by=user, modified_by=user),
            Page(title='Title 6', slug='title-6', content='Content of page 6',
                 public=True, created_by=user, modified_by=user),
            ])

    def test_lookups(self):
        """Test lookups"""
        lookup_values = (
            ('published', _('Yes')),
            ('unpublished', _('No')),
        )
        page_lf = PublishedListFilter(None, {'published': None}, Page, None)
        self.assertEqual(page_lf.lookups(None, None), lookup_values)

    def test_queryset_with_none_value(self):
        """Test queryset with None value"""
        page_lf = PublishedListFilter(None, {'published': None}, Page, None)
        self.assertIsNone(page_lf.value())
        qs = page_lf.queryset('', Page.objects.all()).order_by('title')
        expected = ['<Page: Title 1>', '<Page: Title 2>', '<Page: Title 3>',
                    '<Page: Title 4>', '<Page: Title 5>', '<Page: Title 6>']
        self.assertQuerysetEqual(qs, expected)

    def test_queryset_with_published_value(self):
        """Test queryset with published value"""
        page_lf = PublishedListFilter(None, {'published': 'published'}, Page, None)
        self.assertEqual(page_lf.value(), 'published')
        qs = page_lf.queryset('', Page.objects.all()).order_by('title')
        expected = ['<Page: Title 1>', '<Page: Title 2>', '<Page: Title 3>']
        self.assertQuerysetEqual(qs, expected)

    def test_queryset_with_unpublished_value(self):
        """Test queryset with unpublished value"""
        page_lf = PublishedListFilter(None, {'published': 'unpublished'}, Page, None)
        self.assertEqual(page_lf.value(), 'unpublished')
        qs = page_lf.queryset('', Page.objects.all()).order_by('title')
        expected = ['<Page: Title 4>', '<Page: Title 5>', '<Page: Title 6>']
        self.assertQuerysetEqual(qs, expected)
