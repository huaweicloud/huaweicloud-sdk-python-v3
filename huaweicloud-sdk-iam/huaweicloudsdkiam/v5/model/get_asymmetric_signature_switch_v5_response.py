# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAsymmetricSignatureSwitchV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asymmetric_signature': 'AsymmetricSignatureWithDomainId'
    }

    attribute_map = {
        'asymmetric_signature': 'asymmetric_signature'
    }

    def __init__(self, asymmetric_signature=None):
        """GetAsymmetricSignatureSwitchV5Response

        The model defined in huaweicloud sdk

        :param asymmetric_signature: 
        :type asymmetric_signature: :class:`huaweicloudsdkiam.v5.AsymmetricSignatureWithDomainId`
        """
        
        super(GetAsymmetricSignatureSwitchV5Response, self).__init__()

        self._asymmetric_signature = None
        self.discriminator = None

        if asymmetric_signature is not None:
            self.asymmetric_signature = asymmetric_signature

    @property
    def asymmetric_signature(self):
        """Gets the asymmetric_signature of this GetAsymmetricSignatureSwitchV5Response.

        :return: The asymmetric_signature of this GetAsymmetricSignatureSwitchV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.AsymmetricSignatureWithDomainId`
        """
        return self._asymmetric_signature

    @asymmetric_signature.setter
    def asymmetric_signature(self, asymmetric_signature):
        """Sets the asymmetric_signature of this GetAsymmetricSignatureSwitchV5Response.

        :param asymmetric_signature: The asymmetric_signature of this GetAsymmetricSignatureSwitchV5Response.
        :type asymmetric_signature: :class:`huaweicloudsdkiam.v5.AsymmetricSignatureWithDomainId`
        """
        self._asymmetric_signature = asymmetric_signature

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
        if not isinstance(other, GetAsymmetricSignatureSwitchV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
