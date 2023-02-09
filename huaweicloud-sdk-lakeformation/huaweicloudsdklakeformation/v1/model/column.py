# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Column:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_type': 'str',
        'column_name': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'column_type': 'column_type',
        'column_name': 'column_name',
        'comment': 'comment'
    }

    def __init__(self, column_type=None, column_name=None, comment=None):
        """Column

        The model defined in huaweicloud sdk

        :param column_type: 列类型，包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar
        :type column_type: str
        :param column_name: 列名
        :type column_name: str
        :param comment: 列描述信息
        :type comment: str
        """
        
        

        self._column_type = None
        self._column_name = None
        self._comment = None
        self.discriminator = None

        self.column_type = column_type
        self.column_name = column_name
        if comment is not None:
            self.comment = comment

    @property
    def column_type(self):
        """Gets the column_type of this Column.

        列类型，包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar

        :return: The column_type of this Column.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this Column.

        列类型，包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar

        :param column_type: The column_type of this Column.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def column_name(self):
        """Gets the column_name of this Column.

        列名

        :return: The column_name of this Column.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this Column.

        列名

        :param column_name: The column_name of this Column.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def comment(self):
        """Gets the comment of this Column.

        列描述信息

        :return: The comment of this Column.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Column.

        列描述信息

        :param comment: The comment of this Column.
        :type comment: str
        """
        self._comment = comment

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
        if not isinstance(other, Column):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
