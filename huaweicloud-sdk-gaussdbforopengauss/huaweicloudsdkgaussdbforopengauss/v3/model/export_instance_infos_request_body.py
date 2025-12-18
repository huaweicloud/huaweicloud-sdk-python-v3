# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportInstanceInfosRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_list': 'list[str]',
        'user_defined_columns': 'list[str]',
        'time_zone': 'str',
        'language': 'str'
    }

    attribute_map = {
        'instance_list': 'instance_list',
        'user_defined_columns': 'user_defined_columns',
        'time_zone': 'time_zone',
        'language': 'language'
    }

    def __init__(self, instance_list=None, user_defined_columns=None, time_zone=None, language=None):
        r"""ExportInstanceInfosRequestBody

        The model defined in huaweicloud sdk

        :param instance_list: **参数解释**:   实例id列表。 **约束限制**:   不涉及。 **取值范围**:   不涉及 **默认取值**:   不涉及。
        :type instance_list: list[str]
        :param user_defined_columns: **参数解释**:   导出字段列表。 **约束限制**:   不涉及。 **取值范围**:   - name：实例名称   - id：实例ID   - alias：实例备注   - editionMode：产品类型   - haModel：实例类型   - deployMode：部署形态   - engine：数据库引擎版本   - hotfixVersions：已升级热补丁   - instanceStatus：实例状态   - payModel：计费模式   - targetEngineVersion：目标版本   - flavor：性能规格   - availableZones：可用区   - privateIp：内网地址   - dnsName：DNS   - ipv6：IPv6地址   - dbPort：数据库端口   - publicIp：弹性公网IP   - createAt：创建时间   - volumeType：存储空间类型   - volumeSize：存储空间大小   - vpcName：虚拟私有云名称   - vpcId：虚拟私有云ID   - securityGroupName：安全组   - enterpriseProjectName：企业项目  **默认取值**:   不涉及。
        :type user_defined_columns: list[str]
        :param time_zone: **参数解释**:   时区。 **约束限制**:   不涉及。 **取值范围**:   - +08:00 **默认取值**:   +08:00
        :type time_zone: str
        :param language: **参数解释**:   语言。 **约束限制**:   不涉及。 **取值范围**:   - zh-cn    - en-us  **默认取值**:   zh-cn
        :type language: str
        """
        
        

        self._instance_list = None
        self._user_defined_columns = None
        self._time_zone = None
        self._language = None
        self.discriminator = None

        if instance_list is not None:
            self.instance_list = instance_list
        self.user_defined_columns = user_defined_columns
        if time_zone is not None:
            self.time_zone = time_zone
        if language is not None:
            self.language = language

    @property
    def instance_list(self):
        r"""Gets the instance_list of this ExportInstanceInfosRequestBody.

        **参数解释**:   实例id列表。 **约束限制**:   不涉及。 **取值范围**:   不涉及 **默认取值**:   不涉及。

        :return: The instance_list of this ExportInstanceInfosRequestBody.
        :rtype: list[str]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        r"""Sets the instance_list of this ExportInstanceInfosRequestBody.

        **参数解释**:   实例id列表。 **约束限制**:   不涉及。 **取值范围**:   不涉及 **默认取值**:   不涉及。

        :param instance_list: The instance_list of this ExportInstanceInfosRequestBody.
        :type instance_list: list[str]
        """
        self._instance_list = instance_list

    @property
    def user_defined_columns(self):
        r"""Gets the user_defined_columns of this ExportInstanceInfosRequestBody.

        **参数解释**:   导出字段列表。 **约束限制**:   不涉及。 **取值范围**:   - name：实例名称   - id：实例ID   - alias：实例备注   - editionMode：产品类型   - haModel：实例类型   - deployMode：部署形态   - engine：数据库引擎版本   - hotfixVersions：已升级热补丁   - instanceStatus：实例状态   - payModel：计费模式   - targetEngineVersion：目标版本   - flavor：性能规格   - availableZones：可用区   - privateIp：内网地址   - dnsName：DNS   - ipv6：IPv6地址   - dbPort：数据库端口   - publicIp：弹性公网IP   - createAt：创建时间   - volumeType：存储空间类型   - volumeSize：存储空间大小   - vpcName：虚拟私有云名称   - vpcId：虚拟私有云ID   - securityGroupName：安全组   - enterpriseProjectName：企业项目  **默认取值**:   不涉及。

        :return: The user_defined_columns of this ExportInstanceInfosRequestBody.
        :rtype: list[str]
        """
        return self._user_defined_columns

    @user_defined_columns.setter
    def user_defined_columns(self, user_defined_columns):
        r"""Sets the user_defined_columns of this ExportInstanceInfosRequestBody.

        **参数解释**:   导出字段列表。 **约束限制**:   不涉及。 **取值范围**:   - name：实例名称   - id：实例ID   - alias：实例备注   - editionMode：产品类型   - haModel：实例类型   - deployMode：部署形态   - engine：数据库引擎版本   - hotfixVersions：已升级热补丁   - instanceStatus：实例状态   - payModel：计费模式   - targetEngineVersion：目标版本   - flavor：性能规格   - availableZones：可用区   - privateIp：内网地址   - dnsName：DNS   - ipv6：IPv6地址   - dbPort：数据库端口   - publicIp：弹性公网IP   - createAt：创建时间   - volumeType：存储空间类型   - volumeSize：存储空间大小   - vpcName：虚拟私有云名称   - vpcId：虚拟私有云ID   - securityGroupName：安全组   - enterpriseProjectName：企业项目  **默认取值**:   不涉及。

        :param user_defined_columns: The user_defined_columns of this ExportInstanceInfosRequestBody.
        :type user_defined_columns: list[str]
        """
        self._user_defined_columns = user_defined_columns

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ExportInstanceInfosRequestBody.

        **参数解释**:   时区。 **约束限制**:   不涉及。 **取值范围**:   - +08:00 **默认取值**:   +08:00

        :return: The time_zone of this ExportInstanceInfosRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ExportInstanceInfosRequestBody.

        **参数解释**:   时区。 **约束限制**:   不涉及。 **取值范围**:   - +08:00 **默认取值**:   +08:00

        :param time_zone: The time_zone of this ExportInstanceInfosRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def language(self):
        r"""Gets the language of this ExportInstanceInfosRequestBody.

        **参数解释**:   语言。 **约束限制**:   不涉及。 **取值范围**:   - zh-cn    - en-us  **默认取值**:   zh-cn

        :return: The language of this ExportInstanceInfosRequestBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportInstanceInfosRequestBody.

        **参数解释**:   语言。 **约束限制**:   不涉及。 **取值范围**:   - zh-cn    - en-us  **默认取值**:   zh-cn

        :param language: The language of this ExportInstanceInfosRequestBody.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ExportInstanceInfosRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
