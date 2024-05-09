# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcEgressRequestBodySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidrs': 'list[EgressCidr]'
    }

    attribute_map = {
        'cidrs': 'cidrs'
    }

    def __init__(self, cidrs=None):
        """VpcEgressRequestBodySpec

        The model defined in huaweicloud sdk

        :param cidrs: CAE环境访问VPC配置。
        :type cidrs: list[:class:`huaweicloudsdkcae.v1.EgressCidr`]
        """
        
        

        self._cidrs = None
        self.discriminator = None

        self.cidrs = cidrs

    @property
    def cidrs(self):
        """Gets the cidrs of this VpcEgressRequestBodySpec.

        CAE环境访问VPC配置。

        :return: The cidrs of this VpcEgressRequestBodySpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.EgressCidr`]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this VpcEgressRequestBodySpec.

        CAE环境访问VPC配置。

        :param cidrs: The cidrs of this VpcEgressRequestBodySpec.
        :type cidrs: list[:class:`huaweicloudsdkcae.v1.EgressCidr`]
        """
        self._cidrs = cidrs

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
        if not isinstance(other, VpcEgressRequestBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
