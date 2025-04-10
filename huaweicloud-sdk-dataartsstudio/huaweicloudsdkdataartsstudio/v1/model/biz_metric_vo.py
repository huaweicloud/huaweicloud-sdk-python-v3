# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizMetricVO:

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
        'code': 'str',
        'name_alias': 'str',
        'biz_type': 'BizTypeEnum',
        'status': 'BizStatusEnum',
        'biz_catalog_id': 'str',
        'biz_catalog_path': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'data_origin': 'str',
        'unit': 'str',
        'time_filters': 'str',
        'dimensions': 'str',
        'general_filters': 'str',
        'interval_type': 'str',
        'apply_scenario': 'str',
        'technical_metric': 'str',
        'technical_metric_name': 'str',
        'technical_metric_type': 'BizTypeEnum',
        'measure': 'str',
        'owner': 'str',
        'owner_department': 'str',
        'destination': 'str',
        'guid': 'str',
        'definition': 'str',
        'expression': 'str',
        'remark': 'str',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'biz_metric': 'SyncStatusEnum',
        'summary_status': 'SyncStatusEnum',
        'self_defined_fields': 'list[SelfDefinedFieldVO]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'name_alias': 'name_alias',
        'biz_type': 'biz_type',
        'status': 'status',
        'biz_catalog_id': 'biz_catalog_id',
        'biz_catalog_path': 'biz_catalog_path',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'data_origin': 'data_origin',
        'unit': 'unit',
        'time_filters': 'time_filters',
        'dimensions': 'dimensions',
        'general_filters': 'general_filters',
        'interval_type': 'interval_type',
        'apply_scenario': 'apply_scenario',
        'technical_metric': 'technical_metric',
        'technical_metric_name': 'technical_metric_name',
        'technical_metric_type': 'technical_metric_type',
        'measure': 'measure',
        'owner': 'owner',
        'owner_department': 'owner_department',
        'destination': 'destination',
        'guid': 'guid',
        'definition': 'definition',
        'expression': 'expression',
        'remark': 'remark',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'biz_metric': 'biz_metric',
        'summary_status': 'summary_status',
        'self_defined_fields': 'self_defined_fields'
    }

    def __init__(self, id=None, name=None, code=None, name_alias=None, biz_type=None, status=None, biz_catalog_id=None, biz_catalog_path=None, create_by=None, update_by=None, data_origin=None, unit=None, time_filters=None, dimensions=None, general_filters=None, interval_type=None, apply_scenario=None, technical_metric=None, technical_metric_name=None, technical_metric_type=None, measure=None, owner=None, owner_department=None, destination=None, guid=None, definition=None, expression=None, remark=None, approval_info=None, new_biz=None, create_time=None, update_time=None, l1=None, l2=None, l3=None, biz_metric=None, summary_status=None, self_defined_fields=None):
        r"""BizMetricVO

        The model defined in huaweicloud sdk

        :param id: 编码，更新时必填，创建时为空，ID字符串。
        :type id: str
        :param name: 指标名称。
        :type name: str
        :param code: 指标编码，只读。
        :type code: str
        :param name_alias: 指标别名。
        :type name_alias: str
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param biz_catalog_id: 归属的流程架构的ID，ID字符串。
        :type biz_catalog_id: str
        :param biz_catalog_path: 归属的流程架构路径，只读。
        :type biz_catalog_path: str
        :param create_by: 创建人，只读。
        :type create_by: str
        :param update_by: 更新人，只读。
        :type update_by: str
        :param data_origin: 数据来源。
        :type data_origin: str
        :param unit: 计量单位。
        :type unit: str
        :param time_filters: 统计周期(时间限定)。
        :type time_filters: str
        :param dimensions: 统计维度。
        :type dimensions: str
        :param general_filters: 统计口径和修饰词。
        :type general_filters: str
        :param interval_type: 刷新频率。 枚举值：   - MINUTE: 每分钟   - HOUR: 每小时   - DAY: 每天   - WEEK: 每周   - MONTH: 每月   - YEAR: 每年   - REAL_TIME: 实时   - HALF_HOUR: 每半小时   - QUART: 每15分钟   - DOUBLE_WEEK: 每两周   - HALF_YEAR: 每半年   - HALF_DAY: 每半天 
        :type interval_type: str
        :param apply_scenario: 应用场景。
        :type apply_scenario: str
        :param technical_metric: 关联技术指标，ID字符串。
        :type technical_metric: str
        :param technical_metric_name: 关联技术指标名称，只读。
        :type technical_metric_name: str
        :param technical_metric_type: 
        :type technical_metric_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param measure: 度量对象。
        :type measure: str
        :param owner: 指标责任人。
        :type owner: str
        :param owner_department: 指标管理部门。
        :type owner_department: str
        :param destination: 设置目的。
        :type destination: str
        :param guid: 资产同步后的guid，只读。
        :type guid: str
        :param definition: 指标定义。
        :type definition: str
        :param expression: 计算公式。
        :type expression: str
        :param remark: 备注。
        :type remark: str
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
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
        :param biz_metric: 
        :type biz_metric: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param summary_status: 
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param self_defined_fields: 自定义项
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._name_alias = None
        self._biz_type = None
        self._status = None
        self._biz_catalog_id = None
        self._biz_catalog_path = None
        self._create_by = None
        self._update_by = None
        self._data_origin = None
        self._unit = None
        self._time_filters = None
        self._dimensions = None
        self._general_filters = None
        self._interval_type = None
        self._apply_scenario = None
        self._technical_metric = None
        self._technical_metric_name = None
        self._technical_metric_type = None
        self._measure = None
        self._owner = None
        self._owner_department = None
        self._destination = None
        self._guid = None
        self._definition = None
        self._expression = None
        self._remark = None
        self._approval_info = None
        self._new_biz = None
        self._create_time = None
        self._update_time = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._biz_metric = None
        self._summary_status = None
        self._self_defined_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if code is not None:
            self.code = code
        if name_alias is not None:
            self.name_alias = name_alias
        if biz_type is not None:
            self.biz_type = biz_type
        if status is not None:
            self.status = status
        self.biz_catalog_id = biz_catalog_id
        if biz_catalog_path is not None:
            self.biz_catalog_path = biz_catalog_path
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if data_origin is not None:
            self.data_origin = data_origin
        if unit is not None:
            self.unit = unit
        self.time_filters = time_filters
        if dimensions is not None:
            self.dimensions = dimensions
        if general_filters is not None:
            self.general_filters = general_filters
        self.interval_type = interval_type
        if apply_scenario is not None:
            self.apply_scenario = apply_scenario
        if technical_metric is not None:
            self.technical_metric = technical_metric
        if technical_metric_name is not None:
            self.technical_metric_name = technical_metric_name
        if technical_metric_type is not None:
            self.technical_metric_type = technical_metric_type
        if measure is not None:
            self.measure = measure
        self.owner = owner
        self.owner_department = owner_department
        self.destination = destination
        if guid is not None:
            self.guid = guid
        self.definition = definition
        self.expression = expression
        if remark is not None:
            self.remark = remark
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz
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
        if biz_metric is not None:
            self.biz_metric = biz_metric
        if summary_status is not None:
            self.summary_status = summary_status
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields

    @property
    def id(self):
        r"""Gets the id of this BizMetricVO.

        编码，更新时必填，创建时为空，ID字符串。

        :return: The id of this BizMetricVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BizMetricVO.

        编码，更新时必填，创建时为空，ID字符串。

        :param id: The id of this BizMetricVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BizMetricVO.

        指标名称。

        :return: The name of this BizMetricVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BizMetricVO.

        指标名称。

        :param name: The name of this BizMetricVO.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this BizMetricVO.

        指标编码，只读。

        :return: The code of this BizMetricVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BizMetricVO.

        指标编码，只读。

        :param code: The code of this BizMetricVO.
        :type code: str
        """
        self._code = code

    @property
    def name_alias(self):
        r"""Gets the name_alias of this BizMetricVO.

        指标别名。

        :return: The name_alias of this BizMetricVO.
        :rtype: str
        """
        return self._name_alias

    @name_alias.setter
    def name_alias(self, name_alias):
        r"""Sets the name_alias of this BizMetricVO.

        指标别名。

        :param name_alias: The name_alias of this BizMetricVO.
        :type name_alias: str
        """
        self._name_alias = name_alias

    @property
    def biz_type(self):
        r"""Gets the biz_type of this BizMetricVO.

        :return: The biz_type of this BizMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this BizMetricVO.

        :param biz_type: The biz_type of this BizMetricVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def status(self):
        r"""Gets the status of this BizMetricVO.

        :return: The status of this BizMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BizMetricVO.

        :param status: The status of this BizMetricVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def biz_catalog_id(self):
        r"""Gets the biz_catalog_id of this BizMetricVO.

        归属的流程架构的ID，ID字符串。

        :return: The biz_catalog_id of this BizMetricVO.
        :rtype: str
        """
        return self._biz_catalog_id

    @biz_catalog_id.setter
    def biz_catalog_id(self, biz_catalog_id):
        r"""Sets the biz_catalog_id of this BizMetricVO.

        归属的流程架构的ID，ID字符串。

        :param biz_catalog_id: The biz_catalog_id of this BizMetricVO.
        :type biz_catalog_id: str
        """
        self._biz_catalog_id = biz_catalog_id

    @property
    def biz_catalog_path(self):
        r"""Gets the biz_catalog_path of this BizMetricVO.

        归属的流程架构路径，只读。

        :return: The biz_catalog_path of this BizMetricVO.
        :rtype: str
        """
        return self._biz_catalog_path

    @biz_catalog_path.setter
    def biz_catalog_path(self, biz_catalog_path):
        r"""Sets the biz_catalog_path of this BizMetricVO.

        归属的流程架构路径，只读。

        :param biz_catalog_path: The biz_catalog_path of this BizMetricVO.
        :type biz_catalog_path: str
        """
        self._biz_catalog_path = biz_catalog_path

    @property
    def create_by(self):
        r"""Gets the create_by of this BizMetricVO.

        创建人，只读。

        :return: The create_by of this BizMetricVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this BizMetricVO.

        创建人，只读。

        :param create_by: The create_by of this BizMetricVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this BizMetricVO.

        更新人，只读。

        :return: The update_by of this BizMetricVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this BizMetricVO.

        更新人，只读。

        :param update_by: The update_by of this BizMetricVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def data_origin(self):
        r"""Gets the data_origin of this BizMetricVO.

        数据来源。

        :return: The data_origin of this BizMetricVO.
        :rtype: str
        """
        return self._data_origin

    @data_origin.setter
    def data_origin(self, data_origin):
        r"""Sets the data_origin of this BizMetricVO.

        数据来源。

        :param data_origin: The data_origin of this BizMetricVO.
        :type data_origin: str
        """
        self._data_origin = data_origin

    @property
    def unit(self):
        r"""Gets the unit of this BizMetricVO.

        计量单位。

        :return: The unit of this BizMetricVO.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this BizMetricVO.

        计量单位。

        :param unit: The unit of this BizMetricVO.
        :type unit: str
        """
        self._unit = unit

    @property
    def time_filters(self):
        r"""Gets the time_filters of this BizMetricVO.

        统计周期(时间限定)。

        :return: The time_filters of this BizMetricVO.
        :rtype: str
        """
        return self._time_filters

    @time_filters.setter
    def time_filters(self, time_filters):
        r"""Sets the time_filters of this BizMetricVO.

        统计周期(时间限定)。

        :param time_filters: The time_filters of this BizMetricVO.
        :type time_filters: str
        """
        self._time_filters = time_filters

    @property
    def dimensions(self):
        r"""Gets the dimensions of this BizMetricVO.

        统计维度。

        :return: The dimensions of this BizMetricVO.
        :rtype: str
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this BizMetricVO.

        统计维度。

        :param dimensions: The dimensions of this BizMetricVO.
        :type dimensions: str
        """
        self._dimensions = dimensions

    @property
    def general_filters(self):
        r"""Gets the general_filters of this BizMetricVO.

        统计口径和修饰词。

        :return: The general_filters of this BizMetricVO.
        :rtype: str
        """
        return self._general_filters

    @general_filters.setter
    def general_filters(self, general_filters):
        r"""Sets the general_filters of this BizMetricVO.

        统计口径和修饰词。

        :param general_filters: The general_filters of this BizMetricVO.
        :type general_filters: str
        """
        self._general_filters = general_filters

    @property
    def interval_type(self):
        r"""Gets the interval_type of this BizMetricVO.

        刷新频率。 枚举值：   - MINUTE: 每分钟   - HOUR: 每小时   - DAY: 每天   - WEEK: 每周   - MONTH: 每月   - YEAR: 每年   - REAL_TIME: 实时   - HALF_HOUR: 每半小时   - QUART: 每15分钟   - DOUBLE_WEEK: 每两周   - HALF_YEAR: 每半年   - HALF_DAY: 每半天 

        :return: The interval_type of this BizMetricVO.
        :rtype: str
        """
        return self._interval_type

    @interval_type.setter
    def interval_type(self, interval_type):
        r"""Sets the interval_type of this BizMetricVO.

        刷新频率。 枚举值：   - MINUTE: 每分钟   - HOUR: 每小时   - DAY: 每天   - WEEK: 每周   - MONTH: 每月   - YEAR: 每年   - REAL_TIME: 实时   - HALF_HOUR: 每半小时   - QUART: 每15分钟   - DOUBLE_WEEK: 每两周   - HALF_YEAR: 每半年   - HALF_DAY: 每半天 

        :param interval_type: The interval_type of this BizMetricVO.
        :type interval_type: str
        """
        self._interval_type = interval_type

    @property
    def apply_scenario(self):
        r"""Gets the apply_scenario of this BizMetricVO.

        应用场景。

        :return: The apply_scenario of this BizMetricVO.
        :rtype: str
        """
        return self._apply_scenario

    @apply_scenario.setter
    def apply_scenario(self, apply_scenario):
        r"""Sets the apply_scenario of this BizMetricVO.

        应用场景。

        :param apply_scenario: The apply_scenario of this BizMetricVO.
        :type apply_scenario: str
        """
        self._apply_scenario = apply_scenario

    @property
    def technical_metric(self):
        r"""Gets the technical_metric of this BizMetricVO.

        关联技术指标，ID字符串。

        :return: The technical_metric of this BizMetricVO.
        :rtype: str
        """
        return self._technical_metric

    @technical_metric.setter
    def technical_metric(self, technical_metric):
        r"""Sets the technical_metric of this BizMetricVO.

        关联技术指标，ID字符串。

        :param technical_metric: The technical_metric of this BizMetricVO.
        :type technical_metric: str
        """
        self._technical_metric = technical_metric

    @property
    def technical_metric_name(self):
        r"""Gets the technical_metric_name of this BizMetricVO.

        关联技术指标名称，只读。

        :return: The technical_metric_name of this BizMetricVO.
        :rtype: str
        """
        return self._technical_metric_name

    @technical_metric_name.setter
    def technical_metric_name(self, technical_metric_name):
        r"""Sets the technical_metric_name of this BizMetricVO.

        关联技术指标名称，只读。

        :param technical_metric_name: The technical_metric_name of this BizMetricVO.
        :type technical_metric_name: str
        """
        self._technical_metric_name = technical_metric_name

    @property
    def technical_metric_type(self):
        r"""Gets the technical_metric_type of this BizMetricVO.

        :return: The technical_metric_type of this BizMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._technical_metric_type

    @technical_metric_type.setter
    def technical_metric_type(self, technical_metric_type):
        r"""Sets the technical_metric_type of this BizMetricVO.

        :param technical_metric_type: The technical_metric_type of this BizMetricVO.
        :type technical_metric_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._technical_metric_type = technical_metric_type

    @property
    def measure(self):
        r"""Gets the measure of this BizMetricVO.

        度量对象。

        :return: The measure of this BizMetricVO.
        :rtype: str
        """
        return self._measure

    @measure.setter
    def measure(self, measure):
        r"""Sets the measure of this BizMetricVO.

        度量对象。

        :param measure: The measure of this BizMetricVO.
        :type measure: str
        """
        self._measure = measure

    @property
    def owner(self):
        r"""Gets the owner of this BizMetricVO.

        指标责任人。

        :return: The owner of this BizMetricVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this BizMetricVO.

        指标责任人。

        :param owner: The owner of this BizMetricVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_department(self):
        r"""Gets the owner_department of this BizMetricVO.

        指标管理部门。

        :return: The owner_department of this BizMetricVO.
        :rtype: str
        """
        return self._owner_department

    @owner_department.setter
    def owner_department(self, owner_department):
        r"""Sets the owner_department of this BizMetricVO.

        指标管理部门。

        :param owner_department: The owner_department of this BizMetricVO.
        :type owner_department: str
        """
        self._owner_department = owner_department

    @property
    def destination(self):
        r"""Gets the destination of this BizMetricVO.

        设置目的。

        :return: The destination of this BizMetricVO.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this BizMetricVO.

        设置目的。

        :param destination: The destination of this BizMetricVO.
        :type destination: str
        """
        self._destination = destination

    @property
    def guid(self):
        r"""Gets the guid of this BizMetricVO.

        资产同步后的guid，只读。

        :return: The guid of this BizMetricVO.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this BizMetricVO.

        资产同步后的guid，只读。

        :param guid: The guid of this BizMetricVO.
        :type guid: str
        """
        self._guid = guid

    @property
    def definition(self):
        r"""Gets the definition of this BizMetricVO.

        指标定义。

        :return: The definition of this BizMetricVO.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        r"""Sets the definition of this BizMetricVO.

        指标定义。

        :param definition: The definition of this BizMetricVO.
        :type definition: str
        """
        self._definition = definition

    @property
    def expression(self):
        r"""Gets the expression of this BizMetricVO.

        计算公式。

        :return: The expression of this BizMetricVO.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this BizMetricVO.

        计算公式。

        :param expression: The expression of this BizMetricVO.
        :type expression: str
        """
        self._expression = expression

    @property
    def remark(self):
        r"""Gets the remark of this BizMetricVO.

        备注。

        :return: The remark of this BizMetricVO.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this BizMetricVO.

        备注。

        :param remark: The remark of this BizMetricVO.
        :type remark: str
        """
        self._remark = remark

    @property
    def approval_info(self):
        r"""Gets the approval_info of this BizMetricVO.

        :return: The approval_info of this BizMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        r"""Sets the approval_info of this BizMetricVO.

        :param approval_info: The approval_info of this BizMetricVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        r"""Gets the new_biz of this BizMetricVO.

        :return: The new_biz of this BizMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        r"""Sets the new_biz of this BizMetricVO.

        :param new_biz: The new_biz of this BizMetricVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def create_time(self):
        r"""Gets the create_time of this BizMetricVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this BizMetricVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BizMetricVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this BizMetricVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this BizMetricVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this BizMetricVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this BizMetricVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this BizMetricVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def l1(self):
        r"""Gets the l1 of this BizMetricVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this BizMetricVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        r"""Sets the l1 of this BizMetricVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this BizMetricVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        r"""Gets the l2 of this BizMetricVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this BizMetricVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        r"""Sets the l2 of this BizMetricVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this BizMetricVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        r"""Gets the l3 of this BizMetricVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this BizMetricVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        r"""Sets the l3 of this BizMetricVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this BizMetricVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def biz_metric(self):
        r"""Gets the biz_metric of this BizMetricVO.

        :return: The biz_metric of this BizMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._biz_metric

    @biz_metric.setter
    def biz_metric(self, biz_metric):
        r"""Sets the biz_metric of this BizMetricVO.

        :param biz_metric: The biz_metric of this BizMetricVO.
        :type biz_metric: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._biz_metric = biz_metric

    @property
    def summary_status(self):
        r"""Gets the summary_status of this BizMetricVO.

        :return: The summary_status of this BizMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._summary_status

    @summary_status.setter
    def summary_status(self, summary_status):
        r"""Sets the summary_status of this BizMetricVO.

        :param summary_status: The summary_status of this BizMetricVO.
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._summary_status = summary_status

    @property
    def self_defined_fields(self):
        r"""Gets the self_defined_fields of this BizMetricVO.

        自定义项

        :return: The self_defined_fields of this BizMetricVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        r"""Sets the self_defined_fields of this BizMetricVO.

        自定义项

        :param self_defined_fields: The self_defined_fields of this BizMetricVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

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
        if not isinstance(other, BizMetricVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
