# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Region:

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
        'region_name': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'region_name': 'region_name'
    }

    def __init__(self, region_id=None, region_name=None):
        r"""Region

        The model defined in huaweicloud sdk

        :param region_id: 区域id
        :type region_id: str
        :param region_name: 区域名称
        :type region_name: str
        """
        
        

        self._region_id = None
        self._region_name = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name

    @property
    def region_id(self):
        r"""Gets the region_id of this Region.

        区域id

        :return: The region_id of this Region.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this Region.

        区域id

        :param region_id: The region_id of this Region.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        r"""Gets the region_name of this Region.

        区域名称

        :return: The region_name of this Region.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this Region.

        区域名称

        :param region_name: The region_name of this Region.
        :type region_name: str
        """
        self._region_name = region_name

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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
