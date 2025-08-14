# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'server_group_id': 'str',
        'server_name': 'str',
        'machine_name': 'str',
        'ip_addr': 'str',
        'server_id': 'str',
        'maintain_status': 'str',
        'scaling_auto_create': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'server_group_id': 'server_group_id',
        'server_name': 'server_name',
        'machine_name': 'machine_name',
        'ip_addr': 'ip_addr',
        'server_id': 'server_id',
        'maintain_status': 'maintain_status',
        'scaling_auto_create': 'scaling_auto_create'
    }

    def __init__(self, offset=None, limit=None, server_group_id=None, server_name=None, machine_name=None, ip_addr=None, server_id=None, maintain_status=None, scaling_auto_create=None):
        r"""ListServersRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]，默认值10。
        :type limit: int
        :param server_group_id: 服务器组唯一标识。
        :type server_group_id: str
        :param server_name: 服务器名称，支持部分匹配。
        :type server_name: str
        :param machine_name: 机器名称，支持部分匹配。
        :type machine_name: str
        :param ip_addr: ip地址，支持部分匹配。
        :type ip_addr: str
        :param server_id: 服务器唯一标识。
        :type server_id: str
        :param maintain_status: 服务器维护状态： - true : 维护态的实例。 - false: 非维护态的实例。
        :type maintain_status: str
        :param scaling_auto_create: 是否是弹性创建： true : 通过弹性伸缩创建。 false: 不是通过弹性伸缩创建。
        :type scaling_auto_create: str
        """
        
        

        self._offset = None
        self._limit = None
        self._server_group_id = None
        self._server_name = None
        self._machine_name = None
        self._ip_addr = None
        self._server_id = None
        self._maintain_status = None
        self._scaling_auto_create = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if server_name is not None:
            self.server_name = server_name
        if machine_name is not None:
            self.machine_name = machine_name
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if server_id is not None:
            self.server_id = server_id
        if maintain_status is not None:
            self.maintain_status = maintain_status
        if scaling_auto_create is not None:
            self.scaling_auto_create = scaling_auto_create

    @property
    def offset(self):
        r"""Gets the offset of this ListServersRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListServersRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListServersRequest.

        查询的数量，值区间[1-100]，默认值10。

        :return: The limit of this ListServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServersRequest.

        查询的数量，值区间[1-100]，默认值10。

        :param limit: The limit of this ListServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this ListServersRequest.

        服务器组唯一标识。

        :return: The server_group_id of this ListServersRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this ListServersRequest.

        服务器组唯一标识。

        :param server_group_id: The server_group_id of this ListServersRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def server_name(self):
        r"""Gets the server_name of this ListServersRequest.

        服务器名称，支持部分匹配。

        :return: The server_name of this ListServersRequest.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ListServersRequest.

        服务器名称，支持部分匹配。

        :param server_name: The server_name of this ListServersRequest.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def machine_name(self):
        r"""Gets the machine_name of this ListServersRequest.

        机器名称，支持部分匹配。

        :return: The machine_name of this ListServersRequest.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        r"""Sets the machine_name of this ListServersRequest.

        机器名称，支持部分匹配。

        :param machine_name: The machine_name of this ListServersRequest.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this ListServersRequest.

        ip地址，支持部分匹配。

        :return: The ip_addr of this ListServersRequest.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this ListServersRequest.

        ip地址，支持部分匹配。

        :param ip_addr: The ip_addr of this ListServersRequest.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def server_id(self):
        r"""Gets the server_id of this ListServersRequest.

        服务器唯一标识。

        :return: The server_id of this ListServersRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListServersRequest.

        服务器唯一标识。

        :param server_id: The server_id of this ListServersRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def maintain_status(self):
        r"""Gets the maintain_status of this ListServersRequest.

        服务器维护状态： - true : 维护态的实例。 - false: 非维护态的实例。

        :return: The maintain_status of this ListServersRequest.
        :rtype: str
        """
        return self._maintain_status

    @maintain_status.setter
    def maintain_status(self, maintain_status):
        r"""Sets the maintain_status of this ListServersRequest.

        服务器维护状态： - true : 维护态的实例。 - false: 非维护态的实例。

        :param maintain_status: The maintain_status of this ListServersRequest.
        :type maintain_status: str
        """
        self._maintain_status = maintain_status

    @property
    def scaling_auto_create(self):
        r"""Gets the scaling_auto_create of this ListServersRequest.

        是否是弹性创建： true : 通过弹性伸缩创建。 false: 不是通过弹性伸缩创建。

        :return: The scaling_auto_create of this ListServersRequest.
        :rtype: str
        """
        return self._scaling_auto_create

    @scaling_auto_create.setter
    def scaling_auto_create(self, scaling_auto_create):
        r"""Sets the scaling_auto_create of this ListServersRequest.

        是否是弹性创建： true : 通过弹性伸缩创建。 false: 不是通过弹性伸缩创建。

        :param scaling_auto_create: The scaling_auto_create of this ListServersRequest.
        :type scaling_auto_create: str
        """
        self._scaling_auto_create = scaling_auto_create

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
        if not isinstance(other, ListServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
