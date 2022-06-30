# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSyntaxConversionProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_objects_count': 'int',
        'completed_objects_count': 'int',
        'objects_list': 'list[DatabaseObject]'
    }

    attribute_map = {
        'total_objects_count': 'total_objects_count',
        'completed_objects_count': 'completed_objects_count',
        'objects_list': 'objects_list'
    }

    def __init__(self, total_objects_count=None, completed_objects_count=None, objects_list=None):
        """ListSyntaxConversionProgressResponse

        The model defined in huaweicloud sdk

        :param total_objects_count: 对象总数。
        :type total_objects_count: int
        :param completed_objects_count: 完成语法转换的对象数量。
        :type completed_objects_count: int
        :param objects_list: 语法转换的对象列表。
        :type objects_list: list[:class:`huaweicloudsdkugo.v1.DatabaseObject`]
        """
        
        super(ListSyntaxConversionProgressResponse, self).__init__()

        self._total_objects_count = None
        self._completed_objects_count = None
        self._objects_list = None
        self.discriminator = None

        if total_objects_count is not None:
            self.total_objects_count = total_objects_count
        if completed_objects_count is not None:
            self.completed_objects_count = completed_objects_count
        if objects_list is not None:
            self.objects_list = objects_list

    @property
    def total_objects_count(self):
        """Gets the total_objects_count of this ListSyntaxConversionProgressResponse.

        对象总数。

        :return: The total_objects_count of this ListSyntaxConversionProgressResponse.
        :rtype: int
        """
        return self._total_objects_count

    @total_objects_count.setter
    def total_objects_count(self, total_objects_count):
        """Sets the total_objects_count of this ListSyntaxConversionProgressResponse.

        对象总数。

        :param total_objects_count: The total_objects_count of this ListSyntaxConversionProgressResponse.
        :type total_objects_count: int
        """
        self._total_objects_count = total_objects_count

    @property
    def completed_objects_count(self):
        """Gets the completed_objects_count of this ListSyntaxConversionProgressResponse.

        完成语法转换的对象数量。

        :return: The completed_objects_count of this ListSyntaxConversionProgressResponse.
        :rtype: int
        """
        return self._completed_objects_count

    @completed_objects_count.setter
    def completed_objects_count(self, completed_objects_count):
        """Sets the completed_objects_count of this ListSyntaxConversionProgressResponse.

        完成语法转换的对象数量。

        :param completed_objects_count: The completed_objects_count of this ListSyntaxConversionProgressResponse.
        :type completed_objects_count: int
        """
        self._completed_objects_count = completed_objects_count

    @property
    def objects_list(self):
        """Gets the objects_list of this ListSyntaxConversionProgressResponse.

        语法转换的对象列表。

        :return: The objects_list of this ListSyntaxConversionProgressResponse.
        :rtype: list[:class:`huaweicloudsdkugo.v1.DatabaseObject`]
        """
        return self._objects_list

    @objects_list.setter
    def objects_list(self, objects_list):
        """Sets the objects_list of this ListSyntaxConversionProgressResponse.

        语法转换的对象列表。

        :param objects_list: The objects_list of this ListSyntaxConversionProgressResponse.
        :type objects_list: list[:class:`huaweicloudsdkugo.v1.DatabaseObject`]
        """
        self._objects_list = objects_list

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
        if not isinstance(other, ListSyntaxConversionProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
