# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'dew_secret_name': 'str',
        'ssl_enable': 'bool',
        'dcs_id': 'str',
        'vpcep_service_id': 'str'
    }

    attribute_map = {
        'username': 'username',
        'dew_secret_name': 'dew_secret_name',
        'ssl_enable': 'ssl_enable',
        'dcs_id': 'dcs_id',
        'vpcep_service_id': 'vpcep_service_id'
    }

    def __init__(self, username=None, dew_secret_name=None, ssl_enable=None, dcs_id=None, vpcep_service_id=None):
        r"""RedisConfig

        The model defined in huaweicloud sdk

        :param username: **参数解释**：账号名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及特殊字符，长度为1~64个字符。 **默认取值**：default。
        :type username: str
        :param dew_secret_name: **参数解释**：DEW的凭据名称。存储着DCS账号的密码，格式为：凭据键为password，值为实际的密码。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及特殊字符，长度为1~64个字符。 **默认取值**：不涉及。
        :type dew_secret_name: str
        :param ssl_enable: **参数解释**：是否开启SSL。 **约束限制**：不涉及。 **取值范围**：   - true：开启SSL。   - false：关闭SSL。 **默认取值**：true。
        :type ssl_enable: bool
        :param dcs_id: **参数解释**：DCS实例的ID。获取方式：在DCS控制台实例详情页查看，或通过调用查询DCS实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及中划线，长度为4~1024个字符。 **默认取值**：不涉及。
        :type dcs_id: str
        :param vpcep_service_id: **参数解释**：VPCEP服务端ID，用于连接客户侧网络。获取方式：在VPCEP控制台查看，或通过调用查询VPCEP服务列表接口获取。开启GCS高可用时必填，用于通过VPCEP方式连接客户侧DCS。 **约束限制**：开启GCS高可用时必填。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type vpcep_service_id: str
        """
        
        

        self._username = None
        self._dew_secret_name = None
        self._ssl_enable = None
        self._dcs_id = None
        self._vpcep_service_id = None
        self.discriminator = None

        if username is not None:
            self.username = username
        self.dew_secret_name = dew_secret_name
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        self.dcs_id = dcs_id
        self.vpcep_service_id = vpcep_service_id

    @property
    def username(self):
        r"""Gets the username of this RedisConfig.

        **参数解释**：账号名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及特殊字符，长度为1~64个字符。 **默认取值**：default。

        :return: The username of this RedisConfig.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RedisConfig.

        **参数解释**：账号名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及特殊字符，长度为1~64个字符。 **默认取值**：default。

        :param username: The username of this RedisConfig.
        :type username: str
        """
        self._username = username

    @property
    def dew_secret_name(self):
        r"""Gets the dew_secret_name of this RedisConfig.

        **参数解释**：DEW的凭据名称。存储着DCS账号的密码，格式为：凭据键为password，值为实际的密码。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及特殊字符，长度为1~64个字符。 **默认取值**：不涉及。

        :return: The dew_secret_name of this RedisConfig.
        :rtype: str
        """
        return self._dew_secret_name

    @dew_secret_name.setter
    def dew_secret_name(self, dew_secret_name):
        r"""Sets the dew_secret_name of this RedisConfig.

        **参数解释**：DEW的凭据名称。存储着DCS账号的密码，格式为：凭据键为password，值为实际的密码。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及特殊字符，长度为1~64个字符。 **默认取值**：不涉及。

        :param dew_secret_name: The dew_secret_name of this RedisConfig.
        :type dew_secret_name: str
        """
        self._dew_secret_name = dew_secret_name

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this RedisConfig.

        **参数解释**：是否开启SSL。 **约束限制**：不涉及。 **取值范围**：   - true：开启SSL。   - false：关闭SSL。 **默认取值**：true。

        :return: The ssl_enable of this RedisConfig.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this RedisConfig.

        **参数解释**：是否开启SSL。 **约束限制**：不涉及。 **取值范围**：   - true：开启SSL。   - false：关闭SSL。 **默认取值**：true。

        :param ssl_enable: The ssl_enable of this RedisConfig.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def dcs_id(self):
        r"""Gets the dcs_id of this RedisConfig.

        **参数解释**：DCS实例的ID。获取方式：在DCS控制台实例详情页查看，或通过调用查询DCS实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及中划线，长度为4~1024个字符。 **默认取值**：不涉及。

        :return: The dcs_id of this RedisConfig.
        :rtype: str
        """
        return self._dcs_id

    @dcs_id.setter
    def dcs_id(self, dcs_id):
        r"""Sets the dcs_id of this RedisConfig.

        **参数解释**：DCS实例的ID。获取方式：在DCS控制台实例详情页查看，或通过调用查询DCS实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字及中划线，长度为4~1024个字符。 **默认取值**：不涉及。

        :param dcs_id: The dcs_id of this RedisConfig.
        :type dcs_id: str
        """
        self._dcs_id = dcs_id

    @property
    def vpcep_service_id(self):
        r"""Gets the vpcep_service_id of this RedisConfig.

        **参数解释**：VPCEP服务端ID，用于连接客户侧网络。获取方式：在VPCEP控制台查看，或通过调用查询VPCEP服务列表接口获取。开启GCS高可用时必填，用于通过VPCEP方式连接客户侧DCS。 **约束限制**：开启GCS高可用时必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The vpcep_service_id of this RedisConfig.
        :rtype: str
        """
        return self._vpcep_service_id

    @vpcep_service_id.setter
    def vpcep_service_id(self, vpcep_service_id):
        r"""Sets the vpcep_service_id of this RedisConfig.

        **参数解释**：VPCEP服务端ID，用于连接客户侧网络。获取方式：在VPCEP控制台查看，或通过调用查询VPCEP服务列表接口获取。开启GCS高可用时必填，用于通过VPCEP方式连接客户侧DCS。 **约束限制**：开启GCS高可用时必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param vpcep_service_id: The vpcep_service_id of this RedisConfig.
        :type vpcep_service_id: str
        """
        self._vpcep_service_id = vpcep_service_id

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
        if not isinstance(other, RedisConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
