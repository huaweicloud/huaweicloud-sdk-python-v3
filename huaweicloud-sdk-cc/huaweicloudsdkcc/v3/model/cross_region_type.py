# coding: utf-8

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
        'cross_region_type': 'str'
    }

    attribute_map = {
        'cross_region_type': 'cross_region_type'
    }

    def __init__(self, cross_region_type=None):
        r"""CrossRegionType

        The model defined in huaweicloud sdk

        :param cross_region_type: 跨地域类型。 - intra-region （同地域） - inter-region （跨地域）
        :type cross_region_type: str
        """
        
        

        self._cross_region_type = None
        self.discriminator = None

        self.cross_region_type = cross_region_type

    @property
    def cross_region_type(self):
        r"""Gets the cross_region_type of this CrossRegionType.

        跨地域类型。 - intra-region （同地域） - inter-region （跨地域）

        :return: The cross_region_type of this CrossRegionType.
        :rtype: str
        """
        return self._cross_region_type

    @cross_region_type.setter
    def cross_region_type(self, cross_region_type):
        r"""Sets the cross_region_type of this CrossRegionType.

        跨地域类型。 - intra-region （同地域） - inter-region （跨地域）

        :param cross_region_type: The cross_region_type of this CrossRegionType.
        :type cross_region_type: str
        """
        self._cross_region_type = cross_region_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
