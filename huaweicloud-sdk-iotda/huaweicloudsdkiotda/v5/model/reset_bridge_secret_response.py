# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetBridgeSecretResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bridge_id': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'bridge_id': 'bridge_id',
        'secret': 'secret'
    }

    def __init__(self, bridge_id=None, secret=None):
        r"""ResetBridgeSecretResponse

        The model defined in huaweicloud sdk

        :param bridge_id: 网桥ID
        :type bridge_id: str
        :param secret: 网桥密钥。
        :type secret: str
        """
        
        super(ResetBridgeSecretResponse, self).__init__()

        self._bridge_id = None
        self._secret = None
        self.discriminator = None

        if bridge_id is not None:
            self.bridge_id = bridge_id
        if secret is not None:
            self.secret = secret

    @property
    def bridge_id(self):
        r"""Gets the bridge_id of this ResetBridgeSecretResponse.

        网桥ID

        :return: The bridge_id of this ResetBridgeSecretResponse.
        :rtype: str
        """
        return self._bridge_id

    @bridge_id.setter
    def bridge_id(self, bridge_id):
        r"""Sets the bridge_id of this ResetBridgeSecretResponse.

        网桥ID

        :param bridge_id: The bridge_id of this ResetBridgeSecretResponse.
        :type bridge_id: str
        """
        self._bridge_id = bridge_id

    @property
    def secret(self):
        r"""Gets the secret of this ResetBridgeSecretResponse.

        网桥密钥。

        :return: The secret of this ResetBridgeSecretResponse.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this ResetBridgeSecretResponse.

        网桥密钥。

        :param secret: The secret of this ResetBridgeSecretResponse.
        :type secret: str
        """
        self._secret = secret

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
        if not isinstance(other, ResetBridgeSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
