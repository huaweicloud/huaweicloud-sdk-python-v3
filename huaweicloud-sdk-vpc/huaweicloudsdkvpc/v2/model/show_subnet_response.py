# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubnetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet': 'Subnet'
    }

    attribute_map = {
        'subnet': 'subnet'
    }

    def __init__(self, subnet=None):
        r"""ShowSubnetResponse

        The model defined in huaweicloud sdk

        :param subnet: 
        :type subnet: :class:`huaweicloudsdkvpc.v2.Subnet`
        """
        
        super(ShowSubnetResponse, self).__init__()

        self._subnet = None
        self.discriminator = None

        if subnet is not None:
            self.subnet = subnet

    @property
    def subnet(self):
        r"""Gets the subnet of this ShowSubnetResponse.

        :return: The subnet of this ShowSubnetResponse.
        :rtype: :class:`huaweicloudsdkvpc.v2.Subnet`
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        r"""Sets the subnet of this ShowSubnetResponse.

        :param subnet: The subnet of this ShowSubnetResponse.
        :type subnet: :class:`huaweicloudsdkvpc.v2.Subnet`
        """
        self._subnet = subnet

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
        if not isinstance(other, ShowSubnetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
