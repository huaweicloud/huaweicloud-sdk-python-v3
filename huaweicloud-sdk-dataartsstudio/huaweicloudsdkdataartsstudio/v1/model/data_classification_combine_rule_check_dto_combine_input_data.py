# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationCombineRuleCheckDTOCombineInputData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_content': 'str',
        'column_name': 'str',
        'column_comment': 'str',
        'table_comment': 'str',
        'table_name': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'column_content': 'column_content',
        'column_name': 'column_name',
        'column_comment': 'column_comment',
        'table_comment': 'table_comment',
        'table_name': 'table_name',
        'database_name': 'database_name'
    }

    def __init__(self, column_content=None, column_name=None, column_comment=None, table_comment=None, table_name=None, database_name=None):
        r"""DataClassificationCombineRuleCheckDTOCombineInputData

        The model defined in huaweicloud sdk

        :param column_content: 字段内容模拟数据
        :type column_content: str
        :param column_name: 列名模拟数据
        :type column_name: str
        :param column_comment: 列注释模拟数据
        :type column_comment: str
        :param table_comment: 表注释模拟数据
        :type table_comment: str
        :param table_name: 表名模拟数据
        :type table_name: str
        :param database_name: 库名模拟数据
        :type database_name: str
        """
        
        

        self._column_content = None
        self._column_name = None
        self._column_comment = None
        self._table_comment = None
        self._table_name = None
        self._database_name = None
        self.discriminator = None

        if column_content is not None:
            self.column_content = column_content
        if column_name is not None:
            self.column_name = column_name
        if column_comment is not None:
            self.column_comment = column_comment
        if table_comment is not None:
            self.table_comment = table_comment
        if table_name is not None:
            self.table_name = table_name
        if database_name is not None:
            self.database_name = database_name

    @property
    def column_content(self):
        r"""Gets the column_content of this DataClassificationCombineRuleCheckDTOCombineInputData.

        字段内容模拟数据

        :return: The column_content of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :rtype: str
        """
        return self._column_content

    @column_content.setter
    def column_content(self, column_content):
        r"""Sets the column_content of this DataClassificationCombineRuleCheckDTOCombineInputData.

        字段内容模拟数据

        :param column_content: The column_content of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :type column_content: str
        """
        self._column_content = column_content

    @property
    def column_name(self):
        r"""Gets the column_name of this DataClassificationCombineRuleCheckDTOCombineInputData.

        列名模拟数据

        :return: The column_name of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this DataClassificationCombineRuleCheckDTOCombineInputData.

        列名模拟数据

        :param column_name: The column_name of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_comment(self):
        r"""Gets the column_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.

        列注释模拟数据

        :return: The column_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :rtype: str
        """
        return self._column_comment

    @column_comment.setter
    def column_comment(self, column_comment):
        r"""Sets the column_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.

        列注释模拟数据

        :param column_comment: The column_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :type column_comment: str
        """
        self._column_comment = column_comment

    @property
    def table_comment(self):
        r"""Gets the table_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.

        表注释模拟数据

        :return: The table_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :rtype: str
        """
        return self._table_comment

    @table_comment.setter
    def table_comment(self, table_comment):
        r"""Sets the table_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.

        表注释模拟数据

        :param table_comment: The table_comment of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :type table_comment: str
        """
        self._table_comment = table_comment

    @property
    def table_name(self):
        r"""Gets the table_name of this DataClassificationCombineRuleCheckDTOCombineInputData.

        表名模拟数据

        :return: The table_name of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DataClassificationCombineRuleCheckDTOCombineInputData.

        表名模拟数据

        :param table_name: The table_name of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def database_name(self):
        r"""Gets the database_name of this DataClassificationCombineRuleCheckDTOCombineInputData.

        库名模拟数据

        :return: The database_name of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DataClassificationCombineRuleCheckDTOCombineInputData.

        库名模拟数据

        :param database_name: The database_name of this DataClassificationCombineRuleCheckDTOCombineInputData.
        :type database_name: str
        """
        self._database_name = database_name

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
        if not isinstance(other, DataClassificationCombineRuleCheckDTOCombineInputData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
