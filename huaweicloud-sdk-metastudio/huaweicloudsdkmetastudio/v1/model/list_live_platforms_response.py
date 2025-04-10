# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLivePlatformsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'live_platforms': 'list[LivePlatformInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'live_platforms': 'live_platforms',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, live_platforms=None, x_request_id=None):
        r"""ListLivePlatformsResponse

        The model defined in huaweicloud sdk

        :param live_platforms: 直播平台列表
        :type live_platforms: list[:class:`huaweicloudsdkmetastudio.v1.LivePlatformInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListLivePlatformsResponse, self).__init__()

        self._live_platforms = None
        self._x_request_id = None
        self.discriminator = None

        if live_platforms is not None:
            self.live_platforms = live_platforms
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def live_platforms(self):
        r"""Gets the live_platforms of this ListLivePlatformsResponse.

        直播平台列表

        :return: The live_platforms of this ListLivePlatformsResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LivePlatformInfo`]
        """
        return self._live_platforms

    @live_platforms.setter
    def live_platforms(self, live_platforms):
        r"""Sets the live_platforms of this ListLivePlatformsResponse.

        直播平台列表

        :param live_platforms: The live_platforms of this ListLivePlatformsResponse.
        :type live_platforms: list[:class:`huaweicloudsdkmetastudio.v1.LivePlatformInfo`]
        """
        self._live_platforms = live_platforms

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListLivePlatformsResponse.

        :return: The x_request_id of this ListLivePlatformsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListLivePlatformsResponse.

        :param x_request_id: The x_request_id of this ListLivePlatformsResponse.
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
        if not isinstance(other, ListLivePlatformsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
