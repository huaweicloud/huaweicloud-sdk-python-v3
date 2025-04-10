# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUrlAuthchainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keychain': 'list[str]'
    }

    attribute_map = {
        'keychain': 'keychain'
    }

    def __init__(self, keychain=None):
        r"""CreateUrlAuthchainResponse

        The model defined in huaweicloud sdk

        :param keychain: 生成的鉴权串列表
        :type keychain: list[str]
        """
        
        super(CreateUrlAuthchainResponse, self).__init__()

        self._keychain = None
        self.discriminator = None

        if keychain is not None:
            self.keychain = keychain

    @property
    def keychain(self):
        r"""Gets the keychain of this CreateUrlAuthchainResponse.

        生成的鉴权串列表

        :return: The keychain of this CreateUrlAuthchainResponse.
        :rtype: list[str]
        """
        return self._keychain

    @keychain.setter
    def keychain(self, keychain):
        r"""Sets the keychain of this CreateUrlAuthchainResponse.

        生成的鉴权串列表

        :param keychain: The keychain of this CreateUrlAuthchainResponse.
        :type keychain: list[str]
        """
        self._keychain = keychain

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
        if not isinstance(other, CreateUrlAuthchainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
