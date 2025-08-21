# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnLineageConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'input_columns': 'list[ColumnConfig]',
        'output_column': 'ColumnConfig'
    }

    attribute_map = {
        'name': 'name',
        'input_columns': 'input_columns',
        'output_column': 'output_column'
    }

    def __init__(self, name=None, input_columns=None, output_column=None):
        r"""ColumnLineageConfig

        The model defined in huaweicloud sdk

        :param name: 字段血缘节点名称。
        :type name: str
        :param input_columns: 输入字段血缘信息。
        :type input_columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnConfig`]
        :param output_column: 
        :type output_column: :class:`huaweicloudsdkdataartsstudio.v1.ColumnConfig`
        """
        
        

        self._name = None
        self._input_columns = None
        self._output_column = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.input_columns = input_columns
        self.output_column = output_column

    @property
    def name(self):
        r"""Gets the name of this ColumnLineageConfig.

        字段血缘节点名称。

        :return: The name of this ColumnLineageConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ColumnLineageConfig.

        字段血缘节点名称。

        :param name: The name of this ColumnLineageConfig.
        :type name: str
        """
        self._name = name

    @property
    def input_columns(self):
        r"""Gets the input_columns of this ColumnLineageConfig.

        输入字段血缘信息。

        :return: The input_columns of this ColumnLineageConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnConfig`]
        """
        return self._input_columns

    @input_columns.setter
    def input_columns(self, input_columns):
        r"""Sets the input_columns of this ColumnLineageConfig.

        输入字段血缘信息。

        :param input_columns: The input_columns of this ColumnLineageConfig.
        :type input_columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnConfig`]
        """
        self._input_columns = input_columns

    @property
    def output_column(self):
        r"""Gets the output_column of this ColumnLineageConfig.

        :return: The output_column of this ColumnLineageConfig.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ColumnConfig`
        """
        return self._output_column

    @output_column.setter
    def output_column(self, output_column):
        r"""Sets the output_column of this ColumnLineageConfig.

        :param output_column: The output_column of this ColumnLineageConfig.
        :type output_column: :class:`huaweicloudsdkdataartsstudio.v1.ColumnConfig`
        """
        self._output_column = output_column

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
        if not isinstance(other, ColumnLineageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
