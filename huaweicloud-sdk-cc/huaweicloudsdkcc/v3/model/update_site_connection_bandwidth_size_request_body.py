# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSiteConnectionBandwidthSizeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_connection': 'UpdateSiteConnectionBandwidthSize'
    }

    attribute_map = {
        'site_connection': 'site_connection'
    }

    def __init__(self, site_connection=None):
        r"""UpdateSiteConnectionBandwidthSizeRequestBody

        The model defined in huaweicloud sdk

        :param site_connection: 
        :type site_connection: :class:`huaweicloudsdkcc.v3.UpdateSiteConnectionBandwidthSize`
        """
        
        

        self._site_connection = None
        self.discriminator = None

        self.site_connection = site_connection

    @property
    def site_connection(self):
        r"""Gets the site_connection of this UpdateSiteConnectionBandwidthSizeRequestBody.

        :return: The site_connection of this UpdateSiteConnectionBandwidthSizeRequestBody.
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateSiteConnectionBandwidthSize`
        """
        return self._site_connection

    @site_connection.setter
    def site_connection(self, site_connection):
        r"""Sets the site_connection of this UpdateSiteConnectionBandwidthSizeRequestBody.

        :param site_connection: The site_connection of this UpdateSiteConnectionBandwidthSizeRequestBody.
        :type site_connection: :class:`huaweicloudsdkcc.v3.UpdateSiteConnectionBandwidthSize`
        """
        self._site_connection = site_connection

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
        if not isinstance(other, UpdateSiteConnectionBandwidthSizeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
