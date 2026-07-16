# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SfsTurboConnectionStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sfs_id': 'str',
        'connection_type': 'str',
        'ip_addr': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'sfs_id': 'sfsId',
        'connection_type': 'connectionType',
        'ip_addr': 'ipAddr',
        'status': 'status'
    }

    def __init__(self, name=None, sfs_id=None, connection_type=None, ip_addr=None, status=None):
        r"""SfsTurboConnectionStatus

        The model defined in huaweicloud sdk

        :param name: **参数解释**：sfsTurbo实例的名称。 **取值范围**：不涉及。
        :type name: str
        :param sfs_id: **参数解释**：sfsTurbo实例的ID。 **取值范围**：不涉及。
        :type sfs_id: str
        :param connection_type: **参数解释**：关联方式。 **取值范围**：可选值如下： - VpcPort：通过挂载网卡直通 - Peering：通过对等连接打通
        :type connection_type: str
        :param ip_addr: **参数解释**：SFS Turbo的访问地址。 **取值范围**：不涉及。
        :type ip_addr: str
        :param status: **参数解释**：与SFS Turbo的连接状态信息。 **取值范围**：可选值如下： - Active：SFS连通状态正常 - Abnormal：SFS连通状态异常 - Creating：SFS连通状态创建关联中 - Deleting：SFS连通状态解除关联中
        :type status: str
        """
        
        

        self._name = None
        self._sfs_id = None
        self._connection_type = None
        self._ip_addr = None
        self._status = None
        self.discriminator = None

        self.name = name
        self.sfs_id = sfs_id
        self.connection_type = connection_type
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this SfsTurboConnectionStatus.

        **参数解释**：sfsTurbo实例的名称。 **取值范围**：不涉及。

        :return: The name of this SfsTurboConnectionStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SfsTurboConnectionStatus.

        **参数解释**：sfsTurbo实例的名称。 **取值范围**：不涉及。

        :param name: The name of this SfsTurboConnectionStatus.
        :type name: str
        """
        self._name = name

    @property
    def sfs_id(self):
        r"""Gets the sfs_id of this SfsTurboConnectionStatus.

        **参数解释**：sfsTurbo实例的ID。 **取值范围**：不涉及。

        :return: The sfs_id of this SfsTurboConnectionStatus.
        :rtype: str
        """
        return self._sfs_id

    @sfs_id.setter
    def sfs_id(self, sfs_id):
        r"""Sets the sfs_id of this SfsTurboConnectionStatus.

        **参数解释**：sfsTurbo实例的ID。 **取值范围**：不涉及。

        :param sfs_id: The sfs_id of this SfsTurboConnectionStatus.
        :type sfs_id: str
        """
        self._sfs_id = sfs_id

    @property
    def connection_type(self):
        r"""Gets the connection_type of this SfsTurboConnectionStatus.

        **参数解释**：关联方式。 **取值范围**：可选值如下： - VpcPort：通过挂载网卡直通 - Peering：通过对等连接打通

        :return: The connection_type of this SfsTurboConnectionStatus.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this SfsTurboConnectionStatus.

        **参数解释**：关联方式。 **取值范围**：可选值如下： - VpcPort：通过挂载网卡直通 - Peering：通过对等连接打通

        :param connection_type: The connection_type of this SfsTurboConnectionStatus.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this SfsTurboConnectionStatus.

        **参数解释**：SFS Turbo的访问地址。 **取值范围**：不涉及。

        :return: The ip_addr of this SfsTurboConnectionStatus.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this SfsTurboConnectionStatus.

        **参数解释**：SFS Turbo的访问地址。 **取值范围**：不涉及。

        :param ip_addr: The ip_addr of this SfsTurboConnectionStatus.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def status(self):
        r"""Gets the status of this SfsTurboConnectionStatus.

        **参数解释**：与SFS Turbo的连接状态信息。 **取值范围**：可选值如下： - Active：SFS连通状态正常 - Abnormal：SFS连通状态异常 - Creating：SFS连通状态创建关联中 - Deleting：SFS连通状态解除关联中

        :return: The status of this SfsTurboConnectionStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SfsTurboConnectionStatus.

        **参数解释**：与SFS Turbo的连接状态信息。 **取值范围**：可选值如下： - Active：SFS连通状态正常 - Abnormal：SFS连通状态异常 - Creating：SFS连通状态创建关联中 - Deleting：SFS连通状态解除关联中

        :param status: The status of this SfsTurboConnectionStatus.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, SfsTurboConnectionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
