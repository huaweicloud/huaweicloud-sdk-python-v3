# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateAntiVirusResultRequestInfo:

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
        'memo': 'str',
        'operate_results': 'list[OperateResultRequestInfo]',
        'event_white_rules': 'list[AntiVirusEventWhiteRuleListRequestInfo]'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'memo': 'memo',
        'operate_results': 'operate_results',
        'event_white_rules': 'event_white_rules'
    }

    def __init__(self, operate_type=None, memo=None, operate_results=None, event_white_rules=None):
        r"""OperateAntiVirusResultRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: 处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - manual_isolate_and_kill：隔离文件   - unhandle：取消手动处理   - do_not_ignore：取消忽略   - remove_from_alarm_whitelist：删除告警白名单   - do_not_isolate_or_kill：取消隔离文件
        :type operate_type: str
        :param memo: 备注信息
        :type memo: str
        :param operate_results: 处置的结果列表
        :type operate_results: list[:class:`huaweicloudsdkhss.v5.OperateResultRequestInfo`]
        :param event_white_rules: 新增告警白名单规则列表
        :type event_white_rules: list[:class:`huaweicloudsdkhss.v5.AntiVirusEventWhiteRuleListRequestInfo`]
        """
        
        

        self._operate_type = None
        self._memo = None
        self._operate_results = None
        self._event_white_rules = None
        self.discriminator = None

        self.operate_type = operate_type
        if memo is not None:
            self.memo = memo
        if operate_results is not None:
            self.operate_results = operate_results
        if event_white_rules is not None:
            self.event_white_rules = event_white_rules

    @property
    def operate_type(self):
        r"""Gets the operate_type of this OperateAntiVirusResultRequestInfo.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - manual_isolate_and_kill：隔离文件   - unhandle：取消手动处理   - do_not_ignore：取消忽略   - remove_from_alarm_whitelist：删除告警白名单   - do_not_isolate_or_kill：取消隔离文件

        :return: The operate_type of this OperateAntiVirusResultRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this OperateAntiVirusResultRequestInfo.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - manual_isolate_and_kill：隔离文件   - unhandle：取消手动处理   - do_not_ignore：取消忽略   - remove_from_alarm_whitelist：删除告警白名单   - do_not_isolate_or_kill：取消隔离文件

        :param operate_type: The operate_type of this OperateAntiVirusResultRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def memo(self):
        r"""Gets the memo of this OperateAntiVirusResultRequestInfo.

        备注信息

        :return: The memo of this OperateAntiVirusResultRequestInfo.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        r"""Sets the memo of this OperateAntiVirusResultRequestInfo.

        备注信息

        :param memo: The memo of this OperateAntiVirusResultRequestInfo.
        :type memo: str
        """
        self._memo = memo

    @property
    def operate_results(self):
        r"""Gets the operate_results of this OperateAntiVirusResultRequestInfo.

        处置的结果列表

        :return: The operate_results of this OperateAntiVirusResultRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.OperateResultRequestInfo`]
        """
        return self._operate_results

    @operate_results.setter
    def operate_results(self, operate_results):
        r"""Sets the operate_results of this OperateAntiVirusResultRequestInfo.

        处置的结果列表

        :param operate_results: The operate_results of this OperateAntiVirusResultRequestInfo.
        :type operate_results: list[:class:`huaweicloudsdkhss.v5.OperateResultRequestInfo`]
        """
        self._operate_results = operate_results

    @property
    def event_white_rules(self):
        r"""Gets the event_white_rules of this OperateAntiVirusResultRequestInfo.

        新增告警白名单规则列表

        :return: The event_white_rules of this OperateAntiVirusResultRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AntiVirusEventWhiteRuleListRequestInfo`]
        """
        return self._event_white_rules

    @event_white_rules.setter
    def event_white_rules(self, event_white_rules):
        r"""Sets the event_white_rules of this OperateAntiVirusResultRequestInfo.

        新增告警白名单规则列表

        :param event_white_rules: The event_white_rules of this OperateAntiVirusResultRequestInfo.
        :type event_white_rules: list[:class:`huaweicloudsdkhss.v5.AntiVirusEventWhiteRuleListRequestInfo`]
        """
        self._event_white_rules = event_white_rules

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
        if not isinstance(other, OperateAntiVirusResultRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
