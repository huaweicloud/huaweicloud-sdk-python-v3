# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRoutetablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'routetables': 'list[ListRoutetableOption]',
        'count': 'int'
    }

    attribute_map = {
        'routetables': 'routetables',
        'count': 'count'
    }

    def __init__(self, routetables=None, count=None):
        """ListRoutetablesResponse

        The model defined in huaweicloud sdk

        :param routetables: 路由表
        :type routetables: list[:class:`huaweicloudsdkiec.v1.ListRoutetableOption`]
        :param count: 数量
        :type count: int
        """
        
        super(ListRoutetablesResponse, self).__init__()

        self._routetables = None
        self._count = None
        self.discriminator = None

        if routetables is not None:
            self.routetables = routetables
        if count is not None:
            self.count = count

    @property
    def routetables(self):
        """Gets the routetables of this ListRoutetablesResponse.

        路由表

        :return: The routetables of this ListRoutetablesResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.ListRoutetableOption`]
        """
        return self._routetables

    @routetables.setter
    def routetables(self, routetables):
        """Sets the routetables of this ListRoutetablesResponse.

        路由表

        :param routetables: The routetables of this ListRoutetablesResponse.
        :type routetables: list[:class:`huaweicloudsdkiec.v1.ListRoutetableOption`]
        """
        self._routetables = routetables

    @property
    def count(self):
        """Gets the count of this ListRoutetablesResponse.

        数量

        :return: The count of this ListRoutetablesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRoutetablesResponse.

        数量

        :param count: The count of this ListRoutetablesResponse.
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
        if not isinstance(other, ListRoutetablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
