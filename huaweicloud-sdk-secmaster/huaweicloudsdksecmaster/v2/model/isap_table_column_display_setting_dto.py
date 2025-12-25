# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapTableColumnDisplaySettingDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'column_alias': 'str',
        'column_alias_en': 'str',
        'display_by_default': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_alias': 'column_alias',
        'column_alias_en': 'column_alias_en',
        'display_by_default': 'display_by_default'
    }

    def __init__(self, column_name=None, column_alias=None, column_alias_en=None, display_by_default=None):
        r"""IsapTableColumnDisplaySettingDto

        The model defined in huaweicloud sdk

        :param column_name: 表格列名称
        :type column_name: str
        :param column_alias: 表格列别名
        :type column_alias: str
        :param column_alias_en: 表格列别名
        :type column_alias_en: str
        :param display_by_default: 是否默认展示
        :type display_by_default: bool
        """
        
        

        self._column_name = None
        self._column_alias = None
        self._column_alias_en = None
        self._display_by_default = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if column_alias is not None:
            self.column_alias = column_alias
        if column_alias_en is not None:
            self.column_alias_en = column_alias_en
        if display_by_default is not None:
            self.display_by_default = display_by_default

    @property
    def column_name(self):
        r"""Gets the column_name of this IsapTableColumnDisplaySettingDto.

        表格列名称

        :return: The column_name of this IsapTableColumnDisplaySettingDto.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this IsapTableColumnDisplaySettingDto.

        表格列名称

        :param column_name: The column_name of this IsapTableColumnDisplaySettingDto.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_alias(self):
        r"""Gets the column_alias of this IsapTableColumnDisplaySettingDto.

        表格列别名

        :return: The column_alias of this IsapTableColumnDisplaySettingDto.
        :rtype: str
        """
        return self._column_alias

    @column_alias.setter
    def column_alias(self, column_alias):
        r"""Sets the column_alias of this IsapTableColumnDisplaySettingDto.

        表格列别名

        :param column_alias: The column_alias of this IsapTableColumnDisplaySettingDto.
        :type column_alias: str
        """
        self._column_alias = column_alias

    @property
    def column_alias_en(self):
        r"""Gets the column_alias_en of this IsapTableColumnDisplaySettingDto.

        表格列别名

        :return: The column_alias_en of this IsapTableColumnDisplaySettingDto.
        :rtype: str
        """
        return self._column_alias_en

    @column_alias_en.setter
    def column_alias_en(self, column_alias_en):
        r"""Sets the column_alias_en of this IsapTableColumnDisplaySettingDto.

        表格列别名

        :param column_alias_en: The column_alias_en of this IsapTableColumnDisplaySettingDto.
        :type column_alias_en: str
        """
        self._column_alias_en = column_alias_en

    @property
    def display_by_default(self):
        r"""Gets the display_by_default of this IsapTableColumnDisplaySettingDto.

        是否默认展示

        :return: The display_by_default of this IsapTableColumnDisplaySettingDto.
        :rtype: bool
        """
        return self._display_by_default

    @display_by_default.setter
    def display_by_default(self, display_by_default):
        r"""Sets the display_by_default of this IsapTableColumnDisplaySettingDto.

        是否默认展示

        :param display_by_default: The display_by_default of this IsapTableColumnDisplaySettingDto.
        :type display_by_default: bool
        """
        self._display_by_default = display_by_default

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
        if not isinstance(other, IsapTableColumnDisplaySettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
