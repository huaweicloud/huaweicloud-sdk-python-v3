# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataEncryption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cmkid': 'str',
        'encrypted_algorithm': 'str'
    }

    attribute_map = {
        'cmkid': 'cmkid',
        'encrypted_algorithm': 'encrypted_algorithm'
    }

    def __init__(self, cmkid=None, encrypted_algorithm=None):
        r"""DataEncryption

        The model defined in huaweicloud sdk

        :param cmkid: 存储库的密钥ID。如果为非加密存储库，默认值为None
        :type cmkid: str
        :param encrypted_algorithm: 存储库的加密算法类型。如果为非加密存储库，默认值为None
        :type encrypted_algorithm: str
        """
        
        

        self._cmkid = None
        self._encrypted_algorithm = None
        self.discriminator = None

        if cmkid is not None:
            self.cmkid = cmkid
        if encrypted_algorithm is not None:
            self.encrypted_algorithm = encrypted_algorithm

    @property
    def cmkid(self):
        r"""Gets the cmkid of this DataEncryption.

        存储库的密钥ID。如果为非加密存储库，默认值为None

        :return: The cmkid of this DataEncryption.
        :rtype: str
        """
        return self._cmkid

    @cmkid.setter
    def cmkid(self, cmkid):
        r"""Sets the cmkid of this DataEncryption.

        存储库的密钥ID。如果为非加密存储库，默认值为None

        :param cmkid: The cmkid of this DataEncryption.
        :type cmkid: str
        """
        self._cmkid = cmkid

    @property
    def encrypted_algorithm(self):
        r"""Gets the encrypted_algorithm of this DataEncryption.

        存储库的加密算法类型。如果为非加密存储库，默认值为None

        :return: The encrypted_algorithm of this DataEncryption.
        :rtype: str
        """
        return self._encrypted_algorithm

    @encrypted_algorithm.setter
    def encrypted_algorithm(self, encrypted_algorithm):
        r"""Sets the encrypted_algorithm of this DataEncryption.

        存储库的加密算法类型。如果为非加密存储库，默认值为None

        :param encrypted_algorithm: The encrypted_algorithm of this DataEncryption.
        :type encrypted_algorithm: str
        """
        self._encrypted_algorithm = encrypted_algorithm

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataEncryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
