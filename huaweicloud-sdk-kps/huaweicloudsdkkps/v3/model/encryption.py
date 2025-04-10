# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Encryption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'kms_key_name': 'str',
        'kms_key_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'kms_key_name': 'kms_key_name',
        'kms_key_id': 'kms_key_id'
    }

    def __init__(self, type=None, kms_key_name=None, kms_key_id=None):
        r"""Encryption

        The model defined in huaweicloud sdk

        :param type: 取值范围：“kms”或“default”。 - “default”为默认加密方式，适用于没有kms服务的局点。 - “kms”为采用kms服务加密方式。 若局点没有kms服务，请填“default”。
        :type type: str
        :param kms_key_name: kms密钥的名称。  - 若“type”为“kms”，则必须填入\&quot;kms_key_name\&quot;或\&quot;kms_key_id\&quot;。
        :type kms_key_name: str
        :param kms_key_id: kms密钥的ID。  - 若“type”为“kms”，则必须填入\&quot;kms_key_name\&quot;或\&quot;kms_key_id\&quot;。
        :type kms_key_id: str
        """
        
        

        self._type = None
        self._kms_key_name = None
        self._kms_key_id = None
        self.discriminator = None

        self.type = type
        if kms_key_name is not None:
            self.kms_key_name = kms_key_name
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id

    @property
    def type(self):
        r"""Gets the type of this Encryption.

        取值范围：“kms”或“default”。 - “default”为默认加密方式，适用于没有kms服务的局点。 - “kms”为采用kms服务加密方式。 若局点没有kms服务，请填“default”。

        :return: The type of this Encryption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Encryption.

        取值范围：“kms”或“default”。 - “default”为默认加密方式，适用于没有kms服务的局点。 - “kms”为采用kms服务加密方式。 若局点没有kms服务，请填“default”。

        :param type: The type of this Encryption.
        :type type: str
        """
        self._type = type

    @property
    def kms_key_name(self):
        r"""Gets the kms_key_name of this Encryption.

        kms密钥的名称。  - 若“type”为“kms”，则必须填入\"kms_key_name\"或\"kms_key_id\"。

        :return: The kms_key_name of this Encryption.
        :rtype: str
        """
        return self._kms_key_name

    @kms_key_name.setter
    def kms_key_name(self, kms_key_name):
        r"""Sets the kms_key_name of this Encryption.

        kms密钥的名称。  - 若“type”为“kms”，则必须填入\"kms_key_name\"或\"kms_key_id\"。

        :param kms_key_name: The kms_key_name of this Encryption.
        :type kms_key_name: str
        """
        self._kms_key_name = kms_key_name

    @property
    def kms_key_id(self):
        r"""Gets the kms_key_id of this Encryption.

        kms密钥的ID。  - 若“type”为“kms”，则必须填入\"kms_key_name\"或\"kms_key_id\"。

        :return: The kms_key_id of this Encryption.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        r"""Sets the kms_key_id of this Encryption.

        kms密钥的ID。  - 若“type”为“kms”，则必须填入\"kms_key_name\"或\"kms_key_id\"。

        :param kms_key_id: The kms_key_id of this Encryption.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

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
        if not isinstance(other, Encryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
