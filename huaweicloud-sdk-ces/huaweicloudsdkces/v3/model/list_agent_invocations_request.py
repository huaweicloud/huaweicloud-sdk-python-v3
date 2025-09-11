# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentInvocationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_type': 'str',
        'invocation_id': 'str',
        'invocation_type': 'str',
        'invocation_target': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'invocation_id': 'invocation_id',
        'invocation_type': 'invocation_type',
        'invocation_target': 'invocation_target',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, instance_type=None, invocation_id=None, invocation_type=None, invocation_target=None, offset=None, limit=None):
        r"""ListAgentInvocationsRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 **默认取值**: 不涉及 
        :type instance_id: str
        :param instance_type: **参数解释**: 主机类型，仅支持ECS弹性云服务器和BMS裸金属服务器 **约束限制**: 不涉及 **取值范围**: - ECS: 弹性云服务器 - BMS：裸金属服务器 **默认取值**: 不涉及 
        :type instance_type: str
        :param invocation_id: **参数解释**: 任务id **约束限制**: 不涉及 **取值范围**: 以字母或数字开头，后续可包含字母、数字、下划线或连字符的字符串，长度至少为 1 **默认取值**: 不涉及 
        :type invocation_id: str
        :param invocation_type: **参数解释**: 任务类型, 仅包含：INSTALL安装, UPDATE升级, ROLLBACK回退，RETRY重试，SET_REMOTE_INSTALLER设置远程安装主机，REMOTE_INSTALL执行远程安装。 **约束限制**: 不涉及。 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回退 - RETRY：重试 - SET_REMOTE_INSTALLER：设置远程安装主机 - REMOTE_INSTALL：执行远程安装 **默认取值**: 不涉及 
        :type invocation_type: str
        :param invocation_target: **参数解释**: 任务对象, 支持telescope监控 **约束限制**: 不涉及。 **取值范围**: - telescope: 主机监控插件telescope **默认取值**: telescope。 
        :type invocation_target: str
        :param offset: **参数解释**: 分页偏移量 **约束限制**: 不涉及 **取值范围**: 数字范围为[0,9999999999999] **默认取值**: 0 
        :type offset: int
        :param limit: **参数解释**: 分页大小。 **约束限制**: 不涉及。 **取值范围**: 数字范围为[1,100] **默认取值**: 100 
        :type limit: int
        """
        
        

        self._instance_id = None
        self._instance_type = None
        self._invocation_id = None
        self._invocation_type = None
        self._invocation_target = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if invocation_id is not None:
            self.invocation_id = invocation_id
        if invocation_type is not None:
            self.invocation_type = invocation_type
        if invocation_target is not None:
            self.invocation_target = invocation_target
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAgentInvocationsRequest.

        **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 **默认取值**: 不涉及 

        :return: The instance_id of this ListAgentInvocationsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAgentInvocationsRequest.

        **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 **默认取值**: 不涉及 

        :param instance_id: The instance_id of this ListAgentInvocationsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ListAgentInvocationsRequest.

        **参数解释**: 主机类型，仅支持ECS弹性云服务器和BMS裸金属服务器 **约束限制**: 不涉及 **取值范围**: - ECS: 弹性云服务器 - BMS：裸金属服务器 **默认取值**: 不涉及 

        :return: The instance_type of this ListAgentInvocationsRequest.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ListAgentInvocationsRequest.

        **参数解释**: 主机类型，仅支持ECS弹性云服务器和BMS裸金属服务器 **约束限制**: 不涉及 **取值范围**: - ECS: 弹性云服务器 - BMS：裸金属服务器 **默认取值**: 不涉及 

        :param instance_type: The instance_type of this ListAgentInvocationsRequest.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def invocation_id(self):
        r"""Gets the invocation_id of this ListAgentInvocationsRequest.

        **参数解释**: 任务id **约束限制**: 不涉及 **取值范围**: 以字母或数字开头，后续可包含字母、数字、下划线或连字符的字符串，长度至少为 1 **默认取值**: 不涉及 

        :return: The invocation_id of this ListAgentInvocationsRequest.
        :rtype: str
        """
        return self._invocation_id

    @invocation_id.setter
    def invocation_id(self, invocation_id):
        r"""Sets the invocation_id of this ListAgentInvocationsRequest.

        **参数解释**: 任务id **约束限制**: 不涉及 **取值范围**: 以字母或数字开头，后续可包含字母、数字、下划线或连字符的字符串，长度至少为 1 **默认取值**: 不涉及 

        :param invocation_id: The invocation_id of this ListAgentInvocationsRequest.
        :type invocation_id: str
        """
        self._invocation_id = invocation_id

    @property
    def invocation_type(self):
        r"""Gets the invocation_type of this ListAgentInvocationsRequest.

        **参数解释**: 任务类型, 仅包含：INSTALL安装, UPDATE升级, ROLLBACK回退，RETRY重试，SET_REMOTE_INSTALLER设置远程安装主机，REMOTE_INSTALL执行远程安装。 **约束限制**: 不涉及。 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回退 - RETRY：重试 - SET_REMOTE_INSTALLER：设置远程安装主机 - REMOTE_INSTALL：执行远程安装 **默认取值**: 不涉及 

        :return: The invocation_type of this ListAgentInvocationsRequest.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        r"""Sets the invocation_type of this ListAgentInvocationsRequest.

        **参数解释**: 任务类型, 仅包含：INSTALL安装, UPDATE升级, ROLLBACK回退，RETRY重试，SET_REMOTE_INSTALLER设置远程安装主机，REMOTE_INSTALL执行远程安装。 **约束限制**: 不涉及。 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回退 - RETRY：重试 - SET_REMOTE_INSTALLER：设置远程安装主机 - REMOTE_INSTALL：执行远程安装 **默认取值**: 不涉及 

        :param invocation_type: The invocation_type of this ListAgentInvocationsRequest.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def invocation_target(self):
        r"""Gets the invocation_target of this ListAgentInvocationsRequest.

        **参数解释**: 任务对象, 支持telescope监控 **约束限制**: 不涉及。 **取值范围**: - telescope: 主机监控插件telescope **默认取值**: telescope。 

        :return: The invocation_target of this ListAgentInvocationsRequest.
        :rtype: str
        """
        return self._invocation_target

    @invocation_target.setter
    def invocation_target(self, invocation_target):
        r"""Sets the invocation_target of this ListAgentInvocationsRequest.

        **参数解释**: 任务对象, 支持telescope监控 **约束限制**: 不涉及。 **取值范围**: - telescope: 主机监控插件telescope **默认取值**: telescope。 

        :param invocation_target: The invocation_target of this ListAgentInvocationsRequest.
        :type invocation_target: str
        """
        self._invocation_target = invocation_target

    @property
    def offset(self):
        r"""Gets the offset of this ListAgentInvocationsRequest.

        **参数解释**: 分页偏移量 **约束限制**: 不涉及 **取值范围**: 数字范围为[0,9999999999999] **默认取值**: 0 

        :return: The offset of this ListAgentInvocationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAgentInvocationsRequest.

        **参数解释**: 分页偏移量 **约束限制**: 不涉及 **取值范围**: 数字范围为[0,9999999999999] **默认取值**: 0 

        :param offset: The offset of this ListAgentInvocationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAgentInvocationsRequest.

        **参数解释**: 分页大小。 **约束限制**: 不涉及。 **取值范围**: 数字范围为[1,100] **默认取值**: 100 

        :return: The limit of this ListAgentInvocationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAgentInvocationsRequest.

        **参数解释**: 分页大小。 **约束限制**: 不涉及。 **取值范围**: 数字范围为[1,100] **默认取值**: 100 

        :param limit: The limit of this ListAgentInvocationsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAgentInvocationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
