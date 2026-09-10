# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peer_id': 'str',
        'status': 'str',
        'name': 'str',
        'err_msg': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'peer_id': 'peer_id',
        'status': 'status',
        'name': 'name',
        'err_msg': 'err_msg',
        'update_time': 'update_time'
    }

    def __init__(self, peer_id=None, status=None, name=None, err_msg=None, update_time=None):
        r"""ConnectionClusterInfo

        The model defined in huaweicloud sdk

        :param peer_id: 对等连接ID。
        :type peer_id: str
        :param status: 连接状态。 CREATING：资源组网络连接正在创建中； ACTIVE：资源组网络连接创建成功，与目的地址连接正常； FAILED：资源组网络连接创建失败。
        :type status: str
        :param name: 集群名称。
        :type name: str
        :param err_msg: 状态为失败时的详细报错信息。
        :type err_msg: str
        :param update_time: 更新时间。
        :type update_time: int
        """
        
        

        self._peer_id = None
        self._status = None
        self._name = None
        self._err_msg = None
        self._update_time = None
        self.discriminator = None

        if peer_id is not None:
            self.peer_id = peer_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if err_msg is not None:
            self.err_msg = err_msg
        if update_time is not None:
            self.update_time = update_time

    @property
    def peer_id(self):
        r"""Gets the peer_id of this ConnectionClusterInfo.

        对等连接ID。

        :return: The peer_id of this ConnectionClusterInfo.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        r"""Sets the peer_id of this ConnectionClusterInfo.

        对等连接ID。

        :param peer_id: The peer_id of this ConnectionClusterInfo.
        :type peer_id: str
        """
        self._peer_id = peer_id

    @property
    def status(self):
        r"""Gets the status of this ConnectionClusterInfo.

        连接状态。 CREATING：资源组网络连接正在创建中； ACTIVE：资源组网络连接创建成功，与目的地址连接正常； FAILED：资源组网络连接创建失败。

        :return: The status of this ConnectionClusterInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConnectionClusterInfo.

        连接状态。 CREATING：资源组网络连接正在创建中； ACTIVE：资源组网络连接创建成功，与目的地址连接正常； FAILED：资源组网络连接创建失败。

        :param status: The status of this ConnectionClusterInfo.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ConnectionClusterInfo.

        集群名称。

        :return: The name of this ConnectionClusterInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConnectionClusterInfo.

        集群名称。

        :param name: The name of this ConnectionClusterInfo.
        :type name: str
        """
        self._name = name

    @property
    def err_msg(self):
        r"""Gets the err_msg of this ConnectionClusterInfo.

        状态为失败时的详细报错信息。

        :return: The err_msg of this ConnectionClusterInfo.
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        r"""Sets the err_msg of this ConnectionClusterInfo.

        状态为失败时的详细报错信息。

        :param err_msg: The err_msg of this ConnectionClusterInfo.
        :type err_msg: str
        """
        self._err_msg = err_msg

    @property
    def update_time(self):
        r"""Gets the update_time of this ConnectionClusterInfo.

        更新时间。

        :return: The update_time of this ConnectionClusterInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ConnectionClusterInfo.

        更新时间。

        :param update_time: The update_time of this ConnectionClusterInfo.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectionClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
