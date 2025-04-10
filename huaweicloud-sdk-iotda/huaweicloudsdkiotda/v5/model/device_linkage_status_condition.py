# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceLinkageStatusCondition:

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
        'status_list': 'list[str]',
        'duration': 'int'
    }

    attribute_map = {
        'device_id': 'device_id',
        'product_id': 'product_id',
        'status_list': 'status_list',
        'duration': 'duration'
    }

    def __init__(self, device_id=None, product_id=None, status_list=None, duration=None):
        r"""DeviceLinkageStatusCondition

        The model defined in huaweicloud sdk

        :param device_id: **参数说明**：设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。存在该参数时设备状态触发根据指定设备触发，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type device_id: str
        :param product_id: **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。存在该参数且device_id为空时设备状态触发匹配该产品下所有设备触发，该参数值和device_id不能同时为空。
        :type product_id: str
        :param status_list: **参数说明**：状态列表，设备状态条件携带该参数。 **取值范围**： - ONLINE：设备上线 - OFFLINE：设备下线
        :type status_list: list[str]
        :param duration: **持续时长**：设备状态持续时长，取值范围: 0-60(分钟)。
        :type duration: int
        """
        
        

        self._device_id = None
        self._product_id = None
        self._status_list = None
        self._duration = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if product_id is not None:
            self.product_id = product_id
        if status_list is not None:
            self.status_list = status_list
        if duration is not None:
            self.duration = duration

    @property
    def device_id(self):
        r"""Gets the device_id of this DeviceLinkageStatusCondition.

        **参数说明**：设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。存在该参数时设备状态触发根据指定设备触发，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The device_id of this DeviceLinkageStatusCondition.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this DeviceLinkageStatusCondition.

        **参数说明**：设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。存在该参数时设备状态触发根据指定设备触发，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param device_id: The device_id of this DeviceLinkageStatusCondition.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def product_id(self):
        r"""Gets the product_id of this DeviceLinkageStatusCondition.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。存在该参数且device_id为空时设备状态触发匹配该产品下所有设备触发，该参数值和device_id不能同时为空。

        :return: The product_id of this DeviceLinkageStatusCondition.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this DeviceLinkageStatusCondition.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。存在该参数且device_id为空时设备状态触发匹配该产品下所有设备触发，该参数值和device_id不能同时为空。

        :param product_id: The product_id of this DeviceLinkageStatusCondition.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def status_list(self):
        r"""Gets the status_list of this DeviceLinkageStatusCondition.

        **参数说明**：状态列表，设备状态条件携带该参数。 **取值范围**： - ONLINE：设备上线 - OFFLINE：设备下线

        :return: The status_list of this DeviceLinkageStatusCondition.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this DeviceLinkageStatusCondition.

        **参数说明**：状态列表，设备状态条件携带该参数。 **取值范围**： - ONLINE：设备上线 - OFFLINE：设备下线

        :param status_list: The status_list of this DeviceLinkageStatusCondition.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def duration(self):
        r"""Gets the duration of this DeviceLinkageStatusCondition.

        **持续时长**：设备状态持续时长，取值范围: 0-60(分钟)。

        :return: The duration of this DeviceLinkageStatusCondition.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this DeviceLinkageStatusCondition.

        **持续时长**：设备状态持续时长，取值范围: 0-60(分钟)。

        :param duration: The duration of this DeviceLinkageStatusCondition.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, DeviceLinkageStatusCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
