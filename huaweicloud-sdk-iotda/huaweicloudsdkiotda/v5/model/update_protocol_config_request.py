# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProtocolConfigRequest:

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
        'protocol_id': 'str',
        'body': 'UpdateProtocolConfigDTO'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'protocol_id': 'protocol_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, protocol_id=None, body=None):
        r"""UpdateProtocolConfigRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。
        :type instance_id: str
        :param protocol_id: **参数说明**：泛协议配置ID。
        :type protocol_id: str
        :param body: Body of the UpdateProtocolConfigRequest
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateProtocolConfigDTO`
        """
        
        

        self._instance_id = None
        self._protocol_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.protocol_id = protocol_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateProtocolConfigRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :return: The instance_id of this UpdateProtocolConfigRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateProtocolConfigRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :param instance_id: The instance_id of this UpdateProtocolConfigRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def protocol_id(self):
        r"""Gets the protocol_id of this UpdateProtocolConfigRequest.

        **参数说明**：泛协议配置ID。

        :return: The protocol_id of this UpdateProtocolConfigRequest.
        :rtype: str
        """
        return self._protocol_id

    @protocol_id.setter
    def protocol_id(self, protocol_id):
        r"""Sets the protocol_id of this UpdateProtocolConfigRequest.

        **参数说明**：泛协议配置ID。

        :param protocol_id: The protocol_id of this UpdateProtocolConfigRequest.
        :type protocol_id: str
        """
        self._protocol_id = protocol_id

    @property
    def body(self):
        r"""Gets the body of this UpdateProtocolConfigRequest.

        :return: The body of this UpdateProtocolConfigRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateProtocolConfigDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateProtocolConfigRequest.

        :param body: The body of this UpdateProtocolConfigRequest.
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateProtocolConfigDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateProtocolConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
