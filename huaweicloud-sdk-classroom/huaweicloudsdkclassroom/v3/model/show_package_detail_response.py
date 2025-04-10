# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPackageDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'tag_name': 'str',
        'school': 'str',
        'teacher_name': 'str',
        'order_count': 'int',
        'image_url': 'str',
        'description': 'str',
        'exercise_cnt': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag_name': 'tag_name',
        'school': 'school',
        'teacher_name': 'teacher_name',
        'order_count': 'order_count',
        'image_url': 'image_url',
        'description': 'description',
        'exercise_cnt': 'exercise_cnt'
    }

    def __init__(self, id=None, name=None, tag_name=None, school=None, teacher_name=None, order_count=None, image_url=None, description=None, exercise_cnt=None):
        r"""ShowPackageDetailResponse

        The model defined in huaweicloud sdk

        :param id: 习题库id
        :type id: str
        :param name: 习题库名称
        :type name: str
        :param tag_name: 标签名称
        :type tag_name: str
        :param school: 学习名称
        :type school: str
        :param teacher_name: 教师名称
        :type teacher_name: str
        :param order_count: 租户习题库编号
        :type order_count: int
        :param image_url: 背景图url
        :type image_url: str
        :param description: 习题库描述
        :type description: str
        :param exercise_cnt: 习题库里的习题数量
        :type exercise_cnt: int
        """
        
        super(ShowPackageDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._tag_name = None
        self._school = None
        self._teacher_name = None
        self._order_count = None
        self._image_url = None
        self._description = None
        self._exercise_cnt = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag_name is not None:
            self.tag_name = tag_name
        if school is not None:
            self.school = school
        if teacher_name is not None:
            self.teacher_name = teacher_name
        if order_count is not None:
            self.order_count = order_count
        if image_url is not None:
            self.image_url = image_url
        if description is not None:
            self.description = description
        if exercise_cnt is not None:
            self.exercise_cnt = exercise_cnt

    @property
    def id(self):
        r"""Gets the id of this ShowPackageDetailResponse.

        习题库id

        :return: The id of this ShowPackageDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPackageDetailResponse.

        习题库id

        :param id: The id of this ShowPackageDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowPackageDetailResponse.

        习题库名称

        :return: The name of this ShowPackageDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPackageDetailResponse.

        习题库名称

        :param name: The name of this ShowPackageDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def tag_name(self):
        r"""Gets the tag_name of this ShowPackageDetailResponse.

        标签名称

        :return: The tag_name of this ShowPackageDetailResponse.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this ShowPackageDetailResponse.

        标签名称

        :param tag_name: The tag_name of this ShowPackageDetailResponse.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def school(self):
        r"""Gets the school of this ShowPackageDetailResponse.

        学习名称

        :return: The school of this ShowPackageDetailResponse.
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        r"""Sets the school of this ShowPackageDetailResponse.

        学习名称

        :param school: The school of this ShowPackageDetailResponse.
        :type school: str
        """
        self._school = school

    @property
    def teacher_name(self):
        r"""Gets the teacher_name of this ShowPackageDetailResponse.

        教师名称

        :return: The teacher_name of this ShowPackageDetailResponse.
        :rtype: str
        """
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name):
        r"""Sets the teacher_name of this ShowPackageDetailResponse.

        教师名称

        :param teacher_name: The teacher_name of this ShowPackageDetailResponse.
        :type teacher_name: str
        """
        self._teacher_name = teacher_name

    @property
    def order_count(self):
        r"""Gets the order_count of this ShowPackageDetailResponse.

        租户习题库编号

        :return: The order_count of this ShowPackageDetailResponse.
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        r"""Sets the order_count of this ShowPackageDetailResponse.

        租户习题库编号

        :param order_count: The order_count of this ShowPackageDetailResponse.
        :type order_count: int
        """
        self._order_count = order_count

    @property
    def image_url(self):
        r"""Gets the image_url of this ShowPackageDetailResponse.

        背景图url

        :return: The image_url of this ShowPackageDetailResponse.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this ShowPackageDetailResponse.

        背景图url

        :param image_url: The image_url of this ShowPackageDetailResponse.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def description(self):
        r"""Gets the description of this ShowPackageDetailResponse.

        习题库描述

        :return: The description of this ShowPackageDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPackageDetailResponse.

        习题库描述

        :param description: The description of this ShowPackageDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def exercise_cnt(self):
        r"""Gets the exercise_cnt of this ShowPackageDetailResponse.

        习题库里的习题数量

        :return: The exercise_cnt of this ShowPackageDetailResponse.
        :rtype: int
        """
        return self._exercise_cnt

    @exercise_cnt.setter
    def exercise_cnt(self, exercise_cnt):
        r"""Sets the exercise_cnt of this ShowPackageDetailResponse.

        习题库里的习题数量

        :param exercise_cnt: The exercise_cnt of this ShowPackageDetailResponse.
        :type exercise_cnt: int
        """
        self._exercise_cnt = exercise_cnt

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowPackageDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
