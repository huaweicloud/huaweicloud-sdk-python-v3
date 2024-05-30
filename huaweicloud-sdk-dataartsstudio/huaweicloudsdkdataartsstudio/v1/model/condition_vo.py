# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionVO:

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
        'condition_fn': 'str',
        'condition_fn_param': 'str',
        'status': 'BizStatusEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'base_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'create_by': 'create_by',
        'condition_fn': 'condition_fn',
        'condition_fn_param': 'condition_fn_param',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'base_time': 'base_time'
    }

    def __init__(self, id=None, name_en=None, name_ch=None, description=None, create_by=None, condition_fn=None, condition_fn_param=None, status=None, create_time=None, update_time=None, approval_info=None, new_biz=None, base_time=None):
        """ConditionVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param name_en: 字段名
        :type name_en: str
        :param name_ch: 业务属性。
        :type name_ch: str
        :param description: 描述。
        :type description: str
        :param create_by: 创建人。
        :type create_by: str
        :param condition_fn: 限定计算方法。 枚举值：   - LAST_YEAR: 前一年   - CURRENT_YEAR: 本年   - BETWEEN_YEAR: 自定义年区间   - LAST_MONTH: 前一月   - CURRENT_MONTH: 本月   - BETWEEN_MONTH: 自定义月区间   - LAST_DAY: 前一天   - CURRENT_DAY: 本日   - BETWEEN_DAY: 自定义日区间   - LAST_HOUR: 上一小时   - CURRENT_HOUR: 当前小时   - BETWEEN_HOUR: 自定义小时区间   - LAST_MINUTE: 上一分钟   - CURRENT_MINUTE: 当前分钟   - BETWEEN_MINUTE: 自定义分钟区间 
        :type condition_fn: str
        :param condition_fn_param: 限定计算参数。
        :type condition_fn_param: str
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
        :param base_time: 基准时间。
        :type base_time: int
        """
        
        

        self._id = None
        self._name_en = None
        self._name_ch = None
        self._description = None
        self._create_by = None
        self._condition_fn = None
        self._condition_fn_param = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._approval_info = None
        self._new_biz = None
        self._base_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_en = name_en
        self.name_ch = name_ch
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        if condition_fn is not None:
            self.condition_fn = condition_fn
        if condition_fn_param is not None:
            self.condition_fn_param = condition_fn_param
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
        if base_time is not None:
            self.base_time = base_time

    @property
    def id(self):
        """Gets the id of this ConditionVO.

        编码，填写String类型替代Long类型。

        :return: The id of this ConditionVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConditionVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this ConditionVO.
        :type id: str
        """
        self._id = id

    @property
    def name_en(self):
        """Gets the name_en of this ConditionVO.

        字段名

        :return: The name_en of this ConditionVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this ConditionVO.

        字段名

        :param name_en: The name_en of this ConditionVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this ConditionVO.

        业务属性。

        :return: The name_ch of this ConditionVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this ConditionVO.

        业务属性。

        :param name_ch: The name_ch of this ConditionVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        """Gets the description of this ConditionVO.

        描述。

        :return: The description of this ConditionVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConditionVO.

        描述。

        :param description: The description of this ConditionVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        """Gets the create_by of this ConditionVO.

        创建人。

        :return: The create_by of this ConditionVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this ConditionVO.

        创建人。

        :param create_by: The create_by of this ConditionVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def condition_fn(self):
        """Gets the condition_fn of this ConditionVO.

        限定计算方法。 枚举值：   - LAST_YEAR: 前一年   - CURRENT_YEAR: 本年   - BETWEEN_YEAR: 自定义年区间   - LAST_MONTH: 前一月   - CURRENT_MONTH: 本月   - BETWEEN_MONTH: 自定义月区间   - LAST_DAY: 前一天   - CURRENT_DAY: 本日   - BETWEEN_DAY: 自定义日区间   - LAST_HOUR: 上一小时   - CURRENT_HOUR: 当前小时   - BETWEEN_HOUR: 自定义小时区间   - LAST_MINUTE: 上一分钟   - CURRENT_MINUTE: 当前分钟   - BETWEEN_MINUTE: 自定义分钟区间 

        :return: The condition_fn of this ConditionVO.
        :rtype: str
        """
        return self._condition_fn

    @condition_fn.setter
    def condition_fn(self, condition_fn):
        """Sets the condition_fn of this ConditionVO.

        限定计算方法。 枚举值：   - LAST_YEAR: 前一年   - CURRENT_YEAR: 本年   - BETWEEN_YEAR: 自定义年区间   - LAST_MONTH: 前一月   - CURRENT_MONTH: 本月   - BETWEEN_MONTH: 自定义月区间   - LAST_DAY: 前一天   - CURRENT_DAY: 本日   - BETWEEN_DAY: 自定义日区间   - LAST_HOUR: 上一小时   - CURRENT_HOUR: 当前小时   - BETWEEN_HOUR: 自定义小时区间   - LAST_MINUTE: 上一分钟   - CURRENT_MINUTE: 当前分钟   - BETWEEN_MINUTE: 自定义分钟区间 

        :param condition_fn: The condition_fn of this ConditionVO.
        :type condition_fn: str
        """
        self._condition_fn = condition_fn

    @property
    def condition_fn_param(self):
        """Gets the condition_fn_param of this ConditionVO.

        限定计算参数。

        :return: The condition_fn_param of this ConditionVO.
        :rtype: str
        """
        return self._condition_fn_param

    @condition_fn_param.setter
    def condition_fn_param(self, condition_fn_param):
        """Sets the condition_fn_param of this ConditionVO.

        限定计算参数。

        :param condition_fn_param: The condition_fn_param of this ConditionVO.
        :type condition_fn_param: str
        """
        self._condition_fn_param = condition_fn_param

    @property
    def status(self):
        """Gets the status of this ConditionVO.

        :return: The status of this ConditionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConditionVO.

        :param status: The status of this ConditionVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ConditionVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this ConditionVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ConditionVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this ConditionVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ConditionVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this ConditionVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ConditionVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this ConditionVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def approval_info(self):
        """Gets the approval_info of this ConditionVO.

        :return: The approval_info of this ConditionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        """Sets the approval_info of this ConditionVO.

        :param approval_info: The approval_info of this ConditionVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        """Gets the new_biz of this ConditionVO.

        :return: The new_biz of this ConditionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this ConditionVO.

        :param new_biz: The new_biz of this ConditionVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def base_time(self):
        """Gets the base_time of this ConditionVO.

        基准时间。

        :return: The base_time of this ConditionVO.
        :rtype: int
        """
        return self._base_time

    @base_time.setter
    def base_time(self, base_time):
        """Sets the base_time of this ConditionVO.

        基准时间。

        :param base_time: The base_time of this ConditionVO.
        :type base_time: int
        """
        self._base_time = base_time

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
        if not isinstance(other, ConditionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
