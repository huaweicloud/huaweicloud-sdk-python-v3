# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'server_name': 'str',
        'server_type': 'str',
        'data_volumes': 'list[VolumeInfo]',
        'root_volume': 'VolumeInfo',
        'cpu_type': 'str',
        'cpu': 'str',
        'mem': 'str',
        'internal_ip': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'server_name': 'server_name',
        'server_type': 'server_type',
        'data_volumes': 'data_volumes',
        'root_volume': 'root_volume',
        'cpu_type': 'cpu_type',
        'cpu': 'cpu',
        'mem': 'mem',
        'internal_ip': 'internal_ip'
    }

    def __init__(self, server_id=None, server_name=None, server_type=None, data_volumes=None, root_volume=None, cpu_type=None, cpu=None, mem=None, internal_ip=None):
        r"""ServerInfo

        The model defined in huaweicloud sdk

        :param server_id: 服务器ID。
        :type server_id: str
        :param server_name: 服务器名称。
        :type server_name: str
        :param server_type: ECS或者BMS。
        :type server_type: str
        :param data_volumes: 数据盘。
        :type data_volumes: list[:class:`huaweicloudsdkmrs.v2.VolumeInfo`]
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkmrs.v2.VolumeInfo`
        :param cpu_type: CPU类型。x86或者ARM。
        :type cpu_type: str
        :param cpu: CPU大小。
        :type cpu: str
        :param mem: 内存大小。
        :type mem: str
        :param internal_ip: 内部IP。
        :type internal_ip: str
        """
        
        

        self._server_id = None
        self._server_name = None
        self._server_type = None
        self._data_volumes = None
        self._root_volume = None
        self._cpu_type = None
        self._cpu = None
        self._mem = None
        self._internal_ip = None
        self.discriminator = None

        self.server_id = server_id
        self.server_name = server_name
        self.server_type = server_type
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if root_volume is not None:
            self.root_volume = root_volume
        if cpu_type is not None:
            self.cpu_type = cpu_type
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if internal_ip is not None:
            self.internal_ip = internal_ip

    @property
    def server_id(self):
        r"""Gets the server_id of this ServerInfo.

        服务器ID。

        :return: The server_id of this ServerInfo.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ServerInfo.

        服务器ID。

        :param server_id: The server_id of this ServerInfo.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_name(self):
        r"""Gets the server_name of this ServerInfo.

        服务器名称。

        :return: The server_name of this ServerInfo.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ServerInfo.

        服务器名称。

        :param server_name: The server_name of this ServerInfo.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_type(self):
        r"""Gets the server_type of this ServerInfo.

        ECS或者BMS。

        :return: The server_type of this ServerInfo.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServerInfo.

        ECS或者BMS。

        :param server_type: The server_type of this ServerInfo.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this ServerInfo.

        数据盘。

        :return: The data_volumes of this ServerInfo.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.VolumeInfo`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this ServerInfo.

        数据盘。

        :param data_volumes: The data_volumes of this ServerInfo.
        :type data_volumes: list[:class:`huaweicloudsdkmrs.v2.VolumeInfo`]
        """
        self._data_volumes = data_volumes

    @property
    def root_volume(self):
        r"""Gets the root_volume of this ServerInfo.

        :return: The root_volume of this ServerInfo.
        :rtype: :class:`huaweicloudsdkmrs.v2.VolumeInfo`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this ServerInfo.

        :param root_volume: The root_volume of this ServerInfo.
        :type root_volume: :class:`huaweicloudsdkmrs.v2.VolumeInfo`
        """
        self._root_volume = root_volume

    @property
    def cpu_type(self):
        r"""Gets the cpu_type of this ServerInfo.

        CPU类型。x86或者ARM。

        :return: The cpu_type of this ServerInfo.
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        r"""Sets the cpu_type of this ServerInfo.

        CPU类型。x86或者ARM。

        :param cpu_type: The cpu_type of this ServerInfo.
        :type cpu_type: str
        """
        self._cpu_type = cpu_type

    @property
    def cpu(self):
        r"""Gets the cpu of this ServerInfo.

        CPU大小。

        :return: The cpu of this ServerInfo.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ServerInfo.

        CPU大小。

        :param cpu: The cpu of this ServerInfo.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this ServerInfo.

        内存大小。

        :return: The mem of this ServerInfo.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this ServerInfo.

        内存大小。

        :param mem: The mem of this ServerInfo.
        :type mem: str
        """
        self._mem = mem

    @property
    def internal_ip(self):
        r"""Gets the internal_ip of this ServerInfo.

        内部IP。

        :return: The internal_ip of this ServerInfo.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        r"""Sets the internal_ip of this ServerInfo.

        内部IP。

        :param internal_ip: The internal_ip of this ServerInfo.
        :type internal_ip: str
        """
        self._internal_ip = internal_ip

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
        if not isinstance(other, ServerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
