# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagResourcesRequest:

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
        'resource_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, resource_type=None, resource_id=None, limit=None, marker=None):
        """ListTagResourcesRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型 organizations:policies服务策略 organizations:ous组织OU organizations:accounts 帐号信息 organizations:roots根
        :type resource_type: str
        :param resource_id: 根、组织单元、帐号或策略的唯一标识符（ID）。
        :type resource_id: str
        :param limit: 页面中最大结果数量。
        :type limit: int
        :param marker: 分页标记。
        :type marker: str
        """
        
        

        self._resource_type = None
        self._resource_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def resource_type(self):
        """Gets the resource_type of this ListTagResourcesRequest.

        资源类型 organizations:policies服务策略 organizations:ous组织OU organizations:accounts 帐号信息 organizations:roots根

        :return: The resource_type of this ListTagResourcesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListTagResourcesRequest.

        资源类型 organizations:policies服务策略 organizations:ous组织OU organizations:accounts 帐号信息 organizations:roots根

        :param resource_type: The resource_type of this ListTagResourcesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this ListTagResourcesRequest.

        根、组织单元、帐号或策略的唯一标识符（ID）。

        :return: The resource_id of this ListTagResourcesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListTagResourcesRequest.

        根、组织单元、帐号或策略的唯一标识符（ID）。

        :param resource_id: The resource_id of this ListTagResourcesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def limit(self):
        """Gets the limit of this ListTagResourcesRequest.

        页面中最大结果数量。

        :return: The limit of this ListTagResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTagResourcesRequest.

        页面中最大结果数量。

        :param limit: The limit of this ListTagResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListTagResourcesRequest.

        分页标记。

        :return: The marker of this ListTagResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListTagResourcesRequest.

        分页标记。

        :param marker: The marker of this ListTagResourcesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListTagResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
