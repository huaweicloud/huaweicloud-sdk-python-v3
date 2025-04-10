# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityNoMaskingTableResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'tables': 'list[DiagnoseNoMaskingDetail]'
    }

    attribute_map = {
        'total': 'total',
        'tables': 'tables'
    }

    def __init__(self, total=None, tables=None):
        r"""ShowSecurityNoMaskingTableResultResponse

        The model defined in huaweicloud sdk

        :param total: 表总数
        :type total: int
        :param tables: 查询的表集合
        :type tables: list[:class:`huaweicloudsdkdataartsstudio.v1.DiagnoseNoMaskingDetail`]
        """
        
        super(ShowSecurityNoMaskingTableResultResponse, self).__init__()

        self._total = None
        self._tables = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if tables is not None:
            self.tables = tables

    @property
    def total(self):
        r"""Gets the total of this ShowSecurityNoMaskingTableResultResponse.

        表总数

        :return: The total of this ShowSecurityNoMaskingTableResultResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowSecurityNoMaskingTableResultResponse.

        表总数

        :param total: The total of this ShowSecurityNoMaskingTableResultResponse.
        :type total: int
        """
        self._total = total

    @property
    def tables(self):
        r"""Gets the tables of this ShowSecurityNoMaskingTableResultResponse.

        查询的表集合

        :return: The tables of this ShowSecurityNoMaskingTableResultResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DiagnoseNoMaskingDetail`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this ShowSecurityNoMaskingTableResultResponse.

        查询的表集合

        :param tables: The tables of this ShowSecurityNoMaskingTableResultResponse.
        :type tables: list[:class:`huaweicloudsdkdataartsstudio.v1.DiagnoseNoMaskingDetail`]
        """
        self._tables = tables

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
        if not isinstance(other, ShowSecurityNoMaskingTableResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
