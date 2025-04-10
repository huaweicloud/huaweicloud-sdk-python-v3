# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableLineageV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_tables': 'list[TableInfoV2]',
        'output_tables': 'list[TableInfoV2]',
        'column_lineages': 'list[ColumnLineageV2]'
    }

    attribute_map = {
        'input_tables': 'input_tables',
        'output_tables': 'output_tables',
        'column_lineages': 'column_lineages'
    }

    def __init__(self, input_tables=None, output_tables=None, column_lineages=None):
        r"""TableLineageV2

        The model defined in huaweicloud sdk

        :param input_tables: 上游血缘表列表，列表大小：1至100
        :type input_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfoV2`]
        :param output_tables: 下游血缘表列表，列表大小：1至100
        :type output_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfoV2`]
        :param column_lineages: 字段血缘列表，列表大小：0至100
        :type column_lineages: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineageV2`]
        """
        
        

        self._input_tables = None
        self._output_tables = None
        self._column_lineages = None
        self.discriminator = None

        self.input_tables = input_tables
        self.output_tables = output_tables
        if column_lineages is not None:
            self.column_lineages = column_lineages

    @property
    def input_tables(self):
        r"""Gets the input_tables of this TableLineageV2.

        上游血缘表列表，列表大小：1至100

        :return: The input_tables of this TableLineageV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfoV2`]
        """
        return self._input_tables

    @input_tables.setter
    def input_tables(self, input_tables):
        r"""Sets the input_tables of this TableLineageV2.

        上游血缘表列表，列表大小：1至100

        :param input_tables: The input_tables of this TableLineageV2.
        :type input_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfoV2`]
        """
        self._input_tables = input_tables

    @property
    def output_tables(self):
        r"""Gets the output_tables of this TableLineageV2.

        下游血缘表列表，列表大小：1至100

        :return: The output_tables of this TableLineageV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfoV2`]
        """
        return self._output_tables

    @output_tables.setter
    def output_tables(self, output_tables):
        r"""Sets the output_tables of this TableLineageV2.

        下游血缘表列表，列表大小：1至100

        :param output_tables: The output_tables of this TableLineageV2.
        :type output_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfoV2`]
        """
        self._output_tables = output_tables

    @property
    def column_lineages(self):
        r"""Gets the column_lineages of this TableLineageV2.

        字段血缘列表，列表大小：0至100

        :return: The column_lineages of this TableLineageV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineageV2`]
        """
        return self._column_lineages

    @column_lineages.setter
    def column_lineages(self, column_lineages):
        r"""Sets the column_lineages of this TableLineageV2.

        字段血缘列表，列表大小：0至100

        :param column_lineages: The column_lineages of this TableLineageV2.
        :type column_lineages: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineageV2`]
        """
        self._column_lineages = column_lineages

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
        if not isinstance(other, TableLineageV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
