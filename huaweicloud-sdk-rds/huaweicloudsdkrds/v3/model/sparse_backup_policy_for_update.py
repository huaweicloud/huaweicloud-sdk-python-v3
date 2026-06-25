# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparseBackupPolicyForUpdate:

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
        'period': 'str',
        'keep_days': 'int',
        'reserve_backups': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'period': 'period',
        'keep_days': 'keep_days',
        'reserve_backups': 'reserve_backups'
    }

    def __init__(self, id=None, period=None, keep_days=None, reserve_backups=None):
        r"""SparseBackupPolicyForUpdate

        The model defined in huaweicloud sdk

        :param id: 参数解释：  备份策略ID。  约束限制：  备份策略可能关联多个已生成的备份集，修改、删除策略会对该策略所关联的已生成的备份集生效。如果修改某策略的备份保留天数小于原保留天数或删除某策略，可能会导致关联该条策略的现有全量备份过期删除，请检查策略后再次确认。  取值范围：  不填写ID时，表示新增一条备份策略。 填写当前存在的备份策略ID时，表示修改或删除该条备份策略的内容，ID获取方法请参见查询稀疏备份策略接口。 如您要删除该备份策略，请填写其keep_days为0，period为null，同时必须填写reserve_backups来说明是否保留已生成的与该条备份策略关联的自动备份。 如您要修改该备份策略，至少需要填写period、keep_days其中之一。  默认取值：  不涉及。
        :type id: str
        :param period: 参数解释：  备份周期配置。  约束限制：  该字段为UTC时区的Cron表达式，和备份时间段start_time共同作用。实例基础备份策略的start_time获取方法请参见查询自动备份策略接口，稀疏备份策略的start_time与基础备份策略一致。 比如当地时区为UTC+08:00，接口查询到的start_time为21:00-22:00时，对应的备份时间是当地时间05:00-06:00。当您设置稀疏备份策略的period为1 * *，意为该条策略将在UTC时区的每月1号21:00-22:00执行任务，也即您所在的UTC+08:00时区的每月2号05:00-06:00执行任务。 新增策略时，此字段必填。  取值范围：  格式必须为“日期 月份 星期”形式的Cron表达式，时区为UTC时区，且需要符合周策略、月策略或者年策略的形式，规则如下： · 周策略 日期需填写*，月份需填写*。星期支持填写1~7（1表示星期一，2表示星期二，依次类推），支持填写多个数字，需以逗号隔开。 取值示例： \\* \\* 6 表示每周六执行任务。 \\* \\* 1,2,3 表示每周一、二、三执行任务。 · 月策略 月份需填写*，星期需填写*。日期支持填写1~28和特殊字符L（表示最后一天），支持填写多个数字，需以逗号隔开。 取值示例： 1,2 * * 表示每月1号、2号执行任务。 L * * 表示每月的最后一天执行任务。 · 年策略 星期需填写*。日期支持填写1~31，月份支持填写1~12，日期和月份的组合需要为有效的日期。 取值示例： 15 3 * 表示每年的3月15日执行任务。  默认取值：  不涉及。
        :type period: str
        :param keep_days: 参数解释：  备份文件可以保存的天数。  约束限制：  新增策略时，此字段必填。  取值范围：  0～3660。取0值时，表示删除该条备份策略。  默认取值：  不涉及。
        :type keep_days: int
        :param reserve_backups: 参数解释：  删除备份策略时是否保留备份集。  约束限制：  仅在keep_days填写0时生效，删除备份策略时，此字段必填。 备份策略可能关联多个已生成的备份集，如果设置本字段为false，所有关联此策略的备份数据都会被立即清理，请谨慎操作。  取值范围：  true：表示保留该条备份策略关联的自动备份。 false：表示删除该条备份策略的同时，立即删除该条策略关联的自动备份。  默认取值：  不涉及。
        :type reserve_backups: bool
        """
        
        

        self._id = None
        self._period = None
        self._keep_days = None
        self._reserve_backups = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if period is not None:
            self.period = period
        if keep_days is not None:
            self.keep_days = keep_days
        if reserve_backups is not None:
            self.reserve_backups = reserve_backups

    @property
    def id(self):
        r"""Gets the id of this SparseBackupPolicyForUpdate.

        参数解释：  备份策略ID。  约束限制：  备份策略可能关联多个已生成的备份集，修改、删除策略会对该策略所关联的已生成的备份集生效。如果修改某策略的备份保留天数小于原保留天数或删除某策略，可能会导致关联该条策略的现有全量备份过期删除，请检查策略后再次确认。  取值范围：  不填写ID时，表示新增一条备份策略。 填写当前存在的备份策略ID时，表示修改或删除该条备份策略的内容，ID获取方法请参见查询稀疏备份策略接口。 如您要删除该备份策略，请填写其keep_days为0，period为null，同时必须填写reserve_backups来说明是否保留已生成的与该条备份策略关联的自动备份。 如您要修改该备份策略，至少需要填写period、keep_days其中之一。  默认取值：  不涉及。

        :return: The id of this SparseBackupPolicyForUpdate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SparseBackupPolicyForUpdate.

        参数解释：  备份策略ID。  约束限制：  备份策略可能关联多个已生成的备份集，修改、删除策略会对该策略所关联的已生成的备份集生效。如果修改某策略的备份保留天数小于原保留天数或删除某策略，可能会导致关联该条策略的现有全量备份过期删除，请检查策略后再次确认。  取值范围：  不填写ID时，表示新增一条备份策略。 填写当前存在的备份策略ID时，表示修改或删除该条备份策略的内容，ID获取方法请参见查询稀疏备份策略接口。 如您要删除该备份策略，请填写其keep_days为0，period为null，同时必须填写reserve_backups来说明是否保留已生成的与该条备份策略关联的自动备份。 如您要修改该备份策略，至少需要填写period、keep_days其中之一。  默认取值：  不涉及。

        :param id: The id of this SparseBackupPolicyForUpdate.
        :type id: str
        """
        self._id = id

    @property
    def period(self):
        r"""Gets the period of this SparseBackupPolicyForUpdate.

        参数解释：  备份周期配置。  约束限制：  该字段为UTC时区的Cron表达式，和备份时间段start_time共同作用。实例基础备份策略的start_time获取方法请参见查询自动备份策略接口，稀疏备份策略的start_time与基础备份策略一致。 比如当地时区为UTC+08:00，接口查询到的start_time为21:00-22:00时，对应的备份时间是当地时间05:00-06:00。当您设置稀疏备份策略的period为1 * *，意为该条策略将在UTC时区的每月1号21:00-22:00执行任务，也即您所在的UTC+08:00时区的每月2号05:00-06:00执行任务。 新增策略时，此字段必填。  取值范围：  格式必须为“日期 月份 星期”形式的Cron表达式，时区为UTC时区，且需要符合周策略、月策略或者年策略的形式，规则如下： · 周策略 日期需填写*，月份需填写*。星期支持填写1~7（1表示星期一，2表示星期二，依次类推），支持填写多个数字，需以逗号隔开。 取值示例： \\* \\* 6 表示每周六执行任务。 \\* \\* 1,2,3 表示每周一、二、三执行任务。 · 月策略 月份需填写*，星期需填写*。日期支持填写1~28和特殊字符L（表示最后一天），支持填写多个数字，需以逗号隔开。 取值示例： 1,2 * * 表示每月1号、2号执行任务。 L * * 表示每月的最后一天执行任务。 · 年策略 星期需填写*。日期支持填写1~31，月份支持填写1~12，日期和月份的组合需要为有效的日期。 取值示例： 15 3 * 表示每年的3月15日执行任务。  默认取值：  不涉及。

        :return: The period of this SparseBackupPolicyForUpdate.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this SparseBackupPolicyForUpdate.

        参数解释：  备份周期配置。  约束限制：  该字段为UTC时区的Cron表达式，和备份时间段start_time共同作用。实例基础备份策略的start_time获取方法请参见查询自动备份策略接口，稀疏备份策略的start_time与基础备份策略一致。 比如当地时区为UTC+08:00，接口查询到的start_time为21:00-22:00时，对应的备份时间是当地时间05:00-06:00。当您设置稀疏备份策略的period为1 * *，意为该条策略将在UTC时区的每月1号21:00-22:00执行任务，也即您所在的UTC+08:00时区的每月2号05:00-06:00执行任务。 新增策略时，此字段必填。  取值范围：  格式必须为“日期 月份 星期”形式的Cron表达式，时区为UTC时区，且需要符合周策略、月策略或者年策略的形式，规则如下： · 周策略 日期需填写*，月份需填写*。星期支持填写1~7（1表示星期一，2表示星期二，依次类推），支持填写多个数字，需以逗号隔开。 取值示例： \\* \\* 6 表示每周六执行任务。 \\* \\* 1,2,3 表示每周一、二、三执行任务。 · 月策略 月份需填写*，星期需填写*。日期支持填写1~28和特殊字符L（表示最后一天），支持填写多个数字，需以逗号隔开。 取值示例： 1,2 * * 表示每月1号、2号执行任务。 L * * 表示每月的最后一天执行任务。 · 年策略 星期需填写*。日期支持填写1~31，月份支持填写1~12，日期和月份的组合需要为有效的日期。 取值示例： 15 3 * 表示每年的3月15日执行任务。  默认取值：  不涉及。

        :param period: The period of this SparseBackupPolicyForUpdate.
        :type period: str
        """
        self._period = period

    @property
    def keep_days(self):
        r"""Gets the keep_days of this SparseBackupPolicyForUpdate.

        参数解释：  备份文件可以保存的天数。  约束限制：  新增策略时，此字段必填。  取值范围：  0～3660。取0值时，表示删除该条备份策略。  默认取值：  不涉及。

        :return: The keep_days of this SparseBackupPolicyForUpdate.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this SparseBackupPolicyForUpdate.

        参数解释：  备份文件可以保存的天数。  约束限制：  新增策略时，此字段必填。  取值范围：  0～3660。取0值时，表示删除该条备份策略。  默认取值：  不涉及。

        :param keep_days: The keep_days of this SparseBackupPolicyForUpdate.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def reserve_backups(self):
        r"""Gets the reserve_backups of this SparseBackupPolicyForUpdate.

        参数解释：  删除备份策略时是否保留备份集。  约束限制：  仅在keep_days填写0时生效，删除备份策略时，此字段必填。 备份策略可能关联多个已生成的备份集，如果设置本字段为false，所有关联此策略的备份数据都会被立即清理，请谨慎操作。  取值范围：  true：表示保留该条备份策略关联的自动备份。 false：表示删除该条备份策略的同时，立即删除该条策略关联的自动备份。  默认取值：  不涉及。

        :return: The reserve_backups of this SparseBackupPolicyForUpdate.
        :rtype: bool
        """
        return self._reserve_backups

    @reserve_backups.setter
    def reserve_backups(self, reserve_backups):
        r"""Sets the reserve_backups of this SparseBackupPolicyForUpdate.

        参数解释：  删除备份策略时是否保留备份集。  约束限制：  仅在keep_days填写0时生效，删除备份策略时，此字段必填。 备份策略可能关联多个已生成的备份集，如果设置本字段为false，所有关联此策略的备份数据都会被立即清理，请谨慎操作。  取值范围：  true：表示保留该条备份策略关联的自动备份。 false：表示删除该条备份策略的同时，立即删除该条策略关联的自动备份。  默认取值：  不涉及。

        :param reserve_backups: The reserve_backups of this SparseBackupPolicyForUpdate.
        :type reserve_backups: bool
        """
        self._reserve_backups = reserve_backups

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
        if not isinstance(other, SparseBackupPolicyForUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
