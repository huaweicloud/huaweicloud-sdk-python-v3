# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateMacRequestBody:

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
        'message': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'mac_algorithm': 'mac_algorithm',
        'message': 'message'
    }

    def __init__(self, key_id=None, mac_algorithm=None, message=None):
        """GenerateMacRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param mac_algorithm: Mac算法，HMAC_SM3只有中国区支持。枚举如下： - HMAC_SHA_256 - HMAC_SHA_384 - HMAC_SHA_512 - HMAC_SM3
        :type mac_algorithm: str
        :param message: 待处理消息。原消息最小长度1、最大长度4096。请将原消息转为Base64格式后传入
        :type message: str
        """
        
        

        self._key_id = None
        self._mac_algorithm = None
        self._message = None
        self.discriminator = None

        self.key_id = key_id
        self.mac_algorithm = mac_algorithm
        self.message = message

    @property
    def key_id(self):
        """Gets the key_id of this GenerateMacRequestBody.

        密钥ID

        :return: The key_id of this GenerateMacRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this GenerateMacRequestBody.

        密钥ID

        :param key_id: The key_id of this GenerateMacRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def mac_algorithm(self):
        """Gets the mac_algorithm of this GenerateMacRequestBody.

        Mac算法，HMAC_SM3只有中国区支持。枚举如下： - HMAC_SHA_256 - HMAC_SHA_384 - HMAC_SHA_512 - HMAC_SM3

        :return: The mac_algorithm of this GenerateMacRequestBody.
        :rtype: str
        """
        return self._mac_algorithm

    @mac_algorithm.setter
    def mac_algorithm(self, mac_algorithm):
        """Sets the mac_algorithm of this GenerateMacRequestBody.

        Mac算法，HMAC_SM3只有中国区支持。枚举如下： - HMAC_SHA_256 - HMAC_SHA_384 - HMAC_SHA_512 - HMAC_SM3

        :param mac_algorithm: The mac_algorithm of this GenerateMacRequestBody.
        :type mac_algorithm: str
        """
        self._mac_algorithm = mac_algorithm

    @property
    def message(self):
        """Gets the message of this GenerateMacRequestBody.

        待处理消息。原消息最小长度1、最大长度4096。请将原消息转为Base64格式后传入

        :return: The message of this GenerateMacRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GenerateMacRequestBody.

        待处理消息。原消息最小长度1、最大长度4096。请将原消息转为Base64格式后传入

        :param message: The message of this GenerateMacRequestBody.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, GenerateMacRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
