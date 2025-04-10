# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDeviceResponse(SdkResponse):

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
        'password': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'password': 'password'
    }

    def __init__(self, device_id=None, password=None):
        r"""AddDeviceResponse

        The model defined in huaweicloud sdk

        :param device_id: 设备ID
        :type device_id: str
        :param password: 设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；修改设备、查询设备及查询设备列表接口不返回该参数。
        :type password: str
        """
        
        super(AddDeviceResponse, self).__init__()

        self._device_id = None
        self._password = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if password is not None:
            self.password = password

    @property
    def device_id(self):
        r"""Gets the device_id of this AddDeviceResponse.

        设备ID

        :return: The device_id of this AddDeviceResponse.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this AddDeviceResponse.

        设备ID

        :param device_id: The device_id of this AddDeviceResponse.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def password(self):
        r"""Gets the password of this AddDeviceResponse.

        设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；修改设备、查询设备及查询设备列表接口不返回该参数。

        :return: The password of this AddDeviceResponse.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this AddDeviceResponse.

        设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；修改设备、查询设备及查询设备列表接口不返回该参数。

        :param password: The password of this AddDeviceResponse.
        :type password: str
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
        if not isinstance(other, AddDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
