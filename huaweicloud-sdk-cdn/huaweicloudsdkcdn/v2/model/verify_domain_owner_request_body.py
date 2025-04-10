# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyDomainOwnerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verify_type': 'str'
    }

    attribute_map = {
        'verify_type': 'verify_type'
    }

    def __init__(self, verify_type=None):
        r"""VerifyDomainOwnerRequestBody

        The model defined in huaweicloud sdk

        :param verify_type: 校验类型： - dns：DNS解析校验； - file：文件校验； - all：DNS与文件都会进行探测，默认为all。
        :type verify_type: str
        """
        
        

        self._verify_type = None
        self.discriminator = None

        if verify_type is not None:
            self.verify_type = verify_type

    @property
    def verify_type(self):
        r"""Gets the verify_type of this VerifyDomainOwnerRequestBody.

        校验类型： - dns：DNS解析校验； - file：文件校验； - all：DNS与文件都会进行探测，默认为all。

        :return: The verify_type of this VerifyDomainOwnerRequestBody.
        :rtype: str
        """
        return self._verify_type

    @verify_type.setter
    def verify_type(self, verify_type):
        r"""Sets the verify_type of this VerifyDomainOwnerRequestBody.

        校验类型： - dns：DNS解析校验； - file：文件校验； - all：DNS与文件都会进行探测，默认为all。

        :param verify_type: The verify_type of this VerifyDomainOwnerRequestBody.
        :type verify_type: str
        """
        self._verify_type = verify_type

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
        if not isinstance(other, VerifyDomainOwnerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
