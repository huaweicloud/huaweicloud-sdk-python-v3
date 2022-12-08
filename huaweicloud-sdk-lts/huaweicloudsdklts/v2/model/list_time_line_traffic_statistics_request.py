# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTimeLineTrafficStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timezone': 'str',
        'body': 'TimelineTrafficStatisticsRequestBody'
    }

    attribute_map = {
        'timezone': 'timezone',
        'body': 'body'
    }

    def __init__(self, timezone=None, body=None):
        """ListTimeLineTrafficStatisticsRequest

        The model defined in huaweicloud sdk

        :param timezone: 时区
        :type timezone: str
        :param body: Body of the ListTimeLineTrafficStatisticsRequest
        :type body: :class:`huaweicloudsdklts.v2.TimelineTrafficStatisticsRequestBody`
        """
        
        

        self._timezone = None
        self._body = None
        self.discriminator = None

        self.timezone = timezone
        if body is not None:
            self.body = body

    @property
    def timezone(self):
        """Gets the timezone of this ListTimeLineTrafficStatisticsRequest.

        时区

        :return: The timezone of this ListTimeLineTrafficStatisticsRequest.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ListTimeLineTrafficStatisticsRequest.

        时区

        :param timezone: The timezone of this ListTimeLineTrafficStatisticsRequest.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def body(self):
        """Gets the body of this ListTimeLineTrafficStatisticsRequest.

        :return: The body of this ListTimeLineTrafficStatisticsRequest.
        :rtype: :class:`huaweicloudsdklts.v2.TimelineTrafficStatisticsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListTimeLineTrafficStatisticsRequest.

        :param body: The body of this ListTimeLineTrafficStatisticsRequest.
        :type body: :class:`huaweicloudsdklts.v2.TimelineTrafficStatisticsRequestBody`
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
        if not isinstance(other, ListTimeLineTrafficStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
