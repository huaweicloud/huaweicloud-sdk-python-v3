# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordCallbackConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'publish_domain': 'str',
        'app': 'str',
        'notify_callback_url': 'str',
        'notify_event_subscription': 'list[str]',
        'sign_type': 'str',
        'create_time': 'date',
        'update_time': 'date'
    }

    attribute_map = {
        'id': 'id',
        'publish_domain': 'publish_domain',
        'app': 'app',
        'notify_callback_url': 'notify_callback_url',
        'notify_event_subscription': 'notify_event_subscription',
        'sign_type': 'sign_type',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, publish_domain=None, app=None, notify_callback_url=None, notify_event_subscription=None, sign_type=None, create_time=None, update_time=None):
        r"""RecordCallbackConfig

        The model defined in huaweicloud sdk

        :param id: 配置id，由服务端返回。创建或修改的时候不携带
        :type id: str
        :param publish_domain: 直播推流域名
        :type publish_domain: str
        :param app: app名称。如果匹配任意需填写为*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*
        :type app: str
        :param notify_callback_url: 录制回调通知url地址
        :type notify_callback_url: str
        :param notify_event_subscription: 订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE
        :type notify_event_subscription: list[str]
        :param sign_type: 加密类型
        :type sign_type: str
        :param create_time: 创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回
        :type create_time: date
        :param update_time: 修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回
        :type update_time: date
        """
        
        

        self._id = None
        self._publish_domain = None
        self._app = None
        self._notify_callback_url = None
        self._notify_event_subscription = None
        self._sign_type = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.publish_domain = publish_domain
        self.app = app
        if notify_callback_url is not None:
            self.notify_callback_url = notify_callback_url
        if notify_event_subscription is not None:
            self.notify_event_subscription = notify_event_subscription
        if sign_type is not None:
            self.sign_type = sign_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this RecordCallbackConfig.

        配置id，由服务端返回。创建或修改的时候不携带

        :return: The id of this RecordCallbackConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecordCallbackConfig.

        配置id，由服务端返回。创建或修改的时候不携带

        :param id: The id of this RecordCallbackConfig.
        :type id: str
        """
        self._id = id

    @property
    def publish_domain(self):
        r"""Gets the publish_domain of this RecordCallbackConfig.

        直播推流域名

        :return: The publish_domain of this RecordCallbackConfig.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        r"""Sets the publish_domain of this RecordCallbackConfig.

        直播推流域名

        :param publish_domain: The publish_domain of this RecordCallbackConfig.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        r"""Gets the app of this RecordCallbackConfig.

        app名称。如果匹配任意需填写为*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :return: The app of this RecordCallbackConfig.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this RecordCallbackConfig.

        app名称。如果匹配任意需填写为*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :param app: The app of this RecordCallbackConfig.
        :type app: str
        """
        self._app = app

    @property
    def notify_callback_url(self):
        r"""Gets the notify_callback_url of this RecordCallbackConfig.

        录制回调通知url地址

        :return: The notify_callback_url of this RecordCallbackConfig.
        :rtype: str
        """
        return self._notify_callback_url

    @notify_callback_url.setter
    def notify_callback_url(self, notify_callback_url):
        r"""Sets the notify_callback_url of this RecordCallbackConfig.

        录制回调通知url地址

        :param notify_callback_url: The notify_callback_url of this RecordCallbackConfig.
        :type notify_callback_url: str
        """
        self._notify_callback_url = notify_callback_url

    @property
    def notify_event_subscription(self):
        r"""Gets the notify_event_subscription of this RecordCallbackConfig.

        订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE

        :return: The notify_event_subscription of this RecordCallbackConfig.
        :rtype: list[str]
        """
        return self._notify_event_subscription

    @notify_event_subscription.setter
    def notify_event_subscription(self, notify_event_subscription):
        r"""Sets the notify_event_subscription of this RecordCallbackConfig.

        订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE

        :param notify_event_subscription: The notify_event_subscription of this RecordCallbackConfig.
        :type notify_event_subscription: list[str]
        """
        self._notify_event_subscription = notify_event_subscription

    @property
    def sign_type(self):
        r"""Gets the sign_type of this RecordCallbackConfig.

        加密类型

        :return: The sign_type of this RecordCallbackConfig.
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        r"""Sets the sign_type of this RecordCallbackConfig.

        加密类型

        :param sign_type: The sign_type of this RecordCallbackConfig.
        :type sign_type: str
        """
        self._sign_type = sign_type

    @property
    def create_time(self):
        r"""Gets the create_time of this RecordCallbackConfig.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The create_time of this RecordCallbackConfig.
        :rtype: date
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this RecordCallbackConfig.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param create_time: The create_time of this RecordCallbackConfig.
        :type create_time: date
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this RecordCallbackConfig.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The update_time of this RecordCallbackConfig.
        :rtype: date
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this RecordCallbackConfig.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param update_time: The update_time of this RecordCallbackConfig.
        :type update_time: date
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
        if not isinstance(other, RecordCallbackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
