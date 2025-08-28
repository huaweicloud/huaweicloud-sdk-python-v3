# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsymmetricSignatureWithDomainId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'asymmetric_signature_switch': 'bool'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'asymmetric_signature_switch': 'asymmetric_signature_switch'
    }

    def __init__(self, domain_id=None, asymmetric_signature_switch=None):
        r"""AsymmetricSignatureWithDomainId

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID。
        :type domain_id: str
        :param asymmetric_signature_switch: 非对称签名开关。
        :type asymmetric_signature_switch: bool
        """
        
        

        self._domain_id = None
        self._asymmetric_signature_switch = None
        self.discriminator = None

        self.domain_id = domain_id
        self.asymmetric_signature_switch = asymmetric_signature_switch

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AsymmetricSignatureWithDomainId.

        账号ID。

        :return: The domain_id of this AsymmetricSignatureWithDomainId.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AsymmetricSignatureWithDomainId.

        账号ID。

        :param domain_id: The domain_id of this AsymmetricSignatureWithDomainId.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def asymmetric_signature_switch(self):
        r"""Gets the asymmetric_signature_switch of this AsymmetricSignatureWithDomainId.

        非对称签名开关。

        :return: The asymmetric_signature_switch of this AsymmetricSignatureWithDomainId.
        :rtype: bool
        """
        return self._asymmetric_signature_switch

    @asymmetric_signature_switch.setter
    def asymmetric_signature_switch(self, asymmetric_signature_switch):
        r"""Sets the asymmetric_signature_switch of this AsymmetricSignatureWithDomainId.

        非对称签名开关。

        :param asymmetric_signature_switch: The asymmetric_signature_switch of this AsymmetricSignatureWithDomainId.
        :type asymmetric_signature_switch: bool
        """
        self._asymmetric_signature_switch = asymmetric_signature_switch

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
        if not isinstance(other, AsymmetricSignatureWithDomainId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
