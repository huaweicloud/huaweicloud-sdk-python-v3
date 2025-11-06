# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LTSSubFieldsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_type': 'str',
        'field_name': 'str',
        'quick_analysis': 'bool',
        'field_analysis_alias': 'str'
    }

    attribute_map = {
        'field_type': 'fieldType',
        'field_name': 'fieldName',
        'quick_analysis': 'quickAnalysis',
        'field_analysis_alias': 'fieldAnalysisAlias'
    }

    def __init__(self, field_type=None, field_name=None, quick_analysis=None, field_analysis_alias=None):
        r"""LTSSubFieldsInfo

        The model defined in huaweicloud sdk

        :param field_type: 字段类型
        :type field_type: str
        :param field_name: 字段名称
        :type field_name: str
        :param quick_analysis: 是否快速分析
        :type quick_analysis: bool
        :param field_analysis_alias: **参数解释：** 别名，设置别名后，只支持使用别名进行SQL搜索分析，不支持使用别名进行关键字搜索。 **约束限制：** 不涉及。 **取值范围：** 长度不能大于256。 **默认取值：** 不涉及。
        :type field_analysis_alias: str
        """
        
        

        self._field_type = None
        self._field_name = None
        self._quick_analysis = None
        self._field_analysis_alias = None
        self.discriminator = None

        self.field_type = field_type
        self.field_name = field_name
        if quick_analysis is not None:
            self.quick_analysis = quick_analysis
        if field_analysis_alias is not None:
            self.field_analysis_alias = field_analysis_alias

    @property
    def field_type(self):
        r"""Gets the field_type of this LTSSubFieldsInfo.

        字段类型

        :return: The field_type of this LTSSubFieldsInfo.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this LTSSubFieldsInfo.

        字段类型

        :param field_type: The field_type of this LTSSubFieldsInfo.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def field_name(self):
        r"""Gets the field_name of this LTSSubFieldsInfo.

        字段名称

        :return: The field_name of this LTSSubFieldsInfo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this LTSSubFieldsInfo.

        字段名称

        :param field_name: The field_name of this LTSSubFieldsInfo.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def quick_analysis(self):
        r"""Gets the quick_analysis of this LTSSubFieldsInfo.

        是否快速分析

        :return: The quick_analysis of this LTSSubFieldsInfo.
        :rtype: bool
        """
        return self._quick_analysis

    @quick_analysis.setter
    def quick_analysis(self, quick_analysis):
        r"""Sets the quick_analysis of this LTSSubFieldsInfo.

        是否快速分析

        :param quick_analysis: The quick_analysis of this LTSSubFieldsInfo.
        :type quick_analysis: bool
        """
        self._quick_analysis = quick_analysis

    @property
    def field_analysis_alias(self):
        r"""Gets the field_analysis_alias of this LTSSubFieldsInfo.

        **参数解释：** 别名，设置别名后，只支持使用别名进行SQL搜索分析，不支持使用别名进行关键字搜索。 **约束限制：** 不涉及。 **取值范围：** 长度不能大于256。 **默认取值：** 不涉及。

        :return: The field_analysis_alias of this LTSSubFieldsInfo.
        :rtype: str
        """
        return self._field_analysis_alias

    @field_analysis_alias.setter
    def field_analysis_alias(self, field_analysis_alias):
        r"""Sets the field_analysis_alias of this LTSSubFieldsInfo.

        **参数解释：** 别名，设置别名后，只支持使用别名进行SQL搜索分析，不支持使用别名进行关键字搜索。 **约束限制：** 不涉及。 **取值范围：** 长度不能大于256。 **默认取值：** 不涉及。

        :param field_analysis_alias: The field_analysis_alias of this LTSSubFieldsInfo.
        :type field_analysis_alias: str
        """
        self._field_analysis_alias = field_analysis_alias

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
        if not isinstance(other, LTSSubFieldsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
