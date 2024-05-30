# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompoundMetricVO:

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
        'dimension_group': 'str',
        'group_name': 'str',
        'group_code': 'str',
        'compound_type': 'str',
        'comparison_type': 'str',
        'metric_ids': 'list[str]',
        'metric_names': 'list[str]',
        'compound_metric_ids': 'list[str]',
        'compound_metric_names': 'list[str]',
        'cal_fn_ids': 'list[str]',
        'cal_exp': 'str',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'data_type': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'status': 'BizStatusEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'monitor': 'MetricMonitorVO',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'summary_table_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'dimension_group': 'dimension_group',
        'group_name': 'group_name',
        'group_code': 'group_code',
        'compound_type': 'compound_type',
        'comparison_type': 'comparison_type',
        'metric_ids': 'metric_ids',
        'metric_names': 'metric_names',
        'compound_metric_ids': 'compound_metric_ids',
        'compound_metric_names': 'compound_metric_names',
        'cal_fn_ids': 'cal_fn_ids',
        'cal_exp': 'cal_exp',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'data_type': 'data_type',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'monitor': 'monitor',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'summary_table_id': 'summary_table_id'
    }

    def __init__(self, id=None, name_en=None, name_ch=None, description=None, dimension_group=None, group_name=None, group_code=None, compound_type=None, comparison_type=None, metric_ids=None, metric_names=None, compound_metric_ids=None, compound_metric_names=None, cal_fn_ids=None, cal_exp=None, l1_id=None, l2_id=None, l3_id=None, data_type=None, create_by=None, update_by=None, status=None, create_time=None, update_time=None, approval_info=None, new_biz=None, monitor=None, l1=None, l2=None, l3=None, summary_table_id=None):
        """CompoundMetricVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param name_en: 字段名。
        :type name_en: str
        :param name_ch: 业务属性。
        :type name_ch: str
        :param description: 描述
        :type description: str
        :param dimension_group: 颗粒度ID。
        :type dimension_group: str
        :param group_name: 颗粒度名称，只读。
        :type group_name: str
        :param group_code: 颗粒度编码，只读。
        :type group_code: str
        :param compound_type: 复合指标类型。 枚举值：   - EXPRESSION: 表达式   - PERIODICITY_VALUED_COMPARISON: 环比   - INTERVAL_VALUED_COMPARISON: 同比 
        :type compound_type: str
        :param comparison_type: 比较类型。 枚举值：   - YEAR_TO_YEAR: 年同比   - MONTH_TO_MONTH: 月同比   - WEEK_TO_WEEK: 周同比 
        :type comparison_type: str
        :param metric_ids: 指标信息，填写String类型替代Long类型。
        :type metric_ids: list[str]
        :param metric_names: 指标名称信息。
        :type metric_names: list[str]
        :param compound_metric_ids: 复合指标信息，填写String类型替代Long类型。
        :type compound_metric_ids: list[str]
        :param compound_metric_names: 复合指标名称信息
        :type compound_metric_names: list[str]
        :param cal_fn_ids: 引用函数ID，填写String类型替代Long类型。
        :type cal_fn_ids: list[str]
        :param cal_exp: 计算表达式，形如${index_id} + ${compound#index_id}，其中index_id代表引用的衍生指标ID，compound#index_id代表引用的复合指标ID。
        :type cal_exp: str
        :param l1_id: 主题域分组ID，只读，填写String类型替代Long类型。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象ID，填写String类型替代Long类型。
        :type l3_id: str
        :param data_type: 字段类型。
        :type data_type: str
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param monitor: 
        :type monitor: :class:`huaweicloudsdkdataartsstudio.v1.MetricMonitorVO`
        :param l1: 主题域分组中文名，只读，创建和更新时无需填写。
        :type l1: str
        :param l2: 主题域中文名，只读，创建和更新时无需填写。
        :type l2: str
        :param l3: 业务对象中文名，只读，创建和更新时无需填写。
        :type l3: str
        :param summary_table_id: 汇总表ID，只读，填写String类型替代Long类型。
        :type summary_table_id: str
        """
        
        

        self._id = None
        self._name_en = None
        self._name_ch = None
        self._description = None
        self._dimension_group = None
        self._group_name = None
        self._group_code = None
        self._compound_type = None
        self._comparison_type = None
        self._metric_ids = None
        self._metric_names = None
        self._compound_metric_ids = None
        self._compound_metric_names = None
        self._cal_fn_ids = None
        self._cal_exp = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._data_type = None
        self._create_by = None
        self._update_by = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._approval_info = None
        self._new_biz = None
        self._monitor = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._summary_table_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_en = name_en
        self.name_ch = name_ch
        if description is not None:
            self.description = description
        self.dimension_group = dimension_group
        if group_name is not None:
            self.group_name = group_name
        if group_code is not None:
            self.group_code = group_code
        if compound_type is not None:
            self.compound_type = compound_type
        if comparison_type is not None:
            self.comparison_type = comparison_type
        self.metric_ids = metric_ids
        if metric_names is not None:
            self.metric_names = metric_names
        if compound_metric_ids is not None:
            self.compound_metric_ids = compound_metric_ids
        if compound_metric_names is not None:
            self.compound_metric_names = compound_metric_names
        if cal_fn_ids is not None:
            self.cal_fn_ids = cal_fn_ids
        self.cal_exp = cal_exp
        if l1_id is not None:
            self.l1_id = l1_id
        if l2_id is not None:
            self.l2_id = l2_id
        if l3_id is not None:
            self.l3_id = l3_id
        if data_type is not None:
            self.data_type = data_type
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz
        if monitor is not None:
            self.monitor = monitor
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        if summary_table_id is not None:
            self.summary_table_id = summary_table_id

    @property
    def id(self):
        """Gets the id of this CompoundMetricVO.

        编码，填写String类型替代Long类型。

        :return: The id of this CompoundMetricVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompoundMetricVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this CompoundMetricVO.
        :type id: str
        """
        self._id = id

    @property
    def name_en(self):
        """Gets the name_en of this CompoundMetricVO.

        字段名。

        :return: The name_en of this CompoundMetricVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this CompoundMetricVO.

        字段名。

        :param name_en: The name_en of this CompoundMetricVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this CompoundMetricVO.

        业务属性。

        :return: The name_ch of this CompoundMetricVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this CompoundMetricVO.

        业务属性。

        :param name_ch: The name_ch of this CompoundMetricVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        """Gets the description of this CompoundMetricVO.

        描述

        :return: The description of this CompoundMetricVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CompoundMetricVO.

        描述

        :param description: The description of this CompoundMetricVO.
        :type description: str
        """
        self._description = description

    @property
    def dimension_group(self):
        """Gets the dimension_group of this CompoundMetricVO.

        颗粒度ID。

        :return: The dimension_group of this CompoundMetricVO.
        :rtype: str
        """
        return self._dimension_group

    @dimension_group.setter
    def dimension_group(self, dimension_group):
        """Sets the dimension_group of this CompoundMetricVO.

        颗粒度ID。

        :param dimension_group: The dimension_group of this CompoundMetricVO.
        :type dimension_group: str
        """
        self._dimension_group = dimension_group

    @property
    def group_name(self):
        """Gets the group_name of this CompoundMetricVO.

        颗粒度名称，只读。

        :return: The group_name of this CompoundMetricVO.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this CompoundMetricVO.

        颗粒度名称，只读。

        :param group_name: The group_name of this CompoundMetricVO.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_code(self):
        """Gets the group_code of this CompoundMetricVO.

        颗粒度编码，只读。

        :return: The group_code of this CompoundMetricVO.
        :rtype: str
        """
        return self._group_code

    @group_code.setter
    def group_code(self, group_code):
        """Sets the group_code of this CompoundMetricVO.

        颗粒度编码，只读。

        :param group_code: The group_code of this CompoundMetricVO.
        :type group_code: str
        """
        self._group_code = group_code

    @property
    def compound_type(self):
        """Gets the compound_type of this CompoundMetricVO.

        复合指标类型。 枚举值：   - EXPRESSION: 表达式   - PERIODICITY_VALUED_COMPARISON: 环比   - INTERVAL_VALUED_COMPARISON: 同比 

        :return: The compound_type of this CompoundMetricVO.
        :rtype: str
        """
        return self._compound_type

    @compound_type.setter
    def compound_type(self, compound_type):
        """Sets the compound_type of this CompoundMetricVO.

        复合指标类型。 枚举值：   - EXPRESSION: 表达式   - PERIODICITY_VALUED_COMPARISON: 环比   - INTERVAL_VALUED_COMPARISON: 同比 

        :param compound_type: The compound_type of this CompoundMetricVO.
        :type compound_type: str
        """
        self._compound_type = compound_type

    @property
    def comparison_type(self):
        """Gets the comparison_type of this CompoundMetricVO.

        比较类型。 枚举值：   - YEAR_TO_YEAR: 年同比   - MONTH_TO_MONTH: 月同比   - WEEK_TO_WEEK: 周同比 

        :return: The comparison_type of this CompoundMetricVO.
        :rtype: str
        """
        return self._comparison_type

    @comparison_type.setter
    def comparison_type(self, comparison_type):
        """Sets the comparison_type of this CompoundMetricVO.

        比较类型。 枚举值：   - YEAR_TO_YEAR: 年同比   - MONTH_TO_MONTH: 月同比   - WEEK_TO_WEEK: 周同比 

        :param comparison_type: The comparison_type of this CompoundMetricVO.
        :type comparison_type: str
        """
        self._comparison_type = comparison_type

    @property
    def metric_ids(self):
        """Gets the metric_ids of this CompoundMetricVO.

        指标信息，填写String类型替代Long类型。

        :return: The metric_ids of this CompoundMetricVO.
        :rtype: list[str]
        """
        return self._metric_ids

    @metric_ids.setter
    def metric_ids(self, metric_ids):
        """Sets the metric_ids of this CompoundMetricVO.

        指标信息，填写String类型替代Long类型。

        :param metric_ids: The metric_ids of this CompoundMetricVO.
        :type metric_ids: list[str]
        """
        self._metric_ids = metric_ids

    @property
    def metric_names(self):
        """Gets the metric_names of this CompoundMetricVO.

        指标名称信息。

        :return: The metric_names of this CompoundMetricVO.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        """Sets the metric_names of this CompoundMetricVO.

        指标名称信息。

        :param metric_names: The metric_names of this CompoundMetricVO.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def compound_metric_ids(self):
        """Gets the compound_metric_ids of this CompoundMetricVO.

        复合指标信息，填写String类型替代Long类型。

        :return: The compound_metric_ids of this CompoundMetricVO.
        :rtype: list[str]
        """
        return self._compound_metric_ids

    @compound_metric_ids.setter
    def compound_metric_ids(self, compound_metric_ids):
        """Sets the compound_metric_ids of this CompoundMetricVO.

        复合指标信息，填写String类型替代Long类型。

        :param compound_metric_ids: The compound_metric_ids of this CompoundMetricVO.
        :type compound_metric_ids: list[str]
        """
        self._compound_metric_ids = compound_metric_ids

    @property
    def compound_metric_names(self):
        """Gets the compound_metric_names of this CompoundMetricVO.

        复合指标名称信息

        :return: The compound_metric_names of this CompoundMetricVO.
        :rtype: list[str]
        """
        return self._compound_metric_names

    @compound_metric_names.setter
    def compound_metric_names(self, compound_metric_names):
        """Sets the compound_metric_names of this CompoundMetricVO.

        复合指标名称信息

        :param compound_metric_names: The compound_metric_names of this CompoundMetricVO.
        :type compound_metric_names: list[str]
        """
        self._compound_metric_names = compound_metric_names

    @property
    def cal_fn_ids(self):
        """Gets the cal_fn_ids of this CompoundMetricVO.

        引用函数ID，填写String类型替代Long类型。

        :return: The cal_fn_ids of this CompoundMetricVO.
        :rtype: list[str]
        """
        return self._cal_fn_ids

    @cal_fn_ids.setter
    def cal_fn_ids(self, cal_fn_ids):
        """Sets the cal_fn_ids of this CompoundMetricVO.

        引用函数ID，填写String类型替代Long类型。

        :param cal_fn_ids: The cal_fn_ids of this CompoundMetricVO.
        :type cal_fn_ids: list[str]
        """
        self._cal_fn_ids = cal_fn_ids

    @property
    def cal_exp(self):
        """Gets the cal_exp of this CompoundMetricVO.

        计算表达式，形如${index_id} + ${compound#index_id}，其中index_id代表引用的衍生指标ID，compound#index_id代表引用的复合指标ID。

        :return: The cal_exp of this CompoundMetricVO.
        :rtype: str
        """
        return self._cal_exp

    @cal_exp.setter
    def cal_exp(self, cal_exp):
        """Sets the cal_exp of this CompoundMetricVO.

        计算表达式，形如${index_id} + ${compound#index_id}，其中index_id代表引用的衍生指标ID，compound#index_id代表引用的复合指标ID。

        :param cal_exp: The cal_exp of this CompoundMetricVO.
        :type cal_exp: str
        """
        self._cal_exp = cal_exp

    @property
    def l1_id(self):
        """Gets the l1_id of this CompoundMetricVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :return: The l1_id of this CompoundMetricVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        """Sets the l1_id of this CompoundMetricVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :param l1_id: The l1_id of this CompoundMetricVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        """Gets the l2_id of this CompoundMetricVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this CompoundMetricVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this CompoundMetricVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this CompoundMetricVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        """Gets the l3_id of this CompoundMetricVO.

        业务对象ID，填写String类型替代Long类型。

        :return: The l3_id of this CompoundMetricVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this CompoundMetricVO.

        业务对象ID，填写String类型替代Long类型。

        :param l3_id: The l3_id of this CompoundMetricVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def data_type(self):
        """Gets the data_type of this CompoundMetricVO.

        字段类型。

        :return: The data_type of this CompoundMetricVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CompoundMetricVO.

        字段类型。

        :param data_type: The data_type of this CompoundMetricVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def create_by(self):
        """Gets the create_by of this CompoundMetricVO.

        创建人。

        :return: The create_by of this CompoundMetricVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this CompoundMetricVO.

        创建人。

        :param create_by: The create_by of this CompoundMetricVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this CompoundMetricVO.

        更新人。

        :return: The update_by of this CompoundMetricVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this CompoundMetricVO.

        更新人。

        :param update_by: The update_by of this CompoundMetricVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def status(self):
        """Gets the status of this CompoundMetricVO.

        :return: The status of this CompoundMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CompoundMetricVO.

        :param status: The status of this CompoundMetricVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CompoundMetricVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this CompoundMetricVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CompoundMetricVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this CompoundMetricVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CompoundMetricVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this CompoundMetricVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CompoundMetricVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this CompoundMetricVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def approval_info(self):
        """Gets the approval_info of this CompoundMetricVO.

        :return: The approval_info of this CompoundMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        """Sets the approval_info of this CompoundMetricVO.

        :param approval_info: The approval_info of this CompoundMetricVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        """Gets the new_biz of this CompoundMetricVO.

        :return: The new_biz of this CompoundMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this CompoundMetricVO.

        :param new_biz: The new_biz of this CompoundMetricVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def monitor(self):
        """Gets the monitor of this CompoundMetricVO.

        :return: The monitor of this CompoundMetricVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.MetricMonitorVO`
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        """Sets the monitor of this CompoundMetricVO.

        :param monitor: The monitor of this CompoundMetricVO.
        :type monitor: :class:`huaweicloudsdkdataartsstudio.v1.MetricMonitorVO`
        """
        self._monitor = monitor

    @property
    def l1(self):
        """Gets the l1 of this CompoundMetricVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this CompoundMetricVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this CompoundMetricVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this CompoundMetricVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this CompoundMetricVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this CompoundMetricVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this CompoundMetricVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this CompoundMetricVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this CompoundMetricVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this CompoundMetricVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this CompoundMetricVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this CompoundMetricVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def summary_table_id(self):
        """Gets the summary_table_id of this CompoundMetricVO.

        汇总表ID，只读，填写String类型替代Long类型。

        :return: The summary_table_id of this CompoundMetricVO.
        :rtype: str
        """
        return self._summary_table_id

    @summary_table_id.setter
    def summary_table_id(self, summary_table_id):
        """Sets the summary_table_id of this CompoundMetricVO.

        汇总表ID，只读，填写String类型替代Long类型。

        :param summary_table_id: The summary_table_id of this CompoundMetricVO.
        :type summary_table_id: str
        """
        self._summary_table_id = summary_table_id

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
        if not isinstance(other, CompoundMetricVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
