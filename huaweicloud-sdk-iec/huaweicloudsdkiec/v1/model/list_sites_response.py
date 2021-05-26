# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSitesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'sites': 'list[Site]'
    }

    attribute_map = {
        'count': 'count',
        'sites': 'sites'
    }

    def __init__(self, count=None, sites=None):
        """ListSitesResponse - a model defined in huaweicloud sdk"""
        
        super(ListSitesResponse, self).__init__()

        self._count = None
        self._sites = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if sites is not None:
            self.sites = sites

    @property
    def count(self):
        """Gets the count of this ListSitesResponse.

        边缘站点总数。

        :return: The count of this ListSitesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSitesResponse.

        边缘站点总数。

        :param count: The count of this ListSitesResponse.
        :type: int
        """
        self._count = count

    @property
    def sites(self):
        """Gets the sites of this ListSitesResponse.

        站点列表。

        :return: The sites of this ListSitesResponse.
        :rtype: list[Site]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this ListSitesResponse.

        站点列表。

        :param sites: The sites of this ListSitesResponse.
        :type: list[Site]
        """
        self._sites = sites

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSitesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
