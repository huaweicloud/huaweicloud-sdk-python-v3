# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceMultiCountResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'count': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'count': 'count'
    }

    def __init__(self, resource_type=None, count=None):
        r"""ResourceMultiCountResponseData

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型
        :type resource_type: str
        :param count: 资源数量
        :type count: int
        """
        
        

        self._resource_type = None
        self._count = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if count is not None:
            self.count = count

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceMultiCountResponseData.

        资源类型

        :return: The resource_type of this ResourceMultiCountResponseData.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceMultiCountResponseData.

        资源类型

        :param resource_type: The resource_type of this ResourceMultiCountResponseData.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def count(self):
        r"""Gets the count of this ResourceMultiCountResponseData.

        资源数量

        :return: The count of this ResourceMultiCountResponseData.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ResourceMultiCountResponseData.

        资源数量

        :param count: The count of this ResourceMultiCountResponseData.
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
        if not isinstance(other, ResourceMultiCountResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
