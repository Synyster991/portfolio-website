from django.test import TestCase
from tutor import models


def sample_course():
    return models.Course.objects.create(
        title='Python Course',
        language='Python',
        body='Lorem ipsun Lorem ipsun Lorem ipsun Lorem ipsun.',
        author='John Smith'
    )


def sample_video(fk_course=None):
    if not fk_course:
        temp_course = sample_course()
    else:
        temp_course = fk_course

    return models.Video.objects.create(
        title='Fundamentals',
        language='Python',
        body='Lorem ipsun Lorem ipsun Lorem ipsun Lorem ipsun.',
        author='John Smith',
        source_link='www.github.com/Synyster991',
        video_link='www.filipdimitrievski.com',
        course=temp_course
    )


class CourseModelTests(TestCase):
    """Test basic functionality of Course model"""
    def test_list_all_course(self):
        """Test listing all courses"""
        sample_course()
        exists = models.Course.objects.all().exists()

        self.assertTrue(exists)

    def test_list_specific_course(self):
        """Test list specific course"""
        course1 = sample_course()
        sample_course()
        res = models.Course.objects.filter(
            pk=course1.pk
        )
        exists = res.exists()

        self.assertTrue(exists)
        self.assertEqual(len(res), 1)

    def test_string_representation(self):
        """Test __str__"""
        course1 = sample_course()

        self.assertEqual(str(course1), course1.title)


class VideoModelTests(TestCase):
    """Test basic functionality of Video model"""
    def test_list_videos_for_specific_course(self):
        """Test list videos for specific courses"""
        course1 = sample_course()
        sample_video(course1)
        sample_video()

        res = models.Video.objects.filter(
            course=course1
        )
        exists = res.exists()

        self.assertTrue(exists)
        self.assertEqual(len(res), 1)

    def test_string_representation(self):
        """Test __str__"""
        video1 = sample_video()

        self.assertEqual(str(video1), video1.title)
