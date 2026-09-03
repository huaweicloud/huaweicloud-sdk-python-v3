# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertConfigVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_expression': 'list[AlertExpression]',
        'alert_period_begin': 'str',
        'alert_period_end': 'str',
        'block_alert': 'BlockAlert',
        'default_alert_template': 'AlertTemplate',
        'enable': 'str',
        'error_alert': 'ErrorAlert',
        'failed_alert': 'FailedAlert',
        'recover_notice_enable': 'str',
        'restrain_alert_enable': 'str',
        'resume_alert_num': 'int',
        'resume_alert_time': 'str',
        'timeout_alert': 'TimeoutAlert',
        'timeout_alert_v4': 'TimeoutAlert'
    }

    attribute_map = {
        'alert_expression': 'alert_expression',
        'alert_period_begin': 'alertPeriodBegin',
        'alert_period_end': 'alertPeriodEnd',
        'block_alert': 'blockAlert',
        'default_alert_template': 'defaultAlertTemplate',
        'enable': 'enable',
        'error_alert': 'errorAlert',
        'failed_alert': 'failedAlert',
        'recover_notice_enable': 'recoverNoticeEnable',
        'restrain_alert_enable': 'restrainAlertEnable',
        'resume_alert_num': 'resume_alert_num',
        'resume_alert_time': 'resumeAlertTime',
        'timeout_alert': 'timeoutAlert',
        'timeout_alert_v4': 'timeoutAlertV4'
    }

    def __init__(self, alert_expression=None, alert_period_begin=None, alert_period_end=None, block_alert=None, default_alert_template=None, enable=None, error_alert=None, failed_alert=None, recover_notice_enable=None, restrain_alert_enable=None, resume_alert_num=None, resume_alert_time=None, timeout_alert=None, timeout_alert_v4=None):
        r"""AlertConfigVo

        The model defined in huaweicloud sdk

        :param alert_expression: 告警表达式
        :type alert_expression: list[:class:`huaweicloudsdkcloudtest.v1.AlertExpression`]
        :param alert_period_begin: 告警区间，开始时间
        :type alert_period_begin: str
        :param alert_period_end: 告警区间，开始时间
        :type alert_period_end: str
        :param block_alert: 
        :type block_alert: :class:`huaweicloudsdkcloudtest.v1.BlockAlert`
        :param default_alert_template: 
        :type default_alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        :param enable: 告警开启 0关闭 1开启
        :type enable: str
        :param error_alert: 
        :type error_alert: :class:`huaweicloudsdkcloudtest.v1.ErrorAlert`
        :param failed_alert: 
        :type failed_alert: :class:`huaweicloudsdkcloudtest.v1.FailedAlert`
        :param recover_notice_enable: 告警恢复通知开关 0关闭 1开启
        :type recover_notice_enable: str
        :param restrain_alert_enable: 告警收敛开关 0关闭 1开启
        :type restrain_alert_enable: str
        :param resume_alert_num: 智能告警 成功多少次后发送恢复告警
        :type resume_alert_num: int
        :param resume_alert_time: 智能告警 指定时间后发送恢复告警
        :type resume_alert_time: str
        :param timeout_alert: 
        :type timeout_alert: :class:`huaweicloudsdkcloudtest.v1.TimeoutAlert`
        :param timeout_alert_v4: 
        :type timeout_alert_v4: :class:`huaweicloudsdkcloudtest.v1.TimeoutAlert`
        """
        
        

        self._alert_expression = None
        self._alert_period_begin = None
        self._alert_period_end = None
        self._block_alert = None
        self._default_alert_template = None
        self._enable = None
        self._error_alert = None
        self._failed_alert = None
        self._recover_notice_enable = None
        self._restrain_alert_enable = None
        self._resume_alert_num = None
        self._resume_alert_time = None
        self._timeout_alert = None
        self._timeout_alert_v4 = None
        self.discriminator = None

        if alert_expression is not None:
            self.alert_expression = alert_expression
        if alert_period_begin is not None:
            self.alert_period_begin = alert_period_begin
        if alert_period_end is not None:
            self.alert_period_end = alert_period_end
        if block_alert is not None:
            self.block_alert = block_alert
        if default_alert_template is not None:
            self.default_alert_template = default_alert_template
        if enable is not None:
            self.enable = enable
        if error_alert is not None:
            self.error_alert = error_alert
        if failed_alert is not None:
            self.failed_alert = failed_alert
        if recover_notice_enable is not None:
            self.recover_notice_enable = recover_notice_enable
        if restrain_alert_enable is not None:
            self.restrain_alert_enable = restrain_alert_enable
        if resume_alert_num is not None:
            self.resume_alert_num = resume_alert_num
        if resume_alert_time is not None:
            self.resume_alert_time = resume_alert_time
        if timeout_alert is not None:
            self.timeout_alert = timeout_alert
        if timeout_alert_v4 is not None:
            self.timeout_alert_v4 = timeout_alert_v4

    @property
    def alert_expression(self):
        r"""Gets the alert_expression of this AlertConfigVo.

        告警表达式

        :return: The alert_expression of this AlertConfigVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AlertExpression`]
        """
        return self._alert_expression

    @alert_expression.setter
    def alert_expression(self, alert_expression):
        r"""Sets the alert_expression of this AlertConfigVo.

        告警表达式

        :param alert_expression: The alert_expression of this AlertConfigVo.
        :type alert_expression: list[:class:`huaweicloudsdkcloudtest.v1.AlertExpression`]
        """
        self._alert_expression = alert_expression

    @property
    def alert_period_begin(self):
        r"""Gets the alert_period_begin of this AlertConfigVo.

        告警区间，开始时间

        :return: The alert_period_begin of this AlertConfigVo.
        :rtype: str
        """
        return self._alert_period_begin

    @alert_period_begin.setter
    def alert_period_begin(self, alert_period_begin):
        r"""Sets the alert_period_begin of this AlertConfigVo.

        告警区间，开始时间

        :param alert_period_begin: The alert_period_begin of this AlertConfigVo.
        :type alert_period_begin: str
        """
        self._alert_period_begin = alert_period_begin

    @property
    def alert_period_end(self):
        r"""Gets the alert_period_end of this AlertConfigVo.

        告警区间，开始时间

        :return: The alert_period_end of this AlertConfigVo.
        :rtype: str
        """
        return self._alert_period_end

    @alert_period_end.setter
    def alert_period_end(self, alert_period_end):
        r"""Sets the alert_period_end of this AlertConfigVo.

        告警区间，开始时间

        :param alert_period_end: The alert_period_end of this AlertConfigVo.
        :type alert_period_end: str
        """
        self._alert_period_end = alert_period_end

    @property
    def block_alert(self):
        r"""Gets the block_alert of this AlertConfigVo.

        :return: The block_alert of this AlertConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.BlockAlert`
        """
        return self._block_alert

    @block_alert.setter
    def block_alert(self, block_alert):
        r"""Sets the block_alert of this AlertConfigVo.

        :param block_alert: The block_alert of this AlertConfigVo.
        :type block_alert: :class:`huaweicloudsdkcloudtest.v1.BlockAlert`
        """
        self._block_alert = block_alert

    @property
    def default_alert_template(self):
        r"""Gets the default_alert_template of this AlertConfigVo.

        :return: The default_alert_template of this AlertConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        return self._default_alert_template

    @default_alert_template.setter
    def default_alert_template(self, default_alert_template):
        r"""Sets the default_alert_template of this AlertConfigVo.

        :param default_alert_template: The default_alert_template of this AlertConfigVo.
        :type default_alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        self._default_alert_template = default_alert_template

    @property
    def enable(self):
        r"""Gets the enable of this AlertConfigVo.

        告警开启 0关闭 1开启

        :return: The enable of this AlertConfigVo.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this AlertConfigVo.

        告警开启 0关闭 1开启

        :param enable: The enable of this AlertConfigVo.
        :type enable: str
        """
        self._enable = enable

    @property
    def error_alert(self):
        r"""Gets the error_alert of this AlertConfigVo.

        :return: The error_alert of this AlertConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ErrorAlert`
        """
        return self._error_alert

    @error_alert.setter
    def error_alert(self, error_alert):
        r"""Sets the error_alert of this AlertConfigVo.

        :param error_alert: The error_alert of this AlertConfigVo.
        :type error_alert: :class:`huaweicloudsdkcloudtest.v1.ErrorAlert`
        """
        self._error_alert = error_alert

    @property
    def failed_alert(self):
        r"""Gets the failed_alert of this AlertConfigVo.

        :return: The failed_alert of this AlertConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.FailedAlert`
        """
        return self._failed_alert

    @failed_alert.setter
    def failed_alert(self, failed_alert):
        r"""Sets the failed_alert of this AlertConfigVo.

        :param failed_alert: The failed_alert of this AlertConfigVo.
        :type failed_alert: :class:`huaweicloudsdkcloudtest.v1.FailedAlert`
        """
        self._failed_alert = failed_alert

    @property
    def recover_notice_enable(self):
        r"""Gets the recover_notice_enable of this AlertConfigVo.

        告警恢复通知开关 0关闭 1开启

        :return: The recover_notice_enable of this AlertConfigVo.
        :rtype: str
        """
        return self._recover_notice_enable

    @recover_notice_enable.setter
    def recover_notice_enable(self, recover_notice_enable):
        r"""Sets the recover_notice_enable of this AlertConfigVo.

        告警恢复通知开关 0关闭 1开启

        :param recover_notice_enable: The recover_notice_enable of this AlertConfigVo.
        :type recover_notice_enable: str
        """
        self._recover_notice_enable = recover_notice_enable

    @property
    def restrain_alert_enable(self):
        r"""Gets the restrain_alert_enable of this AlertConfigVo.

        告警收敛开关 0关闭 1开启

        :return: The restrain_alert_enable of this AlertConfigVo.
        :rtype: str
        """
        return self._restrain_alert_enable

    @restrain_alert_enable.setter
    def restrain_alert_enable(self, restrain_alert_enable):
        r"""Sets the restrain_alert_enable of this AlertConfigVo.

        告警收敛开关 0关闭 1开启

        :param restrain_alert_enable: The restrain_alert_enable of this AlertConfigVo.
        :type restrain_alert_enable: str
        """
        self._restrain_alert_enable = restrain_alert_enable

    @property
    def resume_alert_num(self):
        r"""Gets the resume_alert_num of this AlertConfigVo.

        智能告警 成功多少次后发送恢复告警

        :return: The resume_alert_num of this AlertConfigVo.
        :rtype: int
        """
        return self._resume_alert_num

    @resume_alert_num.setter
    def resume_alert_num(self, resume_alert_num):
        r"""Sets the resume_alert_num of this AlertConfigVo.

        智能告警 成功多少次后发送恢复告警

        :param resume_alert_num: The resume_alert_num of this AlertConfigVo.
        :type resume_alert_num: int
        """
        self._resume_alert_num = resume_alert_num

    @property
    def resume_alert_time(self):
        r"""Gets the resume_alert_time of this AlertConfigVo.

        智能告警 指定时间后发送恢复告警

        :return: The resume_alert_time of this AlertConfigVo.
        :rtype: str
        """
        return self._resume_alert_time

    @resume_alert_time.setter
    def resume_alert_time(self, resume_alert_time):
        r"""Sets the resume_alert_time of this AlertConfigVo.

        智能告警 指定时间后发送恢复告警

        :param resume_alert_time: The resume_alert_time of this AlertConfigVo.
        :type resume_alert_time: str
        """
        self._resume_alert_time = resume_alert_time

    @property
    def timeout_alert(self):
        r"""Gets the timeout_alert of this AlertConfigVo.

        :return: The timeout_alert of this AlertConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TimeoutAlert`
        """
        return self._timeout_alert

    @timeout_alert.setter
    def timeout_alert(self, timeout_alert):
        r"""Sets the timeout_alert of this AlertConfigVo.

        :param timeout_alert: The timeout_alert of this AlertConfigVo.
        :type timeout_alert: :class:`huaweicloudsdkcloudtest.v1.TimeoutAlert`
        """
        self._timeout_alert = timeout_alert

    @property
    def timeout_alert_v4(self):
        r"""Gets the timeout_alert_v4 of this AlertConfigVo.

        :return: The timeout_alert_v4 of this AlertConfigVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TimeoutAlert`
        """
        return self._timeout_alert_v4

    @timeout_alert_v4.setter
    def timeout_alert_v4(self, timeout_alert_v4):
        r"""Sets the timeout_alert_v4 of this AlertConfigVo.

        :param timeout_alert_v4: The timeout_alert_v4 of this AlertConfigVo.
        :type timeout_alert_v4: :class:`huaweicloudsdkcloudtest.v1.TimeoutAlert`
        """
        self._timeout_alert_v4 = timeout_alert_v4

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlertConfigVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
