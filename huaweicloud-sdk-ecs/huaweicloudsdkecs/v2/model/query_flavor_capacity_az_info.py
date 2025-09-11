# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryFlavorCapacityAzInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'availability_zone': 'str',
        'prefer': 'bool'
    }

    attribute_map = {
        'region_id': 'region_id',
        'availability_zone': 'availability_zone',
        'prefer': 'prefer'
    }

    def __init__(self, region_id=None, availability_zone=None, prefer=None):
        r"""QueryFlavorCapacityAzInfo

        The model defined in huaweicloud sdk

        :param region_id: 
        :type region_id: str
        :param availability_zone: 
        :type availability_zone: str
        :param prefer: 
        :type prefer: bool
        """
        
        

        self._region_id = None
        self._availability_zone = None
        self._prefer = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if prefer is not None:
            self.prefer = prefer

    @property
    def region_id(self):
        r"""Gets the region_id of this QueryFlavorCapacityAzInfo.

        :return: The region_id of this QueryFlavorCapacityAzInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this QueryFlavorCapacityAzInfo.

        :param region_id: The region_id of this QueryFlavorCapacityAzInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this QueryFlavorCapacityAzInfo.

        :return: The availability_zone of this QueryFlavorCapacityAzInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this QueryFlavorCapacityAzInfo.

        :param availability_zone: The availability_zone of this QueryFlavorCapacityAzInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def prefer(self):
        r"""Gets the prefer of this QueryFlavorCapacityAzInfo.

        :return: The prefer of this QueryFlavorCapacityAzInfo.
        :rtype: bool
        """
        return self._prefer

    @prefer.setter
    def prefer(self, prefer):
        r"""Sets the prefer of this QueryFlavorCapacityAzInfo.

        :param prefer: The prefer of this QueryFlavorCapacityAzInfo.
        :type prefer: bool
        """
        self._prefer = prefer

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
        if not isinstance(other, QueryFlavorCapacityAzInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
