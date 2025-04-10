# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateForwardingConfigRequest:

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
        'forwarding_type': 'str',
        'forwarding_config_id': 'str',
        'body': 'UpdateForwardingConfigRequestDTO'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'forwarding_type': 'forwarding_type',
        'forwarding_config_id': 'forwarding_config_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, forwarding_type=None, forwarding_config_id=None, body=None):
        r"""UpdateForwardingConfigRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。
        :type instance_id: str
        :param forwarding_type: **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。
        :type forwarding_type: str
        :param forwarding_config_id: **参数说明**：转发配置的唯一ID。
        :type forwarding_config_id: str
        :param body: Body of the UpdateForwardingConfigRequest
        :type body: :class:`huaweicloudsdkdris.v1.UpdateForwardingConfigRequestDTO`
        """
        
        

        self._instance_id = None
        self._forwarding_type = None
        self._forwarding_config_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.forwarding_type = forwarding_type
        self.forwarding_config_id = forwarding_config_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateForwardingConfigRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :return: The instance_id of this UpdateForwardingConfigRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateForwardingConfigRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :param instance_id: The instance_id of this UpdateForwardingConfigRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def forwarding_type(self):
        r"""Gets the forwarding_type of this UpdateForwardingConfigRequest.

        **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。

        :return: The forwarding_type of this UpdateForwardingConfigRequest.
        :rtype: str
        """
        return self._forwarding_type

    @forwarding_type.setter
    def forwarding_type(self, forwarding_type):
        r"""Sets the forwarding_type of this UpdateForwardingConfigRequest.

        **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。

        :param forwarding_type: The forwarding_type of this UpdateForwardingConfigRequest.
        :type forwarding_type: str
        """
        self._forwarding_type = forwarding_type

    @property
    def forwarding_config_id(self):
        r"""Gets the forwarding_config_id of this UpdateForwardingConfigRequest.

        **参数说明**：转发配置的唯一ID。

        :return: The forwarding_config_id of this UpdateForwardingConfigRequest.
        :rtype: str
        """
        return self._forwarding_config_id

    @forwarding_config_id.setter
    def forwarding_config_id(self, forwarding_config_id):
        r"""Sets the forwarding_config_id of this UpdateForwardingConfigRequest.

        **参数说明**：转发配置的唯一ID。

        :param forwarding_config_id: The forwarding_config_id of this UpdateForwardingConfigRequest.
        :type forwarding_config_id: str
        """
        self._forwarding_config_id = forwarding_config_id

    @property
    def body(self):
        r"""Gets the body of this UpdateForwardingConfigRequest.

        :return: The body of this UpdateForwardingConfigRequest.
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateForwardingConfigRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateForwardingConfigRequest.

        :param body: The body of this UpdateForwardingConfigRequest.
        :type body: :class:`huaweicloudsdkdris.v1.UpdateForwardingConfigRequestDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateForwardingConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
