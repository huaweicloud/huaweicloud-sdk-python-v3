# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectedInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'protected_instances': 'list[ShowProtectedInstanceParams]',
        'count': 'int'
    }

    attribute_map = {
        'protected_instances': 'protected_instances',
        'count': 'count'
    }

    def __init__(self, protected_instances=None, count=None):
        """ListProtectedInstancesResponse

        The model defined in huaweicloud sdk

        :param protected_instances: 保护实例的信息列表。
        :type protected_instances: list[:class:`huaweicloudsdksdrs.v1.ShowProtectedInstanceParams`]
        :param count: 列表中包含的保护实例个数。
        :type count: int
        """
        
        super(ListProtectedInstancesResponse, self).__init__()

        self._protected_instances = None
        self._count = None
        self.discriminator = None

        if protected_instances is not None:
            self.protected_instances = protected_instances
        if count is not None:
            self.count = count

    @property
    def protected_instances(self):
        """Gets the protected_instances of this ListProtectedInstancesResponse.

        保护实例的信息列表。

        :return: The protected_instances of this ListProtectedInstancesResponse.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ShowProtectedInstanceParams`]
        """
        return self._protected_instances

    @protected_instances.setter
    def protected_instances(self, protected_instances):
        """Sets the protected_instances of this ListProtectedInstancesResponse.

        保护实例的信息列表。

        :param protected_instances: The protected_instances of this ListProtectedInstancesResponse.
        :type protected_instances: list[:class:`huaweicloudsdksdrs.v1.ShowProtectedInstanceParams`]
        """
        self._protected_instances = protected_instances

    @property
    def count(self):
        """Gets the count of this ListProtectedInstancesResponse.

        列表中包含的保护实例个数。

        :return: The count of this ListProtectedInstancesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListProtectedInstancesResponse.

        列表中包含的保护实例个数。

        :param count: The count of this ListProtectedInstancesResponse.
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
        if not isinstance(other, ListProtectedInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
