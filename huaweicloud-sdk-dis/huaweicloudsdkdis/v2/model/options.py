# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Options:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fill_missing_fields': 'str',
        'ignore_extra_data': 'str',
        'compatible_illegal_chars': 'str',
        'reject_limit': 'str',
        'error_table_name': 'str'
    }

    attribute_map = {
        'fill_missing_fields': 'fill_missing_fields',
        'ignore_extra_data': 'ignore_extra_data',
        'compatible_illegal_chars': 'compatible_illegal_chars',
        'reject_limit': 'reject_limit',
        'error_table_name': 'error_table_name'
    }

    def __init__(self, fill_missing_fields=None, ignore_extra_data=None, compatible_illegal_chars=None, reject_limit=None, error_table_name=None):
        r"""Options

        The model defined in huaweicloud sdk

        :param fill_missing_fields: 数据入库时，数据源文件中某行的最后一个字段缺失时，请选择是直接将字段设为Null，还是在错误表中报错提示。  取值范围：   - true/on - false/off  缺省值：false/off
        :type fill_missing_fields: str
        :param ignore_extra_data: 数据源文件中的字段比外表定义列数多时，是否忽略多出的列。该参数只在数据导入过程中使用。  取值范围：  - true/on - false/off  缺省值：false/off
        :type ignore_extra_data: str
        :param compatible_illegal_chars: 导入非法字符容错参数。是将非法字符按照转换规则转换后入库，还是报错中止导入。  取值范围：  - true/on - false/off  缺省值：false/off
        :type compatible_illegal_chars: str
        :param reject_limit: 指定本次数据导入允许出现的数据格式错误个数，当导入过程中出现的数据格式错误未达到限定值时，本次数据导入可以成功。  取值范围：  - 整型值 - unlimited（无限制）  缺省值为0，有错误信息立即返回。
        :type reject_limit: str
        :param error_table_name: 用于记录数据格式错误信息的错误表表名。并行导入结束后查询此错误信息表，能够获取详细的错误信息。
        :type error_table_name: str
        """
        
        

        self._fill_missing_fields = None
        self._ignore_extra_data = None
        self._compatible_illegal_chars = None
        self._reject_limit = None
        self._error_table_name = None
        self.discriminator = None

        if fill_missing_fields is not None:
            self.fill_missing_fields = fill_missing_fields
        if ignore_extra_data is not None:
            self.ignore_extra_data = ignore_extra_data
        if compatible_illegal_chars is not None:
            self.compatible_illegal_chars = compatible_illegal_chars
        if reject_limit is not None:
            self.reject_limit = reject_limit
        if error_table_name is not None:
            self.error_table_name = error_table_name

    @property
    def fill_missing_fields(self):
        r"""Gets the fill_missing_fields of this Options.

        数据入库时，数据源文件中某行的最后一个字段缺失时，请选择是直接将字段设为Null，还是在错误表中报错提示。  取值范围：   - true/on - false/off  缺省值：false/off

        :return: The fill_missing_fields of this Options.
        :rtype: str
        """
        return self._fill_missing_fields

    @fill_missing_fields.setter
    def fill_missing_fields(self, fill_missing_fields):
        r"""Sets the fill_missing_fields of this Options.

        数据入库时，数据源文件中某行的最后一个字段缺失时，请选择是直接将字段设为Null，还是在错误表中报错提示。  取值范围：   - true/on - false/off  缺省值：false/off

        :param fill_missing_fields: The fill_missing_fields of this Options.
        :type fill_missing_fields: str
        """
        self._fill_missing_fields = fill_missing_fields

    @property
    def ignore_extra_data(self):
        r"""Gets the ignore_extra_data of this Options.

        数据源文件中的字段比外表定义列数多时，是否忽略多出的列。该参数只在数据导入过程中使用。  取值范围：  - true/on - false/off  缺省值：false/off

        :return: The ignore_extra_data of this Options.
        :rtype: str
        """
        return self._ignore_extra_data

    @ignore_extra_data.setter
    def ignore_extra_data(self, ignore_extra_data):
        r"""Sets the ignore_extra_data of this Options.

        数据源文件中的字段比外表定义列数多时，是否忽略多出的列。该参数只在数据导入过程中使用。  取值范围：  - true/on - false/off  缺省值：false/off

        :param ignore_extra_data: The ignore_extra_data of this Options.
        :type ignore_extra_data: str
        """
        self._ignore_extra_data = ignore_extra_data

    @property
    def compatible_illegal_chars(self):
        r"""Gets the compatible_illegal_chars of this Options.

        导入非法字符容错参数。是将非法字符按照转换规则转换后入库，还是报错中止导入。  取值范围：  - true/on - false/off  缺省值：false/off

        :return: The compatible_illegal_chars of this Options.
        :rtype: str
        """
        return self._compatible_illegal_chars

    @compatible_illegal_chars.setter
    def compatible_illegal_chars(self, compatible_illegal_chars):
        r"""Sets the compatible_illegal_chars of this Options.

        导入非法字符容错参数。是将非法字符按照转换规则转换后入库，还是报错中止导入。  取值范围：  - true/on - false/off  缺省值：false/off

        :param compatible_illegal_chars: The compatible_illegal_chars of this Options.
        :type compatible_illegal_chars: str
        """
        self._compatible_illegal_chars = compatible_illegal_chars

    @property
    def reject_limit(self):
        r"""Gets the reject_limit of this Options.

        指定本次数据导入允许出现的数据格式错误个数，当导入过程中出现的数据格式错误未达到限定值时，本次数据导入可以成功。  取值范围：  - 整型值 - unlimited（无限制）  缺省值为0，有错误信息立即返回。

        :return: The reject_limit of this Options.
        :rtype: str
        """
        return self._reject_limit

    @reject_limit.setter
    def reject_limit(self, reject_limit):
        r"""Sets the reject_limit of this Options.

        指定本次数据导入允许出现的数据格式错误个数，当导入过程中出现的数据格式错误未达到限定值时，本次数据导入可以成功。  取值范围：  - 整型值 - unlimited（无限制）  缺省值为0，有错误信息立即返回。

        :param reject_limit: The reject_limit of this Options.
        :type reject_limit: str
        """
        self._reject_limit = reject_limit

    @property
    def error_table_name(self):
        r"""Gets the error_table_name of this Options.

        用于记录数据格式错误信息的错误表表名。并行导入结束后查询此错误信息表，能够获取详细的错误信息。

        :return: The error_table_name of this Options.
        :rtype: str
        """
        return self._error_table_name

    @error_table_name.setter
    def error_table_name(self, error_table_name):
        r"""Sets the error_table_name of this Options.

        用于记录数据格式错误信息的错误表表名。并行导入结束后查询此错误信息表，能够获取详细的错误信息。

        :param error_table_name: The error_table_name of this Options.
        :type error_table_name: str
        """
        self._error_table_name = error_table_name

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
        if not isinstance(other, Options):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
