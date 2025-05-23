# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupedResourceCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'resource_count': 'int'
    }

    attribute_map = {
        'group_name': 'group_name',
        'resource_count': 'resource_count'
    }

    def __init__(self, group_name=None, resource_count=None):
        r"""GroupedResourceCount

        The model defined in huaweicloud sdk

        :param group_name: 分组名称。
        :type group_name: str
        :param resource_count: 资源数量。
        :type resource_count: int
        """
        
        

        self._group_name = None
        self._resource_count = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if resource_count is not None:
            self.resource_count = resource_count

    @property
    def group_name(self):
        r"""Gets the group_name of this GroupedResourceCount.

        分组名称。

        :return: The group_name of this GroupedResourceCount.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this GroupedResourceCount.

        分组名称。

        :param group_name: The group_name of this GroupedResourceCount.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def resource_count(self):
        r"""Gets the resource_count of this GroupedResourceCount.

        资源数量。

        :return: The resource_count of this GroupedResourceCount.
        :rtype: int
        """
        return self._resource_count

    @resource_count.setter
    def resource_count(self, resource_count):
        r"""Sets the resource_count of this GroupedResourceCount.

        资源数量。

        :param resource_count: The resource_count of this GroupedResourceCount.
        :type resource_count: int
        """
        self._resource_count = resource_count

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
        if not isinstance(other, GroupedResourceCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
