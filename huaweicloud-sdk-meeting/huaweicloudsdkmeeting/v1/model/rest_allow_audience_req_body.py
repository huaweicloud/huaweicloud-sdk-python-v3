# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestAllowAudienceReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allow_audience': 'int'
    }

    attribute_map = {
        'allow_audience': 'allowAudience'
    }

    def __init__(self, allow_audience=None):
        r"""RestAllowAudienceReqBody

        The model defined in huaweicloud sdk

        :param allow_audience: 主持人是否允许入会 1：允许入会
        :type allow_audience: int
        """
        
        

        self._allow_audience = None
        self.discriminator = None

        self.allow_audience = allow_audience

    @property
    def allow_audience(self):
        r"""Gets the allow_audience of this RestAllowAudienceReqBody.

        主持人是否允许入会 1：允许入会

        :return: The allow_audience of this RestAllowAudienceReqBody.
        :rtype: int
        """
        return self._allow_audience

    @allow_audience.setter
    def allow_audience(self, allow_audience):
        r"""Sets the allow_audience of this RestAllowAudienceReqBody.

        主持人是否允许入会 1：允许入会

        :param allow_audience: The allow_audience of this RestAllowAudienceReqBody.
        :type allow_audience: int
        """
        self._allow_audience = allow_audience

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
        if not isinstance(other, RestAllowAudienceReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
