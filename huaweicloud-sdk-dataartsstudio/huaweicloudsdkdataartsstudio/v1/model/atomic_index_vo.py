# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtomicIndexVO:

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
        'cal_exp': 'str',
        'cal_fn_ids': 'list[str]',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'table_id': 'str',
        'tb_name': 'str',
        'dw_type': 'str',
        'field_ids': 'list[str]',
        'field_names': 'list[str]',
        'status': 'BizStatusEnum',
        'biz_type': 'BizTypeEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO'
    }

    attribute_map = {
        'id': 'id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'create_by': 'create_by',
        'cal_exp': 'cal_exp',
        'cal_fn_ids': 'cal_fn_ids',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'table_id': 'table_id',
        'tb_name': 'tb_name',
        'dw_type': 'dw_type',
        'field_ids': 'field_ids',
        'field_names': 'field_names',
        'status': 'status',
        'biz_type': 'biz_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz'
    }

    def __init__(self, id=None, name_en=None, name_ch=None, description=None, create_by=None, cal_exp=None, cal_fn_ids=None, l1_id=None, l2_id=None, l3_id=None, table_id=None, tb_name=None, dw_type=None, field_ids=None, field_names=None, status=None, biz_type=None, create_time=None, update_time=None, l1=None, l2=None, l3=None, approval_info=None, new_biz=None):
        """AtomicIndexVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param name_en: 原子指标英文名。
        :type name_en: str
        :param name_ch: 原子指标英文名。
        :type name_ch: str
        :param description: 描述。
        :type description: str
        :param create_by: 创建人。
        :type create_by: str
        :param cal_exp: 计算表达式，形如&#39;sum(${fact_column_id})&#39;，其中fact_column_id表示引用事实表中的字段ID
        :type cal_exp: str
        :param cal_fn_ids: 引用函数ID，填写String类型替代Long类型。
        :type cal_fn_ids: list[str]
        :param l1_id: 主题域分组ID，只读，填写String类型替代Long类型。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象guid，填写String类型替代Long类型。
        :type l3_id: str
        :param table_id: 事实表ID，填写String类型替代Long类型。
        :type table_id: str
        :param tb_name: 事实表名称。
        :type tb_name: str
        :param dw_type: 数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。
        :type dw_type: str
        :param field_ids: 字段ID信息，填写String类型替代Long类型。
        :type field_ids: list[str]
        :param field_names: 字段名称信息。
        :type field_names: list[str]
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
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
        self._cal_exp = None
        self._cal_fn_ids = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._table_id = None
        self._tb_name = None
        self._dw_type = None
        self._field_ids = None
        self._field_names = None
        self._status = None
        self._biz_type = None
        self._create_time = None
        self._update_time = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
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
        self.cal_exp = cal_exp
        if cal_fn_ids is not None:
            self.cal_fn_ids = cal_fn_ids
        if l1_id is not None:
            self.l1_id = l1_id
        if l2_id is not None:
            self.l2_id = l2_id
        self.l3_id = l3_id
        self.table_id = table_id
        if tb_name is not None:
            self.tb_name = tb_name
        if dw_type is not None:
            self.dw_type = dw_type
        self.field_ids = field_ids
        if field_names is not None:
            self.field_names = field_names
        if status is not None:
            self.status = status
        if biz_type is not None:
            self.biz_type = biz_type
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
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz

    @property
    def id(self):
        """Gets the id of this AtomicIndexVO.

        编码，填写String类型替代Long类型。

        :return: The id of this AtomicIndexVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AtomicIndexVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this AtomicIndexVO.
        :type id: str
        """
        self._id = id

    @property
    def name_en(self):
        """Gets the name_en of this AtomicIndexVO.

        原子指标英文名。

        :return: The name_en of this AtomicIndexVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this AtomicIndexVO.

        原子指标英文名。

        :param name_en: The name_en of this AtomicIndexVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this AtomicIndexVO.

        原子指标英文名。

        :return: The name_ch of this AtomicIndexVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this AtomicIndexVO.

        原子指标英文名。

        :param name_ch: The name_ch of this AtomicIndexVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        """Gets the description of this AtomicIndexVO.

        描述。

        :return: The description of this AtomicIndexVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AtomicIndexVO.

        描述。

        :param description: The description of this AtomicIndexVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        """Gets the create_by of this AtomicIndexVO.

        创建人。

        :return: The create_by of this AtomicIndexVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this AtomicIndexVO.

        创建人。

        :param create_by: The create_by of this AtomicIndexVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def cal_exp(self):
        """Gets the cal_exp of this AtomicIndexVO.

        计算表达式，形如'sum(${fact_column_id})'，其中fact_column_id表示引用事实表中的字段ID

        :return: The cal_exp of this AtomicIndexVO.
        :rtype: str
        """
        return self._cal_exp

    @cal_exp.setter
    def cal_exp(self, cal_exp):
        """Sets the cal_exp of this AtomicIndexVO.

        计算表达式，形如'sum(${fact_column_id})'，其中fact_column_id表示引用事实表中的字段ID

        :param cal_exp: The cal_exp of this AtomicIndexVO.
        :type cal_exp: str
        """
        self._cal_exp = cal_exp

    @property
    def cal_fn_ids(self):
        """Gets the cal_fn_ids of this AtomicIndexVO.

        引用函数ID，填写String类型替代Long类型。

        :return: The cal_fn_ids of this AtomicIndexVO.
        :rtype: list[str]
        """
        return self._cal_fn_ids

    @cal_fn_ids.setter
    def cal_fn_ids(self, cal_fn_ids):
        """Sets the cal_fn_ids of this AtomicIndexVO.

        引用函数ID，填写String类型替代Long类型。

        :param cal_fn_ids: The cal_fn_ids of this AtomicIndexVO.
        :type cal_fn_ids: list[str]
        """
        self._cal_fn_ids = cal_fn_ids

    @property
    def l1_id(self):
        """Gets the l1_id of this AtomicIndexVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :return: The l1_id of this AtomicIndexVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        """Sets the l1_id of this AtomicIndexVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :param l1_id: The l1_id of this AtomicIndexVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        """Gets the l2_id of this AtomicIndexVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this AtomicIndexVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this AtomicIndexVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this AtomicIndexVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        """Gets the l3_id of this AtomicIndexVO.

        业务对象guid，填写String类型替代Long类型。

        :return: The l3_id of this AtomicIndexVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this AtomicIndexVO.

        业务对象guid，填写String类型替代Long类型。

        :param l3_id: The l3_id of this AtomicIndexVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def table_id(self):
        """Gets the table_id of this AtomicIndexVO.

        事实表ID，填写String类型替代Long类型。

        :return: The table_id of this AtomicIndexVO.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this AtomicIndexVO.

        事实表ID，填写String类型替代Long类型。

        :param table_id: The table_id of this AtomicIndexVO.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def tb_name(self):
        """Gets the tb_name of this AtomicIndexVO.

        事实表名称。

        :return: The tb_name of this AtomicIndexVO.
        :rtype: str
        """
        return self._tb_name

    @tb_name.setter
    def tb_name(self, tb_name):
        """Sets the tb_name of this AtomicIndexVO.

        事实表名称。

        :param tb_name: The tb_name of this AtomicIndexVO.
        :type tb_name: str
        """
        self._tb_name = tb_name

    @property
    def dw_type(self):
        """Gets the dw_type of this AtomicIndexVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this AtomicIndexVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        """Sets the dw_type of this AtomicIndexVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this AtomicIndexVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def field_ids(self):
        """Gets the field_ids of this AtomicIndexVO.

        字段ID信息，填写String类型替代Long类型。

        :return: The field_ids of this AtomicIndexVO.
        :rtype: list[str]
        """
        return self._field_ids

    @field_ids.setter
    def field_ids(self, field_ids):
        """Sets the field_ids of this AtomicIndexVO.

        字段ID信息，填写String类型替代Long类型。

        :param field_ids: The field_ids of this AtomicIndexVO.
        :type field_ids: list[str]
        """
        self._field_ids = field_ids

    @property
    def field_names(self):
        """Gets the field_names of this AtomicIndexVO.

        字段名称信息。

        :return: The field_names of this AtomicIndexVO.
        :rtype: list[str]
        """
        return self._field_names

    @field_names.setter
    def field_names(self, field_names):
        """Sets the field_names of this AtomicIndexVO.

        字段名称信息。

        :param field_names: The field_names of this AtomicIndexVO.
        :type field_names: list[str]
        """
        self._field_names = field_names

    @property
    def status(self):
        """Gets the status of this AtomicIndexVO.

        :return: The status of this AtomicIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AtomicIndexVO.

        :param status: The status of this AtomicIndexVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def biz_type(self):
        """Gets the biz_type of this AtomicIndexVO.

        :return: The biz_type of this AtomicIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this AtomicIndexVO.

        :param biz_type: The biz_type of this AtomicIndexVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def create_time(self):
        """Gets the create_time of this AtomicIndexVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this AtomicIndexVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AtomicIndexVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this AtomicIndexVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AtomicIndexVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this AtomicIndexVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AtomicIndexVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this AtomicIndexVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def l1(self):
        """Gets the l1 of this AtomicIndexVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this AtomicIndexVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this AtomicIndexVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this AtomicIndexVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this AtomicIndexVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this AtomicIndexVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this AtomicIndexVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this AtomicIndexVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this AtomicIndexVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this AtomicIndexVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this AtomicIndexVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this AtomicIndexVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def approval_info(self):
        """Gets the approval_info of this AtomicIndexVO.

        :return: The approval_info of this AtomicIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        """Sets the approval_info of this AtomicIndexVO.

        :param approval_info: The approval_info of this AtomicIndexVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        """Gets the new_biz of this AtomicIndexVO.

        :return: The new_biz of this AtomicIndexVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this AtomicIndexVO.

        :param new_biz: The new_biz of this AtomicIndexVO.
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
        if not isinstance(other, AtomicIndexVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
