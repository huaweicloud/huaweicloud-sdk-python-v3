# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataCompareDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'table_line_compare_result_infos': 'list[TableLineCompareResultInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'table_line_compare_result_infos': 'table_line_compare_result_infos'
    }

    def __init__(self, total_count=None, table_line_compare_result_infos=None):
        r"""ListDataCompareDetailResponse

        The model defined in huaweicloud sdk

        :param total_count: 对比数量
        :type total_count: int
        :param table_line_compare_result_infos: 对比信息列表
        :type table_line_compare_result_infos: list[:class:`huaweicloudsdkdrs.v3.TableLineCompareResultInfo`]
        """
        
        super(ListDataCompareDetailResponse, self).__init__()

        self._total_count = None
        self._table_line_compare_result_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if table_line_compare_result_infos is not None:
            self.table_line_compare_result_infos = table_line_compare_result_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDataCompareDetailResponse.

        对比数量

        :return: The total_count of this ListDataCompareDetailResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDataCompareDetailResponse.

        对比数量

        :param total_count: The total_count of this ListDataCompareDetailResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def table_line_compare_result_infos(self):
        r"""Gets the table_line_compare_result_infos of this ListDataCompareDetailResponse.

        对比信息列表

        :return: The table_line_compare_result_infos of this ListDataCompareDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.TableLineCompareResultInfo`]
        """
        return self._table_line_compare_result_infos

    @table_line_compare_result_infos.setter
    def table_line_compare_result_infos(self, table_line_compare_result_infos):
        r"""Sets the table_line_compare_result_infos of this ListDataCompareDetailResponse.

        对比信息列表

        :param table_line_compare_result_infos: The table_line_compare_result_infos of this ListDataCompareDetailResponse.
        :type table_line_compare_result_infos: list[:class:`huaweicloudsdkdrs.v3.TableLineCompareResultInfo`]
        """
        self._table_line_compare_result_infos = table_line_compare_result_infos

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
        if not isinstance(other, ListDataCompareDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
