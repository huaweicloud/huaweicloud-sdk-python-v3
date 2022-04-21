# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportdetailItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'custom_transactions': 'list[str]',
        'detail_datas': 'list[DetailDataInfo]',
        'performance': 'PerformanceInfo'
    }

    attribute_map = {
        'custom_transactions': 'customTransactions',
        'detail_datas': 'detailDatas',
        'performance': 'performance'
    }

    def __init__(self, custom_transactions=None, detail_datas=None, performance=None):
        """ReportdetailItemInfo

        The model defined in huaweicloud sdk

        :param custom_transactions: 自定义事务数据
        :type custom_transactions: list[str]
        :param detail_datas: aw数据
        :type detail_datas: list[:class:`huaweicloudsdkcpts.v1.DetailDataInfo`]
        :param performance: 
        :type performance: :class:`huaweicloudsdkcpts.v1.PerformanceInfo`
        """
        
        

        self._custom_transactions = None
        self._detail_datas = None
        self._performance = None
        self.discriminator = None

        if custom_transactions is not None:
            self.custom_transactions = custom_transactions
        if detail_datas is not None:
            self.detail_datas = detail_datas
        if performance is not None:
            self.performance = performance

    @property
    def custom_transactions(self):
        """Gets the custom_transactions of this ReportdetailItemInfo.

        自定义事务数据

        :return: The custom_transactions of this ReportdetailItemInfo.
        :rtype: list[str]
        """
        return self._custom_transactions

    @custom_transactions.setter
    def custom_transactions(self, custom_transactions):
        """Sets the custom_transactions of this ReportdetailItemInfo.

        自定义事务数据

        :param custom_transactions: The custom_transactions of this ReportdetailItemInfo.
        :type custom_transactions: list[str]
        """
        self._custom_transactions = custom_transactions

    @property
    def detail_datas(self):
        """Gets the detail_datas of this ReportdetailItemInfo.

        aw数据

        :return: The detail_datas of this ReportdetailItemInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.DetailDataInfo`]
        """
        return self._detail_datas

    @detail_datas.setter
    def detail_datas(self, detail_datas):
        """Sets the detail_datas of this ReportdetailItemInfo.

        aw数据

        :param detail_datas: The detail_datas of this ReportdetailItemInfo.
        :type detail_datas: list[:class:`huaweicloudsdkcpts.v1.DetailDataInfo`]
        """
        self._detail_datas = detail_datas

    @property
    def performance(self):
        """Gets the performance of this ReportdetailItemInfo.


        :return: The performance of this ReportdetailItemInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.PerformanceInfo`
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this ReportdetailItemInfo.


        :param performance: The performance of this ReportdetailItemInfo.
        :type performance: :class:`huaweicloudsdkcpts.v1.PerformanceInfo`
        """
        self._performance = performance

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
        if not isinstance(other, ReportdetailItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
