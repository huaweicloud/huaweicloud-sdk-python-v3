# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateMacResponse(SdkResponse):

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
        'mac': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'mac_algorithm': 'mac_algorithm',
        'mac': 'mac'
    }

    def __init__(self, key_id=None, mac_algorithm=None, mac=None):
        """GenerateMacResponse

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param mac_algorithm: Mac算法
        :type mac_algorithm: str
        :param mac: 生成的消息验证码
        :type mac: str
        """
        
        super(GenerateMacResponse, self).__init__()

        self._key_id = None
        self._mac_algorithm = None
        self._mac = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if mac_algorithm is not None:
            self.mac_algorithm = mac_algorithm
        if mac is not None:
            self.mac = mac

    @property
    def key_id(self):
        """Gets the key_id of this GenerateMacResponse.

        密钥ID

        :return: The key_id of this GenerateMacResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this GenerateMacResponse.

        密钥ID

        :param key_id: The key_id of this GenerateMacResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def mac_algorithm(self):
        """Gets the mac_algorithm of this GenerateMacResponse.

        Mac算法

        :return: The mac_algorithm of this GenerateMacResponse.
        :rtype: str
        """
        return self._mac_algorithm

    @mac_algorithm.setter
    def mac_algorithm(self, mac_algorithm):
        """Sets the mac_algorithm of this GenerateMacResponse.

        Mac算法

        :param mac_algorithm: The mac_algorithm of this GenerateMacResponse.
        :type mac_algorithm: str
        """
        self._mac_algorithm = mac_algorithm

    @property
    def mac(self):
        """Gets the mac of this GenerateMacResponse.

        生成的消息验证码

        :return: The mac of this GenerateMacResponse.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this GenerateMacResponse.

        生成的消息验证码

        :param mac: The mac of this GenerateMacResponse.
        :type mac: str
        """
        self._mac = mac

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
        if not isinstance(other, GenerateMacResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
