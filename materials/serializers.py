from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    count_lessons_in_course = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons_in_course(self, course):
        return course.lesson_set.count()


class CourseDetailSerializer(ModelSerializer):
    count_lessons_in_course = SerializerMethodField()

    def get_count_lessons_in_course(self, course):
        return course.lesson_set.count()

    class Meta:
        model = Course
        fields = ('name', "count_lessons_in_course",)

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'