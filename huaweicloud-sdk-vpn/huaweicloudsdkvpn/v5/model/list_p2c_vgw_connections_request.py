# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListP2cVgwConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'p2c_vgw_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'p2c_vgw_id': 'p2c_vgw_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, p2c_vgw_id=None, limit=None, offset=None):
        """ListP2cVgwConnectionsRequest

        The model defined in huaweicloud sdk

        :param p2c_vgw_id: P2C VPN网关实例ID
        :type p2c_vgw_id: str
        :param limit: 分页查询时每页返回的记录数量
        :type limit: int
        :param offset: 分页查询的偏移量
        :type offset: int
        """
        
        

        self._p2c_vgw_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.p2c_vgw_id = p2c_vgw_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def p2c_vgw_id(self):
        """Gets the p2c_vgw_id of this ListP2cVgwConnectionsRequest.

        P2C VPN网关实例ID

        :return: The p2c_vgw_id of this ListP2cVgwConnectionsRequest.
        :rtype: str
        """
        return self._p2c_vgw_id

    @p2c_vgw_id.setter
    def p2c_vgw_id(self, p2c_vgw_id):
        """Sets the p2c_vgw_id of this ListP2cVgwConnectionsRequest.

        P2C VPN网关实例ID

        :param p2c_vgw_id: The p2c_vgw_id of this ListP2cVgwConnectionsRequest.
        :type p2c_vgw_id: str
        """
        self._p2c_vgw_id = p2c_vgw_id

    @property
    def limit(self):
        """Gets the limit of this ListP2cVgwConnectionsRequest.

        分页查询时每页返回的记录数量

        :return: The limit of this ListP2cVgwConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListP2cVgwConnectionsRequest.

        分页查询时每页返回的记录数量

        :param limit: The limit of this ListP2cVgwConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListP2cVgwConnectionsRequest.

        分页查询的偏移量

        :return: The offset of this ListP2cVgwConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListP2cVgwConnectionsRequest.

        分页查询的偏移量

        :param offset: The offset of this ListP2cVgwConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListP2cVgwConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
