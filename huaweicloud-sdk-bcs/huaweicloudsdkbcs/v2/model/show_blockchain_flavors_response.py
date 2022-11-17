# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBlockchainFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_spec': 'InstanceSpc'
    }

    attribute_map = {
        'enterprise_spec': 'enterprise_spec'
    }

    def __init__(self, enterprise_spec=None):
        """ShowBlockchainFlavorsResponse

        The model defined in huaweicloud sdk

        :param enterprise_spec: 
        :type enterprise_spec: :class:`huaweicloudsdkbcs.v2.InstanceSpc`
        """
        
        super(ShowBlockchainFlavorsResponse, self).__init__()

        self._enterprise_spec = None
        self.discriminator = None

        if enterprise_spec is not None:
            self.enterprise_spec = enterprise_spec

    @property
    def enterprise_spec(self):
        """Gets the enterprise_spec of this ShowBlockchainFlavorsResponse.

        :return: The enterprise_spec of this ShowBlockchainFlavorsResponse.
        :rtype: :class:`huaweicloudsdkbcs.v2.InstanceSpc`
        """
        return self._enterprise_spec

    @enterprise_spec.setter
    def enterprise_spec(self, enterprise_spec):
        """Sets the enterprise_spec of this ShowBlockchainFlavorsResponse.

        :param enterprise_spec: The enterprise_spec of this ShowBlockchainFlavorsResponse.
        :type enterprise_spec: :class:`huaweicloudsdkbcs.v2.InstanceSpc`
        """
        self._enterprise_spec = enterprise_spec

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
        if not isinstance(other, ShowBlockchainFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
