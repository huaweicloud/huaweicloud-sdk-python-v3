# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptCluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_key_id': 'str',
        'master_key_name': 'str',
        'crypt_algorithm': 'str'
    }

    attribute_map = {
        'master_key_id': 'master_key_id',
        'master_key_name': 'master_key_name',
        'crypt_algorithm': 'crypt_algorithm'
    }

    def __init__(self, master_key_id=None, master_key_name=None, crypt_algorithm=None):
        r"""EncryptCluster

        The model defined in huaweicloud sdk

        :param master_key_id: **参数解释**： KMS密钥ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type master_key_id: str
        :param master_key_name: **参数解释**： KMS密钥名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type master_key_name: str
        :param crypt_algorithm: **参数解释**： 加密类型。国密、国际加密。 **约束限制**： 不涉及。 **取值范围**： generalCipher：AES-CBC算法加密。 SMcompatible：sm4算法加密。 **默认取值**： 不涉及。
        :type crypt_algorithm: str
        """
        
        

        self._master_key_id = None
        self._master_key_name = None
        self._crypt_algorithm = None
        self.discriminator = None

        self.master_key_id = master_key_id
        if master_key_name is not None:
            self.master_key_name = master_key_name
        self.crypt_algorithm = crypt_algorithm

    @property
    def master_key_id(self):
        r"""Gets the master_key_id of this EncryptCluster.

        **参数解释**： KMS密钥ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The master_key_id of this EncryptCluster.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        r"""Sets the master_key_id of this EncryptCluster.

        **参数解释**： KMS密钥ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param master_key_id: The master_key_id of this EncryptCluster.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

    @property
    def master_key_name(self):
        r"""Gets the master_key_name of this EncryptCluster.

        **参数解释**： KMS密钥名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The master_key_name of this EncryptCluster.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        r"""Sets the master_key_name of this EncryptCluster.

        **参数解释**： KMS密钥名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param master_key_name: The master_key_name of this EncryptCluster.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def crypt_algorithm(self):
        r"""Gets the crypt_algorithm of this EncryptCluster.

        **参数解释**： 加密类型。国密、国际加密。 **约束限制**： 不涉及。 **取值范围**： generalCipher：AES-CBC算法加密。 SMcompatible：sm4算法加密。 **默认取值**： 不涉及。

        :return: The crypt_algorithm of this EncryptCluster.
        :rtype: str
        """
        return self._crypt_algorithm

    @crypt_algorithm.setter
    def crypt_algorithm(self, crypt_algorithm):
        r"""Sets the crypt_algorithm of this EncryptCluster.

        **参数解释**： 加密类型。国密、国际加密。 **约束限制**： 不涉及。 **取值范围**： generalCipher：AES-CBC算法加密。 SMcompatible：sm4算法加密。 **默认取值**： 不涉及。

        :param crypt_algorithm: The crypt_algorithm of this EncryptCluster.
        :type crypt_algorithm: str
        """
        self._crypt_algorithm = crypt_algorithm

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
        if not isinstance(other, EncryptCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
