# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertNoticeConfigResponse(SdkResponse):

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
        'name': 'str',
        'enabled': 'bool',
        'topic_urn': 'str',
        'sendfreq': 'int',
        'locale': 'str',
        'times': 'int',
        'threat': 'list[str]',
        'prefer_html': 'bool',
        'notice_class': 'str',
        'nearly_expired_time': 'str',
        'is_all_enterprise_project': 'bool',
        'enterprise_project_id': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'enabled': 'enabled',
        'topic_urn': 'topic_urn',
        'sendfreq': 'sendfreq',
        'locale': 'locale',
        'times': 'times',
        'threat': 'threat',
        'prefer_html': 'prefer_html',
        'notice_class': 'notice_class',
        'nearly_expired_time': 'nearly_expired_time',
        'is_all_enterprise_project': 'is_all_enterprise_project',
        'enterprise_project_id': 'enterprise_project_id',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, enabled=None, topic_urn=None, sendfreq=None, locale=None, times=None, threat=None, prefer_html=None, notice_class=None, nearly_expired_time=None, is_all_enterprise_project=None, enterprise_project_id=None, update_time=None):
        r"""CreateAlertNoticeConfigResponse

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param name: 告警通知名称
        :type name: str
        :param enabled: 是否开启   - false: 不开启   - true: 开启
        :type enabled: bool
        :param topic_urn: 主题
        :type topic_urn: str
        :param sendfreq: 时间间隔，单位为分钟。当通知类型为防护事件时，该参数表示在该时间间隔内，攻击次数等于或者大于设定阈值时，将发送告警通知，支持的值：5、15、30、60、120、360、720、1440；当通知类型为证书到期时，该参数表示每隔多长时间发送一次告警通知，支持的值1天、1周（需要转换成分钟）。
        :type sendfreq: int
        :param locale: 语言
        :type locale: str
        :param times: 当通知类型为防护事件时，需要填写该参数。在该时间间隔内，当攻击次数大于或等于您设置的阈值时才会发送告警通知
        :type times: int
        :param threat: 事件类型
        :type threat: list[str]
        :param prefer_html: 预留参数，可忽略
        :type prefer_html: bool
        :param notice_class: 通知类型
        :type notice_class: str
        :param nearly_expired_time: 提前通知天数
        :type nearly_expired_time: str
        :param is_all_enterprise_project: 是否是所有企业项目
        :type is_all_enterprise_project: bool
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param update_time: 更新时间
        :type update_time: int
        """
        
        super(CreateAlertNoticeConfigResponse, self).__init__()

        self._id = None
        self._name = None
        self._enabled = None
        self._topic_urn = None
        self._sendfreq = None
        self._locale = None
        self._times = None
        self._threat = None
        self._prefer_html = None
        self._notice_class = None
        self._nearly_expired_time = None
        self._is_all_enterprise_project = None
        self._enterprise_project_id = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if sendfreq is not None:
            self.sendfreq = sendfreq
        if locale is not None:
            self.locale = locale
        if times is not None:
            self.times = times
        if threat is not None:
            self.threat = threat
        if prefer_html is not None:
            self.prefer_html = prefer_html
        if notice_class is not None:
            self.notice_class = notice_class
        if nearly_expired_time is not None:
            self.nearly_expired_time = nearly_expired_time
        if is_all_enterprise_project is not None:
            self.is_all_enterprise_project = is_all_enterprise_project
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this CreateAlertNoticeConfigResponse.

        ID

        :return: The id of this CreateAlertNoticeConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAlertNoticeConfigResponse.

        ID

        :param id: The id of this CreateAlertNoticeConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateAlertNoticeConfigResponse.

        告警通知名称

        :return: The name of this CreateAlertNoticeConfigResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAlertNoticeConfigResponse.

        告警通知名称

        :param name: The name of this CreateAlertNoticeConfigResponse.
        :type name: str
        """
        self._name = name

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateAlertNoticeConfigResponse.

        是否开启   - false: 不开启   - true: 开启

        :return: The enabled of this CreateAlertNoticeConfigResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateAlertNoticeConfigResponse.

        是否开启   - false: 不开启   - true: 开启

        :param enabled: The enabled of this CreateAlertNoticeConfigResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this CreateAlertNoticeConfigResponse.

        主题

        :return: The topic_urn of this CreateAlertNoticeConfigResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this CreateAlertNoticeConfigResponse.

        主题

        :param topic_urn: The topic_urn of this CreateAlertNoticeConfigResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def sendfreq(self):
        r"""Gets the sendfreq of this CreateAlertNoticeConfigResponse.

        时间间隔，单位为分钟。当通知类型为防护事件时，该参数表示在该时间间隔内，攻击次数等于或者大于设定阈值时，将发送告警通知，支持的值：5、15、30、60、120、360、720、1440；当通知类型为证书到期时，该参数表示每隔多长时间发送一次告警通知，支持的值1天、1周（需要转换成分钟）。

        :return: The sendfreq of this CreateAlertNoticeConfigResponse.
        :rtype: int
        """
        return self._sendfreq

    @sendfreq.setter
    def sendfreq(self, sendfreq):
        r"""Sets the sendfreq of this CreateAlertNoticeConfigResponse.

        时间间隔，单位为分钟。当通知类型为防护事件时，该参数表示在该时间间隔内，攻击次数等于或者大于设定阈值时，将发送告警通知，支持的值：5、15、30、60、120、360、720、1440；当通知类型为证书到期时，该参数表示每隔多长时间发送一次告警通知，支持的值1天、1周（需要转换成分钟）。

        :param sendfreq: The sendfreq of this CreateAlertNoticeConfigResponse.
        :type sendfreq: int
        """
        self._sendfreq = sendfreq

    @property
    def locale(self):
        r"""Gets the locale of this CreateAlertNoticeConfigResponse.

        语言

        :return: The locale of this CreateAlertNoticeConfigResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this CreateAlertNoticeConfigResponse.

        语言

        :param locale: The locale of this CreateAlertNoticeConfigResponse.
        :type locale: str
        """
        self._locale = locale

    @property
    def times(self):
        r"""Gets the times of this CreateAlertNoticeConfigResponse.

        当通知类型为防护事件时，需要填写该参数。在该时间间隔内，当攻击次数大于或等于您设置的阈值时才会发送告警通知

        :return: The times of this CreateAlertNoticeConfigResponse.
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        r"""Sets the times of this CreateAlertNoticeConfigResponse.

        当通知类型为防护事件时，需要填写该参数。在该时间间隔内，当攻击次数大于或等于您设置的阈值时才会发送告警通知

        :param times: The times of this CreateAlertNoticeConfigResponse.
        :type times: int
        """
        self._times = times

    @property
    def threat(self):
        r"""Gets the threat of this CreateAlertNoticeConfigResponse.

        事件类型

        :return: The threat of this CreateAlertNoticeConfigResponse.
        :rtype: list[str]
        """
        return self._threat

    @threat.setter
    def threat(self, threat):
        r"""Sets the threat of this CreateAlertNoticeConfigResponse.

        事件类型

        :param threat: The threat of this CreateAlertNoticeConfigResponse.
        :type threat: list[str]
        """
        self._threat = threat

    @property
    def prefer_html(self):
        r"""Gets the prefer_html of this CreateAlertNoticeConfigResponse.

        预留参数，可忽略

        :return: The prefer_html of this CreateAlertNoticeConfigResponse.
        :rtype: bool
        """
        return self._prefer_html

    @prefer_html.setter
    def prefer_html(self, prefer_html):
        r"""Sets the prefer_html of this CreateAlertNoticeConfigResponse.

        预留参数，可忽略

        :param prefer_html: The prefer_html of this CreateAlertNoticeConfigResponse.
        :type prefer_html: bool
        """
        self._prefer_html = prefer_html

    @property
    def notice_class(self):
        r"""Gets the notice_class of this CreateAlertNoticeConfigResponse.

        通知类型

        :return: The notice_class of this CreateAlertNoticeConfigResponse.
        :rtype: str
        """
        return self._notice_class

    @notice_class.setter
    def notice_class(self, notice_class):
        r"""Sets the notice_class of this CreateAlertNoticeConfigResponse.

        通知类型

        :param notice_class: The notice_class of this CreateAlertNoticeConfigResponse.
        :type notice_class: str
        """
        self._notice_class = notice_class

    @property
    def nearly_expired_time(self):
        r"""Gets the nearly_expired_time of this CreateAlertNoticeConfigResponse.

        提前通知天数

        :return: The nearly_expired_time of this CreateAlertNoticeConfigResponse.
        :rtype: str
        """
        return self._nearly_expired_time

    @nearly_expired_time.setter
    def nearly_expired_time(self, nearly_expired_time):
        r"""Sets the nearly_expired_time of this CreateAlertNoticeConfigResponse.

        提前通知天数

        :param nearly_expired_time: The nearly_expired_time of this CreateAlertNoticeConfigResponse.
        :type nearly_expired_time: str
        """
        self._nearly_expired_time = nearly_expired_time

    @property
    def is_all_enterprise_project(self):
        r"""Gets the is_all_enterprise_project of this CreateAlertNoticeConfigResponse.

        是否是所有企业项目

        :return: The is_all_enterprise_project of this CreateAlertNoticeConfigResponse.
        :rtype: bool
        """
        return self._is_all_enterprise_project

    @is_all_enterprise_project.setter
    def is_all_enterprise_project(self, is_all_enterprise_project):
        r"""Sets the is_all_enterprise_project of this CreateAlertNoticeConfigResponse.

        是否是所有企业项目

        :param is_all_enterprise_project: The is_all_enterprise_project of this CreateAlertNoticeConfigResponse.
        :type is_all_enterprise_project: bool
        """
        self._is_all_enterprise_project = is_all_enterprise_project

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateAlertNoticeConfigResponse.

        企业项目ID

        :return: The enterprise_project_id of this CreateAlertNoticeConfigResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateAlertNoticeConfigResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateAlertNoticeConfigResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateAlertNoticeConfigResponse.

        更新时间

        :return: The update_time of this CreateAlertNoticeConfigResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateAlertNoticeConfigResponse.

        更新时间

        :param update_time: The update_time of this CreateAlertNoticeConfigResponse.
        :type update_time: int
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
        if not isinstance(other, CreateAlertNoticeConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
