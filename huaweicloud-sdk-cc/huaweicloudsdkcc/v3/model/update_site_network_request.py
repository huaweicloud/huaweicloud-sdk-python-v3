# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSiteNetworkRequest:

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
        'body': 'UpdateSiteNetworkRequestBody'
    }

    attribute_map = {
        'site_network_id': 'site_network_id',
        'body': 'body'
    }

    def __init__(self, site_network_id=None, body=None):
        r"""UpdateSiteNetworkRequest

        The model defined in huaweicloud sdk

        :param site_network_id: 分支网络的ID。
        :type site_network_id: str
        :param body: Body of the UpdateSiteNetworkRequest
        :type body: :class:`huaweicloudsdkcc.v3.UpdateSiteNetworkRequestBody`
        """
        
        

        self._site_network_id = None
        self._body = None
        self.discriminator = None

        self.site_network_id = site_network_id
        if body is not None:
            self.body = body

    @property
    def site_network_id(self):
        r"""Gets the site_network_id of this UpdateSiteNetworkRequest.

        分支网络的ID。

        :return: The site_network_id of this UpdateSiteNetworkRequest.
        :rtype: str
        """
        return self._site_network_id

    @site_network_id.setter
    def site_network_id(self, site_network_id):
        r"""Sets the site_network_id of this UpdateSiteNetworkRequest.

        分支网络的ID。

        :param site_network_id: The site_network_id of this UpdateSiteNetworkRequest.
        :type site_network_id: str
        """
        self._site_network_id = site_network_id

    @property
    def body(self):
        r"""Gets the body of this UpdateSiteNetworkRequest.

        :return: The body of this UpdateSiteNetworkRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateSiteNetworkRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateSiteNetworkRequest.

        :param body: The body of this UpdateSiteNetworkRequest.
        :type body: :class:`huaweicloudsdkcc.v3.UpdateSiteNetworkRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateSiteNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
