# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordCallbackConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'app': 'str',
        'notify_callback_url': 'str',
        'notify_event_subscription': 'list[str]',
        'sign_type': 'str',
        'key': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'notify_callback_url': 'notify_callback_url',
        'notify_event_subscription': 'notify_event_subscription',
        'sign_type': 'sign_type',
        'key': 'key'
    }

    def __init__(self, publish_domain=None, app=None, notify_callback_url=None, notify_event_subscription=None, sign_type=None, key=None):
        """RecordCallbackConfigRequest

        The model defined in huaweicloud sdk

        :param publish_domain: 直播推流域名
        :type publish_domain: str
        :param app: app名称。如果需要匹配任意应用则需填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*
        :type app: str
        :param notify_callback_url: 录制回调通知url地址
        :type notify_callback_url: str
        :param notify_event_subscription: 订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE
        :type notify_event_subscription: list[str]
        :param sign_type: 加密类型
        :type sign_type: str
        :param key: 回调秘钥，主要用于鉴权。为了保护用户数据信息安全，建议填写。
        :type key: str
        """
        
        

        self._publish_domain = None
        self._app = None
        self._notify_callback_url = None
        self._notify_event_subscription = None
        self._sign_type = None
        self._key = None
        self.discriminator = None

        self.publish_domain = publish_domain
        self.app = app
        if notify_callback_url is not None:
            self.notify_callback_url = notify_callback_url
        if notify_event_subscription is not None:
            self.notify_event_subscription = notify_event_subscription
        if sign_type is not None:
            self.sign_type = sign_type
        if key is not None:
            self.key = key

    @property
    def publish_domain(self):
        """Gets the publish_domain of this RecordCallbackConfigRequest.

        直播推流域名

        :return: The publish_domain of this RecordCallbackConfigRequest.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this RecordCallbackConfigRequest.

        直播推流域名

        :param publish_domain: The publish_domain of this RecordCallbackConfigRequest.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this RecordCallbackConfigRequest.

        app名称。如果需要匹配任意应用则需填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :return: The app of this RecordCallbackConfigRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RecordCallbackConfigRequest.

        app名称。如果需要匹配任意应用则需填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :param app: The app of this RecordCallbackConfigRequest.
        :type app: str
        """
        self._app = app

    @property
    def notify_callback_url(self):
        """Gets the notify_callback_url of this RecordCallbackConfigRequest.

        录制回调通知url地址

        :return: The notify_callback_url of this RecordCallbackConfigRequest.
        :rtype: str
        """
        return self._notify_callback_url

    @notify_callback_url.setter
    def notify_callback_url(self, notify_callback_url):
        """Sets the notify_callback_url of this RecordCallbackConfigRequest.

        录制回调通知url地址

        :param notify_callback_url: The notify_callback_url of this RecordCallbackConfigRequest.
        :type notify_callback_url: str
        """
        self._notify_callback_url = notify_callback_url

    @property
    def notify_event_subscription(self):
        """Gets the notify_event_subscription of this RecordCallbackConfigRequest.

        订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE

        :return: The notify_event_subscription of this RecordCallbackConfigRequest.
        :rtype: list[str]
        """
        return self._notify_event_subscription

    @notify_event_subscription.setter
    def notify_event_subscription(self, notify_event_subscription):
        """Sets the notify_event_subscription of this RecordCallbackConfigRequest.

        订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE

        :param notify_event_subscription: The notify_event_subscription of this RecordCallbackConfigRequest.
        :type notify_event_subscription: list[str]
        """
        self._notify_event_subscription = notify_event_subscription

    @property
    def sign_type(self):
        """Gets the sign_type of this RecordCallbackConfigRequest.

        加密类型

        :return: The sign_type of this RecordCallbackConfigRequest.
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        """Sets the sign_type of this RecordCallbackConfigRequest.

        加密类型

        :param sign_type: The sign_type of this RecordCallbackConfigRequest.
        :type sign_type: str
        """
        self._sign_type = sign_type

    @property
    def key(self):
        """Gets the key of this RecordCallbackConfigRequest.

        回调秘钥，主要用于鉴权。为了保护用户数据信息安全，建议填写。

        :return: The key of this RecordCallbackConfigRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RecordCallbackConfigRequest.

        回调秘钥，主要用于鉴权。为了保护用户数据信息安全，建议填写。

        :param key: The key of this RecordCallbackConfigRequest.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, RecordCallbackConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
