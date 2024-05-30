# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClouddcnSubnetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clouddcn_subnet': 'ClouddcnSubnet'
    }

    attribute_map = {
        'clouddcn_subnet': 'clouddcn_subnet'
    }

    def __init__(self, clouddcn_subnet=None):
        """CreateClouddcnSubnetResponse

        The model defined in huaweicloud sdk

        :param clouddcn_subnet: 
        :type clouddcn_subnet: :class:`huaweicloudsdkvpc.v3.ClouddcnSubnet`
        """
        
        super(CreateClouddcnSubnetResponse, self).__init__()

        self._clouddcn_subnet = None
        self.discriminator = None

        if clouddcn_subnet is not None:
            self.clouddcn_subnet = clouddcn_subnet

    @property
    def clouddcn_subnet(self):
        """Gets the clouddcn_subnet of this CreateClouddcnSubnetResponse.

        :return: The clouddcn_subnet of this CreateClouddcnSubnetResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.ClouddcnSubnet`
        """
        return self._clouddcn_subnet

    @clouddcn_subnet.setter
    def clouddcn_subnet(self, clouddcn_subnet):
        """Sets the clouddcn_subnet of this CreateClouddcnSubnetResponse.

        :param clouddcn_subnet: The clouddcn_subnet of this CreateClouddcnSubnetResponse.
        :type clouddcn_subnet: :class:`huaweicloudsdkvpc.v3.ClouddcnSubnet`
        """
        self._clouddcn_subnet = clouddcn_subnet

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
        if not isinstance(other, CreateClouddcnSubnetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
