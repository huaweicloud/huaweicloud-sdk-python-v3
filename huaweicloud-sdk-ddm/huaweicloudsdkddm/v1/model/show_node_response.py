# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'name': 'str',
        'node_id': 'str',
        'private_ip': 'str',
        'floating_ip': 'str',
        'server_id': 'str',
        'subnet_name': 'str',
        'datavolume_id': 'str',
        'res_subnet_ip': 'str',
        'systemvolume_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'name': 'name',
        'node_id': 'node_id',
        'private_ip': 'private_ip',
        'floating_ip': 'floating_ip',
        'server_id': 'server_id',
        'subnet_name': 'subnet_name',
        'datavolume_id': 'datavolume_id',
        'res_subnet_ip': 'res_subnet_ip',
        'systemvolume_id': 'systemvolume_id'
    }

    def __init__(self, status=None, name=None, node_id=None, private_ip=None, floating_ip=None, server_id=None, subnet_name=None, datavolume_id=None, res_subnet_ip=None, systemvolume_id=None):
        r"""ShowNodeResponse

        The model defined in huaweicloud sdk

        :param status: 节点状态。
        :type status: str
        :param name: 节点名称。
        :type name: str
        :param node_id: 节点id。
        :type node_id: str
        :param private_ip: 节点私有ip。
        :type private_ip: str
        :param floating_ip: 节点浮动ip。
        :type floating_ip: str
        :param server_id: 虚机id。
        :type server_id: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param datavolume_id: 数据盘id。
        :type datavolume_id: str
        :param res_subnet_ip: 资源子网ip。
        :type res_subnet_ip: str
        :param systemvolume_id: 系统盘id。
        :type systemvolume_id: str
        """
        
        super(ShowNodeResponse, self).__init__()

        self._status = None
        self._name = None
        self._node_id = None
        self._private_ip = None
        self._floating_ip = None
        self._server_id = None
        self._subnet_name = None
        self._datavolume_id = None
        self._res_subnet_ip = None
        self._systemvolume_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if private_ip is not None:
            self.private_ip = private_ip
        if floating_ip is not None:
            self.floating_ip = floating_ip
        if server_id is not None:
            self.server_id = server_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if datavolume_id is not None:
            self.datavolume_id = datavolume_id
        if res_subnet_ip is not None:
            self.res_subnet_ip = res_subnet_ip
        if systemvolume_id is not None:
            self.systemvolume_id = systemvolume_id

    @property
    def status(self):
        r"""Gets the status of this ShowNodeResponse.

        节点状态。

        :return: The status of this ShowNodeResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowNodeResponse.

        节点状态。

        :param status: The status of this ShowNodeResponse.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ShowNodeResponse.

        节点名称。

        :return: The name of this ShowNodeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowNodeResponse.

        节点名称。

        :param name: The name of this ShowNodeResponse.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowNodeResponse.

        节点id。

        :return: The node_id of this ShowNodeResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowNodeResponse.

        节点id。

        :param node_id: The node_id of this ShowNodeResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ShowNodeResponse.

        节点私有ip。

        :return: The private_ip of this ShowNodeResponse.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ShowNodeResponse.

        节点私有ip。

        :param private_ip: The private_ip of this ShowNodeResponse.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def floating_ip(self):
        r"""Gets the floating_ip of this ShowNodeResponse.

        节点浮动ip。

        :return: The floating_ip of this ShowNodeResponse.
        :rtype: str
        """
        return self._floating_ip

    @floating_ip.setter
    def floating_ip(self, floating_ip):
        r"""Sets the floating_ip of this ShowNodeResponse.

        节点浮动ip。

        :param floating_ip: The floating_ip of this ShowNodeResponse.
        :type floating_ip: str
        """
        self._floating_ip = floating_ip

    @property
    def server_id(self):
        r"""Gets the server_id of this ShowNodeResponse.

        虚机id。

        :return: The server_id of this ShowNodeResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ShowNodeResponse.

        虚机id。

        :param server_id: The server_id of this ShowNodeResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this ShowNodeResponse.

        子网名称。

        :return: The subnet_name of this ShowNodeResponse.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this ShowNodeResponse.

        子网名称。

        :param subnet_name: The subnet_name of this ShowNodeResponse.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def datavolume_id(self):
        r"""Gets the datavolume_id of this ShowNodeResponse.

        数据盘id。

        :return: The datavolume_id of this ShowNodeResponse.
        :rtype: str
        """
        return self._datavolume_id

    @datavolume_id.setter
    def datavolume_id(self, datavolume_id):
        r"""Sets the datavolume_id of this ShowNodeResponse.

        数据盘id。

        :param datavolume_id: The datavolume_id of this ShowNodeResponse.
        :type datavolume_id: str
        """
        self._datavolume_id = datavolume_id

    @property
    def res_subnet_ip(self):
        r"""Gets the res_subnet_ip of this ShowNodeResponse.

        资源子网ip。

        :return: The res_subnet_ip of this ShowNodeResponse.
        :rtype: str
        """
        return self._res_subnet_ip

    @res_subnet_ip.setter
    def res_subnet_ip(self, res_subnet_ip):
        r"""Sets the res_subnet_ip of this ShowNodeResponse.

        资源子网ip。

        :param res_subnet_ip: The res_subnet_ip of this ShowNodeResponse.
        :type res_subnet_ip: str
        """
        self._res_subnet_ip = res_subnet_ip

    @property
    def systemvolume_id(self):
        r"""Gets the systemvolume_id of this ShowNodeResponse.

        系统盘id。

        :return: The systemvolume_id of this ShowNodeResponse.
        :rtype: str
        """
        return self._systemvolume_id

    @systemvolume_id.setter
    def systemvolume_id(self, systemvolume_id):
        r"""Sets the systemvolume_id of this ShowNodeResponse.

        系统盘id。

        :param systemvolume_id: The systemvolume_id of this ShowNodeResponse.
        :type systemvolume_id: str
        """
        self._systemvolume_id = systemvolume_id

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
        if not isinstance(other, ShowNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
