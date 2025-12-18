# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlavorCapacityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'count': 'str',
        'region_ids': 'str'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'count': 'count',
        'region_ids': 'region_ids'
    }

    def __init__(self, flavor_id=None, count=None, region_ids=None):
        r"""ShowFlavorCapacityRequest

        The model defined in huaweicloud sdk

        :param flavor_id: 
        :type flavor_id: str
        :param count: 
        :type count: str
        :param region_ids: 
        :type region_ids: str
        """
        
        

        self._flavor_id = None
        self._count = None
        self._region_ids = None
        self.discriminator = None

        self.flavor_id = flavor_id
        if count is not None:
            self.count = count
        if region_ids is not None:
            self.region_ids = region_ids

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ShowFlavorCapacityRequest.

        :return: The flavor_id of this ShowFlavorCapacityRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ShowFlavorCapacityRequest.

        :param flavor_id: The flavor_id of this ShowFlavorCapacityRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def count(self):
        r"""Gets the count of this ShowFlavorCapacityRequest.

        :return: The count of this ShowFlavorCapacityRequest.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowFlavorCapacityRequest.

        :param count: The count of this ShowFlavorCapacityRequest.
        :type count: str
        """
        self._count = count

    @property
    def region_ids(self):
        r"""Gets the region_ids of this ShowFlavorCapacityRequest.

        :return: The region_ids of this ShowFlavorCapacityRequest.
        :rtype: str
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        r"""Sets the region_ids of this ShowFlavorCapacityRequest.

        :param region_ids: The region_ids of this ShowFlavorCapacityRequest.
        :type region_ids: str
        """
        self._region_ids = region_ids

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
        if not isinstance(other, ShowFlavorCapacityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
