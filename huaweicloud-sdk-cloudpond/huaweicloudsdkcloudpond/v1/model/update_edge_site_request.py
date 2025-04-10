# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeSiteRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'body': 'UpdateEdgeSiteRequestBody'
    }

    attribute_map = {
        'site_id': 'site_id',
        'body': 'body'
    }

    def __init__(self, site_id=None, body=None):
        r"""UpdateEdgeSiteRequest

        The model defined in huaweicloud sdk

        :param site_id: 边缘小站ID
        :type site_id: str
        :param body: Body of the UpdateEdgeSiteRequest
        :type body: :class:`huaweicloudsdkcloudpond.v1.UpdateEdgeSiteRequestBody`
        """
        
        

        self._site_id = None
        self._body = None
        self.discriminator = None

        self.site_id = site_id
        if body is not None:
            self.body = body

    @property
    def site_id(self):
        r"""Gets the site_id of this UpdateEdgeSiteRequest.

        边缘小站ID

        :return: The site_id of this UpdateEdgeSiteRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this UpdateEdgeSiteRequest.

        边缘小站ID

        :param site_id: The site_id of this UpdateEdgeSiteRequest.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def body(self):
        r"""Gets the body of this UpdateEdgeSiteRequest.

        :return: The body of this UpdateEdgeSiteRequest.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.UpdateEdgeSiteRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateEdgeSiteRequest.

        :param body: The body of this UpdateEdgeSiteRequest.
        :type body: :class:`huaweicloudsdkcloudpond.v1.UpdateEdgeSiteRequestBody`
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
        if not isinstance(other, UpdateEdgeSiteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
