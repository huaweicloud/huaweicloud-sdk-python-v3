# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthenticationTemplateResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'object',
        'timestamp': 'TimestampResource',
        'password': 'object'
    }

    attribute_map = {
        'device_id': 'device_id',
        'timestamp': 'timestamp',
        'password': 'password'
    }

    def __init__(self, device_id=None, timestamp=None, password=None):
        r"""AuthenticationTemplateResource

        The model defined in huaweicloud sdk

        :param device_id: 设备ID，json对象只能使用FunctionDefinition下的函数从parameters中获取设备ID的取值。
        :type device_id: object
        :param timestamp: 
        :type timestamp: :class:`huaweicloudsdkiotda.v5.TimestampResource`
        :param password: mqtt认证密码，该字段只在设备认证方式为密码认证时生效，证书认证时无效，只能使用FunctionDefinition下的函数从parameters中编程密码的生成方式，平台比较函数解析结果与设备mqtt连接时携带的password是否相等，相等则认证通过。函数中必须包含设备原始秘钥参数${iotda::device::secret}，且只能在hash函数中使用。
        :type password: object
        """
        
        

        self._device_id = None
        self._timestamp = None
        self._password = None
        self.discriminator = None

        self.device_id = device_id
        if timestamp is not None:
            self.timestamp = timestamp
        if password is not None:
            self.password = password

    @property
    def device_id(self):
        r"""Gets the device_id of this AuthenticationTemplateResource.

        设备ID，json对象只能使用FunctionDefinition下的函数从parameters中获取设备ID的取值。

        :return: The device_id of this AuthenticationTemplateResource.
        :rtype: object
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this AuthenticationTemplateResource.

        设备ID，json对象只能使用FunctionDefinition下的函数从parameters中获取设备ID的取值。

        :param device_id: The device_id of this AuthenticationTemplateResource.
        :type device_id: object
        """
        self._device_id = device_id

    @property
    def timestamp(self):
        r"""Gets the timestamp of this AuthenticationTemplateResource.

        :return: The timestamp of this AuthenticationTemplateResource.
        :rtype: :class:`huaweicloudsdkiotda.v5.TimestampResource`
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this AuthenticationTemplateResource.

        :param timestamp: The timestamp of this AuthenticationTemplateResource.
        :type timestamp: :class:`huaweicloudsdkiotda.v5.TimestampResource`
        """
        self._timestamp = timestamp

    @property
    def password(self):
        r"""Gets the password of this AuthenticationTemplateResource.

        mqtt认证密码，该字段只在设备认证方式为密码认证时生效，证书认证时无效，只能使用FunctionDefinition下的函数从parameters中编程密码的生成方式，平台比较函数解析结果与设备mqtt连接时携带的password是否相等，相等则认证通过。函数中必须包含设备原始秘钥参数${iotda::device::secret}，且只能在hash函数中使用。

        :return: The password of this AuthenticationTemplateResource.
        :rtype: object
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this AuthenticationTemplateResource.

        mqtt认证密码，该字段只在设备认证方式为密码认证时生效，证书认证时无效，只能使用FunctionDefinition下的函数从parameters中编程密码的生成方式，平台比较函数解析结果与设备mqtt连接时携带的password是否相等，相等则认证通过。函数中必须包含设备原始秘钥参数${iotda::device::secret}，且只能在hash函数中使用。

        :param password: The password of this AuthenticationTemplateResource.
        :type password: object
        """
        self._password = password

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
        if not isinstance(other, AuthenticationTemplateResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
