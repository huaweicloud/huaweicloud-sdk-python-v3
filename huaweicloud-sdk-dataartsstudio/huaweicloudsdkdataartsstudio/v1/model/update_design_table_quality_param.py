# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDesignTableQualityParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'biz_type': 'str',
        'dirty_out_switch': 'bool',
        'dirty_out_database': 'str',
        'dirty_out_prefix': 'str',
        'dirty_out_suffix': 'str'
    }

    attribute_map = {
        'biz_type': 'biz_type',
        'dirty_out_switch': 'dirty_out_switch',
        'dirty_out_database': 'dirty_out_database',
        'dirty_out_prefix': 'dirty_out_prefix',
        'dirty_out_suffix': 'dirty_out_suffix'
    }

    def __init__(self, biz_type=None, dirty_out_switch=None, dirty_out_database=None, dirty_out_prefix=None, dirty_out_suffix=None):
        """UpdateDesignTableQualityParam

        The model defined in huaweicloud sdk

        :param biz_type: 表类型。 枚举值：   - TABLE_MODEL: 关系模型（逻辑模型/物理模型）   - AGGREGATION_LOGIC_TABLE: 汇总表   - FACT_LOGIC_TABLE: 事实表   - DIMENSION: 维度   - DIMENSION_LOGIC_TABLE: 维度表 
        :type biz_type: str
        :param dirty_out_switch: 异常数据输出开关。
        :type dirty_out_switch: bool
        :param dirty_out_database: 异常数据输出库。
        :type dirty_out_database: str
        :param dirty_out_prefix: 异常表前缀。
        :type dirty_out_prefix: str
        :param dirty_out_suffix: 异常表后缀。
        :type dirty_out_suffix: str
        """
        
        

        self._biz_type = None
        self._dirty_out_switch = None
        self._dirty_out_database = None
        self._dirty_out_prefix = None
        self._dirty_out_suffix = None
        self.discriminator = None

        if biz_type is not None:
            self.biz_type = biz_type
        if dirty_out_switch is not None:
            self.dirty_out_switch = dirty_out_switch
        if dirty_out_database is not None:
            self.dirty_out_database = dirty_out_database
        if dirty_out_prefix is not None:
            self.dirty_out_prefix = dirty_out_prefix
        if dirty_out_suffix is not None:
            self.dirty_out_suffix = dirty_out_suffix

    @property
    def biz_type(self):
        """Gets the biz_type of this UpdateDesignTableQualityParam.

        表类型。 枚举值：   - TABLE_MODEL: 关系模型（逻辑模型/物理模型）   - AGGREGATION_LOGIC_TABLE: 汇总表   - FACT_LOGIC_TABLE: 事实表   - DIMENSION: 维度   - DIMENSION_LOGIC_TABLE: 维度表 

        :return: The biz_type of this UpdateDesignTableQualityParam.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this UpdateDesignTableQualityParam.

        表类型。 枚举值：   - TABLE_MODEL: 关系模型（逻辑模型/物理模型）   - AGGREGATION_LOGIC_TABLE: 汇总表   - FACT_LOGIC_TABLE: 事实表   - DIMENSION: 维度   - DIMENSION_LOGIC_TABLE: 维度表 

        :param biz_type: The biz_type of this UpdateDesignTableQualityParam.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def dirty_out_switch(self):
        """Gets the dirty_out_switch of this UpdateDesignTableQualityParam.

        异常数据输出开关。

        :return: The dirty_out_switch of this UpdateDesignTableQualityParam.
        :rtype: bool
        """
        return self._dirty_out_switch

    @dirty_out_switch.setter
    def dirty_out_switch(self, dirty_out_switch):
        """Sets the dirty_out_switch of this UpdateDesignTableQualityParam.

        异常数据输出开关。

        :param dirty_out_switch: The dirty_out_switch of this UpdateDesignTableQualityParam.
        :type dirty_out_switch: bool
        """
        self._dirty_out_switch = dirty_out_switch

    @property
    def dirty_out_database(self):
        """Gets the dirty_out_database of this UpdateDesignTableQualityParam.

        异常数据输出库。

        :return: The dirty_out_database of this UpdateDesignTableQualityParam.
        :rtype: str
        """
        return self._dirty_out_database

    @dirty_out_database.setter
    def dirty_out_database(self, dirty_out_database):
        """Sets the dirty_out_database of this UpdateDesignTableQualityParam.

        异常数据输出库。

        :param dirty_out_database: The dirty_out_database of this UpdateDesignTableQualityParam.
        :type dirty_out_database: str
        """
        self._dirty_out_database = dirty_out_database

    @property
    def dirty_out_prefix(self):
        """Gets the dirty_out_prefix of this UpdateDesignTableQualityParam.

        异常表前缀。

        :return: The dirty_out_prefix of this UpdateDesignTableQualityParam.
        :rtype: str
        """
        return self._dirty_out_prefix

    @dirty_out_prefix.setter
    def dirty_out_prefix(self, dirty_out_prefix):
        """Sets the dirty_out_prefix of this UpdateDesignTableQualityParam.

        异常表前缀。

        :param dirty_out_prefix: The dirty_out_prefix of this UpdateDesignTableQualityParam.
        :type dirty_out_prefix: str
        """
        self._dirty_out_prefix = dirty_out_prefix

    @property
    def dirty_out_suffix(self):
        """Gets the dirty_out_suffix of this UpdateDesignTableQualityParam.

        异常表后缀。

        :return: The dirty_out_suffix of this UpdateDesignTableQualityParam.
        :rtype: str
        """
        return self._dirty_out_suffix

    @dirty_out_suffix.setter
    def dirty_out_suffix(self, dirty_out_suffix):
        """Sets the dirty_out_suffix of this UpdateDesignTableQualityParam.

        异常表后缀。

        :param dirty_out_suffix: The dirty_out_suffix of this UpdateDesignTableQualityParam.
        :type dirty_out_suffix: str
        """
        self._dirty_out_suffix = dirty_out_suffix

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
        if not isinstance(other, UpdateDesignTableQualityParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
