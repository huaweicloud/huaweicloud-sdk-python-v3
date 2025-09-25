# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetWtpProtectionStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'bool',
        'host_id_list': 'list[str]',
        'charging_mode': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'host_id_list': 'host_id_list',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id'
    }

    def __init__(self, status=None, host_id_list=None, charging_mode=None, resource_id=None):
        r"""SetWtpProtectionStatusRequestInfo

        The model defined in huaweicloud sdk

        :param status: **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: - True ：开启防护，必须填写charging_mode。 - False ：关闭防护，无需填写charging_mode。  **默认取值**: False 
        :type status: bool
        :param host_id_list: **参数解释**: 需要开启或关闭防护的服务器ID列表。 **约束限制** : 开启防护时，需要使用 ListWtpProtectHost 接口查询网页防篡改主机防护状态列表信息，在 ListWtpProtectHost 接口的响应体中，protect_status 等于 closed 且 agent_status 等于 online 的 host_id 是符合开启防护的服务器ID。 **取值范围**: 最少1条，最多20000条 **默认取值** : 不涉及 
        :type host_id_list: list[str]
        :param charging_mode: **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle: 包年/包月，可填写resource_id。 - on_demand: 按需计费，无需填写resource_id。  **默认取值**: on_demand 
        :type charging_mode: str
        :param resource_id: **参数解释**: 资源ID，即网页防篡改配额的配额ID，当charging_mode选择packet_cycle时可填写该字段，表示使用一个指定配额，也可不填写该字段，表示随机选择符合的配额。 **约束限制** : 不涉及 **取值范围**: 字符长度0-64位 **默认取值** : 不涉及 
        :type resource_id: str
        """
        
        

        self._status = None
        self._host_id_list = None
        self._charging_mode = None
        self._resource_id = None
        self.discriminator = None

        self.status = status
        self.host_id_list = host_id_list
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def status(self):
        r"""Gets the status of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: - True ：开启防护，必须填写charging_mode。 - False ：关闭防护，无需填写charging_mode。  **默认取值**: False 

        :return: The status of this SetWtpProtectionStatusRequestInfo.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: - True ：开启防护，必须填写charging_mode。 - False ：关闭防护，无需填写charging_mode。  **默认取值**: False 

        :param status: The status of this SetWtpProtectionStatusRequestInfo.
        :type status: bool
        """
        self._status = status

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 需要开启或关闭防护的服务器ID列表。 **约束限制** : 开启防护时，需要使用 ListWtpProtectHost 接口查询网页防篡改主机防护状态列表信息，在 ListWtpProtectHost 接口的响应体中，protect_status 等于 closed 且 agent_status 等于 online 的 host_id 是符合开启防护的服务器ID。 **取值范围**: 最少1条，最多20000条 **默认取值** : 不涉及 

        :return: The host_id_list of this SetWtpProtectionStatusRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 需要开启或关闭防护的服务器ID列表。 **约束限制** : 开启防护时，需要使用 ListWtpProtectHost 接口查询网页防篡改主机防护状态列表信息，在 ListWtpProtectHost 接口的响应体中，protect_status 等于 closed 且 agent_status 等于 online 的 host_id 是符合开启防护的服务器ID。 **取值范围**: 最少1条，最多20000条 **默认取值** : 不涉及 

        :param host_id_list: The host_id_list of this SetWtpProtectionStatusRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle: 包年/包月，可填写resource_id。 - on_demand: 按需计费，无需填写resource_id。  **默认取值**: on_demand 

        :return: The charging_mode of this SetWtpProtectionStatusRequestInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle: 包年/包月，可填写resource_id。 - on_demand: 按需计费，无需填写resource_id。  **默认取值**: on_demand 

        :param charging_mode: The charging_mode of this SetWtpProtectionStatusRequestInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 资源ID，即网页防篡改配额的配额ID，当charging_mode选择packet_cycle时可填写该字段，表示使用一个指定配额，也可不填写该字段，表示随机选择符合的配额。 **约束限制** : 不涉及 **取值范围**: 字符长度0-64位 **默认取值** : 不涉及 

        :return: The resource_id of this SetWtpProtectionStatusRequestInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SetWtpProtectionStatusRequestInfo.

        **参数解释**: 资源ID，即网页防篡改配额的配额ID，当charging_mode选择packet_cycle时可填写该字段，表示使用一个指定配额，也可不填写该字段，表示随机选择符合的配额。 **约束限制** : 不涉及 **取值范围**: 字符长度0-64位 **默认取值** : 不涉及 

        :param resource_id: The resource_id of this SetWtpProtectionStatusRequestInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, SetWtpProtectionStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
