# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainRegionIspDetail:


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
        'isp': 'str',
        'flux': 'list[int]'
    }

    attribute_map = {
        'region': 'region',
        'isp': 'isp',
        'flux': 'flux'
    }

    def __init__(self, region=None, isp=None, flux=None):
        """DomainRegionIspDetail - a model defined in huaweicloud sdk"""
        
        

        self._region = None
        self._isp = None
        self._flux = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if flux is not None:
            self.flux = flux

    @property
    def region(self):
        """Gets the region of this DomainRegionIspDetail.

        区域

        :return: The region of this DomainRegionIspDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DomainRegionIspDetail.

        区域

        :param region: The region of this DomainRegionIspDetail.
        :type: str
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this DomainRegionIspDetail.

        运营商

        :return: The isp of this DomainRegionIspDetail.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this DomainRegionIspDetail.

        运营商

        :param isp: The isp of this DomainRegionIspDetail.
        :type: str
        """
        self._isp = isp

    @property
    def flux(self):
        """Gets the flux of this DomainRegionIspDetail.

        流量

        :return: The flux of this DomainRegionIspDetail.
        :rtype: list[int]
        """
        return self._flux

    @flux.setter
    def flux(self, flux):
        """Sets the flux of this DomainRegionIspDetail.

        流量

        :param flux: The flux of this DomainRegionIspDetail.
        :type: list[int]
        """
        self._flux = flux

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
        if not isinstance(other, DomainRegionIspDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
