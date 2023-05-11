# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoreInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keystore_id': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'keystore_id': 'keystore_id',
        'domain_id': 'domain_id'
    }

    def __init__(self, keystore_id=None, domain_id=None):
        """KeystoreInfo

        The model defined in huaweicloud sdk

        :param keystore_id: 密钥库ID
        :type keystore_id: str
        :param domain_id: 用户域ID
        :type domain_id: str
        """
        
        

        self._keystore_id = None
        self._domain_id = None
        self.discriminator = None

        if keystore_id is not None:
            self.keystore_id = keystore_id
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def keystore_id(self):
        """Gets the keystore_id of this KeystoreInfo.

        密钥库ID

        :return: The keystore_id of this KeystoreInfo.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        """Sets the keystore_id of this KeystoreInfo.

        密钥库ID

        :param keystore_id: The keystore_id of this KeystoreInfo.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoreInfo.

        用户域ID

        :return: The domain_id of this KeystoreInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoreInfo.

        用户域ID

        :param domain_id: The domain_id of this KeystoreInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, KeystoreInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
