# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpPool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'site_id': 'str',
        'pool_id': 'str',
        'ip_version': 'str',
        'operator': 'Operator',
        'display_name': 'str',
        'allow_share_bandwidth_types': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'site_id': 'site_id',
        'pool_id': 'pool_id',
        'ip_version': 'ip_version',
        'operator': 'operator',
        'display_name': 'display_name',
        'allow_share_bandwidth_types': 'allow_share_bandwidth_types'
    }

    def __init__(self, id=None, site_id=None, pool_id=None, ip_version=None, operator=None, display_name=None, allow_share_bandwidth_types=None):
        r"""IpPool

        The model defined in huaweicloud sdk

        :param id: 线路的ID。
        :type id: str
        :param site_id: 线路所属站点ID。
        :type site_id: str
        :param pool_id: 线路标识。
        :type pool_id: str
        :param ip_version: IPv4或IPv6线路。  取值范围： - 4：IPv4线路 - 6：IPv6线路
        :type ip_version: str
        :param operator: 
        :type operator: :class:`huaweicloudsdkiec.v1.Operator`
        :param display_name: 线路的显示名称。
        :type display_name: str
        :param allow_share_bandwidth_types: 功能说明：表示此线路可以使用的带宽类型列表，如果列表为空，则表示该线路不能使用任何带宽  约束：线路下的ip只能加入到带宽类型在allow_share_bandwidth_types中带宽 
        :type allow_share_bandwidth_types: list[str]
        """
        
        

        self._id = None
        self._site_id = None
        self._pool_id = None
        self._ip_version = None
        self._operator = None
        self._display_name = None
        self._allow_share_bandwidth_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if site_id is not None:
            self.site_id = site_id
        if pool_id is not None:
            self.pool_id = pool_id
        if ip_version is not None:
            self.ip_version = ip_version
        if operator is not None:
            self.operator = operator
        if display_name is not None:
            self.display_name = display_name
        if allow_share_bandwidth_types is not None:
            self.allow_share_bandwidth_types = allow_share_bandwidth_types

    @property
    def id(self):
        r"""Gets the id of this IpPool.

        线路的ID。

        :return: The id of this IpPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IpPool.

        线路的ID。

        :param id: The id of this IpPool.
        :type id: str
        """
        self._id = id

    @property
    def site_id(self):
        r"""Gets the site_id of this IpPool.

        线路所属站点ID。

        :return: The site_id of this IpPool.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this IpPool.

        线路所属站点ID。

        :param site_id: The site_id of this IpPool.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def pool_id(self):
        r"""Gets the pool_id of this IpPool.

        线路标识。

        :return: The pool_id of this IpPool.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this IpPool.

        线路标识。

        :param pool_id: The pool_id of this IpPool.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this IpPool.

        IPv4或IPv6线路。  取值范围： - 4：IPv4线路 - 6：IPv6线路

        :return: The ip_version of this IpPool.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this IpPool.

        IPv4或IPv6线路。  取值范围： - 4：IPv4线路 - 6：IPv6线路

        :param ip_version: The ip_version of this IpPool.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def operator(self):
        r"""Gets the operator of this IpPool.

        :return: The operator of this IpPool.
        :rtype: :class:`huaweicloudsdkiec.v1.Operator`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this IpPool.

        :param operator: The operator of this IpPool.
        :type operator: :class:`huaweicloudsdkiec.v1.Operator`
        """
        self._operator = operator

    @property
    def display_name(self):
        r"""Gets the display_name of this IpPool.

        线路的显示名称。

        :return: The display_name of this IpPool.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this IpPool.

        线路的显示名称。

        :param display_name: The display_name of this IpPool.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def allow_share_bandwidth_types(self):
        r"""Gets the allow_share_bandwidth_types of this IpPool.

        功能说明：表示此线路可以使用的带宽类型列表，如果列表为空，则表示该线路不能使用任何带宽  约束：线路下的ip只能加入到带宽类型在allow_share_bandwidth_types中带宽 

        :return: The allow_share_bandwidth_types of this IpPool.
        :rtype: list[str]
        """
        return self._allow_share_bandwidth_types

    @allow_share_bandwidth_types.setter
    def allow_share_bandwidth_types(self, allow_share_bandwidth_types):
        r"""Sets the allow_share_bandwidth_types of this IpPool.

        功能说明：表示此线路可以使用的带宽类型列表，如果列表为空，则表示该线路不能使用任何带宽  约束：线路下的ip只能加入到带宽类型在allow_share_bandwidth_types中带宽 

        :param allow_share_bandwidth_types: The allow_share_bandwidth_types of this IpPool.
        :type allow_share_bandwidth_types: list[str]
        """
        self._allow_share_bandwidth_types = allow_share_bandwidth_types

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
        if not isinstance(other, IpPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
