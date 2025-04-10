# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGeoBlockingConfigResponse(SdkResponse):

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
        'apps': 'list[GeoBlockingConfigInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'apps': 'apps',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, play_domain=None, apps=None, x_request_id=None):
        r"""ListGeoBlockingConfigResponse

        The model defined in huaweicloud sdk

        :param play_domain: 直播播放域名
        :type play_domain: str
        :param apps: 应用列表
        :type apps: list[:class:`huaweicloudsdklive.v1.GeoBlockingConfigInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListGeoBlockingConfigResponse, self).__init__()

        self._play_domain = None
        self._apps = None
        self._x_request_id = None
        self.discriminator = None

        if play_domain is not None:
            self.play_domain = play_domain
        if apps is not None:
            self.apps = apps
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def play_domain(self):
        r"""Gets the play_domain of this ListGeoBlockingConfigResponse.

        直播播放域名

        :return: The play_domain of this ListGeoBlockingConfigResponse.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        r"""Sets the play_domain of this ListGeoBlockingConfigResponse.

        直播播放域名

        :param play_domain: The play_domain of this ListGeoBlockingConfigResponse.
        :type play_domain: str
        """
        self._play_domain = play_domain

    @property
    def apps(self):
        r"""Gets the apps of this ListGeoBlockingConfigResponse.

        应用列表

        :return: The apps of this ListGeoBlockingConfigResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.GeoBlockingConfigInfo`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        r"""Sets the apps of this ListGeoBlockingConfigResponse.

        应用列表

        :param apps: The apps of this ListGeoBlockingConfigResponse.
        :type apps: list[:class:`huaweicloudsdklive.v1.GeoBlockingConfigInfo`]
        """
        self._apps = apps

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListGeoBlockingConfigResponse.

        :return: The x_request_id of this ListGeoBlockingConfigResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListGeoBlockingConfigResponse.

        :param x_request_id: The x_request_id of this ListGeoBlockingConfigResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListGeoBlockingConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
