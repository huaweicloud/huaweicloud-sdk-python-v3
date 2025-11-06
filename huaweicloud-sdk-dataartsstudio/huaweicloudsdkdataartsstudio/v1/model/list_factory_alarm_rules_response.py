# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryAlarmRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rules_items_details': 'list[AlarmRulesItemsDetails]',
        'assurance_mission_commitment_time_not_completed_count': 'int',
        'assurance_mission_failed_count': 'int',
        'assurance_mission_warning_time_not_completed_count': 'int',
        'baseline_error_count': 'int',
        'cancel_jobs_count': 'int',
        'exception_count': 'int',
        'modify_count': 'int',
        'multi_period_unfinished_count': 'int',
        'overload_count': 'int',
        'recover_jobs_count': 'int',
        'success_count': 'int',
        'total': 'int',
        'total_all': 'int',
        'unfinished_count': 'int'
    }

    attribute_map = {
        'alarm_rules_items_details': 'alarm_rules_items_details',
        'assurance_mission_commitment_time_not_completed_count': 'assurance_mission_commitment_time_not_completed_count',
        'assurance_mission_failed_count': 'assurance_mission_failed_count',
        'assurance_mission_warning_time_not_completed_count': 'assurance_mission_warning_time_not_completed_count',
        'baseline_error_count': 'baseline_error_count',
        'cancel_jobs_count': 'cancel_jobs_count',
        'exception_count': 'exception_count',
        'modify_count': 'modify_count',
        'multi_period_unfinished_count': 'multi_period_unfinished_count',
        'overload_count': 'overload_count',
        'recover_jobs_count': 'recover_jobs_count',
        'success_count': 'success_count',
        'total': 'total',
        'total_all': 'total_all',
        'unfinished_count': 'unfinished_count'
    }

    def __init__(self, alarm_rules_items_details=None, assurance_mission_commitment_time_not_completed_count=None, assurance_mission_failed_count=None, assurance_mission_warning_time_not_completed_count=None, baseline_error_count=None, cancel_jobs_count=None, exception_count=None, modify_count=None, multi_period_unfinished_count=None, overload_count=None, recover_jobs_count=None, success_count=None, total=None, total_all=None, unfinished_count=None):
        r"""ListFactoryAlarmRulesResponse

        The model defined in huaweicloud sdk

        :param alarm_rules_items_details: 通知规则明细。
        :type alarm_rules_items_details: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmRulesItemsDetails`]
        :param assurance_mission_commitment_time_not_completed_count: 保障作业承诺时间未完成数量。
        :type assurance_mission_commitment_time_not_completed_count: int
        :param assurance_mission_failed_count: 保障作业失败数量。
        :type assurance_mission_failed_count: int
        :param assurance_mission_warning_time_not_completed_count: 保障作业预警时间未完成数量。
        :type assurance_mission_warning_time_not_completed_count: int
        :param baseline_error_count: 基线作业失败数量。
        :type baseline_error_count: int
        :param cancel_jobs_count: 作业取消数量。
        :type cancel_jobs_count: int
        :param exception_count: 作业异常数量。
        :type exception_count: int
        :param modify_count: 修改作业数量。
        :type modify_count: int
        :param multi_period_unfinished_count: 多周期未完成数量。
        :type multi_period_unfinished_count: int
        :param overload_count: 资源繁忙作业数量。
        :type overload_count: int
        :param recover_jobs_count: 失败作业恢复数量。
        :type recover_jobs_count: int
        :param success_count: 作业成功数量。
        :type success_count: int
        :param total: 作业总数量。
        :type total: int
        :param total_all: 通知规则数量。
        :type total_all: int
        :param unfinished_count: 未完成作业数量。
        :type unfinished_count: int
        """
        
        super().__init__()

        self._alarm_rules_items_details = None
        self._assurance_mission_commitment_time_not_completed_count = None
        self._assurance_mission_failed_count = None
        self._assurance_mission_warning_time_not_completed_count = None
        self._baseline_error_count = None
        self._cancel_jobs_count = None
        self._exception_count = None
        self._modify_count = None
        self._multi_period_unfinished_count = None
        self._overload_count = None
        self._recover_jobs_count = None
        self._success_count = None
        self._total = None
        self._total_all = None
        self._unfinished_count = None
        self.discriminator = None

        if alarm_rules_items_details is not None:
            self.alarm_rules_items_details = alarm_rules_items_details
        if assurance_mission_commitment_time_not_completed_count is not None:
            self.assurance_mission_commitment_time_not_completed_count = assurance_mission_commitment_time_not_completed_count
        if assurance_mission_failed_count is not None:
            self.assurance_mission_failed_count = assurance_mission_failed_count
        if assurance_mission_warning_time_not_completed_count is not None:
            self.assurance_mission_warning_time_not_completed_count = assurance_mission_warning_time_not_completed_count
        if baseline_error_count is not None:
            self.baseline_error_count = baseline_error_count
        if cancel_jobs_count is not None:
            self.cancel_jobs_count = cancel_jobs_count
        if exception_count is not None:
            self.exception_count = exception_count
        if modify_count is not None:
            self.modify_count = modify_count
        if multi_period_unfinished_count is not None:
            self.multi_period_unfinished_count = multi_period_unfinished_count
        if overload_count is not None:
            self.overload_count = overload_count
        if recover_jobs_count is not None:
            self.recover_jobs_count = recover_jobs_count
        if success_count is not None:
            self.success_count = success_count
        if total is not None:
            self.total = total
        if total_all is not None:
            self.total_all = total_all
        if unfinished_count is not None:
            self.unfinished_count = unfinished_count

    @property
    def alarm_rules_items_details(self):
        r"""Gets the alarm_rules_items_details of this ListFactoryAlarmRulesResponse.

        通知规则明细。

        :return: The alarm_rules_items_details of this ListFactoryAlarmRulesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmRulesItemsDetails`]
        """
        return self._alarm_rules_items_details

    @alarm_rules_items_details.setter
    def alarm_rules_items_details(self, alarm_rules_items_details):
        r"""Sets the alarm_rules_items_details of this ListFactoryAlarmRulesResponse.

        通知规则明细。

        :param alarm_rules_items_details: The alarm_rules_items_details of this ListFactoryAlarmRulesResponse.
        :type alarm_rules_items_details: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmRulesItemsDetails`]
        """
        self._alarm_rules_items_details = alarm_rules_items_details

    @property
    def assurance_mission_commitment_time_not_completed_count(self):
        r"""Gets the assurance_mission_commitment_time_not_completed_count of this ListFactoryAlarmRulesResponse.

        保障作业承诺时间未完成数量。

        :return: The assurance_mission_commitment_time_not_completed_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._assurance_mission_commitment_time_not_completed_count

    @assurance_mission_commitment_time_not_completed_count.setter
    def assurance_mission_commitment_time_not_completed_count(self, assurance_mission_commitment_time_not_completed_count):
        r"""Sets the assurance_mission_commitment_time_not_completed_count of this ListFactoryAlarmRulesResponse.

        保障作业承诺时间未完成数量。

        :param assurance_mission_commitment_time_not_completed_count: The assurance_mission_commitment_time_not_completed_count of this ListFactoryAlarmRulesResponse.
        :type assurance_mission_commitment_time_not_completed_count: int
        """
        self._assurance_mission_commitment_time_not_completed_count = assurance_mission_commitment_time_not_completed_count

    @property
    def assurance_mission_failed_count(self):
        r"""Gets the assurance_mission_failed_count of this ListFactoryAlarmRulesResponse.

        保障作业失败数量。

        :return: The assurance_mission_failed_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._assurance_mission_failed_count

    @assurance_mission_failed_count.setter
    def assurance_mission_failed_count(self, assurance_mission_failed_count):
        r"""Sets the assurance_mission_failed_count of this ListFactoryAlarmRulesResponse.

        保障作业失败数量。

        :param assurance_mission_failed_count: The assurance_mission_failed_count of this ListFactoryAlarmRulesResponse.
        :type assurance_mission_failed_count: int
        """
        self._assurance_mission_failed_count = assurance_mission_failed_count

    @property
    def assurance_mission_warning_time_not_completed_count(self):
        r"""Gets the assurance_mission_warning_time_not_completed_count of this ListFactoryAlarmRulesResponse.

        保障作业预警时间未完成数量。

        :return: The assurance_mission_warning_time_not_completed_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._assurance_mission_warning_time_not_completed_count

    @assurance_mission_warning_time_not_completed_count.setter
    def assurance_mission_warning_time_not_completed_count(self, assurance_mission_warning_time_not_completed_count):
        r"""Sets the assurance_mission_warning_time_not_completed_count of this ListFactoryAlarmRulesResponse.

        保障作业预警时间未完成数量。

        :param assurance_mission_warning_time_not_completed_count: The assurance_mission_warning_time_not_completed_count of this ListFactoryAlarmRulesResponse.
        :type assurance_mission_warning_time_not_completed_count: int
        """
        self._assurance_mission_warning_time_not_completed_count = assurance_mission_warning_time_not_completed_count

    @property
    def baseline_error_count(self):
        r"""Gets the baseline_error_count of this ListFactoryAlarmRulesResponse.

        基线作业失败数量。

        :return: The baseline_error_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._baseline_error_count

    @baseline_error_count.setter
    def baseline_error_count(self, baseline_error_count):
        r"""Sets the baseline_error_count of this ListFactoryAlarmRulesResponse.

        基线作业失败数量。

        :param baseline_error_count: The baseline_error_count of this ListFactoryAlarmRulesResponse.
        :type baseline_error_count: int
        """
        self._baseline_error_count = baseline_error_count

    @property
    def cancel_jobs_count(self):
        r"""Gets the cancel_jobs_count of this ListFactoryAlarmRulesResponse.

        作业取消数量。

        :return: The cancel_jobs_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._cancel_jobs_count

    @cancel_jobs_count.setter
    def cancel_jobs_count(self, cancel_jobs_count):
        r"""Sets the cancel_jobs_count of this ListFactoryAlarmRulesResponse.

        作业取消数量。

        :param cancel_jobs_count: The cancel_jobs_count of this ListFactoryAlarmRulesResponse.
        :type cancel_jobs_count: int
        """
        self._cancel_jobs_count = cancel_jobs_count

    @property
    def exception_count(self):
        r"""Gets the exception_count of this ListFactoryAlarmRulesResponse.

        作业异常数量。

        :return: The exception_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._exception_count

    @exception_count.setter
    def exception_count(self, exception_count):
        r"""Sets the exception_count of this ListFactoryAlarmRulesResponse.

        作业异常数量。

        :param exception_count: The exception_count of this ListFactoryAlarmRulesResponse.
        :type exception_count: int
        """
        self._exception_count = exception_count

    @property
    def modify_count(self):
        r"""Gets the modify_count of this ListFactoryAlarmRulesResponse.

        修改作业数量。

        :return: The modify_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._modify_count

    @modify_count.setter
    def modify_count(self, modify_count):
        r"""Sets the modify_count of this ListFactoryAlarmRulesResponse.

        修改作业数量。

        :param modify_count: The modify_count of this ListFactoryAlarmRulesResponse.
        :type modify_count: int
        """
        self._modify_count = modify_count

    @property
    def multi_period_unfinished_count(self):
        r"""Gets the multi_period_unfinished_count of this ListFactoryAlarmRulesResponse.

        多周期未完成数量。

        :return: The multi_period_unfinished_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._multi_period_unfinished_count

    @multi_period_unfinished_count.setter
    def multi_period_unfinished_count(self, multi_period_unfinished_count):
        r"""Sets the multi_period_unfinished_count of this ListFactoryAlarmRulesResponse.

        多周期未完成数量。

        :param multi_period_unfinished_count: The multi_period_unfinished_count of this ListFactoryAlarmRulesResponse.
        :type multi_period_unfinished_count: int
        """
        self._multi_period_unfinished_count = multi_period_unfinished_count

    @property
    def overload_count(self):
        r"""Gets the overload_count of this ListFactoryAlarmRulesResponse.

        资源繁忙作业数量。

        :return: The overload_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._overload_count

    @overload_count.setter
    def overload_count(self, overload_count):
        r"""Sets the overload_count of this ListFactoryAlarmRulesResponse.

        资源繁忙作业数量。

        :param overload_count: The overload_count of this ListFactoryAlarmRulesResponse.
        :type overload_count: int
        """
        self._overload_count = overload_count

    @property
    def recover_jobs_count(self):
        r"""Gets the recover_jobs_count of this ListFactoryAlarmRulesResponse.

        失败作业恢复数量。

        :return: The recover_jobs_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._recover_jobs_count

    @recover_jobs_count.setter
    def recover_jobs_count(self, recover_jobs_count):
        r"""Sets the recover_jobs_count of this ListFactoryAlarmRulesResponse.

        失败作业恢复数量。

        :param recover_jobs_count: The recover_jobs_count of this ListFactoryAlarmRulesResponse.
        :type recover_jobs_count: int
        """
        self._recover_jobs_count = recover_jobs_count

    @property
    def success_count(self):
        r"""Gets the success_count of this ListFactoryAlarmRulesResponse.

        作业成功数量。

        :return: The success_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ListFactoryAlarmRulesResponse.

        作业成功数量。

        :param success_count: The success_count of this ListFactoryAlarmRulesResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def total(self):
        r"""Gets the total of this ListFactoryAlarmRulesResponse.

        作业总数量。

        :return: The total of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFactoryAlarmRulesResponse.

        作业总数量。

        :param total: The total of this ListFactoryAlarmRulesResponse.
        :type total: int
        """
        self._total = total

    @property
    def total_all(self):
        r"""Gets the total_all of this ListFactoryAlarmRulesResponse.

        通知规则数量。

        :return: The total_all of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._total_all

    @total_all.setter
    def total_all(self, total_all):
        r"""Sets the total_all of this ListFactoryAlarmRulesResponse.

        通知规则数量。

        :param total_all: The total_all of this ListFactoryAlarmRulesResponse.
        :type total_all: int
        """
        self._total_all = total_all

    @property
    def unfinished_count(self):
        r"""Gets the unfinished_count of this ListFactoryAlarmRulesResponse.

        未完成作业数量。

        :return: The unfinished_count of this ListFactoryAlarmRulesResponse.
        :rtype: int
        """
        return self._unfinished_count

    @unfinished_count.setter
    def unfinished_count(self, unfinished_count):
        r"""Sets the unfinished_count of this ListFactoryAlarmRulesResponse.

        未完成作业数量。

        :param unfinished_count: The unfinished_count of this ListFactoryAlarmRulesResponse.
        :type unfinished_count: int
        """
        self._unfinished_count = unfinished_count

    def to_dict(self):
        import warnings
        warnings.warn("ListFactoryAlarmRulesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListFactoryAlarmRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
