# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicIpsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'site_id': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'site_id': 'site_id',
        'port_id': 'port_id'
    }

    def __init__(self, limit=None, offset=None, site_id=None, port_id=None):
        """ListPublicIpsRequest

        The model defined in huaweicloud sdk

        :param limit: 查询返回弹性IP列表数量。取值范围：0~1000。
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param site_id: 站点ID。
        :type site_id: str
        :param port_id: 端口ID
        :type port_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._site_id = None
        self._port_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if site_id is not None:
            self.site_id = site_id
        if port_id is not None:
            self.port_id = port_id

    @property
    def limit(self):
        """Gets the limit of this ListPublicIpsRequest.

        查询返回弹性IP列表数量。取值范围：0~1000。

        :return: The limit of this ListPublicIpsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublicIpsRequest.

        查询返回弹性IP列表数量。取值范围：0~1000。

        :param limit: The limit of this ListPublicIpsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPublicIpsRequest.

        查询的偏移量。

        :return: The offset of this ListPublicIpsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPublicIpsRequest.

        查询的偏移量。

        :param offset: The offset of this ListPublicIpsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def site_id(self):
        """Gets the site_id of this ListPublicIpsRequest.

        站点ID。

        :return: The site_id of this ListPublicIpsRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ListPublicIpsRequest.

        站点ID。

        :param site_id: The site_id of this ListPublicIpsRequest.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def port_id(self):
        """Gets the port_id of this ListPublicIpsRequest.

        端口ID

        :return: The port_id of this ListPublicIpsRequest.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this ListPublicIpsRequest.

        端口ID

        :param port_id: The port_id of this ListPublicIpsRequest.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, ListPublicIpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
