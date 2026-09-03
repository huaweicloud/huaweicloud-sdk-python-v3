# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FtMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_cn': 'str',
        'name_en': 'str',
        'des_en': 'str',
        'des_cn': 'str',
        'type': 'str',
        'group': 'str',
        'group_by': 'list[str]',
        'x_axis': 'str',
        'tags': 'list[str]',
        'unit': 'str',
        'data': 'object'
    }

    attribute_map = {
        'name_cn': 'name_cn',
        'name_en': 'name_en',
        'des_en': 'des_en',
        'des_cn': 'des_cn',
        'type': 'type',
        'group': 'group',
        'group_by': 'group_by',
        'x_axis': 'x_axis',
        'tags': 'tags',
        'unit': 'unit',
        'data': 'data'
    }

    def __init__(self, name_cn=None, name_en=None, des_en=None, des_cn=None, type=None, group=None, group_by=None, x_axis=None, tags=None, unit=None, data=None):
        r"""FtMetric

        The model defined in huaweicloud sdk

        :param name_cn: 指标中文名称，如 训练指标、准确率，前端用作图例或列名
        :type name_cn: str
        :param name_en: 指标英文名称，如 train_loss、val_accuracy，前端用作图例或列名
        :type name_en: str
        :param des_en: 指标中文解释，如 训练指标，前端用作针对指标进行释义
        :type des_en: str
        :param des_cn: 指标英文解释，如 train loss，前端用作针对指标进行释义
        :type des_cn: str
        :param type: 指标绘图类型，可选 line（折线图）或 pie（饼图）、tabel（表格）、scalar（单值），可扩展 image 等
        :type type: str
        :param group: 逻辑分组，如 training、validation、test，可扩展，用于前端分栏或过滤
        :type group: str
        :param group_by: 指定哪些数据点字段用于分组生成多个系列（如 [\&quot;layer\&quot;,\&quot;feature\&quot;]）
        :type group_by: list[str]
        :param x_axis: 明确指定用作 X 轴的数据点字段名（如 \&quot;step\&quot;、\&quot;epoch\&quot;、\&quot;timestamp\&quot;）
        :type x_axis: str
        :param tags: 逻辑分组，如 表面loss，用于前端分组或过滤
        :type tags: list[str]
        :param unit: 单位，如 %、samples/sec，仅用于展示
        :type unit: str
        :param data: 数据点数组，严格按时间/步序升序排列
        :type data: object
        """
        
        

        self._name_cn = None
        self._name_en = None
        self._des_en = None
        self._des_cn = None
        self._type = None
        self._group = None
        self._group_by = None
        self._x_axis = None
        self._tags = None
        self._unit = None
        self._data = None
        self.discriminator = None

        self.name_cn = name_cn
        self.name_en = name_en
        self.des_en = des_en
        self.des_cn = des_cn
        if type is not None:
            self.type = type
        if group is not None:
            self.group = group
        if group_by is not None:
            self.group_by = group_by
        if x_axis is not None:
            self.x_axis = x_axis
        if tags is not None:
            self.tags = tags
        if unit is not None:
            self.unit = unit
        self.data = data

    @property
    def name_cn(self):
        r"""Gets the name_cn of this FtMetric.

        指标中文名称，如 训练指标、准确率，前端用作图例或列名

        :return: The name_cn of this FtMetric.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this FtMetric.

        指标中文名称，如 训练指标、准确率，前端用作图例或列名

        :param name_cn: The name_cn of this FtMetric.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def name_en(self):
        r"""Gets the name_en of this FtMetric.

        指标英文名称，如 train_loss、val_accuracy，前端用作图例或列名

        :return: The name_en of this FtMetric.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this FtMetric.

        指标英文名称，如 train_loss、val_accuracy，前端用作图例或列名

        :param name_en: The name_en of this FtMetric.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def des_en(self):
        r"""Gets the des_en of this FtMetric.

        指标中文解释，如 训练指标，前端用作针对指标进行释义

        :return: The des_en of this FtMetric.
        :rtype: str
        """
        return self._des_en

    @des_en.setter
    def des_en(self, des_en):
        r"""Sets the des_en of this FtMetric.

        指标中文解释，如 训练指标，前端用作针对指标进行释义

        :param des_en: The des_en of this FtMetric.
        :type des_en: str
        """
        self._des_en = des_en

    @property
    def des_cn(self):
        r"""Gets the des_cn of this FtMetric.

        指标英文解释，如 train loss，前端用作针对指标进行释义

        :return: The des_cn of this FtMetric.
        :rtype: str
        """
        return self._des_cn

    @des_cn.setter
    def des_cn(self, des_cn):
        r"""Sets the des_cn of this FtMetric.

        指标英文解释，如 train loss，前端用作针对指标进行释义

        :param des_cn: The des_cn of this FtMetric.
        :type des_cn: str
        """
        self._des_cn = des_cn

    @property
    def type(self):
        r"""Gets the type of this FtMetric.

        指标绘图类型，可选 line（折线图）或 pie（饼图）、tabel（表格）、scalar（单值），可扩展 image 等

        :return: The type of this FtMetric.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FtMetric.

        指标绘图类型，可选 line（折线图）或 pie（饼图）、tabel（表格）、scalar（单值），可扩展 image 等

        :param type: The type of this FtMetric.
        :type type: str
        """
        self._type = type

    @property
    def group(self):
        r"""Gets the group of this FtMetric.

        逻辑分组，如 training、validation、test，可扩展，用于前端分栏或过滤

        :return: The group of this FtMetric.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this FtMetric.

        逻辑分组，如 training、validation、test，可扩展，用于前端分栏或过滤

        :param group: The group of this FtMetric.
        :type group: str
        """
        self._group = group

    @property
    def group_by(self):
        r"""Gets the group_by of this FtMetric.

        指定哪些数据点字段用于分组生成多个系列（如 [\"layer\",\"feature\"]）

        :return: The group_by of this FtMetric.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this FtMetric.

        指定哪些数据点字段用于分组生成多个系列（如 [\"layer\",\"feature\"]）

        :param group_by: The group_by of this FtMetric.
        :type group_by: list[str]
        """
        self._group_by = group_by

    @property
    def x_axis(self):
        r"""Gets the x_axis of this FtMetric.

        明确指定用作 X 轴的数据点字段名（如 \"step\"、\"epoch\"、\"timestamp\"）

        :return: The x_axis of this FtMetric.
        :rtype: str
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, x_axis):
        r"""Sets the x_axis of this FtMetric.

        明确指定用作 X 轴的数据点字段名（如 \"step\"、\"epoch\"、\"timestamp\"）

        :param x_axis: The x_axis of this FtMetric.
        :type x_axis: str
        """
        self._x_axis = x_axis

    @property
    def tags(self):
        r"""Gets the tags of this FtMetric.

        逻辑分组，如 表面loss，用于前端分组或过滤

        :return: The tags of this FtMetric.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this FtMetric.

        逻辑分组，如 表面loss，用于前端分组或过滤

        :param tags: The tags of this FtMetric.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def unit(self):
        r"""Gets the unit of this FtMetric.

        单位，如 %、samples/sec，仅用于展示

        :return: The unit of this FtMetric.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this FtMetric.

        单位，如 %、samples/sec，仅用于展示

        :param unit: The unit of this FtMetric.
        :type unit: str
        """
        self._unit = unit

    @property
    def data(self):
        r"""Gets the data of this FtMetric.

        数据点数组，严格按时间/步序升序排列

        :return: The data of this FtMetric.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this FtMetric.

        数据点数组，严格按时间/步序升序排列

        :param data: The data of this FtMetric.
        :type data: object
        """
        self._data = data

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
        if not isinstance(other, FtMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
