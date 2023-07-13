# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageCard:

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
        'image_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag_name': 'tag_name',
        'school': 'school',
        'teacher_name': 'teacher_name',
        'order_count': 'order_count',
        'image_url': 'image_url'
    }

    def __init__(self, id=None, name=None, tag_name=None, school=None, teacher_name=None, order_count=None, image_url=None):
        """PackageCard

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
        """
        
        

        self._id = None
        self._name = None
        self._tag_name = None
        self._school = None
        self._teacher_name = None
        self._order_count = None
        self._image_url = None
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

    @property
    def id(self):
        """Gets the id of this PackageCard.

        习题库id

        :return: The id of this PackageCard.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageCard.

        习题库id

        :param id: The id of this PackageCard.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PackageCard.

        习题库名称

        :return: The name of this PackageCard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageCard.

        习题库名称

        :param name: The name of this PackageCard.
        :type name: str
        """
        self._name = name

    @property
    def tag_name(self):
        """Gets the tag_name of this PackageCard.

        标签名称

        :return: The tag_name of this PackageCard.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this PackageCard.

        标签名称

        :param tag_name: The tag_name of this PackageCard.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def school(self):
        """Gets the school of this PackageCard.

        学习名称

        :return: The school of this PackageCard.
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this PackageCard.

        学习名称

        :param school: The school of this PackageCard.
        :type school: str
        """
        self._school = school

    @property
    def teacher_name(self):
        """Gets the teacher_name of this PackageCard.

        教师名称

        :return: The teacher_name of this PackageCard.
        :rtype: str
        """
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name):
        """Sets the teacher_name of this PackageCard.

        教师名称

        :param teacher_name: The teacher_name of this PackageCard.
        :type teacher_name: str
        """
        self._teacher_name = teacher_name

    @property
    def order_count(self):
        """Gets the order_count of this PackageCard.

        租户习题库编号

        :return: The order_count of this PackageCard.
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        """Sets the order_count of this PackageCard.

        租户习题库编号

        :param order_count: The order_count of this PackageCard.
        :type order_count: int
        """
        self._order_count = order_count

    @property
    def image_url(self):
        """Gets the image_url of this PackageCard.

        背景图url

        :return: The image_url of this PackageCard.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this PackageCard.

        背景图url

        :param image_url: The image_url of this PackageCard.
        :type image_url: str
        """
        self._image_url = image_url

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
        if not isinstance(other, PackageCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
