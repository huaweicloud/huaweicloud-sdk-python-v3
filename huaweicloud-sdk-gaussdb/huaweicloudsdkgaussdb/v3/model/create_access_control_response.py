# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessControlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open_access_control': 'bool'
    }

    attribute_map = {
        'open_access_control': 'open_access_control'
    }

    def __init__(self, open_access_control=None):
        """CreateAccessControlResponse

        The model defined in huaweicloud sdk

        :param open_access_control: 是否已开启访问控制。 取值： - true：开启。 - false：关闭。
        :type open_access_control: bool
        """
        
        super(CreateAccessControlResponse, self).__init__()

        self._open_access_control = None
        self.discriminator = None

        if open_access_control is not None:
            self.open_access_control = open_access_control

    @property
    def open_access_control(self):
        """Gets the open_access_control of this CreateAccessControlResponse.

        是否已开启访问控制。 取值： - true：开启。 - false：关闭。

        :return: The open_access_control of this CreateAccessControlResponse.
        :rtype: bool
        """
        return self._open_access_control

    @open_access_control.setter
    def open_access_control(self, open_access_control):
        """Sets the open_access_control of this CreateAccessControlResponse.

        是否已开启访问控制。 取值： - true：开启。 - false：关闭。

        :param open_access_control: The open_access_control of this CreateAccessControlResponse.
        :type open_access_control: bool
        """
        self._open_access_control = open_access_control

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
        if not isinstance(other, CreateAccessControlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
