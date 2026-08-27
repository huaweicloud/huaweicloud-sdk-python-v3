# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreCheckForUpgradeDatabasesSingleInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_version': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'current_version': 'current_version',
        'instance_id': 'instance_id'
    }

    def __init__(self, current_version=None, instance_id=None):
        r"""PreCheckForUpgradeDatabasesSingleInstance

        The model defined in huaweicloud sdk

        :param current_version: **参数解释**：  实例当前的内核版本。可通过调用[查询内核版本信息](https://support.huaweicloud.com/api-taurusdb/ShowInstanceDatabaseVersion.html)接口获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type current_version: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        """
        
        

        self._current_version = None
        self._instance_id = None
        self.discriminator = None

        self.current_version = current_version
        self.instance_id = instance_id

    @property
    def current_version(self):
        r"""Gets the current_version of this PreCheckForUpgradeDatabasesSingleInstance.

        **参数解释**：  实例当前的内核版本。可通过调用[查询内核版本信息](https://support.huaweicloud.com/api-taurusdb/ShowInstanceDatabaseVersion.html)接口获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The current_version of this PreCheckForUpgradeDatabasesSingleInstance.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this PreCheckForUpgradeDatabasesSingleInstance.

        **参数解释**：  实例当前的内核版本。可通过调用[查询内核版本信息](https://support.huaweicloud.com/api-taurusdb/ShowInstanceDatabaseVersion.html)接口获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param current_version: The current_version of this PreCheckForUpgradeDatabasesSingleInstance.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this PreCheckForUpgradeDatabasesSingleInstance.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this PreCheckForUpgradeDatabasesSingleInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this PreCheckForUpgradeDatabasesSingleInstance.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this PreCheckForUpgradeDatabasesSingleInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, PreCheckForUpgradeDatabasesSingleInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
