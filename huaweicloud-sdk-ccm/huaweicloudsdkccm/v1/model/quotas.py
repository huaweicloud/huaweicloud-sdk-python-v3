# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quotas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[Resources]'
    }

    attribute_map = {
        'resources': 'resources'
    }

    def __init__(self, resources=None):
        """Quotas

        The model defined in huaweicloud sdk

        :param resources: 资源配额列表，详情请参见**Resources**字段数据结构说明。
        :type resources: list[:class:`huaweicloudsdkccm.v1.Resources`]
        """
        
        

        self._resources = None
        self.discriminator = None

        self.resources = resources

    @property
    def resources(self):
        """Gets the resources of this Quotas.

        资源配额列表，详情请参见**Resources**字段数据结构说明。

        :return: The resources of this Quotas.
        :rtype: list[:class:`huaweicloudsdkccm.v1.Resources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Quotas.

        资源配额列表，详情请参见**Resources**字段数据结构说明。

        :param resources: The resources of this Quotas.
        :type resources: list[:class:`huaweicloudsdkccm.v1.Resources`]
        """
        self._resources = resources

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
        if not isinstance(other, Quotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
