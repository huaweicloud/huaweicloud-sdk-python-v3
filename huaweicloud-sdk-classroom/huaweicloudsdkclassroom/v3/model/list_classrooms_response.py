# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClassroomsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'classrooms': 'list[ClassroomCard]',
        'total': 'int'
    }

    attribute_map = {
        'classrooms': 'classrooms',
        'total': 'total'
    }

    def __init__(self, classrooms=None, total=None):
        """ListClassroomsResponse

        The model defined in huaweicloud sdk

        :param classrooms: 课堂列表
        :type classrooms: list[:class:`huaweicloudsdkclassroom.v3.ClassroomCard`]
        :param total: 课堂总数
        :type total: int
        """
        
        super(ListClassroomsResponse, self).__init__()

        self._classrooms = None
        self._total = None
        self.discriminator = None

        if classrooms is not None:
            self.classrooms = classrooms
        if total is not None:
            self.total = total

    @property
    def classrooms(self):
        """Gets the classrooms of this ListClassroomsResponse.

        课堂列表

        :return: The classrooms of this ListClassroomsResponse.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.ClassroomCard`]
        """
        return self._classrooms

    @classrooms.setter
    def classrooms(self, classrooms):
        """Sets the classrooms of this ListClassroomsResponse.

        课堂列表

        :param classrooms: The classrooms of this ListClassroomsResponse.
        :type classrooms: list[:class:`huaweicloudsdkclassroom.v3.ClassroomCard`]
        """
        self._classrooms = classrooms

    @property
    def total(self):
        """Gets the total of this ListClassroomsResponse.

        课堂总数

        :return: The total of this ListClassroomsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListClassroomsResponse.

        课堂总数

        :param total: The total of this ListClassroomsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListClassroomsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
