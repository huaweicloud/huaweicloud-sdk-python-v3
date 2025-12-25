# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapJobModeSettingDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_overtime_interval': 'int',
        'batch_overtime_unit': 'str',
        'batch_frequency_interval': 'int',
        'batch_frequency_unit': 'str',
        'streaming_state_ttl_interval': 'int',
        'streaming_state_ttl_unit': 'str',
        'streaming_checkpoint_ttl_interval': 'int',
        'streaming_checkpoint_ttl_unit': 'str',
        'streaming_startup_mode': 'str',
        'batch_overtime_strategy_interval': 'int',
        'batch_overtime_strategy_unit': 'str',
        'search_delay_interval': 'int',
        'search_delay_unit': 'str',
        'search_frequency_interval': 'int',
        'search_frequency_unit': 'str',
        'search_overtime_interval': 'int',
        'search_overtime_unit': 'str',
        'search_period_interval': 'int',
        'search_period_unit': 'str',
        'search_table_id': 'str',
        'search_table_name': 'str',
        'field_not_null_policy': 'str',
        'dss_id': 'int'
    }

    attribute_map = {
        'batch_overtime_interval': 'batch_overtime_interval',
        'batch_overtime_unit': 'batch_overtime_unit',
        'batch_frequency_interval': 'batch_frequency_interval',
        'batch_frequency_unit': 'batch_frequency_unit',
        'streaming_state_ttl_interval': 'streaming_state_ttl_interval',
        'streaming_state_ttl_unit': 'streaming_state_ttl_unit',
        'streaming_checkpoint_ttl_interval': 'streaming_checkpoint_ttl_interval',
        'streaming_checkpoint_ttl_unit': 'streaming_checkpoint_ttl_unit',
        'streaming_startup_mode': 'streaming_startup_mode',
        'batch_overtime_strategy_interval': 'batch_overtime_strategy_interval',
        'batch_overtime_strategy_unit': 'batch_overtime_strategy_unit',
        'search_delay_interval': 'search_delay_interval',
        'search_delay_unit': 'search_delay_unit',
        'search_frequency_interval': 'search_frequency_interval',
        'search_frequency_unit': 'search_frequency_unit',
        'search_overtime_interval': 'search_overtime_interval',
        'search_overtime_unit': 'search_overtime_unit',
        'search_period_interval': 'search_period_interval',
        'search_period_unit': 'search_period_unit',
        'search_table_id': 'search_table_id',
        'search_table_name': 'search_table_name',
        'field_not_null_policy': 'field_not_null_policy',
        'dss_id': 'dss_id'
    }

    def __init__(self, batch_overtime_interval=None, batch_overtime_unit=None, batch_frequency_interval=None, batch_frequency_unit=None, streaming_state_ttl_interval=None, streaming_state_ttl_unit=None, streaming_checkpoint_ttl_interval=None, streaming_checkpoint_ttl_unit=None, streaming_startup_mode=None, batch_overtime_strategy_interval=None, batch_overtime_strategy_unit=None, search_delay_interval=None, search_delay_unit=None, search_frequency_interval=None, search_frequency_unit=None, search_overtime_interval=None, search_overtime_unit=None, search_period_interval=None, search_period_unit=None, search_table_id=None, search_table_name=None, field_not_null_policy=None, dss_id=None):
        r"""IsapJobModeSettingDto

        The model defined in huaweicloud sdk

        :param batch_overtime_interval: 整型间隔时长
        :type batch_overtime_interval: int
        :param batch_overtime_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type batch_overtime_unit: str
        :param batch_frequency_interval: 整型间隔时长
        :type batch_frequency_interval: int
        :param batch_frequency_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type batch_frequency_unit: str
        :param streaming_state_ttl_interval: 整型间隔时长
        :type streaming_state_ttl_interval: int
        :param streaming_state_ttl_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type streaming_state_ttl_unit: str
        :param streaming_checkpoint_ttl_interval: 整型间隔时长
        :type streaming_checkpoint_ttl_interval: int
        :param streaming_checkpoint_ttl_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type streaming_checkpoint_ttl_unit: str
        :param streaming_startup_mode: **参数解释**: 作业启动模式 - UPGRADE 升级启动 - REFRESH_NEW 全新启动  **约束限制** 不涉及 **取值范围**: - UPGRADE - REFRESH_NEW  **默认值** 不涉及      
        :type streaming_startup_mode: str
        :param batch_overtime_strategy_interval: 整型间隔时长
        :type batch_overtime_strategy_interval: int
        :param batch_overtime_strategy_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type batch_overtime_strategy_unit: str
        :param search_delay_interval: 整型间隔时长
        :type search_delay_interval: int
        :param search_delay_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type search_delay_unit: str
        :param search_frequency_interval: 整型间隔时长
        :type search_frequency_interval: int
        :param search_frequency_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type search_frequency_unit: str
        :param search_overtime_interval: 整型间隔时长
        :type search_overtime_interval: int
        :param search_overtime_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type search_overtime_unit: str
        :param search_period_interval: 整型间隔时长
        :type search_period_interval: int
        :param search_period_unit: **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        
        :type search_period_unit: str
        :param search_table_id: UUID
        :type search_table_id: str
        :param search_table_name: 表名称
        :type search_table_name: str
        :param field_not_null_policy: 参数解释: 作业表非空字段处理策略  LOOSE 宽松 STRICT 严格 约束限制 不涉及 取值范围:  LOOSE STRICT 默认值 LOOSE
        :type field_not_null_policy: str
        :param dss_id: 长整型间隔时长
        :type dss_id: int
        """
        
        

        self._batch_overtime_interval = None
        self._batch_overtime_unit = None
        self._batch_frequency_interval = None
        self._batch_frequency_unit = None
        self._streaming_state_ttl_interval = None
        self._streaming_state_ttl_unit = None
        self._streaming_checkpoint_ttl_interval = None
        self._streaming_checkpoint_ttl_unit = None
        self._streaming_startup_mode = None
        self._batch_overtime_strategy_interval = None
        self._batch_overtime_strategy_unit = None
        self._search_delay_interval = None
        self._search_delay_unit = None
        self._search_frequency_interval = None
        self._search_frequency_unit = None
        self._search_overtime_interval = None
        self._search_overtime_unit = None
        self._search_period_interval = None
        self._search_period_unit = None
        self._search_table_id = None
        self._search_table_name = None
        self._field_not_null_policy = None
        self._dss_id = None
        self.discriminator = None

        if batch_overtime_interval is not None:
            self.batch_overtime_interval = batch_overtime_interval
        if batch_overtime_unit is not None:
            self.batch_overtime_unit = batch_overtime_unit
        if batch_frequency_interval is not None:
            self.batch_frequency_interval = batch_frequency_interval
        if batch_frequency_unit is not None:
            self.batch_frequency_unit = batch_frequency_unit
        if streaming_state_ttl_interval is not None:
            self.streaming_state_ttl_interval = streaming_state_ttl_interval
        if streaming_state_ttl_unit is not None:
            self.streaming_state_ttl_unit = streaming_state_ttl_unit
        if streaming_checkpoint_ttl_interval is not None:
            self.streaming_checkpoint_ttl_interval = streaming_checkpoint_ttl_interval
        if streaming_checkpoint_ttl_unit is not None:
            self.streaming_checkpoint_ttl_unit = streaming_checkpoint_ttl_unit
        if streaming_startup_mode is not None:
            self.streaming_startup_mode = streaming_startup_mode
        if batch_overtime_strategy_interval is not None:
            self.batch_overtime_strategy_interval = batch_overtime_strategy_interval
        if batch_overtime_strategy_unit is not None:
            self.batch_overtime_strategy_unit = batch_overtime_strategy_unit
        if search_delay_interval is not None:
            self.search_delay_interval = search_delay_interval
        if search_delay_unit is not None:
            self.search_delay_unit = search_delay_unit
        if search_frequency_interval is not None:
            self.search_frequency_interval = search_frequency_interval
        if search_frequency_unit is not None:
            self.search_frequency_unit = search_frequency_unit
        if search_overtime_interval is not None:
            self.search_overtime_interval = search_overtime_interval
        if search_overtime_unit is not None:
            self.search_overtime_unit = search_overtime_unit
        if search_period_interval is not None:
            self.search_period_interval = search_period_interval
        if search_period_unit is not None:
            self.search_period_unit = search_period_unit
        if search_table_id is not None:
            self.search_table_id = search_table_id
        if search_table_name is not None:
            self.search_table_name = search_table_name
        if field_not_null_policy is not None:
            self.field_not_null_policy = field_not_null_policy
        if dss_id is not None:
            self.dss_id = dss_id

    @property
    def batch_overtime_interval(self):
        r"""Gets the batch_overtime_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The batch_overtime_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._batch_overtime_interval

    @batch_overtime_interval.setter
    def batch_overtime_interval(self, batch_overtime_interval):
        r"""Sets the batch_overtime_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param batch_overtime_interval: The batch_overtime_interval of this IsapJobModeSettingDto.
        :type batch_overtime_interval: int
        """
        self._batch_overtime_interval = batch_overtime_interval

    @property
    def batch_overtime_unit(self):
        r"""Gets the batch_overtime_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The batch_overtime_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._batch_overtime_unit

    @batch_overtime_unit.setter
    def batch_overtime_unit(self, batch_overtime_unit):
        r"""Sets the batch_overtime_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param batch_overtime_unit: The batch_overtime_unit of this IsapJobModeSettingDto.
        :type batch_overtime_unit: str
        """
        self._batch_overtime_unit = batch_overtime_unit

    @property
    def batch_frequency_interval(self):
        r"""Gets the batch_frequency_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The batch_frequency_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._batch_frequency_interval

    @batch_frequency_interval.setter
    def batch_frequency_interval(self, batch_frequency_interval):
        r"""Sets the batch_frequency_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param batch_frequency_interval: The batch_frequency_interval of this IsapJobModeSettingDto.
        :type batch_frequency_interval: int
        """
        self._batch_frequency_interval = batch_frequency_interval

    @property
    def batch_frequency_unit(self):
        r"""Gets the batch_frequency_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The batch_frequency_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._batch_frequency_unit

    @batch_frequency_unit.setter
    def batch_frequency_unit(self, batch_frequency_unit):
        r"""Sets the batch_frequency_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param batch_frequency_unit: The batch_frequency_unit of this IsapJobModeSettingDto.
        :type batch_frequency_unit: str
        """
        self._batch_frequency_unit = batch_frequency_unit

    @property
    def streaming_state_ttl_interval(self):
        r"""Gets the streaming_state_ttl_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The streaming_state_ttl_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._streaming_state_ttl_interval

    @streaming_state_ttl_interval.setter
    def streaming_state_ttl_interval(self, streaming_state_ttl_interval):
        r"""Sets the streaming_state_ttl_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param streaming_state_ttl_interval: The streaming_state_ttl_interval of this IsapJobModeSettingDto.
        :type streaming_state_ttl_interval: int
        """
        self._streaming_state_ttl_interval = streaming_state_ttl_interval

    @property
    def streaming_state_ttl_unit(self):
        r"""Gets the streaming_state_ttl_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The streaming_state_ttl_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._streaming_state_ttl_unit

    @streaming_state_ttl_unit.setter
    def streaming_state_ttl_unit(self, streaming_state_ttl_unit):
        r"""Sets the streaming_state_ttl_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param streaming_state_ttl_unit: The streaming_state_ttl_unit of this IsapJobModeSettingDto.
        :type streaming_state_ttl_unit: str
        """
        self._streaming_state_ttl_unit = streaming_state_ttl_unit

    @property
    def streaming_checkpoint_ttl_interval(self):
        r"""Gets the streaming_checkpoint_ttl_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The streaming_checkpoint_ttl_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._streaming_checkpoint_ttl_interval

    @streaming_checkpoint_ttl_interval.setter
    def streaming_checkpoint_ttl_interval(self, streaming_checkpoint_ttl_interval):
        r"""Sets the streaming_checkpoint_ttl_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param streaming_checkpoint_ttl_interval: The streaming_checkpoint_ttl_interval of this IsapJobModeSettingDto.
        :type streaming_checkpoint_ttl_interval: int
        """
        self._streaming_checkpoint_ttl_interval = streaming_checkpoint_ttl_interval

    @property
    def streaming_checkpoint_ttl_unit(self):
        r"""Gets the streaming_checkpoint_ttl_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The streaming_checkpoint_ttl_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._streaming_checkpoint_ttl_unit

    @streaming_checkpoint_ttl_unit.setter
    def streaming_checkpoint_ttl_unit(self, streaming_checkpoint_ttl_unit):
        r"""Sets the streaming_checkpoint_ttl_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param streaming_checkpoint_ttl_unit: The streaming_checkpoint_ttl_unit of this IsapJobModeSettingDto.
        :type streaming_checkpoint_ttl_unit: str
        """
        self._streaming_checkpoint_ttl_unit = streaming_checkpoint_ttl_unit

    @property
    def streaming_startup_mode(self):
        r"""Gets the streaming_startup_mode of this IsapJobModeSettingDto.

        **参数解释**: 作业启动模式 - UPGRADE 升级启动 - REFRESH_NEW 全新启动  **约束限制** 不涉及 **取值范围**: - UPGRADE - REFRESH_NEW  **默认值** 不涉及      

        :return: The streaming_startup_mode of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._streaming_startup_mode

    @streaming_startup_mode.setter
    def streaming_startup_mode(self, streaming_startup_mode):
        r"""Sets the streaming_startup_mode of this IsapJobModeSettingDto.

        **参数解释**: 作业启动模式 - UPGRADE 升级启动 - REFRESH_NEW 全新启动  **约束限制** 不涉及 **取值范围**: - UPGRADE - REFRESH_NEW  **默认值** 不涉及      

        :param streaming_startup_mode: The streaming_startup_mode of this IsapJobModeSettingDto.
        :type streaming_startup_mode: str
        """
        self._streaming_startup_mode = streaming_startup_mode

    @property
    def batch_overtime_strategy_interval(self):
        r"""Gets the batch_overtime_strategy_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The batch_overtime_strategy_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._batch_overtime_strategy_interval

    @batch_overtime_strategy_interval.setter
    def batch_overtime_strategy_interval(self, batch_overtime_strategy_interval):
        r"""Sets the batch_overtime_strategy_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param batch_overtime_strategy_interval: The batch_overtime_strategy_interval of this IsapJobModeSettingDto.
        :type batch_overtime_strategy_interval: int
        """
        self._batch_overtime_strategy_interval = batch_overtime_strategy_interval

    @property
    def batch_overtime_strategy_unit(self):
        r"""Gets the batch_overtime_strategy_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The batch_overtime_strategy_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._batch_overtime_strategy_unit

    @batch_overtime_strategy_unit.setter
    def batch_overtime_strategy_unit(self, batch_overtime_strategy_unit):
        r"""Sets the batch_overtime_strategy_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param batch_overtime_strategy_unit: The batch_overtime_strategy_unit of this IsapJobModeSettingDto.
        :type batch_overtime_strategy_unit: str
        """
        self._batch_overtime_strategy_unit = batch_overtime_strategy_unit

    @property
    def search_delay_interval(self):
        r"""Gets the search_delay_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The search_delay_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._search_delay_interval

    @search_delay_interval.setter
    def search_delay_interval(self, search_delay_interval):
        r"""Sets the search_delay_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param search_delay_interval: The search_delay_interval of this IsapJobModeSettingDto.
        :type search_delay_interval: int
        """
        self._search_delay_interval = search_delay_interval

    @property
    def search_delay_unit(self):
        r"""Gets the search_delay_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The search_delay_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._search_delay_unit

    @search_delay_unit.setter
    def search_delay_unit(self, search_delay_unit):
        r"""Sets the search_delay_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param search_delay_unit: The search_delay_unit of this IsapJobModeSettingDto.
        :type search_delay_unit: str
        """
        self._search_delay_unit = search_delay_unit

    @property
    def search_frequency_interval(self):
        r"""Gets the search_frequency_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The search_frequency_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._search_frequency_interval

    @search_frequency_interval.setter
    def search_frequency_interval(self, search_frequency_interval):
        r"""Sets the search_frequency_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param search_frequency_interval: The search_frequency_interval of this IsapJobModeSettingDto.
        :type search_frequency_interval: int
        """
        self._search_frequency_interval = search_frequency_interval

    @property
    def search_frequency_unit(self):
        r"""Gets the search_frequency_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The search_frequency_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._search_frequency_unit

    @search_frequency_unit.setter
    def search_frequency_unit(self, search_frequency_unit):
        r"""Sets the search_frequency_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param search_frequency_unit: The search_frequency_unit of this IsapJobModeSettingDto.
        :type search_frequency_unit: str
        """
        self._search_frequency_unit = search_frequency_unit

    @property
    def search_overtime_interval(self):
        r"""Gets the search_overtime_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The search_overtime_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._search_overtime_interval

    @search_overtime_interval.setter
    def search_overtime_interval(self, search_overtime_interval):
        r"""Sets the search_overtime_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param search_overtime_interval: The search_overtime_interval of this IsapJobModeSettingDto.
        :type search_overtime_interval: int
        """
        self._search_overtime_interval = search_overtime_interval

    @property
    def search_overtime_unit(self):
        r"""Gets the search_overtime_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The search_overtime_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._search_overtime_unit

    @search_overtime_unit.setter
    def search_overtime_unit(self, search_overtime_unit):
        r"""Sets the search_overtime_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param search_overtime_unit: The search_overtime_unit of this IsapJobModeSettingDto.
        :type search_overtime_unit: str
        """
        self._search_overtime_unit = search_overtime_unit

    @property
    def search_period_interval(self):
        r"""Gets the search_period_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :return: The search_period_interval of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._search_period_interval

    @search_period_interval.setter
    def search_period_interval(self, search_period_interval):
        r"""Sets the search_period_interval of this IsapJobModeSettingDto.

        整型间隔时长

        :param search_period_interval: The search_period_interval of this IsapJobModeSettingDto.
        :type search_period_interval: int
        """
        self._search_period_interval = search_period_interval

    @property
    def search_period_unit(self):
        r"""Gets the search_period_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :return: The search_period_unit of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._search_period_unit

    @search_period_unit.setter
    def search_period_unit(self, search_period_unit):
        r"""Sets the search_period_unit of this IsapJobModeSettingDto.

        **参数解释**: 时间单位 - MINUTE 分钟 - HOUR 小时 - DAY 天 - MONTH 月  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY - MONTH  **默认值** 不涉及        

        :param search_period_unit: The search_period_unit of this IsapJobModeSettingDto.
        :type search_period_unit: str
        """
        self._search_period_unit = search_period_unit

    @property
    def search_table_id(self):
        r"""Gets the search_table_id of this IsapJobModeSettingDto.

        UUID

        :return: The search_table_id of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._search_table_id

    @search_table_id.setter
    def search_table_id(self, search_table_id):
        r"""Sets the search_table_id of this IsapJobModeSettingDto.

        UUID

        :param search_table_id: The search_table_id of this IsapJobModeSettingDto.
        :type search_table_id: str
        """
        self._search_table_id = search_table_id

    @property
    def search_table_name(self):
        r"""Gets the search_table_name of this IsapJobModeSettingDto.

        表名称

        :return: The search_table_name of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._search_table_name

    @search_table_name.setter
    def search_table_name(self, search_table_name):
        r"""Sets the search_table_name of this IsapJobModeSettingDto.

        表名称

        :param search_table_name: The search_table_name of this IsapJobModeSettingDto.
        :type search_table_name: str
        """
        self._search_table_name = search_table_name

    @property
    def field_not_null_policy(self):
        r"""Gets the field_not_null_policy of this IsapJobModeSettingDto.

        参数解释: 作业表非空字段处理策略  LOOSE 宽松 STRICT 严格 约束限制 不涉及 取值范围:  LOOSE STRICT 默认值 LOOSE

        :return: The field_not_null_policy of this IsapJobModeSettingDto.
        :rtype: str
        """
        return self._field_not_null_policy

    @field_not_null_policy.setter
    def field_not_null_policy(self, field_not_null_policy):
        r"""Sets the field_not_null_policy of this IsapJobModeSettingDto.

        参数解释: 作业表非空字段处理策略  LOOSE 宽松 STRICT 严格 约束限制 不涉及 取值范围:  LOOSE STRICT 默认值 LOOSE

        :param field_not_null_policy: The field_not_null_policy of this IsapJobModeSettingDto.
        :type field_not_null_policy: str
        """
        self._field_not_null_policy = field_not_null_policy

    @property
    def dss_id(self):
        r"""Gets the dss_id of this IsapJobModeSettingDto.

        长整型间隔时长

        :return: The dss_id of this IsapJobModeSettingDto.
        :rtype: int
        """
        return self._dss_id

    @dss_id.setter
    def dss_id(self, dss_id):
        r"""Sets the dss_id of this IsapJobModeSettingDto.

        长整型间隔时长

        :param dss_id: The dss_id of this IsapJobModeSettingDto.
        :type dss_id: int
        """
        self._dss_id = dss_id

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
        if not isinstance(other, IsapJobModeSettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
