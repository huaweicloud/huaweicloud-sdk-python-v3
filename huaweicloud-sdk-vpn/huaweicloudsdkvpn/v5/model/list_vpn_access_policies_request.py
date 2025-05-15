# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpnAccessPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_server_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'vpn_server_id': 'vpn_server_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, vpn_server_id=None, limit=None, marker=None):
        r"""ListVpnAccessPoliciesRequest

        The model defined in huaweicloud sdk

        :param vpn_server_id: VPN服务端 ID
        :type vpn_server_id: str
        :param limit: 分页查询时每页返回的记录数量
        :type limit: int
        :param marker: 上一页最后一条资源记录的创建时间，为空时为查询第一页。使用说明：必须与limit一起使用。
        :type marker: str
        """
        
        

        self._vpn_server_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.vpn_server_id = vpn_server_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def vpn_server_id(self):
        r"""Gets the vpn_server_id of this ListVpnAccessPoliciesRequest.

        VPN服务端 ID

        :return: The vpn_server_id of this ListVpnAccessPoliciesRequest.
        :rtype: str
        """
        return self._vpn_server_id

    @vpn_server_id.setter
    def vpn_server_id(self, vpn_server_id):
        r"""Sets the vpn_server_id of this ListVpnAccessPoliciesRequest.

        VPN服务端 ID

        :param vpn_server_id: The vpn_server_id of this ListVpnAccessPoliciesRequest.
        :type vpn_server_id: str
        """
        self._vpn_server_id = vpn_server_id

    @property
    def limit(self):
        r"""Gets the limit of this ListVpnAccessPoliciesRequest.

        分页查询时每页返回的记录数量

        :return: The limit of this ListVpnAccessPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVpnAccessPoliciesRequest.

        分页查询时每页返回的记录数量

        :param limit: The limit of this ListVpnAccessPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListVpnAccessPoliciesRequest.

        上一页最后一条资源记录的创建时间，为空时为查询第一页。使用说明：必须与limit一起使用。

        :return: The marker of this ListVpnAccessPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVpnAccessPoliciesRequest.

        上一页最后一条资源记录的创建时间，为空时为查询第一页。使用说明：必须与limit一起使用。

        :param marker: The marker of this ListVpnAccessPoliciesRequest.
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
        if not isinstance(other, ListVpnAccessPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
