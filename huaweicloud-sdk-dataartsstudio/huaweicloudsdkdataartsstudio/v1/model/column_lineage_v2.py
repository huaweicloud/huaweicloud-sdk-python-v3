# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnLineageV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_columns': 'list[ColumnDetails]',
        'output_columns': 'list[ColumnDetails]'
    }

    attribute_map = {
        'input_columns': 'input_columns',
        'output_columns': 'output_columns'
    }

    def __init__(self, input_columns=None, output_columns=None):
        r"""ColumnLineageV2

        The model defined in huaweicloud sdk

        :param input_columns: 上游血缘字段列表，列表大小：1至100
        :type input_columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnDetails`]
        :param output_columns: 下游血缘字段列表，列表大小：1至100
        :type output_columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnDetails`]
        """
        
        

        self._input_columns = None
        self._output_columns = None
        self.discriminator = None

        self.input_columns = input_columns
        self.output_columns = output_columns

    @property
    def input_columns(self):
        r"""Gets the input_columns of this ColumnLineageV2.

        上游血缘字段列表，列表大小：1至100

        :return: The input_columns of this ColumnLineageV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnDetails`]
        """
        return self._input_columns

    @input_columns.setter
    def input_columns(self, input_columns):
        r"""Sets the input_columns of this ColumnLineageV2.

        上游血缘字段列表，列表大小：1至100

        :param input_columns: The input_columns of this ColumnLineageV2.
        :type input_columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnDetails`]
        """
        self._input_columns = input_columns

    @property
    def output_columns(self):
        r"""Gets the output_columns of this ColumnLineageV2.

        下游血缘字段列表，列表大小：1至100

        :return: The output_columns of this ColumnLineageV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnDetails`]
        """
        return self._output_columns

    @output_columns.setter
    def output_columns(self, output_columns):
        r"""Sets the output_columns of this ColumnLineageV2.

        下游血缘字段列表，列表大小：1至100

        :param output_columns: The output_columns of this ColumnLineageV2.
        :type output_columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnDetails`]
        """
        self._output_columns = output_columns

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
        if not isinstance(other, ColumnLineageV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
