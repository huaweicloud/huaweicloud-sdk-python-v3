# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlSwitchResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_open': 'bool',
        'begin_time': 'str',
        'end_time': 'str',
        'save_days': 'int',
        'storage_mode': 'str',
        'lts_config': 'LtsConfigInfoResult',
        'sql_type_range': 'list[SqlTypeInfoResult]',
        'is_exclude_sys_user': 'bool'
    }

    attribute_map = {
        'is_open': 'is_open',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'save_days': 'save_days',
        'storage_mode': 'storage_mode',
        'lts_config': 'lts_config',
        'sql_type_range': 'sql_type_range',
        'is_exclude_sys_user': 'is_exclude_sys_user'
    }

    def __init__(self, is_open=None, begin_time=None, end_time=None, save_days=None, storage_mode=None, lts_config=None, sql_type_range=None, is_exclude_sys_user=None):
        r"""FullSqlSwitchResult

        The model defined in huaweicloud sdk

        :param is_open: **参数解释**: 是否开启全量SQL。 **取值范围**: - true：已开启。 - false：已关闭。
        :type is_open: bool
        :param begin_time: **参数解释**: 开关状态持续的开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 不涉及。
        :type begin_time: str
        :param end_time: **参数解释**: 开关状态持续的结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 为null则表示，开关状态还在持续，没有发生切换。
        :type end_time: str
        :param save_days: **参数解释**: 已采集的全量SQL数据的最大保留天数。 **取值范围**: [1,30]
        :type save_days: int
        :param storage_mode: **参数解释**: 全量SQL数据存储类型。 **取值范围**: - LTS：LTS云日志服务。
        :type storage_mode: str
        :param lts_config: 
        :type lts_config: :class:`huaweicloudsdkgaussdbforopengauss.v3.LtsConfigInfoResult`
        :param sql_type_range: **参数解释**: SQL采集类型列表。 **取值范围**: 不涉及。
        :type sql_type_range: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeInfoResult`]
        :param is_exclude_sys_user: **参数解释**: 实例ID。 **取值范围**: 不涉及。是否过滤系统用户。使能该选项后，全量SQL采集将会跳过系统用户所执行的SQL记录
        :type is_exclude_sys_user: bool
        """
        
        

        self._is_open = None
        self._begin_time = None
        self._end_time = None
        self._save_days = None
        self._storage_mode = None
        self._lts_config = None
        self._sql_type_range = None
        self._is_exclude_sys_user = None
        self.discriminator = None

        if is_open is not None:
            self.is_open = is_open
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if save_days is not None:
            self.save_days = save_days
        if storage_mode is not None:
            self.storage_mode = storage_mode
        if lts_config is not None:
            self.lts_config = lts_config
        if sql_type_range is not None:
            self.sql_type_range = sql_type_range
        if is_exclude_sys_user is not None:
            self.is_exclude_sys_user = is_exclude_sys_user

    @property
    def is_open(self):
        r"""Gets the is_open of this FullSqlSwitchResult.

        **参数解释**: 是否开启全量SQL。 **取值范围**: - true：已开启。 - false：已关闭。

        :return: The is_open of this FullSqlSwitchResult.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        r"""Sets the is_open of this FullSqlSwitchResult.

        **参数解释**: 是否开启全量SQL。 **取值范围**: - true：已开启。 - false：已关闭。

        :param is_open: The is_open of this FullSqlSwitchResult.
        :type is_open: bool
        """
        self._is_open = is_open

    @property
    def begin_time(self):
        r"""Gets the begin_time of this FullSqlSwitchResult.

        **参数解释**: 开关状态持续的开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 不涉及。

        :return: The begin_time of this FullSqlSwitchResult.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this FullSqlSwitchResult.

        **参数解释**: 开关状态持续的开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 不涉及。

        :param begin_time: The begin_time of this FullSqlSwitchResult.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this FullSqlSwitchResult.

        **参数解释**: 开关状态持续的结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 为null则表示，开关状态还在持续，没有发生切换。

        :return: The end_time of this FullSqlSwitchResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FullSqlSwitchResult.

        **参数解释**: 开关状态持续的结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 为null则表示，开关状态还在持续，没有发生切换。

        :param end_time: The end_time of this FullSqlSwitchResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def save_days(self):
        r"""Gets the save_days of this FullSqlSwitchResult.

        **参数解释**: 已采集的全量SQL数据的最大保留天数。 **取值范围**: [1,30]

        :return: The save_days of this FullSqlSwitchResult.
        :rtype: int
        """
        return self._save_days

    @save_days.setter
    def save_days(self, save_days):
        r"""Sets the save_days of this FullSqlSwitchResult.

        **参数解释**: 已采集的全量SQL数据的最大保留天数。 **取值范围**: [1,30]

        :param save_days: The save_days of this FullSqlSwitchResult.
        :type save_days: int
        """
        self._save_days = save_days

    @property
    def storage_mode(self):
        r"""Gets the storage_mode of this FullSqlSwitchResult.

        **参数解释**: 全量SQL数据存储类型。 **取值范围**: - LTS：LTS云日志服务。

        :return: The storage_mode of this FullSqlSwitchResult.
        :rtype: str
        """
        return self._storage_mode

    @storage_mode.setter
    def storage_mode(self, storage_mode):
        r"""Sets the storage_mode of this FullSqlSwitchResult.

        **参数解释**: 全量SQL数据存储类型。 **取值范围**: - LTS：LTS云日志服务。

        :param storage_mode: The storage_mode of this FullSqlSwitchResult.
        :type storage_mode: str
        """
        self._storage_mode = storage_mode

    @property
    def lts_config(self):
        r"""Gets the lts_config of this FullSqlSwitchResult.

        :return: The lts_config of this FullSqlSwitchResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.LtsConfigInfoResult`
        """
        return self._lts_config

    @lts_config.setter
    def lts_config(self, lts_config):
        r"""Sets the lts_config of this FullSqlSwitchResult.

        :param lts_config: The lts_config of this FullSqlSwitchResult.
        :type lts_config: :class:`huaweicloudsdkgaussdbforopengauss.v3.LtsConfigInfoResult`
        """
        self._lts_config = lts_config

    @property
    def sql_type_range(self):
        r"""Gets the sql_type_range of this FullSqlSwitchResult.

        **参数解释**: SQL采集类型列表。 **取值范围**: 不涉及。

        :return: The sql_type_range of this FullSqlSwitchResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeInfoResult`]
        """
        return self._sql_type_range

    @sql_type_range.setter
    def sql_type_range(self, sql_type_range):
        r"""Sets the sql_type_range of this FullSqlSwitchResult.

        **参数解释**: SQL采集类型列表。 **取值范围**: 不涉及。

        :param sql_type_range: The sql_type_range of this FullSqlSwitchResult.
        :type sql_type_range: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeInfoResult`]
        """
        self._sql_type_range = sql_type_range

    @property
    def is_exclude_sys_user(self):
        r"""Gets the is_exclude_sys_user of this FullSqlSwitchResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。是否过滤系统用户。使能该选项后，全量SQL采集将会跳过系统用户所执行的SQL记录

        :return: The is_exclude_sys_user of this FullSqlSwitchResult.
        :rtype: bool
        """
        return self._is_exclude_sys_user

    @is_exclude_sys_user.setter
    def is_exclude_sys_user(self, is_exclude_sys_user):
        r"""Sets the is_exclude_sys_user of this FullSqlSwitchResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。是否过滤系统用户。使能该选项后，全量SQL采集将会跳过系统用户所执行的SQL记录

        :param is_exclude_sys_user: The is_exclude_sys_user of this FullSqlSwitchResult.
        :type is_exclude_sys_user: bool
        """
        self._is_exclude_sys_user = is_exclude_sys_user

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
        if not isinstance(other, FullSqlSwitchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
