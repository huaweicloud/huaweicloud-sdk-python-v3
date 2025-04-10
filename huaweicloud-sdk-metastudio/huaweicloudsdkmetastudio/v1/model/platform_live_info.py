# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlatformLiveInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'platform_id': 'str',
        'live_id': 'str'
    }

    attribute_map = {
        'platform_id': 'platform_id',
        'live_id': 'live_id'
    }

    def __init__(self, platform_id=None, live_id=None):
        r"""PlatformLiveInfo

        The model defined in huaweicloud sdk

        :param platform_id: 直播平台ID。
        :type platform_id: str
        :param live_id: 直播ID。如果配置，则段落切换回调中会携带该信息。只能包含英文、数字、-、_。 美团对应liveId
        :type live_id: str
        """
        
        

        self._platform_id = None
        self._live_id = None
        self.discriminator = None

        self.platform_id = platform_id
        self.live_id = live_id

    @property
    def platform_id(self):
        r"""Gets the platform_id of this PlatformLiveInfo.

        直播平台ID。

        :return: The platform_id of this PlatformLiveInfo.
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        r"""Sets the platform_id of this PlatformLiveInfo.

        直播平台ID。

        :param platform_id: The platform_id of this PlatformLiveInfo.
        :type platform_id: str
        """
        self._platform_id = platform_id

    @property
    def live_id(self):
        r"""Gets the live_id of this PlatformLiveInfo.

        直播ID。如果配置，则段落切换回调中会携带该信息。只能包含英文、数字、-、_。 美团对应liveId

        :return: The live_id of this PlatformLiveInfo.
        :rtype: str
        """
        return self._live_id

    @live_id.setter
    def live_id(self, live_id):
        r"""Sets the live_id of this PlatformLiveInfo.

        直播ID。如果配置，则段落切换回调中会携带该信息。只能包含英文、数字、-、_。 美团对应liveId

        :param live_id: The live_id of this PlatformLiveInfo.
        :type live_id: str
        """
        self._live_id = live_id

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
        if not isinstance(other, PlatformLiveInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
