# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOtaModule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'product_id': 'str',
        'module_name': 'str',
        'alias_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'product_id': 'product_id',
        'module_name': 'module_name',
        'alias_name': 'alias_name',
        'description': 'description'
    }

    def __init__(self, app_id=None, product_id=None, module_name=None, alias_name=None, description=None):
        r"""CreateOtaModule

        The model defined in huaweicloud sdk

        :param app_id: **参数说明**：资源空间ID。存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的升级包归属到哪个资源空间下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param product_id: **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type product_id: str
        :param module_name: **参数说明**：OTA模块名称，产品下唯一且不可修改。 **取值范围**：长度不超过64，只允许英文字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。
        :type module_name: str
        :param alias_name: **参数说明**：OTA模块别名。 **取值范围**：长度不超过64，只允许中文、英文字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。
        :type alias_name: str
        :param description: **参数说明**：用于描述模块的功能等信息。 **取值范围**：长度不超过1024。
        :type description: str
        """
        
        

        self._app_id = None
        self._product_id = None
        self._module_name = None
        self._alias_name = None
        self._description = None
        self.discriminator = None

        self.app_id = app_id
        self.product_id = product_id
        self.module_name = module_name
        if alias_name is not None:
            self.alias_name = alias_name
        if description is not None:
            self.description = description

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateOtaModule.

        **参数说明**：资源空间ID。存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的升级包归属到哪个资源空间下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this CreateOtaModule.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateOtaModule.

        **参数说明**：资源空间ID。存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的升级包归属到哪个资源空间下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this CreateOtaModule.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateOtaModule.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The product_id of this CreateOtaModule.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateOtaModule.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param product_id: The product_id of this CreateOtaModule.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def module_name(self):
        r"""Gets the module_name of this CreateOtaModule.

        **参数说明**：OTA模块名称，产品下唯一且不可修改。 **取值范围**：长度不超过64，只允许英文字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :return: The module_name of this CreateOtaModule.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this CreateOtaModule.

        **参数说明**：OTA模块名称，产品下唯一且不可修改。 **取值范围**：长度不超过64，只允许英文字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :param module_name: The module_name of this CreateOtaModule.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def alias_name(self):
        r"""Gets the alias_name of this CreateOtaModule.

        **参数说明**：OTA模块别名。 **取值范围**：长度不超过64，只允许中文、英文字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :return: The alias_name of this CreateOtaModule.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this CreateOtaModule.

        **参数说明**：OTA模块别名。 **取值范围**：长度不超过64，只允许中文、英文字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :param alias_name: The alias_name of this CreateOtaModule.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def description(self):
        r"""Gets the description of this CreateOtaModule.

        **参数说明**：用于描述模块的功能等信息。 **取值范围**：长度不超过1024。

        :return: The description of this CreateOtaModule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOtaModule.

        **参数说明**：用于描述模块的功能等信息。 **取值范围**：长度不超过1024。

        :param description: The description of this CreateOtaModule.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateOtaModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
