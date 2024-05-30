# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DerivativeIndexVO:

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
        'name_en': 'str',
        'name_ch': 'str',
        'description': 'str',
        'create_by': 'str',
        'data_type': 'str',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'status': 'BizStatusEnum',
        'atomic_index_id': 'str',
        'time_condition_id': 'str',
        'time_field_id': 'str',
        'time_field_name': 'str',
        'common_conditions': 'list[CommonConditionVO]',
        'dimension_groups': 'list[DerivativeIndexDimensionVO]',
        'monitor': 'MetricMonitorVO',
        'atomic_index': 'AtomicIndexVO',
        'time_condition_name': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'summary_table_id': 'str',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO'
    }

    attribute_map = {
        'id': 'id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'create_by': 'create_by',
        'data_type': 'data_type',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'status': 'status',
        'atomic_index_id': 'atomic_index_id',
        'time_condition_id': 'time_condition_id',
        'time_field_id': 'time_field_id',
        'time_field_name': 'time_field_name',
        'common_conditions': 'common_conditions',
        'dimension_groups': 'dimension_groups',
        'monitor': 'monitor',
        'atomic_index': 'atomic_index',
        'time_condition_name': 'time_condition_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'summary_table_id': 'summary_table_id',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz'
    }

    def __init__(self, id=None, name_en=None, name_ch=None, description=None, create_by=None, data_type=None, l1_id=None, l2_id=None, l3_id=None, status=None, atomic_index_id=None, time_condition_id=None, time_field_id=None, time_field_name=None, common_conditions=None, dimension_groups=None, monitor=None, atomic_index=None, time_condition_name=None, create_time=None, update_time=None, l1=None, l2=None, l3=None, summary_table_id=None, approval_info=None, new_biz=None):
        """DerivativeIndexVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param name_en: 字段名。
        :type name_en: str
        :param name_ch: 中文名。
        :type name_ch: str
        :param description: 描述，只读。
        :type description: str
        :param create_by: 创建人。
        :type create_by: str
        :param data_type: 字段类型。
        :type data_type: str
        :param l1_id: 主题域分组ID，只读，填写String类型替代Long类型。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象guid，填写String类型替代Long类型。
        :type l3_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param atomic_index_id: 原子指标ID，填写String类型替代Long类型。
        :type atomic_index_id: str
        :param time_condition_id: 时间限定ID，填写String类型替代Long类型。
        :type time_condition_id: str
        :param time_field_id: 时间限定关联字段ID，填写String类型替代Long类型。
        :type time_field_id: str
        :param time_field_name: 时间限定关联字段名称，只读。
        :type time_field_name: str
        :param common_conditions: 通用限定信息。
        :type common_conditions: list[:class:`huaweicloudsdkdataartsstudio.v1.CommonConditionVO`]
        :param dimension_groups: 维度组(颗粒度)。
        :type dimension_groups: list[:class:`huaweicloudsdkdataartsstudio.v1.DerivativeIndexDimensionVO`]
        :param monitor: 
        :type monitor: :class:`huaweicloudsdkdataartsstudio.v1.MetricMonitorVO`
        :param atomic_index: 
        :type atomic_index: :class:`huaweicloudsdkdataartsstudio.v1.AtomicIndexVO`
        :param time_condition_name: 时间限定名称，只读。
        :type time_condition_name: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param l1: 主题域分组中文名，只读，创建和更新时无需填写。
        :type l1: str
        :param l2: 主题域中文名，只读，创建和更新时无需填写。
        :type l2: str
        :param l3: 业务对象中文名，只读，创建和更新时无需填写。
        :type l3: str
        :param summary_table_id: 汇总表ID，只读，填写String类型替代Long类型。
        :type summary_table_id: str
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        
        

        self._id = None
        self._name_en = None
        self._name_ch = None
        self._description = None
        self._create_by = None
        self._data_type = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._status = None
        self._atomic_index_id = None
        self._time_condition_id = None
        self._time_field_id = None
        self._time_field_name = None
        self._common_conditions = None
        self._dimension_groups = None
        self._monitor = None
        self._atomic_index = None
        self._time_condition_name = None
        self._create_time = None
        self._update_time = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._summary_table_id = None
        self._approval_info = None
        self._new_biz = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_en = name_en
        self.name_ch = name_ch
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        if data_type is not None:
            self.data_type = data_type
        if l1_id is not None:
            self.l1_id = l1_id
        if l2_id is not None:
            self.l2_id = l2_id
        self.l3_id = l3_id
        if status is not None:
            self.status = status
        self.atomic_index_id = atomic_index_id
        if time_condition_id is not None:
            self.time_condition_id = time_condition_id
        if time_field_id is not None:
            self.time_field_id = time_field_id
        if time_field_name is not None:
            self.time_field_name = time_field_name
        if common_conditions is not None:
            self.common_conditions = common_conditions
        if dimension_groups is not None:
            self.dimension_groups = dimension_groups
        if monitor is not None:
            self.monitor = monitor
        if atomic_index is not None:
            self.atomic_index = atomic_index
        if time_condition_name is not None:
            self.time_condition_name = time_condition_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        if summary_table_id is not None:
            self.summary_table_id = summary_table_id
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz

    @property
    def id(self):
        """Gets the id of this DerivativeIndexVO.

        编码，填写String类型替代Long类型。

        :return: The id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DerivativeIndexVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this DerivativeIndexVO.
        :type id: str
        """
        self._id = id

    @property
    def name_en(self):
        """Gets the name_en of this DerivativeIndexVO.

        字段名。

        :return: The name_en of this DerivativeIndexVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this DerivativeIndexVO.

        字段名。

        :param name_en: The name_en of this DerivativeIndexVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this DerivativeIndexVO.

        中文名。

        :return: The name_ch of this DerivativeIndexVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this DerivativeIndexVO.

        中文名。

        :param name_ch: The name_ch of this DerivativeIndexVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        """Gets the description of this DerivativeIndexVO.

        描述，只读。

        :return: The description of this DerivativeIndexVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DerivativeIndexVO.

        描述，只读。

        :param description: The description of this DerivativeIndexVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        """Gets the create_by of this DerivativeIndexVO.

        创建人。

        :return: The create_by of this DerivativeIndexVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this DerivativeIndexVO.

        创建人。

        :param create_by: The create_by of this DerivativeIndexVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def data_type(self):
        """Gets the data_type of this DerivativeIndexVO.

        字段类型。

        :return: The data_type of this DerivativeIndexVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DerivativeIndexVO.

        字段类型。

        :param data_type: The data_type of this DerivativeIndexVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def l1_id(self):
        """Gets the l1_id of this DerivativeIndexVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :return: The l1_id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        """Sets the l1_id of this DerivativeIndexVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :param l1_id: The l1_id of this DerivativeIndexVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        """Gets the l2_id of this DerivativeIndexVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this DerivativeIndexVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this DerivativeIndexVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        """Gets the l3_id of this DerivativeIndexVO.

        业务对象guid，填写String类型替代Long类型。

        :return: The l3_id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this DerivativeIndexVO.

        业务对象guid，填写String类型替代Long类型。

        :param l3_id: The l3_id of this DerivativeIndexVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def status(self):
        """Gets the status of this DerivativeIndexVO.

        :return: The status of this DerivativeIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DerivativeIndexVO.

        :param status: The status of this DerivativeIndexVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def atomic_index_id(self):
        """Gets the atomic_index_id of this DerivativeIndexVO.

        原子指标ID，填写String类型替代Long类型。

        :return: The atomic_index_id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._atomic_index_id

    @atomic_index_id.setter
    def atomic_index_id(self, atomic_index_id):
        """Sets the atomic_index_id of this DerivativeIndexVO.

        原子指标ID，填写String类型替代Long类型。

        :param atomic_index_id: The atomic_index_id of this DerivativeIndexVO.
        :type atomic_index_id: str
        """
        self._atomic_index_id = atomic_index_id

    @property
    def time_condition_id(self):
        """Gets the time_condition_id of this DerivativeIndexVO.

        时间限定ID，填写String类型替代Long类型。

        :return: The time_condition_id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._time_condition_id

    @time_condition_id.setter
    def time_condition_id(self, time_condition_id):
        """Sets the time_condition_id of this DerivativeIndexVO.

        时间限定ID，填写String类型替代Long类型。

        :param time_condition_id: The time_condition_id of this DerivativeIndexVO.
        :type time_condition_id: str
        """
        self._time_condition_id = time_condition_id

    @property
    def time_field_id(self):
        """Gets the time_field_id of this DerivativeIndexVO.

        时间限定关联字段ID，填写String类型替代Long类型。

        :return: The time_field_id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._time_field_id

    @time_field_id.setter
    def time_field_id(self, time_field_id):
        """Sets the time_field_id of this DerivativeIndexVO.

        时间限定关联字段ID，填写String类型替代Long类型。

        :param time_field_id: The time_field_id of this DerivativeIndexVO.
        :type time_field_id: str
        """
        self._time_field_id = time_field_id

    @property
    def time_field_name(self):
        """Gets the time_field_name of this DerivativeIndexVO.

        时间限定关联字段名称，只读。

        :return: The time_field_name of this DerivativeIndexVO.
        :rtype: str
        """
        return self._time_field_name

    @time_field_name.setter
    def time_field_name(self, time_field_name):
        """Sets the time_field_name of this DerivativeIndexVO.

        时间限定关联字段名称，只读。

        :param time_field_name: The time_field_name of this DerivativeIndexVO.
        :type time_field_name: str
        """
        self._time_field_name = time_field_name

    @property
    def common_conditions(self):
        """Gets the common_conditions of this DerivativeIndexVO.

        通用限定信息。

        :return: The common_conditions of this DerivativeIndexVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CommonConditionVO`]
        """
        return self._common_conditions

    @common_conditions.setter
    def common_conditions(self, common_conditions):
        """Sets the common_conditions of this DerivativeIndexVO.

        通用限定信息。

        :param common_conditions: The common_conditions of this DerivativeIndexVO.
        :type common_conditions: list[:class:`huaweicloudsdkdataartsstudio.v1.CommonConditionVO`]
        """
        self._common_conditions = common_conditions

    @property
    def dimension_groups(self):
        """Gets the dimension_groups of this DerivativeIndexVO.

        维度组(颗粒度)。

        :return: The dimension_groups of this DerivativeIndexVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DerivativeIndexDimensionVO`]
        """
        return self._dimension_groups

    @dimension_groups.setter
    def dimension_groups(self, dimension_groups):
        """Sets the dimension_groups of this DerivativeIndexVO.

        维度组(颗粒度)。

        :param dimension_groups: The dimension_groups of this DerivativeIndexVO.
        :type dimension_groups: list[:class:`huaweicloudsdkdataartsstudio.v1.DerivativeIndexDimensionVO`]
        """
        self._dimension_groups = dimension_groups

    @property
    def monitor(self):
        """Gets the monitor of this DerivativeIndexVO.

        :return: The monitor of this DerivativeIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.MetricMonitorVO`
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        """Sets the monitor of this DerivativeIndexVO.

        :param monitor: The monitor of this DerivativeIndexVO.
        :type monitor: :class:`huaweicloudsdkdataartsstudio.v1.MetricMonitorVO`
        """
        self._monitor = monitor

    @property
    def atomic_index(self):
        """Gets the atomic_index of this DerivativeIndexVO.

        :return: The atomic_index of this DerivativeIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AtomicIndexVO`
        """
        return self._atomic_index

    @atomic_index.setter
    def atomic_index(self, atomic_index):
        """Sets the atomic_index of this DerivativeIndexVO.

        :param atomic_index: The atomic_index of this DerivativeIndexVO.
        :type atomic_index: :class:`huaweicloudsdkdataartsstudio.v1.AtomicIndexVO`
        """
        self._atomic_index = atomic_index

    @property
    def time_condition_name(self):
        """Gets the time_condition_name of this DerivativeIndexVO.

        时间限定名称，只读。

        :return: The time_condition_name of this DerivativeIndexVO.
        :rtype: str
        """
        return self._time_condition_name

    @time_condition_name.setter
    def time_condition_name(self, time_condition_name):
        """Sets the time_condition_name of this DerivativeIndexVO.

        时间限定名称，只读。

        :param time_condition_name: The time_condition_name of this DerivativeIndexVO.
        :type time_condition_name: str
        """
        self._time_condition_name = time_condition_name

    @property
    def create_time(self):
        """Gets the create_time of this DerivativeIndexVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this DerivativeIndexVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DerivativeIndexVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this DerivativeIndexVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DerivativeIndexVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this DerivativeIndexVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DerivativeIndexVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this DerivativeIndexVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def l1(self):
        """Gets the l1 of this DerivativeIndexVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this DerivativeIndexVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this DerivativeIndexVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this DerivativeIndexVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this DerivativeIndexVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this DerivativeIndexVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this DerivativeIndexVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this DerivativeIndexVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this DerivativeIndexVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this DerivativeIndexVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this DerivativeIndexVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this DerivativeIndexVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def summary_table_id(self):
        """Gets the summary_table_id of this DerivativeIndexVO.

        汇总表ID，只读，填写String类型替代Long类型。

        :return: The summary_table_id of this DerivativeIndexVO.
        :rtype: str
        """
        return self._summary_table_id

    @summary_table_id.setter
    def summary_table_id(self, summary_table_id):
        """Sets the summary_table_id of this DerivativeIndexVO.

        汇总表ID，只读，填写String类型替代Long类型。

        :param summary_table_id: The summary_table_id of this DerivativeIndexVO.
        :type summary_table_id: str
        """
        self._summary_table_id = summary_table_id

    @property
    def approval_info(self):
        """Gets the approval_info of this DerivativeIndexVO.

        :return: The approval_info of this DerivativeIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        """Sets the approval_info of this DerivativeIndexVO.

        :param approval_info: The approval_info of this DerivativeIndexVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        """Gets the new_biz of this DerivativeIndexVO.

        :return: The new_biz of this DerivativeIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this DerivativeIndexVO.

        :param new_biz: The new_biz of this DerivativeIndexVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

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
        if not isinstance(other, DerivativeIndexVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
