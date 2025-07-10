# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSiteConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone_id': 'str',
        'site_type': 'str'
    }

    attribute_map = {
        'availability_zone_id': 'availability_zone_id',
        'site_type': 'site_type'
    }

    def __init__(self, availability_zone_id=None, site_type=None):
        r"""ListSiteConfigsRequest

        The model defined in huaweicloud sdk

        :param availability_zone_id: 可用区。
        :type availability_zone_id: str
        :param site_type: 站点类型，支持CENTER、IES。
        :type site_type: str
        """
        
        

        self._availability_zone_id = None
        self._site_type = None
        self.discriminator = None

        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if site_type is not None:
            self.site_type = site_type

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this ListSiteConfigsRequest.

        可用区。

        :return: The availability_zone_id of this ListSiteConfigsRequest.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this ListSiteConfigsRequest.

        可用区。

        :param availability_zone_id: The availability_zone_id of this ListSiteConfigsRequest.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def site_type(self):
        r"""Gets the site_type of this ListSiteConfigsRequest.

        站点类型，支持CENTER、IES。

        :return: The site_type of this ListSiteConfigsRequest.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this ListSiteConfigsRequest.

        站点类型，支持CENTER、IES。

        :param site_type: The site_type of this ListSiteConfigsRequest.
        :type site_type: str
        """
        self._site_type = site_type

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
        if not isinstance(other, ListSiteConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
