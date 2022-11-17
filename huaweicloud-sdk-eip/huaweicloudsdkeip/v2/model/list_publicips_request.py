# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicipsRequest:

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
        'ip_version': 'int',
        'enterprise_project_id': 'str',
        'port_id': 'list[str]',
        'public_ip_address': 'list[str]',
        'private_ip_address': 'list[str]',
        'id': 'list[str]',
        'allow_share_bandwidth_type_any': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'ip_version': 'ip_version',
        'enterprise_project_id': 'enterprise_project_id',
        'port_id': 'port_id',
        'public_ip_address': 'public_ip_address',
        'private_ip_address': 'private_ip_address',
        'id': 'id',
        'allow_share_bandwidth_type_any': 'allow_share_bandwidth_type_any'
    }

    def __init__(self, marker=None, limit=None, ip_version=None, enterprise_project_id=None, port_id=None, public_ip_address=None, private_ip_address=None, id=None, allow_share_bandwidth_type_any=None):
        """ListPublicipsRequest

        The model defined in huaweicloud sdk

        :param marker: 取值为上一页数据的最后一条记录的id，为空时为查询第一页
        :type marker: str
        :param limit: 功能说明：每页返回的个数  取值范围：0~intmax
        :type limit: int
        :param ip_version: IP地址版本信息  4：IPv4  6：IPv6
        :type ip_version: int
        :param enterprise_project_id: 功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的弹性IP弹性公网IP。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的弹性公网IP，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param port_id: 绑定弹性公网IP的端口id
        :type port_id: list[str]
        :param public_ip_address: IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址
        :type public_ip_address: list[str]
        :param private_ip_address: 关联端口的私有IP地址
        :type private_ip_address: list[str]
        :param id: 弹性公网IP唯一标识
        :type id: list[str]
        :param allow_share_bandwidth_type_any: 共享带宽类型，根据任一共享带宽类型过滤EIP列表。 可以指定多个带宽类型，不同的带宽类型间用逗号分隔。
        :type allow_share_bandwidth_type_any: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._ip_version = None
        self._enterprise_project_id = None
        self._port_id = None
        self._public_ip_address = None
        self._private_ip_address = None
        self._id = None
        self._allow_share_bandwidth_type_any = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if ip_version is not None:
            self.ip_version = ip_version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if port_id is not None:
            self.port_id = port_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if id is not None:
            self.id = id
        if allow_share_bandwidth_type_any is not None:
            self.allow_share_bandwidth_type_any = allow_share_bandwidth_type_any

    @property
    def marker(self):
        """Gets the marker of this ListPublicipsRequest.

        取值为上一页数据的最后一条记录的id，为空时为查询第一页

        :return: The marker of this ListPublicipsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPublicipsRequest.

        取值为上一页数据的最后一条记录的id，为空时为查询第一页

        :param marker: The marker of this ListPublicipsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListPublicipsRequest.

        功能说明：每页返回的个数  取值范围：0~intmax

        :return: The limit of this ListPublicipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublicipsRequest.

        功能说明：每页返回的个数  取值范围：0~intmax

        :param limit: The limit of this ListPublicipsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def ip_version(self):
        """Gets the ip_version of this ListPublicipsRequest.

        IP地址版本信息  4：IPv4  6：IPv6

        :return: The ip_version of this ListPublicipsRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListPublicipsRequest.

        IP地址版本信息  4：IPv4  6：IPv6

        :param ip_version: The ip_version of this ListPublicipsRequest.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPublicipsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的弹性IP弹性公网IP。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的弹性公网IP，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListPublicipsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPublicipsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的弹性IP弹性公网IP。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的弹性公网IP，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListPublicipsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def port_id(self):
        """Gets the port_id of this ListPublicipsRequest.

        绑定弹性公网IP的端口id

        :return: The port_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this ListPublicipsRequest.

        绑定弹性公网IP的端口id

        :param port_id: The port_id of this ListPublicipsRequest.
        :type port_id: list[str]
        """
        self._port_id = port_id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this ListPublicipsRequest.

        IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址

        :return: The public_ip_address of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this ListPublicipsRequest.

        IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址

        :param public_ip_address: The public_ip_address of this ListPublicipsRequest.
        :type public_ip_address: list[str]
        """
        self._public_ip_address = public_ip_address

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this ListPublicipsRequest.

        关联端口的私有IP地址

        :return: The private_ip_address of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this ListPublicipsRequest.

        关联端口的私有IP地址

        :param private_ip_address: The private_ip_address of this ListPublicipsRequest.
        :type private_ip_address: list[str]
        """
        self._private_ip_address = private_ip_address

    @property
    def id(self):
        """Gets the id of this ListPublicipsRequest.

        弹性公网IP唯一标识

        :return: The id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPublicipsRequest.

        弹性公网IP唯一标识

        :param id: The id of this ListPublicipsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def allow_share_bandwidth_type_any(self):
        """Gets the allow_share_bandwidth_type_any of this ListPublicipsRequest.

        共享带宽类型，根据任一共享带宽类型过滤EIP列表。 可以指定多个带宽类型，不同的带宽类型间用逗号分隔。

        :return: The allow_share_bandwidth_type_any of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._allow_share_bandwidth_type_any

    @allow_share_bandwidth_type_any.setter
    def allow_share_bandwidth_type_any(self, allow_share_bandwidth_type_any):
        """Sets the allow_share_bandwidth_type_any of this ListPublicipsRequest.

        共享带宽类型，根据任一共享带宽类型过滤EIP列表。 可以指定多个带宽类型，不同的带宽类型间用逗号分隔。

        :param allow_share_bandwidth_type_any: The allow_share_bandwidth_type_any of this ListPublicipsRequest.
        :type allow_share_bandwidth_type_any: list[str]
        """
        self._allow_share_bandwidth_type_any = allow_share_bandwidth_type_any

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
        if not isinstance(other, ListPublicipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
