# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyMacResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'mac_algorithm': 'str',
        'mac_valid': 'bool'
    }

    attribute_map = {
        'key_id': 'key_id',
        'mac_algorithm': 'mac_algorithm',
        'mac_valid': 'mac_valid'
    }

    def __init__(self, key_id=None, mac_algorithm=None, mac_valid=None):
        r"""VerifyMacResponse

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param mac_algorithm: MAC算法
        :type mac_algorithm: str
        :param mac_valid: 消息验证码校验结果
        :type mac_valid: bool
        """
        
        super(VerifyMacResponse, self).__init__()

        self._key_id = None
        self._mac_algorithm = None
        self._mac_valid = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if mac_algorithm is not None:
            self.mac_algorithm = mac_algorithm
        if mac_valid is not None:
            self.mac_valid = mac_valid

    @property
    def key_id(self):
        r"""Gets the key_id of this VerifyMacResponse.

        密钥ID

        :return: The key_id of this VerifyMacResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this VerifyMacResponse.

        密钥ID

        :param key_id: The key_id of this VerifyMacResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def mac_algorithm(self):
        r"""Gets the mac_algorithm of this VerifyMacResponse.

        MAC算法

        :return: The mac_algorithm of this VerifyMacResponse.
        :rtype: str
        """
        return self._mac_algorithm

    @mac_algorithm.setter
    def mac_algorithm(self, mac_algorithm):
        r"""Sets the mac_algorithm of this VerifyMacResponse.

        MAC算法

        :param mac_algorithm: The mac_algorithm of this VerifyMacResponse.
        :type mac_algorithm: str
        """
        self._mac_algorithm = mac_algorithm

    @property
    def mac_valid(self):
        r"""Gets the mac_valid of this VerifyMacResponse.

        消息验证码校验结果

        :return: The mac_valid of this VerifyMacResponse.
        :rtype: bool
        """
        return self._mac_valid

    @mac_valid.setter
    def mac_valid(self, mac_valid):
        r"""Sets the mac_valid of this VerifyMacResponse.

        消息验证码校验结果

        :param mac_valid: The mac_valid of this VerifyMacResponse.
        :type mac_valid: bool
        """
        self._mac_valid = mac_valid

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
        if not isinstance(other, VerifyMacResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
