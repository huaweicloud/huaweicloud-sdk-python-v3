# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreDuplicationRequestInfo:

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
        'power_on': 'bool',
        'mappings': 'list[BackupRestoreServerMappingInfo]'
    }

    attribute_map = {
        'server_id': 'server_id',
        'power_on': 'power_on',
        'mappings': 'mappings'
    }

    def __init__(self, server_id=None, power_on=None, mappings=None):
        r"""RestoreDuplicationRequestInfo

        The model defined in huaweicloud sdk

        :param server_id: **参数解释**: 恢复的目标虚拟机ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type server_id: str
        :param power_on: **参数解释**： 恢复后是否开机, 默认开机。 **约束限制**: 不涉及 **取值范围**: - true：开机 - false: 不开机 **默认取值**: true 
        :type power_on: bool
        :param mappings: **参数解释**： 恢复的映射关系（整机恢复时必填，卷恢复时可选但是不会用到填写的值） **取值范围**: 不涉及 
        :type mappings: list[:class:`huaweicloudsdkhss.v5.BackupRestoreServerMappingInfo`]
        """
        
        

        self._server_id = None
        self._power_on = None
        self._mappings = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if power_on is not None:
            self.power_on = power_on
        if mappings is not None:
            self.mappings = mappings

    @property
    def server_id(self):
        r"""Gets the server_id of this RestoreDuplicationRequestInfo.

        **参数解释**: 恢复的目标虚拟机ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The server_id of this RestoreDuplicationRequestInfo.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this RestoreDuplicationRequestInfo.

        **参数解释**: 恢复的目标虚拟机ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param server_id: The server_id of this RestoreDuplicationRequestInfo.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def power_on(self):
        r"""Gets the power_on of this RestoreDuplicationRequestInfo.

        **参数解释**： 恢复后是否开机, 默认开机。 **约束限制**: 不涉及 **取值范围**: - true：开机 - false: 不开机 **默认取值**: true 

        :return: The power_on of this RestoreDuplicationRequestInfo.
        :rtype: bool
        """
        return self._power_on

    @power_on.setter
    def power_on(self, power_on):
        r"""Sets the power_on of this RestoreDuplicationRequestInfo.

        **参数解释**： 恢复后是否开机, 默认开机。 **约束限制**: 不涉及 **取值范围**: - true：开机 - false: 不开机 **默认取值**: true 

        :param power_on: The power_on of this RestoreDuplicationRequestInfo.
        :type power_on: bool
        """
        self._power_on = power_on

    @property
    def mappings(self):
        r"""Gets the mappings of this RestoreDuplicationRequestInfo.

        **参数解释**： 恢复的映射关系（整机恢复时必填，卷恢复时可选但是不会用到填写的值） **取值范围**: 不涉及 

        :return: The mappings of this RestoreDuplicationRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.BackupRestoreServerMappingInfo`]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        r"""Sets the mappings of this RestoreDuplicationRequestInfo.

        **参数解释**： 恢复的映射关系（整机恢复时必填，卷恢复时可选但是不会用到填写的值） **取值范围**: 不涉及 

        :param mappings: The mappings of this RestoreDuplicationRequestInfo.
        :type mappings: list[:class:`huaweicloudsdkhss.v5.BackupRestoreServerMappingInfo`]
        """
        self._mappings = mappings

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
        if not isinstance(other, RestoreDuplicationRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
