# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeEventRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_type': 'str',
        'handler': 'str',
        'operate_event_list': 'list[OperateEventRequestInfo]',
        'event_white_rule_list': 'list[EventWhiteRuleListRequestInfo]'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'handler': 'handler',
        'operate_event_list': 'operate_event_list',
        'event_white_rule_list': 'event_white_rule_list'
    }

    def __init__(self, operate_type=None, handler=None, operate_event_list=None, event_white_rule_list=None):
        r"""ChangeEventRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: 处理方式，包含如下:   - mark_as_handled : 手动处理   - ignore : 忽略   - add_to_alarm_whitelist : 加入告警白名单   - add_to_login_whitelist : 加入登录白名单   - isolate_and_kill : 隔离查杀   - unhandle : 取消手动处理   - do_not_ignore : 取消忽略   - remove_from_alarm_whitelist : 删除告警白名单   - remove_from_login_whitelist : 删除登录白名单   - do_not_isolate_or_kill : 取消隔离查杀
        :type operate_type: str
        :param handler: 备注信息，已处理的告警才有
        :type handler: str
        :param operate_event_list: 操作的事件列表
        :type operate_event_list: list[:class:`huaweicloudsdkhss.v5.OperateEventRequestInfo`]
        :param event_white_rule_list: 用户自定义告警白名单规则列表
        :type event_white_rule_list: list[:class:`huaweicloudsdkhss.v5.EventWhiteRuleListRequestInfo`]
        """
        
        

        self._operate_type = None
        self._handler = None
        self._operate_event_list = None
        self._event_white_rule_list = None
        self.discriminator = None

        self.operate_type = operate_type
        if handler is not None:
            self.handler = handler
        self.operate_event_list = operate_event_list
        if event_white_rule_list is not None:
            self.event_white_rule_list = event_white_rule_list

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ChangeEventRequestInfo.

        处理方式，包含如下:   - mark_as_handled : 手动处理   - ignore : 忽略   - add_to_alarm_whitelist : 加入告警白名单   - add_to_login_whitelist : 加入登录白名单   - isolate_and_kill : 隔离查杀   - unhandle : 取消手动处理   - do_not_ignore : 取消忽略   - remove_from_alarm_whitelist : 删除告警白名单   - remove_from_login_whitelist : 删除登录白名单   - do_not_isolate_or_kill : 取消隔离查杀

        :return: The operate_type of this ChangeEventRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ChangeEventRequestInfo.

        处理方式，包含如下:   - mark_as_handled : 手动处理   - ignore : 忽略   - add_to_alarm_whitelist : 加入告警白名单   - add_to_login_whitelist : 加入登录白名单   - isolate_and_kill : 隔离查杀   - unhandle : 取消手动处理   - do_not_ignore : 取消忽略   - remove_from_alarm_whitelist : 删除告警白名单   - remove_from_login_whitelist : 删除登录白名单   - do_not_isolate_or_kill : 取消隔离查杀

        :param operate_type: The operate_type of this ChangeEventRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def handler(self):
        r"""Gets the handler of this ChangeEventRequestInfo.

        备注信息，已处理的告警才有

        :return: The handler of this ChangeEventRequestInfo.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        r"""Sets the handler of this ChangeEventRequestInfo.

        备注信息，已处理的告警才有

        :param handler: The handler of this ChangeEventRequestInfo.
        :type handler: str
        """
        self._handler = handler

    @property
    def operate_event_list(self):
        r"""Gets the operate_event_list of this ChangeEventRequestInfo.

        操作的事件列表

        :return: The operate_event_list of this ChangeEventRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.OperateEventRequestInfo`]
        """
        return self._operate_event_list

    @operate_event_list.setter
    def operate_event_list(self, operate_event_list):
        r"""Sets the operate_event_list of this ChangeEventRequestInfo.

        操作的事件列表

        :param operate_event_list: The operate_event_list of this ChangeEventRequestInfo.
        :type operate_event_list: list[:class:`huaweicloudsdkhss.v5.OperateEventRequestInfo`]
        """
        self._operate_event_list = operate_event_list

    @property
    def event_white_rule_list(self):
        r"""Gets the event_white_rule_list of this ChangeEventRequestInfo.

        用户自定义告警白名单规则列表

        :return: The event_white_rule_list of this ChangeEventRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventWhiteRuleListRequestInfo`]
        """
        return self._event_white_rule_list

    @event_white_rule_list.setter
    def event_white_rule_list(self, event_white_rule_list):
        r"""Sets the event_white_rule_list of this ChangeEventRequestInfo.

        用户自定义告警白名单规则列表

        :param event_white_rule_list: The event_white_rule_list of this ChangeEventRequestInfo.
        :type event_white_rule_list: list[:class:`huaweicloudsdkhss.v5.EventWhiteRuleListRequestInfo`]
        """
        self._event_white_rule_list = event_white_rule_list

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
        if not isinstance(other, ChangeEventRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
