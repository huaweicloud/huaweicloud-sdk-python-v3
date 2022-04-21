# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppCallbackUrl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'auth_key': 'str',
        'notify_event_subscription': 'list[str]',
        'update_time': 'str'
    }

    attribute_map = {
        'url': 'url',
        'auth_key': 'auth_key',
        'notify_event_subscription': 'notify_event_subscription',
        'update_time': 'update_time'
    }

    def __init__(self, url=None, auth_key=None, notify_event_subscription=None, update_time=None):
        """AppCallbackUrl

        The model defined in huaweicloud sdk

        :param url: 回调通知url地址，url必须以http://或https://开头，需要支持POST调用。
        :type url: str
        :param auth_key: 回调秘钥，主要用于鉴权。如果不设置或者为空，则回调不会增加鉴权头域字段。 
        :type auth_key: str
        :param notify_event_subscription: 订阅云端录制通知消息。  取值如下：  - RECORD_NEW_FILE_START：录制模块开始创建新的录制文件。  - RECORD_FILE_COMPLETE：录制模块已经生成录制文件。 
        :type notify_event_subscription: list[str]
        :param update_time: 更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC。 
        :type update_time: str
        """
        
        

        self._url = None
        self._auth_key = None
        self._notify_event_subscription = None
        self._update_time = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if auth_key is not None:
            self.auth_key = auth_key
        if notify_event_subscription is not None:
            self.notify_event_subscription = notify_event_subscription
        if update_time is not None:
            self.update_time = update_time

    @property
    def url(self):
        """Gets the url of this AppCallbackUrl.

        回调通知url地址，url必须以http://或https://开头，需要支持POST调用。

        :return: The url of this AppCallbackUrl.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AppCallbackUrl.

        回调通知url地址，url必须以http://或https://开头，需要支持POST调用。

        :param url: The url of this AppCallbackUrl.
        :type url: str
        """
        self._url = url

    @property
    def auth_key(self):
        """Gets the auth_key of this AppCallbackUrl.

        回调秘钥，主要用于鉴权。如果不设置或者为空，则回调不会增加鉴权头域字段。 

        :return: The auth_key of this AppCallbackUrl.
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this AppCallbackUrl.

        回调秘钥，主要用于鉴权。如果不设置或者为空，则回调不会增加鉴权头域字段。 

        :param auth_key: The auth_key of this AppCallbackUrl.
        :type auth_key: str
        """
        self._auth_key = auth_key

    @property
    def notify_event_subscription(self):
        """Gets the notify_event_subscription of this AppCallbackUrl.

        订阅云端录制通知消息。  取值如下：  - RECORD_NEW_FILE_START：录制模块开始创建新的录制文件。  - RECORD_FILE_COMPLETE：录制模块已经生成录制文件。 

        :return: The notify_event_subscription of this AppCallbackUrl.
        :rtype: list[str]
        """
        return self._notify_event_subscription

    @notify_event_subscription.setter
    def notify_event_subscription(self, notify_event_subscription):
        """Sets the notify_event_subscription of this AppCallbackUrl.

        订阅云端录制通知消息。  取值如下：  - RECORD_NEW_FILE_START：录制模块开始创建新的录制文件。  - RECORD_FILE_COMPLETE：录制模块已经生成录制文件。 

        :param notify_event_subscription: The notify_event_subscription of this AppCallbackUrl.
        :type notify_event_subscription: list[str]
        """
        self._notify_event_subscription = notify_event_subscription

    @property
    def update_time(self):
        """Gets the update_time of this AppCallbackUrl.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC。 

        :return: The update_time of this AppCallbackUrl.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AppCallbackUrl.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC。 

        :param update_time: The update_time of this AppCallbackUrl.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, AppCallbackUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
