# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubnetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subnets': 'list[Subnet]',
        'count': 'int'
    }

    attribute_map = {
        'subnets': 'subnets',
        'count': 'count'
    }

    def __init__(self, subnets=None, count=None):
        """ListSubnetsResponse

        The model defined in huaweicloud sdk

        :param subnets: 子网数组。
        :type subnets: list[:class:`huaweicloudsdkiec.v1.Subnet`]
        :param count: 子网数目。
        :type count: int
        """
        
        super(ListSubnetsResponse, self).__init__()

        self._subnets = None
        self._count = None
        self.discriminator = None

        if subnets is not None:
            self.subnets = subnets
        if count is not None:
            self.count = count

    @property
    def subnets(self):
        """Gets the subnets of this ListSubnetsResponse.

        子网数组。

        :return: The subnets of this ListSubnetsResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.Subnet`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this ListSubnetsResponse.

        子网数组。

        :param subnets: The subnets of this ListSubnetsResponse.
        :type subnets: list[:class:`huaweicloudsdkiec.v1.Subnet`]
        """
        self._subnets = subnets

    @property
    def count(self):
        """Gets the count of this ListSubnetsResponse.

        子网数目。

        :return: The count of this ListSubnetsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSubnetsResponse.

        子网数目。

        :param count: The count of this ListSubnetsResponse.
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
        if not isinstance(other, ListSubnetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
