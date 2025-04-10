# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGeoBlockingConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'body': 'GeoBlockingConfigInfo'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'body': 'body'
    }

    def __init__(self, play_domain=None, body=None):
        r"""UpdateGeoBlockingConfigRequest

        The model defined in huaweicloud sdk

        :param play_domain: 播放域名
        :type play_domain: str
        :param body: Body of the UpdateGeoBlockingConfigRequest
        :type body: :class:`huaweicloudsdklive.v1.GeoBlockingConfigInfo`
        """
        
        

        self._play_domain = None
        self._body = None
        self.discriminator = None

        self.play_domain = play_domain
        if body is not None:
            self.body = body

    @property
    def play_domain(self):
        r"""Gets the play_domain of this UpdateGeoBlockingConfigRequest.

        播放域名

        :return: The play_domain of this UpdateGeoBlockingConfigRequest.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        r"""Sets the play_domain of this UpdateGeoBlockingConfigRequest.

        播放域名

        :param play_domain: The play_domain of this UpdateGeoBlockingConfigRequest.
        :type play_domain: str
        """
        self._play_domain = play_domain

    @property
    def body(self):
        r"""Gets the body of this UpdateGeoBlockingConfigRequest.

        :return: The body of this UpdateGeoBlockingConfigRequest.
        :rtype: :class:`huaweicloudsdklive.v1.GeoBlockingConfigInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateGeoBlockingConfigRequest.

        :param body: The body of this UpdateGeoBlockingConfigRequest.
        :type body: :class:`huaweicloudsdklive.v1.GeoBlockingConfigInfo`
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
        if not isinstance(other, UpdateGeoBlockingConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
