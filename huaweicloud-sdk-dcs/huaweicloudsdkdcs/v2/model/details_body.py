# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailsBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_capacity': 'str',
        'new_capacity': 'str',
        'enable_public_ip': 'bool',
        'public_ip_id': 'str',
        'public_ip_address': 'str',
        'enable_ssl': 'bool',
        'old_cache_mode': 'str',
        'new_cache_mode': 'str',
        'old_resource_spec_code': 'str',
        'new_resource_spec_code': 'str',
        'old_replica_num': 'int',
        'new_replica_num': 'int',
        'old_cache_type': 'str',
        'new_cache_type': 'str',
        'replica_ip': 'str',
        'replica_az': 'str',
        'group_name': 'str',
        'old_port': 'int',
        'new_port': 'int',
        'is_only_adjust_charging': 'bool',
        'account_name': 'str',
        'source_ip': 'str',
        'target_ip': 'str',
        'node_name': 'str',
        'rename_commands': 'list[str]',
        'updated_config_length': 'int'
    }

    attribute_map = {
        'old_capacity': 'old_capacity',
        'new_capacity': 'new_capacity',
        'enable_public_ip': 'enable_public_ip',
        'public_ip_id': 'public_ip_id',
        'public_ip_address': 'public_ip_address',
        'enable_ssl': 'enable_ssl',
        'old_cache_mode': 'old_cache_mode',
        'new_cache_mode': 'new_cache_mode',
        'old_resource_spec_code': 'old_resource_spec_code',
        'new_resource_spec_code': 'new_resource_spec_code',
        'old_replica_num': 'old_replica_num',
        'new_replica_num': 'new_replica_num',
        'old_cache_type': 'old_cache_type',
        'new_cache_type': 'new_cache_type',
        'replica_ip': 'replica_ip',
        'replica_az': 'replica_az',
        'group_name': 'group_name',
        'old_port': 'old_port',
        'new_port': 'new_port',
        'is_only_adjust_charging': 'is_only_adjust_charging',
        'account_name': 'account_name',
        'source_ip': 'source_ip',
        'target_ip': 'target_ip',
        'node_name': 'node_name',
        'rename_commands': 'rename_commands',
        'updated_config_length': 'updated_config_length'
    }

    def __init__(self, old_capacity=None, new_capacity=None, enable_public_ip=None, public_ip_id=None, public_ip_address=None, enable_ssl=None, old_cache_mode=None, new_cache_mode=None, old_resource_spec_code=None, new_resource_spec_code=None, old_replica_num=None, new_replica_num=None, old_cache_type=None, new_cache_type=None, replica_ip=None, replica_az=None, group_name=None, old_port=None, new_port=None, is_only_adjust_charging=None, account_name=None, source_ip=None, target_ip=None, node_name=None, rename_commands=None, updated_config_length=None):
        r"""DetailsBody

        The model defined in huaweicloud sdk

        :param old_capacity: 变更前的容量，仅在变更规格时有值。
        :type old_capacity: str
        :param new_capacity: 变更后的容量，仅在变更规格时有值。
        :type new_capacity: str
        :param enable_public_ip: 是否开启公网访问，仅在开启公网访问时有值。
        :type enable_public_ip: bool
        :param public_ip_id: 公网IP的ID，仅在开启公网访问时有值。
        :type public_ip_id: str
        :param public_ip_address: 公网IP地址，仅在开启公网访问时有值。
        :type public_ip_address: str
        :param enable_ssl: 是否开启SSL，仅在开启SSL时有值。
        :type enable_ssl: bool
        :param old_cache_mode: 变更前的缓存类型，仅在变更规格时有值。
        :type old_cache_mode: str
        :param new_cache_mode: 变更后的缓存类型，仅在变更规格时有值。
        :type new_cache_mode: str
        :param old_resource_spec_code: 变更前的规格参数，仅在变更规格时有值。
        :type old_resource_spec_code: str
        :param new_resource_spec_code: 变更后的规格参数，仅在变更规格时有值。
        :type new_resource_spec_code: str
        :param old_replica_num: 变更前的副本数量，仅在变更规格时有值。
        :type old_replica_num: int
        :param new_replica_num: 变更后的副本数量，仅在变更规格时有值。
        :type new_replica_num: int
        :param old_cache_type: 变更前的缓存类型，仅在变更规格时有值。
        :type old_cache_type: str
        :param new_cache_type: 变更后的规格类型，仅在变更规格时有值。
        :type new_cache_type: str
        :param replica_ip: 副本IP。
        :type replica_ip: str
        :param replica_az: 副本所在可用区。
        :type replica_az: str
        :param group_name: 组名。
        :type group_name: str
        :param old_port: 旧端口。
        :type old_port: int
        :param new_port: 新端口。
        :type new_port: int
        :param is_only_adjust_charging: 是否只是调整计费模式。
        :type is_only_adjust_charging: bool
        :param account_name: 账号名称。
        :type account_name: str
        :param source_ip: 源IP。
        :type source_ip: str
        :param target_ip: 目标IP。
        :type target_ip: str
        :param node_name: 节点信息。
        :type node_name: str
        :param rename_commands: 重命名的指令。
        :type rename_commands: list[str]
        :param updated_config_length: 更新配置项的长度。
        :type updated_config_length: int
        """
        
        

        self._old_capacity = None
        self._new_capacity = None
        self._enable_public_ip = None
        self._public_ip_id = None
        self._public_ip_address = None
        self._enable_ssl = None
        self._old_cache_mode = None
        self._new_cache_mode = None
        self._old_resource_spec_code = None
        self._new_resource_spec_code = None
        self._old_replica_num = None
        self._new_replica_num = None
        self._old_cache_type = None
        self._new_cache_type = None
        self._replica_ip = None
        self._replica_az = None
        self._group_name = None
        self._old_port = None
        self._new_port = None
        self._is_only_adjust_charging = None
        self._account_name = None
        self._source_ip = None
        self._target_ip = None
        self._node_name = None
        self._rename_commands = None
        self._updated_config_length = None
        self.discriminator = None

        if old_capacity is not None:
            self.old_capacity = old_capacity
        if new_capacity is not None:
            self.new_capacity = new_capacity
        if enable_public_ip is not None:
            self.enable_public_ip = enable_public_ip
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if old_cache_mode is not None:
            self.old_cache_mode = old_cache_mode
        if new_cache_mode is not None:
            self.new_cache_mode = new_cache_mode
        if old_resource_spec_code is not None:
            self.old_resource_spec_code = old_resource_spec_code
        if new_resource_spec_code is not None:
            self.new_resource_spec_code = new_resource_spec_code
        if old_replica_num is not None:
            self.old_replica_num = old_replica_num
        if new_replica_num is not None:
            self.new_replica_num = new_replica_num
        if old_cache_type is not None:
            self.old_cache_type = old_cache_type
        if new_cache_type is not None:
            self.new_cache_type = new_cache_type
        if replica_ip is not None:
            self.replica_ip = replica_ip
        if replica_az is not None:
            self.replica_az = replica_az
        if group_name is not None:
            self.group_name = group_name
        if old_port is not None:
            self.old_port = old_port
        if new_port is not None:
            self.new_port = new_port
        if is_only_adjust_charging is not None:
            self.is_only_adjust_charging = is_only_adjust_charging
        if account_name is not None:
            self.account_name = account_name
        if source_ip is not None:
            self.source_ip = source_ip
        if target_ip is not None:
            self.target_ip = target_ip
        if node_name is not None:
            self.node_name = node_name
        if rename_commands is not None:
            self.rename_commands = rename_commands
        if updated_config_length is not None:
            self.updated_config_length = updated_config_length

    @property
    def old_capacity(self):
        r"""Gets the old_capacity of this DetailsBody.

        变更前的容量，仅在变更规格时有值。

        :return: The old_capacity of this DetailsBody.
        :rtype: str
        """
        return self._old_capacity

    @old_capacity.setter
    def old_capacity(self, old_capacity):
        r"""Sets the old_capacity of this DetailsBody.

        变更前的容量，仅在变更规格时有值。

        :param old_capacity: The old_capacity of this DetailsBody.
        :type old_capacity: str
        """
        self._old_capacity = old_capacity

    @property
    def new_capacity(self):
        r"""Gets the new_capacity of this DetailsBody.

        变更后的容量，仅在变更规格时有值。

        :return: The new_capacity of this DetailsBody.
        :rtype: str
        """
        return self._new_capacity

    @new_capacity.setter
    def new_capacity(self, new_capacity):
        r"""Sets the new_capacity of this DetailsBody.

        变更后的容量，仅在变更规格时有值。

        :param new_capacity: The new_capacity of this DetailsBody.
        :type new_capacity: str
        """
        self._new_capacity = new_capacity

    @property
    def enable_public_ip(self):
        r"""Gets the enable_public_ip of this DetailsBody.

        是否开启公网访问，仅在开启公网访问时有值。

        :return: The enable_public_ip of this DetailsBody.
        :rtype: bool
        """
        return self._enable_public_ip

    @enable_public_ip.setter
    def enable_public_ip(self, enable_public_ip):
        r"""Sets the enable_public_ip of this DetailsBody.

        是否开启公网访问，仅在开启公网访问时有值。

        :param enable_public_ip: The enable_public_ip of this DetailsBody.
        :type enable_public_ip: bool
        """
        self._enable_public_ip = enable_public_ip

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this DetailsBody.

        公网IP的ID，仅在开启公网访问时有值。

        :return: The public_ip_id of this DetailsBody.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this DetailsBody.

        公网IP的ID，仅在开启公网访问时有值。

        :param public_ip_id: The public_ip_id of this DetailsBody.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def public_ip_address(self):
        r"""Gets the public_ip_address of this DetailsBody.

        公网IP地址，仅在开启公网访问时有值。

        :return: The public_ip_address of this DetailsBody.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        r"""Sets the public_ip_address of this DetailsBody.

        公网IP地址，仅在开启公网访问时有值。

        :param public_ip_address: The public_ip_address of this DetailsBody.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this DetailsBody.

        是否开启SSL，仅在开启SSL时有值。

        :return: The enable_ssl of this DetailsBody.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this DetailsBody.

        是否开启SSL，仅在开启SSL时有值。

        :param enable_ssl: The enable_ssl of this DetailsBody.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def old_cache_mode(self):
        r"""Gets the old_cache_mode of this DetailsBody.

        变更前的缓存类型，仅在变更规格时有值。

        :return: The old_cache_mode of this DetailsBody.
        :rtype: str
        """
        return self._old_cache_mode

    @old_cache_mode.setter
    def old_cache_mode(self, old_cache_mode):
        r"""Sets the old_cache_mode of this DetailsBody.

        变更前的缓存类型，仅在变更规格时有值。

        :param old_cache_mode: The old_cache_mode of this DetailsBody.
        :type old_cache_mode: str
        """
        self._old_cache_mode = old_cache_mode

    @property
    def new_cache_mode(self):
        r"""Gets the new_cache_mode of this DetailsBody.

        变更后的缓存类型，仅在变更规格时有值。

        :return: The new_cache_mode of this DetailsBody.
        :rtype: str
        """
        return self._new_cache_mode

    @new_cache_mode.setter
    def new_cache_mode(self, new_cache_mode):
        r"""Sets the new_cache_mode of this DetailsBody.

        变更后的缓存类型，仅在变更规格时有值。

        :param new_cache_mode: The new_cache_mode of this DetailsBody.
        :type new_cache_mode: str
        """
        self._new_cache_mode = new_cache_mode

    @property
    def old_resource_spec_code(self):
        r"""Gets the old_resource_spec_code of this DetailsBody.

        变更前的规格参数，仅在变更规格时有值。

        :return: The old_resource_spec_code of this DetailsBody.
        :rtype: str
        """
        return self._old_resource_spec_code

    @old_resource_spec_code.setter
    def old_resource_spec_code(self, old_resource_spec_code):
        r"""Sets the old_resource_spec_code of this DetailsBody.

        变更前的规格参数，仅在变更规格时有值。

        :param old_resource_spec_code: The old_resource_spec_code of this DetailsBody.
        :type old_resource_spec_code: str
        """
        self._old_resource_spec_code = old_resource_spec_code

    @property
    def new_resource_spec_code(self):
        r"""Gets the new_resource_spec_code of this DetailsBody.

        变更后的规格参数，仅在变更规格时有值。

        :return: The new_resource_spec_code of this DetailsBody.
        :rtype: str
        """
        return self._new_resource_spec_code

    @new_resource_spec_code.setter
    def new_resource_spec_code(self, new_resource_spec_code):
        r"""Sets the new_resource_spec_code of this DetailsBody.

        变更后的规格参数，仅在变更规格时有值。

        :param new_resource_spec_code: The new_resource_spec_code of this DetailsBody.
        :type new_resource_spec_code: str
        """
        self._new_resource_spec_code = new_resource_spec_code

    @property
    def old_replica_num(self):
        r"""Gets the old_replica_num of this DetailsBody.

        变更前的副本数量，仅在变更规格时有值。

        :return: The old_replica_num of this DetailsBody.
        :rtype: int
        """
        return self._old_replica_num

    @old_replica_num.setter
    def old_replica_num(self, old_replica_num):
        r"""Sets the old_replica_num of this DetailsBody.

        变更前的副本数量，仅在变更规格时有值。

        :param old_replica_num: The old_replica_num of this DetailsBody.
        :type old_replica_num: int
        """
        self._old_replica_num = old_replica_num

    @property
    def new_replica_num(self):
        r"""Gets the new_replica_num of this DetailsBody.

        变更后的副本数量，仅在变更规格时有值。

        :return: The new_replica_num of this DetailsBody.
        :rtype: int
        """
        return self._new_replica_num

    @new_replica_num.setter
    def new_replica_num(self, new_replica_num):
        r"""Sets the new_replica_num of this DetailsBody.

        变更后的副本数量，仅在变更规格时有值。

        :param new_replica_num: The new_replica_num of this DetailsBody.
        :type new_replica_num: int
        """
        self._new_replica_num = new_replica_num

    @property
    def old_cache_type(self):
        r"""Gets the old_cache_type of this DetailsBody.

        变更前的缓存类型，仅在变更规格时有值。

        :return: The old_cache_type of this DetailsBody.
        :rtype: str
        """
        return self._old_cache_type

    @old_cache_type.setter
    def old_cache_type(self, old_cache_type):
        r"""Sets the old_cache_type of this DetailsBody.

        变更前的缓存类型，仅在变更规格时有值。

        :param old_cache_type: The old_cache_type of this DetailsBody.
        :type old_cache_type: str
        """
        self._old_cache_type = old_cache_type

    @property
    def new_cache_type(self):
        r"""Gets the new_cache_type of this DetailsBody.

        变更后的规格类型，仅在变更规格时有值。

        :return: The new_cache_type of this DetailsBody.
        :rtype: str
        """
        return self._new_cache_type

    @new_cache_type.setter
    def new_cache_type(self, new_cache_type):
        r"""Sets the new_cache_type of this DetailsBody.

        变更后的规格类型，仅在变更规格时有值。

        :param new_cache_type: The new_cache_type of this DetailsBody.
        :type new_cache_type: str
        """
        self._new_cache_type = new_cache_type

    @property
    def replica_ip(self):
        r"""Gets the replica_ip of this DetailsBody.

        副本IP。

        :return: The replica_ip of this DetailsBody.
        :rtype: str
        """
        return self._replica_ip

    @replica_ip.setter
    def replica_ip(self, replica_ip):
        r"""Sets the replica_ip of this DetailsBody.

        副本IP。

        :param replica_ip: The replica_ip of this DetailsBody.
        :type replica_ip: str
        """
        self._replica_ip = replica_ip

    @property
    def replica_az(self):
        r"""Gets the replica_az of this DetailsBody.

        副本所在可用区。

        :return: The replica_az of this DetailsBody.
        :rtype: str
        """
        return self._replica_az

    @replica_az.setter
    def replica_az(self, replica_az):
        r"""Sets the replica_az of this DetailsBody.

        副本所在可用区。

        :param replica_az: The replica_az of this DetailsBody.
        :type replica_az: str
        """
        self._replica_az = replica_az

    @property
    def group_name(self):
        r"""Gets the group_name of this DetailsBody.

        组名。

        :return: The group_name of this DetailsBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this DetailsBody.

        组名。

        :param group_name: The group_name of this DetailsBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def old_port(self):
        r"""Gets the old_port of this DetailsBody.

        旧端口。

        :return: The old_port of this DetailsBody.
        :rtype: int
        """
        return self._old_port

    @old_port.setter
    def old_port(self, old_port):
        r"""Sets the old_port of this DetailsBody.

        旧端口。

        :param old_port: The old_port of this DetailsBody.
        :type old_port: int
        """
        self._old_port = old_port

    @property
    def new_port(self):
        r"""Gets the new_port of this DetailsBody.

        新端口。

        :return: The new_port of this DetailsBody.
        :rtype: int
        """
        return self._new_port

    @new_port.setter
    def new_port(self, new_port):
        r"""Sets the new_port of this DetailsBody.

        新端口。

        :param new_port: The new_port of this DetailsBody.
        :type new_port: int
        """
        self._new_port = new_port

    @property
    def is_only_adjust_charging(self):
        r"""Gets the is_only_adjust_charging of this DetailsBody.

        是否只是调整计费模式。

        :return: The is_only_adjust_charging of this DetailsBody.
        :rtype: bool
        """
        return self._is_only_adjust_charging

    @is_only_adjust_charging.setter
    def is_only_adjust_charging(self, is_only_adjust_charging):
        r"""Sets the is_only_adjust_charging of this DetailsBody.

        是否只是调整计费模式。

        :param is_only_adjust_charging: The is_only_adjust_charging of this DetailsBody.
        :type is_only_adjust_charging: bool
        """
        self._is_only_adjust_charging = is_only_adjust_charging

    @property
    def account_name(self):
        r"""Gets the account_name of this DetailsBody.

        账号名称。

        :return: The account_name of this DetailsBody.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this DetailsBody.

        账号名称。

        :param account_name: The account_name of this DetailsBody.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def source_ip(self):
        r"""Gets the source_ip of this DetailsBody.

        源IP。

        :return: The source_ip of this DetailsBody.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        r"""Sets the source_ip of this DetailsBody.

        源IP。

        :param source_ip: The source_ip of this DetailsBody.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def target_ip(self):
        r"""Gets the target_ip of this DetailsBody.

        目标IP。

        :return: The target_ip of this DetailsBody.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        r"""Sets the target_ip of this DetailsBody.

        目标IP。

        :param target_ip: The target_ip of this DetailsBody.
        :type target_ip: str
        """
        self._target_ip = target_ip

    @property
    def node_name(self):
        r"""Gets the node_name of this DetailsBody.

        节点信息。

        :return: The node_name of this DetailsBody.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this DetailsBody.

        节点信息。

        :param node_name: The node_name of this DetailsBody.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def rename_commands(self):
        r"""Gets the rename_commands of this DetailsBody.

        重命名的指令。

        :return: The rename_commands of this DetailsBody.
        :rtype: list[str]
        """
        return self._rename_commands

    @rename_commands.setter
    def rename_commands(self, rename_commands):
        r"""Sets the rename_commands of this DetailsBody.

        重命名的指令。

        :param rename_commands: The rename_commands of this DetailsBody.
        :type rename_commands: list[str]
        """
        self._rename_commands = rename_commands

    @property
    def updated_config_length(self):
        r"""Gets the updated_config_length of this DetailsBody.

        更新配置项的长度。

        :return: The updated_config_length of this DetailsBody.
        :rtype: int
        """
        return self._updated_config_length

    @updated_config_length.setter
    def updated_config_length(self, updated_config_length):
        r"""Sets the updated_config_length of this DetailsBody.

        更新配置项的长度。

        :param updated_config_length: The updated_config_length of this DetailsBody.
        :type updated_config_length: int
        """
        self._updated_config_length = updated_config_length

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
        if not isinstance(other, DetailsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
