# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessPointRequestBody:

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
        'bandwidth_size': 'int'
    }

    attribute_map = {
        'region_id': 'region_id',
        'bandwidth_size': 'bandwidth_size'
    }

    def __init__(self, region_id=None, bandwidth_size=None):
        """CreateAccessPointRequestBody

        The model defined in huaweicloud sdk

        :param region_id: 区域ID
        :type region_id: str
        :param bandwidth_size: 带宽
        :type bandwidth_size: int
        """
        
        

        self._region_id = None
        self._bandwidth_size = None
        self.discriminator = None

        self.region_id = region_id
        self.bandwidth_size = bandwidth_size

    @property
    def region_id(self):
        """Gets the region_id of this CreateAccessPointRequestBody.

        区域ID

        :return: The region_id of this CreateAccessPointRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateAccessPointRequestBody.

        区域ID

        :param region_id: The region_id of this CreateAccessPointRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this CreateAccessPointRequestBody.

        带宽

        :return: The bandwidth_size of this CreateAccessPointRequestBody.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this CreateAccessPointRequestBody.

        带宽

        :param bandwidth_size: The bandwidth_size of this CreateAccessPointRequestBody.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

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
        if not isinstance(other, CreateAccessPointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
