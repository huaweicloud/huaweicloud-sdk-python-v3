# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUnboundProtectedIpRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'package_id': 'package_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, package_id=None, offset=None, limit=None):
        r"""ListUnboundProtectedIpRequest

        The model defined in huaweicloud sdk

        :param package_id: 实例id
        :type package_id: str
        :param offset: 开始查询的偏移量,默认值:0
        :type offset: int
        :param limit: 每页显示的条目数量,默认值:2000
        :type limit: int
        """
        
        

        self._package_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.package_id = package_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def package_id(self):
        r"""Gets the package_id of this ListUnboundProtectedIpRequest.

        实例id

        :return: The package_id of this ListUnboundProtectedIpRequest.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this ListUnboundProtectedIpRequest.

        实例id

        :param package_id: The package_id of this ListUnboundProtectedIpRequest.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def offset(self):
        r"""Gets the offset of this ListUnboundProtectedIpRequest.

        开始查询的偏移量,默认值:0

        :return: The offset of this ListUnboundProtectedIpRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUnboundProtectedIpRequest.

        开始查询的偏移量,默认值:0

        :param offset: The offset of this ListUnboundProtectedIpRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUnboundProtectedIpRequest.

        每页显示的条目数量,默认值:2000

        :return: The limit of this ListUnboundProtectedIpRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUnboundProtectedIpRequest.

        每页显示的条目数量,默认值:2000

        :param limit: The limit of this ListUnboundProtectedIpRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListUnboundProtectedIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
