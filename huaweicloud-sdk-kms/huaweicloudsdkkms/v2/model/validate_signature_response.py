# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateSignatureResponse(SdkResponse):


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
        'signature_vaild': 'bool'
    }

    attribute_map = {
        'key_id': 'key_id',
        'signature_vaild': 'signature_vaild'
    }

    def __init__(self, key_id=None, signature_vaild=None):
        """ValidateSignatureResponse - a model defined in huaweicloud sdk"""
        
        super(ValidateSignatureResponse, self).__init__()

        self._key_id = None
        self._signature_vaild = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if signature_vaild is not None:
            self.signature_vaild = signature_vaild

    @property
    def key_id(self):
        """Gets the key_id of this ValidateSignatureResponse.

        密钥ID。

        :return: The key_id of this ValidateSignatureResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this ValidateSignatureResponse.

        密钥ID。

        :param key_id: The key_id of this ValidateSignatureResponse.
        :type: str
        """
        self._key_id = key_id

    @property
    def signature_vaild(self):
        """Gets the signature_vaild of this ValidateSignatureResponse.

        签名验证合法性，“true”表示验证签名合法，“false”表示验证签名非法。

        :return: The signature_vaild of this ValidateSignatureResponse.
        :rtype: bool
        """
        return self._signature_vaild

    @signature_vaild.setter
    def signature_vaild(self, signature_vaild):
        """Sets the signature_vaild of this ValidateSignatureResponse.

        签名验证合法性，“true”表示验证签名合法，“false”表示验证签名非法。

        :param signature_vaild: The signature_vaild of this ValidateSignatureResponse.
        :type: bool
        """
        self._signature_vaild = signature_vaild

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
        if not isinstance(other, ValidateSignatureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
