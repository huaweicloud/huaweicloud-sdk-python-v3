# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityGroupRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'security_group_id': 'str',
        'remote_ip_prefix': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'security_group_id': 'security_group_id',
        'remote_ip_prefix': 'remote_ip_prefix'
    }

    def __init__(self, marker=None, limit=None, security_group_id=None, remote_ip_prefix=None):
        """ListSecurityGroupRulesRequest

        The model defined in huaweicloud sdk

        :param marker: 功能说明：分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param limit: 每页返回的个数
        :type limit: int
        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param remote_ip_prefix: 功能说明：远端IP地址 取值范围：cidr格式
        :type remote_ip_prefix: str
        """
        
        

        self._marker = None
        self._limit = None
        self._security_group_id = None
        self._remote_ip_prefix = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix

    @property
    def marker(self):
        """Gets the marker of this ListSecurityGroupRulesRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSecurityGroupRulesRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListSecurityGroupRulesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListSecurityGroupRulesRequest.

        每页返回的个数

        :return: The limit of this ListSecurityGroupRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityGroupRulesRequest.

        每页返回的个数

        :param limit: The limit of this ListSecurityGroupRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ListSecurityGroupRulesRequest.

        安全组ID

        :return: The security_group_id of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ListSecurityGroupRulesRequest.

        安全组ID

        :param security_group_id: The security_group_id of this ListSecurityGroupRulesRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this ListSecurityGroupRulesRequest.

        功能说明：远端IP地址 取值范围：cidr格式

        :return: The remote_ip_prefix of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this ListSecurityGroupRulesRequest.

        功能说明：远端IP地址 取值范围：cidr格式

        :param remote_ip_prefix: The remote_ip_prefix of this ListSecurityGroupRulesRequest.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

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
        if not isinstance(other, ListSecurityGroupRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
