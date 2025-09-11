# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentStatusInfo:

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
        'uniagent_status': 'str',
        'extensions': 'list[ExtensionInfo]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'uniagent_status': 'uniagent_status',
        'extensions': 'extensions'
    }

    def __init__(self, instance_id=None, uniagent_status=None, extensions=None):
        r"""AgentStatusInfo

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 机器id **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 
        :type instance_id: str
        :param uniagent_status: **参数解释**: uniagent运行状态 **取值范围**: - none: 未安装 - running: 运行中 - silent: 静默状态，用于大规模插件异常时，紧急规避的一种措施，现象是kill掉telescope，只保留uniagent的心跳功能 - unknown: 心跳故障，不上报心跳数据，属于连接丢失故障 
        :type uniagent_status: str
        :param extensions: **参数解释**: 插件信息列表 **取值范围**: 数组长度为[1,10] 
        :type extensions: list[:class:`huaweicloudsdkces.v3.ExtensionInfo`]
        """
        
        

        self._instance_id = None
        self._uniagent_status = None
        self._extensions = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if uniagent_status is not None:
            self.uniagent_status = uniagent_status
        if extensions is not None:
            self.extensions = extensions

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AgentStatusInfo.

        **参数解释**: 机器id **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 

        :return: The instance_id of this AgentStatusInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AgentStatusInfo.

        **参数解释**: 机器id **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 

        :param instance_id: The instance_id of this AgentStatusInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def uniagent_status(self):
        r"""Gets the uniagent_status of this AgentStatusInfo.

        **参数解释**: uniagent运行状态 **取值范围**: - none: 未安装 - running: 运行中 - silent: 静默状态，用于大规模插件异常时，紧急规避的一种措施，现象是kill掉telescope，只保留uniagent的心跳功能 - unknown: 心跳故障，不上报心跳数据，属于连接丢失故障 

        :return: The uniagent_status of this AgentStatusInfo.
        :rtype: str
        """
        return self._uniagent_status

    @uniagent_status.setter
    def uniagent_status(self, uniagent_status):
        r"""Sets the uniagent_status of this AgentStatusInfo.

        **参数解释**: uniagent运行状态 **取值范围**: - none: 未安装 - running: 运行中 - silent: 静默状态，用于大规模插件异常时，紧急规避的一种措施，现象是kill掉telescope，只保留uniagent的心跳功能 - unknown: 心跳故障，不上报心跳数据，属于连接丢失故障 

        :param uniagent_status: The uniagent_status of this AgentStatusInfo.
        :type uniagent_status: str
        """
        self._uniagent_status = uniagent_status

    @property
    def extensions(self):
        r"""Gets the extensions of this AgentStatusInfo.

        **参数解释**: 插件信息列表 **取值范围**: 数组长度为[1,10] 

        :return: The extensions of this AgentStatusInfo.
        :rtype: list[:class:`huaweicloudsdkces.v3.ExtensionInfo`]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        r"""Sets the extensions of this AgentStatusInfo.

        **参数解释**: 插件信息列表 **取值范围**: 数组长度为[1,10] 

        :param extensions: The extensions of this AgentStatusInfo.
        :type extensions: list[:class:`huaweicloudsdkces.v3.ExtensionInfo`]
        """
        self._extensions = extensions

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
        if not isinstance(other, AgentStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
