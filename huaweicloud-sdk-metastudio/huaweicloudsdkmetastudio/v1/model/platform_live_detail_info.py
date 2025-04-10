# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlatformLiveDetailInfo:

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
        'platform': 'str',
        'account': 'str',
        'live_id': 'str'
    }

    attribute_map = {
        'platform_id': 'platform_id',
        'platform': 'platform',
        'account': 'account',
        'live_id': 'live_id'
    }

    def __init__(self, platform_id=None, platform=None, account=None, live_id=None):
        r"""PlatformLiveDetailInfo

        The model defined in huaweicloud sdk

        :param platform_id: 直播平台ID。
        :type platform_id: str
        :param platform: 直播平台。美团填写meituan
        :type platform: str
        :param account: 授权账号信息。 美团平台对应：opBizCode
        :type account: str
        :param live_id: 直播ID。如果配置，则段落切换回调中会携带该信息。 美团对应liveId
        :type live_id: str
        """
        
        

        self._platform_id = None
        self._platform = None
        self._account = None
        self._live_id = None
        self.discriminator = None

        if platform_id is not None:
            self.platform_id = platform_id
        if platform is not None:
            self.platform = platform
        if account is not None:
            self.account = account
        if live_id is not None:
            self.live_id = live_id

    @property
    def platform_id(self):
        r"""Gets the platform_id of this PlatformLiveDetailInfo.

        直播平台ID。

        :return: The platform_id of this PlatformLiveDetailInfo.
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        r"""Sets the platform_id of this PlatformLiveDetailInfo.

        直播平台ID。

        :param platform_id: The platform_id of this PlatformLiveDetailInfo.
        :type platform_id: str
        """
        self._platform_id = platform_id

    @property
    def platform(self):
        r"""Gets the platform of this PlatformLiveDetailInfo.

        直播平台。美团填写meituan

        :return: The platform of this PlatformLiveDetailInfo.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this PlatformLiveDetailInfo.

        直播平台。美团填写meituan

        :param platform: The platform of this PlatformLiveDetailInfo.
        :type platform: str
        """
        self._platform = platform

    @property
    def account(self):
        r"""Gets the account of this PlatformLiveDetailInfo.

        授权账号信息。 美团平台对应：opBizCode

        :return: The account of this PlatformLiveDetailInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this PlatformLiveDetailInfo.

        授权账号信息。 美团平台对应：opBizCode

        :param account: The account of this PlatformLiveDetailInfo.
        :type account: str
        """
        self._account = account

    @property
    def live_id(self):
        r"""Gets the live_id of this PlatformLiveDetailInfo.

        直播ID。如果配置，则段落切换回调中会携带该信息。 美团对应liveId

        :return: The live_id of this PlatformLiveDetailInfo.
        :rtype: str
        """
        return self._live_id

    @live_id.setter
    def live_id(self, live_id):
        r"""Sets the live_id of this PlatformLiveDetailInfo.

        直播ID。如果配置，则段落切换回调中会携带该信息。 美团对应liveId

        :param live_id: The live_id of this PlatformLiveDetailInfo.
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
        if not isinstance(other, PlatformLiveDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
