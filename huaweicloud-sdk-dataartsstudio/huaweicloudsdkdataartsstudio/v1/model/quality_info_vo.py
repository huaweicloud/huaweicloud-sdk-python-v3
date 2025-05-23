# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualityInfoVO:

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
        'table_id': 'str',
        'attr_id': 'str',
        'biz_type': 'BizTypeEnum',
        'data_quality_id': 'str',
        'show_control': 'int',
        'data_quality_name': 'str',
        'alert_conf': 'str',
        'expression': 'str',
        'extend_info': 'str',
        'from_standard': 'bool',
        'result_description': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'table_id': 'table_id',
        'attr_id': 'attr_id',
        'biz_type': 'biz_type',
        'data_quality_id': 'data_quality_id',
        'show_control': 'show_control',
        'data_quality_name': 'data_quality_name',
        'alert_conf': 'alert_conf',
        'expression': 'expression',
        'extend_info': 'extend_info',
        'from_standard': 'from_standard',
        'result_description': 'result_description',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, table_id=None, attr_id=None, biz_type=None, data_quality_id=None, show_control=None, data_quality_name=None, alert_conf=None, expression=None, extend_info=None, from_standard=None, result_description=None, create_by=None, update_by=None, create_time=None, update_time=None):
        r"""QualityInfoVO

        The model defined in huaweicloud sdk

        :param id: 编码ID，ID字符串。
        :type id: str
        :param table_id: 表ID，只读，ID字符串。
        :type table_id: str
        :param attr_id: 属性ID，只读，ID字符串。
        :type attr_id: str
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param data_quality_id: 质量ID，ID字符串。
        :type data_quality_id: str
        :param show_control: 是否要显示正则表达式。
        :type show_control: int
        :param data_quality_name: 质量名称。
        :type data_quality_name: str
        :param alert_conf: 告警配置。
        :type alert_conf: str
        :param expression: 正则相关校验规则中正则配置。
        :type expression: str
        :param extend_info: 扩展信息。
        :type extend_info: str
        :param from_standard: 是否来源于数据标准质量配置，只读。
        :type from_standard: bool
        :param result_description: 结果说明。
        :type result_description: str
        :param create_by: 创建人，只读。
        :type create_by: str
        :param update_by: 更新人，只读。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._table_id = None
        self._attr_id = None
        self._biz_type = None
        self._data_quality_id = None
        self._show_control = None
        self._data_quality_name = None
        self._alert_conf = None
        self._expression = None
        self._extend_info = None
        self._from_standard = None
        self._result_description = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if table_id is not None:
            self.table_id = table_id
        if attr_id is not None:
            self.attr_id = attr_id
        if biz_type is not None:
            self.biz_type = biz_type
        self.data_quality_id = data_quality_id
        if show_control is not None:
            self.show_control = show_control
        if data_quality_name is not None:
            self.data_quality_name = data_quality_name
        if alert_conf is not None:
            self.alert_conf = alert_conf
        if expression is not None:
            self.expression = expression
        if extend_info is not None:
            self.extend_info = extend_info
        if from_standard is not None:
            self.from_standard = from_standard
        if result_description is not None:
            self.result_description = result_description
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this QualityInfoVO.

        编码ID，ID字符串。

        :return: The id of this QualityInfoVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QualityInfoVO.

        编码ID，ID字符串。

        :param id: The id of this QualityInfoVO.
        :type id: str
        """
        self._id = id

    @property
    def table_id(self):
        r"""Gets the table_id of this QualityInfoVO.

        表ID，只读，ID字符串。

        :return: The table_id of this QualityInfoVO.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this QualityInfoVO.

        表ID，只读，ID字符串。

        :param table_id: The table_id of this QualityInfoVO.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def attr_id(self):
        r"""Gets the attr_id of this QualityInfoVO.

        属性ID，只读，ID字符串。

        :return: The attr_id of this QualityInfoVO.
        :rtype: str
        """
        return self._attr_id

    @attr_id.setter
    def attr_id(self, attr_id):
        r"""Sets the attr_id of this QualityInfoVO.

        属性ID，只读，ID字符串。

        :param attr_id: The attr_id of this QualityInfoVO.
        :type attr_id: str
        """
        self._attr_id = attr_id

    @property
    def biz_type(self):
        r"""Gets the biz_type of this QualityInfoVO.

        :return: The biz_type of this QualityInfoVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this QualityInfoVO.

        :param biz_type: The biz_type of this QualityInfoVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def data_quality_id(self):
        r"""Gets the data_quality_id of this QualityInfoVO.

        质量ID，ID字符串。

        :return: The data_quality_id of this QualityInfoVO.
        :rtype: str
        """
        return self._data_quality_id

    @data_quality_id.setter
    def data_quality_id(self, data_quality_id):
        r"""Sets the data_quality_id of this QualityInfoVO.

        质量ID，ID字符串。

        :param data_quality_id: The data_quality_id of this QualityInfoVO.
        :type data_quality_id: str
        """
        self._data_quality_id = data_quality_id

    @property
    def show_control(self):
        r"""Gets the show_control of this QualityInfoVO.

        是否要显示正则表达式。

        :return: The show_control of this QualityInfoVO.
        :rtype: int
        """
        return self._show_control

    @show_control.setter
    def show_control(self, show_control):
        r"""Sets the show_control of this QualityInfoVO.

        是否要显示正则表达式。

        :param show_control: The show_control of this QualityInfoVO.
        :type show_control: int
        """
        self._show_control = show_control

    @property
    def data_quality_name(self):
        r"""Gets the data_quality_name of this QualityInfoVO.

        质量名称。

        :return: The data_quality_name of this QualityInfoVO.
        :rtype: str
        """
        return self._data_quality_name

    @data_quality_name.setter
    def data_quality_name(self, data_quality_name):
        r"""Sets the data_quality_name of this QualityInfoVO.

        质量名称。

        :param data_quality_name: The data_quality_name of this QualityInfoVO.
        :type data_quality_name: str
        """
        self._data_quality_name = data_quality_name

    @property
    def alert_conf(self):
        r"""Gets the alert_conf of this QualityInfoVO.

        告警配置。

        :return: The alert_conf of this QualityInfoVO.
        :rtype: str
        """
        return self._alert_conf

    @alert_conf.setter
    def alert_conf(self, alert_conf):
        r"""Sets the alert_conf of this QualityInfoVO.

        告警配置。

        :param alert_conf: The alert_conf of this QualityInfoVO.
        :type alert_conf: str
        """
        self._alert_conf = alert_conf

    @property
    def expression(self):
        r"""Gets the expression of this QualityInfoVO.

        正则相关校验规则中正则配置。

        :return: The expression of this QualityInfoVO.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this QualityInfoVO.

        正则相关校验规则中正则配置。

        :param expression: The expression of this QualityInfoVO.
        :type expression: str
        """
        self._expression = expression

    @property
    def extend_info(self):
        r"""Gets the extend_info of this QualityInfoVO.

        扩展信息。

        :return: The extend_info of this QualityInfoVO.
        :rtype: str
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        r"""Sets the extend_info of this QualityInfoVO.

        扩展信息。

        :param extend_info: The extend_info of this QualityInfoVO.
        :type extend_info: str
        """
        self._extend_info = extend_info

    @property
    def from_standard(self):
        r"""Gets the from_standard of this QualityInfoVO.

        是否来源于数据标准质量配置，只读。

        :return: The from_standard of this QualityInfoVO.
        :rtype: bool
        """
        return self._from_standard

    @from_standard.setter
    def from_standard(self, from_standard):
        r"""Sets the from_standard of this QualityInfoVO.

        是否来源于数据标准质量配置，只读。

        :param from_standard: The from_standard of this QualityInfoVO.
        :type from_standard: bool
        """
        self._from_standard = from_standard

    @property
    def result_description(self):
        r"""Gets the result_description of this QualityInfoVO.

        结果说明。

        :return: The result_description of this QualityInfoVO.
        :rtype: str
        """
        return self._result_description

    @result_description.setter
    def result_description(self, result_description):
        r"""Sets the result_description of this QualityInfoVO.

        结果说明。

        :param result_description: The result_description of this QualityInfoVO.
        :type result_description: str
        """
        self._result_description = result_description

    @property
    def create_by(self):
        r"""Gets the create_by of this QualityInfoVO.

        创建人，只读。

        :return: The create_by of this QualityInfoVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this QualityInfoVO.

        创建人，只读。

        :param create_by: The create_by of this QualityInfoVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this QualityInfoVO.

        更新人，只读。

        :return: The update_by of this QualityInfoVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this QualityInfoVO.

        更新人，只读。

        :param update_by: The update_by of this QualityInfoVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        r"""Gets the create_time of this QualityInfoVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this QualityInfoVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QualityInfoVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this QualityInfoVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this QualityInfoVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this QualityInfoVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this QualityInfoVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this QualityInfoVO.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, QualityInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
