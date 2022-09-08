# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseRouterAZ:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone_ids': 'list[str]'
    }

    attribute_map = {
        'availability_zone_ids': 'availability_zone_ids'
    }

    def __init__(self, availability_zone_ids=None):
        """EnterpriseRouterAZ

        The model defined in huaweicloud sdk

        :param availability_zone_ids: 企业路由器实例所在的可用区
        :type availability_zone_ids: list[str]
        """
        
        

        self._availability_zone_ids = None
        self.discriminator = None

        self.availability_zone_ids = availability_zone_ids

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this EnterpriseRouterAZ.

        企业路由器实例所在的可用区

        :return: The availability_zone_ids of this EnterpriseRouterAZ.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this EnterpriseRouterAZ.

        企业路由器实例所在的可用区

        :param availability_zone_ids: The availability_zone_ids of this EnterpriseRouterAZ.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

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
        if not isinstance(other, EnterpriseRouterAZ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
