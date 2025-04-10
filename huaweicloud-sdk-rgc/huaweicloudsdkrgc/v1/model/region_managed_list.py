# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegionManagedList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'region_status': 'str'
    }

    attribute_map = {
        'region': 'region',
        'region_status': 'region_status'
    }

    def __init__(self, region=None, region_status=None):
        r"""RegionManagedList

        The model defined in huaweicloud sdk

        :param region: 区域名字。
        :type region: str
        :param region_status: 区域的状态，取值为可用或者不可用。
        :type region_status: str
        """
        
        

        self._region = None
        self._region_status = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if region_status is not None:
            self.region_status = region_status

    @property
    def region(self):
        r"""Gets the region of this RegionManagedList.

        区域名字。

        :return: The region of this RegionManagedList.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RegionManagedList.

        区域名字。

        :param region: The region of this RegionManagedList.
        :type region: str
        """
        self._region = region

    @property
    def region_status(self):
        r"""Gets the region_status of this RegionManagedList.

        区域的状态，取值为可用或者不可用。

        :return: The region_status of this RegionManagedList.
        :rtype: str
        """
        return self._region_status

    @region_status.setter
    def region_status(self, region_status):
        r"""Sets the region_status of this RegionManagedList.

        区域的状态，取值为可用或者不可用。

        :param region_status: The region_status of this RegionManagedList.
        :type region_status: str
        """
        self._region_status = region_status

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
        if not isinstance(other, RegionManagedList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
