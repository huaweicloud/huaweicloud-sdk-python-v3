# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateSubnetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_ids': 'list[str]'
    }

    attribute_map = {
        'subnet_ids': 'subnet_ids'
    }

    def __init__(self, subnet_ids=None):
        """AssociateSubnetRequestBody

        The model defined in huaweicloud sdk

        :param subnet_ids: 子网ID
        :type subnet_ids: list[str]
        """
        
        

        self._subnet_ids = None
        self.discriminator = None

        self.subnet_ids = subnet_ids

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this AssociateSubnetRequestBody.

        子网ID

        :return: The subnet_ids of this AssociateSubnetRequestBody.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this AssociateSubnetRequestBody.

        子网ID

        :param subnet_ids: The subnet_ids of this AssociateSubnetRequestBody.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

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
        if not isinstance(other, AssociateSubnetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
