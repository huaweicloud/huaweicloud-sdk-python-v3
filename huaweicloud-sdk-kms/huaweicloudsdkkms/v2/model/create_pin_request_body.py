# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePinRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pin_type': 'str',
        'keystore_id': 'str'
    }

    attribute_map = {
        'pin_type': 'pin_type',
        'keystore_id': 'keystore_id'
    }

    def __init__(self, pin_type=None, keystore_id=None):
        r"""CreatePinRequestBody

        The model defined in huaweicloud sdk

        :param pin_type: pin码的类型，默认为“CipherText”： - PlainText - CipherText
        :type pin_type: str
        :param keystore_id: 密钥库ID，指定密文pin时必选： 1：管理面manage_az集群（共享卡集群） 2：数据面共享集群(pod区) 其它：租户专属
        :type keystore_id: str
        """
        
        

        self._pin_type = None
        self._keystore_id = None
        self.discriminator = None

        if pin_type is not None:
            self.pin_type = pin_type
        if keystore_id is not None:
            self.keystore_id = keystore_id

    @property
    def pin_type(self):
        r"""Gets the pin_type of this CreatePinRequestBody.

        pin码的类型，默认为“CipherText”： - PlainText - CipherText

        :return: The pin_type of this CreatePinRequestBody.
        :rtype: str
        """
        return self._pin_type

    @pin_type.setter
    def pin_type(self, pin_type):
        r"""Sets the pin_type of this CreatePinRequestBody.

        pin码的类型，默认为“CipherText”： - PlainText - CipherText

        :param pin_type: The pin_type of this CreatePinRequestBody.
        :type pin_type: str
        """
        self._pin_type = pin_type

    @property
    def keystore_id(self):
        r"""Gets the keystore_id of this CreatePinRequestBody.

        密钥库ID，指定密文pin时必选： 1：管理面manage_az集群（共享卡集群） 2：数据面共享集群(pod区) 其它：租户专属

        :return: The keystore_id of this CreatePinRequestBody.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        r"""Sets the keystore_id of this CreatePinRequestBody.

        密钥库ID，指定密文pin时必选： 1：管理面manage_az集群（共享卡集群） 2：数据面共享集群(pod区) 其它：租户专属

        :param keystore_id: The keystore_id of this CreatePinRequestBody.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

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
        if not isinstance(other, CreatePinRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
