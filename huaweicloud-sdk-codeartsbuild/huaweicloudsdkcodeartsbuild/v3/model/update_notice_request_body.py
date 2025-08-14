# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNoticeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notice_type': 'str',
        'enabled_event_type_names': 'list[str]',
        'send_switch': 'str',
        'param_config': 'str',
        'use_project_notice': 'str'
    }

    attribute_map = {
        'notice_type': 'notice_type',
        'enabled_event_type_names': 'enabled_event_type_names',
        'send_switch': 'send_switch',
        'param_config': 'param_config',
        'use_project_notice': 'use_project_notice'
    }

    def __init__(self, notice_type=None, enabled_event_type_names=None, send_switch=None, param_config=None, use_project_notice=None):
        r"""UpdateNoticeRequestBody

        The model defined in huaweicloud sdk

        :param notice_type: 通知类型
        :type notice_type: str
        :param enabled_event_type_names: 开启的通知的种类
        :type enabled_event_type_names: list[str]
        :param send_switch: 是否开启消息通知。
        :type send_switch: str
        :param param_config: 通知参数配置
        :type param_config: str
        :param use_project_notice: 是否使用项目级消息通知设置。
        :type use_project_notice: str
        """
        
        

        self._notice_type = None
        self._enabled_event_type_names = None
        self._send_switch = None
        self._param_config = None
        self._use_project_notice = None
        self.discriminator = None

        self.notice_type = notice_type
        self.enabled_event_type_names = enabled_event_type_names
        if send_switch is not None:
            self.send_switch = send_switch
        if param_config is not None:
            self.param_config = param_config
        if use_project_notice is not None:
            self.use_project_notice = use_project_notice

    @property
    def notice_type(self):
        r"""Gets the notice_type of this UpdateNoticeRequestBody.

        通知类型

        :return: The notice_type of this UpdateNoticeRequestBody.
        :rtype: str
        """
        return self._notice_type

    @notice_type.setter
    def notice_type(self, notice_type):
        r"""Sets the notice_type of this UpdateNoticeRequestBody.

        通知类型

        :param notice_type: The notice_type of this UpdateNoticeRequestBody.
        :type notice_type: str
        """
        self._notice_type = notice_type

    @property
    def enabled_event_type_names(self):
        r"""Gets the enabled_event_type_names of this UpdateNoticeRequestBody.

        开启的通知的种类

        :return: The enabled_event_type_names of this UpdateNoticeRequestBody.
        :rtype: list[str]
        """
        return self._enabled_event_type_names

    @enabled_event_type_names.setter
    def enabled_event_type_names(self, enabled_event_type_names):
        r"""Sets the enabled_event_type_names of this UpdateNoticeRequestBody.

        开启的通知的种类

        :param enabled_event_type_names: The enabled_event_type_names of this UpdateNoticeRequestBody.
        :type enabled_event_type_names: list[str]
        """
        self._enabled_event_type_names = enabled_event_type_names

    @property
    def send_switch(self):
        r"""Gets the send_switch of this UpdateNoticeRequestBody.

        是否开启消息通知。

        :return: The send_switch of this UpdateNoticeRequestBody.
        :rtype: str
        """
        return self._send_switch

    @send_switch.setter
    def send_switch(self, send_switch):
        r"""Sets the send_switch of this UpdateNoticeRequestBody.

        是否开启消息通知。

        :param send_switch: The send_switch of this UpdateNoticeRequestBody.
        :type send_switch: str
        """
        self._send_switch = send_switch

    @property
    def param_config(self):
        r"""Gets the param_config of this UpdateNoticeRequestBody.

        通知参数配置

        :return: The param_config of this UpdateNoticeRequestBody.
        :rtype: str
        """
        return self._param_config

    @param_config.setter
    def param_config(self, param_config):
        r"""Sets the param_config of this UpdateNoticeRequestBody.

        通知参数配置

        :param param_config: The param_config of this UpdateNoticeRequestBody.
        :type param_config: str
        """
        self._param_config = param_config

    @property
    def use_project_notice(self):
        r"""Gets the use_project_notice of this UpdateNoticeRequestBody.

        是否使用项目级消息通知设置。

        :return: The use_project_notice of this UpdateNoticeRequestBody.
        :rtype: str
        """
        return self._use_project_notice

    @use_project_notice.setter
    def use_project_notice(self, use_project_notice):
        r"""Sets the use_project_notice of this UpdateNoticeRequestBody.

        是否使用项目级消息通知设置。

        :param use_project_notice: The use_project_notice of this UpdateNoticeRequestBody.
        :type use_project_notice: str
        """
        self._use_project_notice = use_project_notice

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
        if not isinstance(other, UpdateNoticeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
