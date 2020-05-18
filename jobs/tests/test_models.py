from django.test import TestCase

from jobs import models


def sample_job():
    return models.Job.objects.create(
        title='RecipeAPI',
        source_link='www.example.com',
        description="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has 
        been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type 
        and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap 
        into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the 
        release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
        software like Aldus PageMaker including versions of Lorem Ipsum""",
        preview_link='www.preview.com',
        image=''
    )


def sample_achievement():
    """Create Dummy achievemnt"""
    return models.Achievement.objects.create(
        title='Django',
        sub_title='Online Course',
        body="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has 
        been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type 
        and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap 
        into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the 
        release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
        software like Aldus PageMaker including versions of Lorem Ipsum""",
        image='',
        issued_by='Udemy'
    )


class JobModelTest(TestCase):
    """Test Job models"""
    def test_listing_jobs(self):
        """Test listing all jobs"""
        sample_job()
        exists = models.Job.objects.filter(title='RecipeAPI').exists()
        self.assertTrue(exists)

    def test_job_string_representation(self):
        """Test Job __str__"""
        sample_job()
        job = models.Job.objects.get(title='RecipeAPI')
        self.assertEqual(str(job), 'RecipeAPI')

    def test_description_summary(self):
        """Test the summary """
        job = sample_job()
        self.assertEqual(len(job.summary()), 100)


class AchievementModelTest(TestCase):
    """Test Achievement Model"""
    def test_listing_achievement(self):
        """Test listing all achievments"""
        sample_achievement()
        exists = models.Achievement.objects.filter(title='Django').exists()
        self.assertTrue(exists)

    def test_achievement_string_representation(self):
        """Test Achievement __str__()"""
        sample_achievement()
        achievement = models.Achievement.objects.get(title='Django')
        self.assertEqual(str(achievement), 'Django')

    def test_description_summary(self):
        """Test the summary"""
        achievement = sample_achievement()
        self.assertEqual(len(achievement.summary()), 100)
