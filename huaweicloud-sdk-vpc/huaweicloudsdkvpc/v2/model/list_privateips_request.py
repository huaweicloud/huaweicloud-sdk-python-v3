# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateipsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, subnet_id=None, limit=None, marker=None):
        r"""ListPrivateipsRequest

        The model defined in huaweicloud sdk

        :param subnet_id: 私有IP所在子网的唯一标识
        :type subnet_id: str
        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源id，为空时查询第一页
        :type marker: str
        """
        
        

        self._subnet_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.subnet_id = subnet_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListPrivateipsRequest.

        私有IP所在子网的唯一标识

        :return: The subnet_id of this ListPrivateipsRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListPrivateipsRequest.

        私有IP所在子网的唯一标识

        :param subnet_id: The subnet_id of this ListPrivateipsRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def limit(self):
        r"""Gets the limit of this ListPrivateipsRequest.

        每页返回的个数

        :return: The limit of this ListPrivateipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPrivateipsRequest.

        每页返回的个数

        :param limit: The limit of this ListPrivateipsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPrivateipsRequest.

        分页查询起始的资源id，为空时查询第一页

        :return: The marker of this ListPrivateipsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPrivateipsRequest.

        分页查询起始的资源id，为空时查询第一页

        :param marker: The marker of this ListPrivateipsRequest.
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
        if not isinstance(other, ListPrivateipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
