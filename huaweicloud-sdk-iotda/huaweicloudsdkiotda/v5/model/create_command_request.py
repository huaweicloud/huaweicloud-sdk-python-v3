# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCommandRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('sp_auth_token')

    openapi_types = {
        'device_id': 'str',
        'sp_auth_token': 'str',
        'instance_id': 'str',
        'body': 'DeviceCommandRequest'
    }

    attribute_map = {
        'device_id': 'device_id',
        'sp_auth_token': 'Sp-Auth-Token',
        'instance_id': 'Instance-Id',
        'body': 'body'
    }

    def __init__(self, device_id=None, sp_auth_token=None, instance_id=None, body=None):
        """CreateCommandRequest

        The model defined in huaweicloud sdk

        :param device_id: **参数说明**：下发消息的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type device_id: str
        :param sp_auth_token: Sp用户Token。通过调用IoBPS服务获取SP用户Token
        :type sp_auth_token: str
        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param body: Body of the CreateCommandRequest
        :type body: :class:`huaweicloudsdkiotda.v5.DeviceCommandRequest`
        """
        
        

        self._device_id = None
        self._sp_auth_token = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        self.device_id = device_id
        if sp_auth_token is not None:
            self.sp_auth_token = sp_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def device_id(self):
        """Gets the device_id of this CreateCommandRequest.

        **参数说明**：下发消息的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The device_id of this CreateCommandRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this CreateCommandRequest.

        **参数说明**：下发消息的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param device_id: The device_id of this CreateCommandRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def sp_auth_token(self):
        """Gets the sp_auth_token of this CreateCommandRequest.

        Sp用户Token。通过调用IoBPS服务获取SP用户Token

        :return: The sp_auth_token of this CreateCommandRequest.
        :rtype: str
        """
        return self._sp_auth_token

    @sp_auth_token.setter
    def sp_auth_token(self, sp_auth_token):
        """Sets the sp_auth_token of this CreateCommandRequest.

        Sp用户Token。通过调用IoBPS服务获取SP用户Token

        :param sp_auth_token: The sp_auth_token of this CreateCommandRequest.
        :type sp_auth_token: str
        """
        self._sp_auth_token = sp_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateCommandRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this CreateCommandRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateCommandRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this CreateCommandRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        """Gets the body of this CreateCommandRequest.


        :return: The body of this CreateCommandRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.DeviceCommandRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateCommandRequest.


        :param body: The body of this CreateCommandRequest.
        :type body: :class:`huaweicloudsdkiotda.v5.DeviceCommandRequest`
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
        if not isinstance(other, CreateCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
