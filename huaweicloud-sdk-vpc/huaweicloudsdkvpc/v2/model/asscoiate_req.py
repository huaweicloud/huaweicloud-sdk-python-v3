# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsscoiateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnets': 'AssociateRouteTableAndSubnetReq'
    }

    attribute_map = {
        'subnets': 'subnets'
    }

    def __init__(self, subnets=None):
        """AsscoiateReq

        The model defined in huaweicloud sdk

        :param subnets: 
        :type subnets: :class:`huaweicloudsdkvpc.v2.AssociateRouteTableAndSubnetReq`
        """
        
        

        self._subnets = None
        self.discriminator = None

        self.subnets = subnets

    @property
    def subnets(self):
        """Gets the subnets of this AsscoiateReq.

        :return: The subnets of this AsscoiateReq.
        :rtype: :class:`huaweicloudsdkvpc.v2.AssociateRouteTableAndSubnetReq`
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this AsscoiateReq.

        :param subnets: The subnets of this AsscoiateReq.
        :type subnets: :class:`huaweicloudsdkvpc.v2.AssociateRouteTableAndSubnetReq`
        """
        self._subnets = subnets

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
        if not isinstance(other, AsscoiateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
