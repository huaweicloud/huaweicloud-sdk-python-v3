# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceDataCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'product_id': 'str',
        'filters': 'list[PropertyFilter]'
    }

    attribute_map = {
        'device_id': 'device_id',
        'product_id': 'product_id',
        'filters': 'filters'
    }

    def __init__(self, device_id=None, product_id=None, filters=None):
        """DeviceDataCondition

        The model defined in huaweicloud sdk

        :param device_id: **参数说明**：设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。存在该参数时设备属性触发根据指定设备触发，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type device_id: str
        :param product_id: **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。存在该参数且device_id为空时设备属性触发匹配该产品下所有设备触发，该参数值和device_id不能同时为空。
        :type product_id: str
        :param filters: 数据过滤条件
        :type filters: list[:class:`huaweicloudsdkiotda.v5.PropertyFilter`]
        """
        
        

        self._device_id = None
        self._product_id = None
        self._filters = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if product_id is not None:
            self.product_id = product_id
        if filters is not None:
            self.filters = filters

    @property
    def device_id(self):
        """Gets the device_id of this DeviceDataCondition.

        **参数说明**：设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。存在该参数时设备属性触发根据指定设备触发，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The device_id of this DeviceDataCondition.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceDataCondition.

        **参数说明**：设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。存在该参数时设备属性触发根据指定设备触发，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param device_id: The device_id of this DeviceDataCondition.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def product_id(self):
        """Gets the product_id of this DeviceDataCondition.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。存在该参数且device_id为空时设备属性触发匹配该产品下所有设备触发，该参数值和device_id不能同时为空。

        :return: The product_id of this DeviceDataCondition.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DeviceDataCondition.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。存在该参数且device_id为空时设备属性触发匹配该产品下所有设备触发，该参数值和device_id不能同时为空。

        :param product_id: The product_id of this DeviceDataCondition.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def filters(self):
        """Gets the filters of this DeviceDataCondition.

        数据过滤条件

        :return: The filters of this DeviceDataCondition.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.PropertyFilter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DeviceDataCondition.

        数据过滤条件

        :param filters: The filters of this DeviceDataCondition.
        :type filters: list[:class:`huaweicloudsdkiotda.v5.PropertyFilter`]
        """
        self._filters = filters

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
        if not isinstance(other, DeviceDataCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
