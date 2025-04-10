# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagValuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_name': 'str',
        'tag_values': 'list[str]',
        'count': 'int'
    }

    attribute_map = {
        'tag_name': 'tag_name',
        'tag_values': 'tag_values',
        'count': 'count'
    }

    def __init__(self, tag_name=None, tag_values=None, count=None):
        r"""ListTagValuesResponse

        The model defined in huaweicloud sdk

        :param tag_name: 标签的名称
        :type tag_name: str
        :param tag_values: 标签的值列表
        :type tag_values: list[str]
        :param count: 当前列表元素总数
        :type count: int
        """
        
        super(ListTagValuesResponse, self).__init__()

        self._tag_name = None
        self._tag_values = None
        self._count = None
        self.discriminator = None

        if tag_name is not None:
            self.tag_name = tag_name
        if tag_values is not None:
            self.tag_values = tag_values
        if count is not None:
            self.count = count

    @property
    def tag_name(self):
        r"""Gets the tag_name of this ListTagValuesResponse.

        标签的名称

        :return: The tag_name of this ListTagValuesResponse.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this ListTagValuesResponse.

        标签的名称

        :param tag_name: The tag_name of this ListTagValuesResponse.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def tag_values(self):
        r"""Gets the tag_values of this ListTagValuesResponse.

        标签的值列表

        :return: The tag_values of this ListTagValuesResponse.
        :rtype: list[str]
        """
        return self._tag_values

    @tag_values.setter
    def tag_values(self, tag_values):
        r"""Sets the tag_values of this ListTagValuesResponse.

        标签的值列表

        :param tag_values: The tag_values of this ListTagValuesResponse.
        :type tag_values: list[str]
        """
        self._tag_values = tag_values

    @property
    def count(self):
        r"""Gets the count of this ListTagValuesResponse.

        当前列表元素总数

        :return: The count of this ListTagValuesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListTagValuesResponse.

        当前列表元素总数

        :param count: The count of this ListTagValuesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListTagValuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
