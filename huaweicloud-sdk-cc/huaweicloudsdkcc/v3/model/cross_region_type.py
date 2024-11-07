# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CrossRegionType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cross_region_type': 'CrossRegionTypeEnum'
    }

    attribute_map = {
        'cross_region_type': 'cross_region_type'
    }

    def __init__(self, cross_region_type=None):
        """CrossRegionType

        The model defined in huaweicloud sdk

        :param cross_region_type: 
        :type cross_region_type: :class:`huaweicloudsdkcc.v3.CrossRegionTypeEnum`
        """
        
        

        self._cross_region_type = None
        self.discriminator = None

        self.cross_region_type = cross_region_type

    @property
    def cross_region_type(self):
        """Gets the cross_region_type of this CrossRegionType.

        :return: The cross_region_type of this CrossRegionType.
        :rtype: :class:`huaweicloudsdkcc.v3.CrossRegionTypeEnum`
        """
        return self._cross_region_type

    @cross_region_type.setter
    def cross_region_type(self, cross_region_type):
        """Sets the cross_region_type of this CrossRegionType.

        :param cross_region_type: The cross_region_type of this CrossRegionType.
        :type cross_region_type: :class:`huaweicloudsdkcc.v3.CrossRegionTypeEnum`
        """
        self._cross_region_type = cross_region_type

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
        if not isinstance(other, CrossRegionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
