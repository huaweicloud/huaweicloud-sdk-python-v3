# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateSiteNetworkBandwidthRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_network_id': 'str',
        'site_connection_id': 'str'
    }

    attribute_map = {
        'site_network_id': 'site_network_id',
        'site_connection_id': 'site_connection_id'
    }

    def __init__(self, site_network_id=None, site_connection_id=None):
        r"""DisassociateSiteNetworkBandwidthRequest

        The model defined in huaweicloud sdk

        :param site_network_id: 分支网络的ID。
        :type site_network_id: str
        :param site_connection_id: 实例ID。
        :type site_connection_id: str
        """
        
        

        self._site_network_id = None
        self._site_connection_id = None
        self.discriminator = None

        self.site_network_id = site_network_id
        self.site_connection_id = site_connection_id

    @property
    def site_network_id(self):
        r"""Gets the site_network_id of this DisassociateSiteNetworkBandwidthRequest.

        分支网络的ID。

        :return: The site_network_id of this DisassociateSiteNetworkBandwidthRequest.
        :rtype: str
        """
        return self._site_network_id

    @site_network_id.setter
    def site_network_id(self, site_network_id):
        r"""Sets the site_network_id of this DisassociateSiteNetworkBandwidthRequest.

        分支网络的ID。

        :param site_network_id: The site_network_id of this DisassociateSiteNetworkBandwidthRequest.
        :type site_network_id: str
        """
        self._site_network_id = site_network_id

    @property
    def site_connection_id(self):
        r"""Gets the site_connection_id of this DisassociateSiteNetworkBandwidthRequest.

        实例ID。

        :return: The site_connection_id of this DisassociateSiteNetworkBandwidthRequest.
        :rtype: str
        """
        return self._site_connection_id

    @site_connection_id.setter
    def site_connection_id(self, site_connection_id):
        r"""Sets the site_connection_id of this DisassociateSiteNetworkBandwidthRequest.

        实例ID。

        :param site_connection_id: The site_connection_id of this DisassociateSiteNetworkBandwidthRequest.
        :type site_connection_id: str
        """
        self._site_connection_id = site_connection_id

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
        if not isinstance(other, DisassociateSiteNetworkBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
