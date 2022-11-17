# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptionStructure:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kms': 'KmsStructure'
    }

    attribute_map = {
        'kms': 'kms'
    }

    def __init__(self, kms=None):
        """EncryptionStructure

        The model defined in huaweicloud sdk

        :param kms: 
        :type kms: :class:`huaweicloudsdkaos.v1.KmsStructure`
        """
        
        

        self._kms = None
        self.discriminator = None

        self.kms = kms

    @property
    def kms(self):
        """Gets the kms of this EncryptionStructure.

        :return: The kms of this EncryptionStructure.
        :rtype: :class:`huaweicloudsdkaos.v1.KmsStructure`
        """
        return self._kms

    @kms.setter
    def kms(self, kms):
        """Sets the kms of this EncryptionStructure.

        :param kms: The kms of this EncryptionStructure.
        :type kms: :class:`huaweicloudsdkaos.v1.KmsStructure`
        """
        self._kms = kms

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
        if not isinstance(other, EncryptionStructure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
