# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOtaModuleRequest:

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
        'module_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'module_id': 'module_id'
    }

    def __init__(self, instance_id=None, module_id=None):
        r"""ShowOtaModuleRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。
        :type instance_id: str
        :param module_id: **参数说明**：OTA模块ID，平台自动生成，用于唯一标识一个模块，创建模块后获得。 **取值范围**：长度不超过36，只允许字母、数字、连接符（-）的组合。
        :type module_id: str
        """
        
        

        self._instance_id = None
        self._module_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.module_id = module_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowOtaModuleRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :return: The instance_id of this ShowOtaModuleRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowOtaModuleRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :param instance_id: The instance_id of this ShowOtaModuleRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def module_id(self):
        r"""Gets the module_id of this ShowOtaModuleRequest.

        **参数说明**：OTA模块ID，平台自动生成，用于唯一标识一个模块，创建模块后获得。 **取值范围**：长度不超过36，只允许字母、数字、连接符（-）的组合。

        :return: The module_id of this ShowOtaModuleRequest.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this ShowOtaModuleRequest.

        **参数说明**：OTA模块ID，平台自动生成，用于唯一标识一个模块，创建模块后获得。 **取值范围**：长度不超过36，只允许字母、数字、连接符（-）的组合。

        :param module_id: The module_id of this ShowOtaModuleRequest.
        :type module_id: str
        """
        self._module_id = module_id

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
        if not isinstance(other, ShowOtaModuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
