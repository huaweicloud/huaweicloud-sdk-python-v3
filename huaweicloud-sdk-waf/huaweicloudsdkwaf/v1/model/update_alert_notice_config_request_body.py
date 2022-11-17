# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlertNoticeConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'enabled': 'bool',
        'topic_urn': 'str',
        'sendfreq': 'int',
        'locale': 'str',
        'times': 'int',
        'threat': 'list[str]',
        'notice_class': 'str',
        'nearly_expired_time': 'str',
        'is_all_enterprise_project': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'enabled': 'enabled',
        'topic_urn': 'topic_urn',
        'sendfreq': 'sendfreq',
        'locale': 'locale',
        'times': 'times',
        'threat': 'threat',
        'notice_class': 'notice_class',
        'nearly_expired_time': 'nearly_expired_time',
        'is_all_enterprise_project': 'is_all_enterprise_project'
    }

    def __init__(self, name=None, enabled=None, topic_urn=None, sendfreq=None, locale=None, times=None, threat=None, notice_class=None, nearly_expired_time=None, is_all_enterprise_project=None):
        """UpdateAlertNoticeConfigRequestBody

        The model defined in huaweicloud sdk

        :param name: 告警通知名称
        :type name: str
        :param enabled: 是否开启   - false: 不开启   - true: 开启
        :type enabled: bool
        :param topic_urn: 主题URN，通过消息通知服务获取
        :type topic_urn: str
        :param sendfreq: 时间间隔，单位为分钟。当通知类型为防护事件时，该参数表示在改时间间隔内，攻击次数等于或者大于设定阈值时，将发送告警通知，支持的值：5、15、30、60、120、360、720、1440；当通知类型为证书到期时，该参数表示每隔多长时间发送一次告警通知，支持的值为1440、10080（单位为分钟）。
        :type sendfreq: int
        :param locale: 语言   - zh-cn：中文   - en-us
        :type locale: str
        :param times: 当通知类型为防护事件时，需要填写该参数。在该时间间隔内，当攻击次数大于或等于您设置的阈值时才会发送告警通知
        :type times: int
        :param threat: 事件类型
        :type threat: list[str]
        :param notice_class: 通知类型    - threat_alert_notice: 防护事件    - cert_alert_notice: 证书到期
        :type notice_class: str
        :param nearly_expired_time: 提前通知天数，通知类型为证书到期通知需要填写该参数
        :type nearly_expired_time: str
        :param is_all_enterprise_project: 是否是所有企业项目
        :type is_all_enterprise_project: bool
        """
        
        

        self._name = None
        self._enabled = None
        self._topic_urn = None
        self._sendfreq = None
        self._locale = None
        self._times = None
        self._threat = None
        self._notice_class = None
        self._nearly_expired_time = None
        self._is_all_enterprise_project = None
        self.discriminator = None

        self.name = name
        if enabled is not None:
            self.enabled = enabled
        self.topic_urn = topic_urn
        if sendfreq is not None:
            self.sendfreq = sendfreq
        if locale is not None:
            self.locale = locale
        if times is not None:
            self.times = times
        if threat is not None:
            self.threat = threat
        self.notice_class = notice_class
        if nearly_expired_time is not None:
            self.nearly_expired_time = nearly_expired_time
        if is_all_enterprise_project is not None:
            self.is_all_enterprise_project = is_all_enterprise_project

    @property
    def name(self):
        """Gets the name of this UpdateAlertNoticeConfigRequestBody.

        告警通知名称

        :return: The name of this UpdateAlertNoticeConfigRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAlertNoticeConfigRequestBody.

        告警通知名称

        :param name: The name of this UpdateAlertNoticeConfigRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this UpdateAlertNoticeConfigRequestBody.

        是否开启   - false: 不开启   - true: 开启

        :return: The enabled of this UpdateAlertNoticeConfigRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateAlertNoticeConfigRequestBody.

        是否开启   - false: 不开启   - true: 开启

        :param enabled: The enabled of this UpdateAlertNoticeConfigRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def topic_urn(self):
        """Gets the topic_urn of this UpdateAlertNoticeConfigRequestBody.

        主题URN，通过消息通知服务获取

        :return: The topic_urn of this UpdateAlertNoticeConfigRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this UpdateAlertNoticeConfigRequestBody.

        主题URN，通过消息通知服务获取

        :param topic_urn: The topic_urn of this UpdateAlertNoticeConfigRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def sendfreq(self):
        """Gets the sendfreq of this UpdateAlertNoticeConfigRequestBody.

        时间间隔，单位为分钟。当通知类型为防护事件时，该参数表示在改时间间隔内，攻击次数等于或者大于设定阈值时，将发送告警通知，支持的值：5、15、30、60、120、360、720、1440；当通知类型为证书到期时，该参数表示每隔多长时间发送一次告警通知，支持的值为1440、10080（单位为分钟）。

        :return: The sendfreq of this UpdateAlertNoticeConfigRequestBody.
        :rtype: int
        """
        return self._sendfreq

    @sendfreq.setter
    def sendfreq(self, sendfreq):
        """Sets the sendfreq of this UpdateAlertNoticeConfigRequestBody.

        时间间隔，单位为分钟。当通知类型为防护事件时，该参数表示在改时间间隔内，攻击次数等于或者大于设定阈值时，将发送告警通知，支持的值：5、15、30、60、120、360、720、1440；当通知类型为证书到期时，该参数表示每隔多长时间发送一次告警通知，支持的值为1440、10080（单位为分钟）。

        :param sendfreq: The sendfreq of this UpdateAlertNoticeConfigRequestBody.
        :type sendfreq: int
        """
        self._sendfreq = sendfreq

    @property
    def locale(self):
        """Gets the locale of this UpdateAlertNoticeConfigRequestBody.

        语言   - zh-cn：中文   - en-us

        :return: The locale of this UpdateAlertNoticeConfigRequestBody.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UpdateAlertNoticeConfigRequestBody.

        语言   - zh-cn：中文   - en-us

        :param locale: The locale of this UpdateAlertNoticeConfigRequestBody.
        :type locale: str
        """
        self._locale = locale

    @property
    def times(self):
        """Gets the times of this UpdateAlertNoticeConfigRequestBody.

        当通知类型为防护事件时，需要填写该参数。在该时间间隔内，当攻击次数大于或等于您设置的阈值时才会发送告警通知

        :return: The times of this UpdateAlertNoticeConfigRequestBody.
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this UpdateAlertNoticeConfigRequestBody.

        当通知类型为防护事件时，需要填写该参数。在该时间间隔内，当攻击次数大于或等于您设置的阈值时才会发送告警通知

        :param times: The times of this UpdateAlertNoticeConfigRequestBody.
        :type times: int
        """
        self._times = times

    @property
    def threat(self):
        """Gets the threat of this UpdateAlertNoticeConfigRequestBody.

        事件类型

        :return: The threat of this UpdateAlertNoticeConfigRequestBody.
        :rtype: list[str]
        """
        return self._threat

    @threat.setter
    def threat(self, threat):
        """Sets the threat of this UpdateAlertNoticeConfigRequestBody.

        事件类型

        :param threat: The threat of this UpdateAlertNoticeConfigRequestBody.
        :type threat: list[str]
        """
        self._threat = threat

    @property
    def notice_class(self):
        """Gets the notice_class of this UpdateAlertNoticeConfigRequestBody.

        通知类型    - threat_alert_notice: 防护事件    - cert_alert_notice: 证书到期

        :return: The notice_class of this UpdateAlertNoticeConfigRequestBody.
        :rtype: str
        """
        return self._notice_class

    @notice_class.setter
    def notice_class(self, notice_class):
        """Sets the notice_class of this UpdateAlertNoticeConfigRequestBody.

        通知类型    - threat_alert_notice: 防护事件    - cert_alert_notice: 证书到期

        :param notice_class: The notice_class of this UpdateAlertNoticeConfigRequestBody.
        :type notice_class: str
        """
        self._notice_class = notice_class

    @property
    def nearly_expired_time(self):
        """Gets the nearly_expired_time of this UpdateAlertNoticeConfigRequestBody.

        提前通知天数，通知类型为证书到期通知需要填写该参数

        :return: The nearly_expired_time of this UpdateAlertNoticeConfigRequestBody.
        :rtype: str
        """
        return self._nearly_expired_time

    @nearly_expired_time.setter
    def nearly_expired_time(self, nearly_expired_time):
        """Sets the nearly_expired_time of this UpdateAlertNoticeConfigRequestBody.

        提前通知天数，通知类型为证书到期通知需要填写该参数

        :param nearly_expired_time: The nearly_expired_time of this UpdateAlertNoticeConfigRequestBody.
        :type nearly_expired_time: str
        """
        self._nearly_expired_time = nearly_expired_time

    @property
    def is_all_enterprise_project(self):
        """Gets the is_all_enterprise_project of this UpdateAlertNoticeConfigRequestBody.

        是否是所有企业项目

        :return: The is_all_enterprise_project of this UpdateAlertNoticeConfigRequestBody.
        :rtype: bool
        """
        return self._is_all_enterprise_project

    @is_all_enterprise_project.setter
    def is_all_enterprise_project(self, is_all_enterprise_project):
        """Sets the is_all_enterprise_project of this UpdateAlertNoticeConfigRequestBody.

        是否是所有企业项目

        :param is_all_enterprise_project: The is_all_enterprise_project of this UpdateAlertNoticeConfigRequestBody.
        :type is_all_enterprise_project: bool
        """
        self._is_all_enterprise_project = is_all_enterprise_project

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
        if not isinstance(other, UpdateAlertNoticeConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
