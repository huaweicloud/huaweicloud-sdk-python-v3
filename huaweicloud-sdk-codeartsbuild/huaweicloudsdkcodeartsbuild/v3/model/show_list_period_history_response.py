# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowListPeriodHistoryResponse(SdkResponse):

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
        'history_records': 'list[HistoryRecord1]'
    }

    attribute_map = {
        'total': 'total',
        'history_records': 'history_records'
    }

    def __init__(self, total=None, history_records=None):
        r"""ShowListPeriodHistoryResponse

        The model defined in huaweicloud sdk

        :param total: 记录总数
        :type total: int
        :param history_records: 构建历史列表
        :type history_records: list[:class:`huaweicloudsdkcodeartsbuild.v3.HistoryRecord1`]
        """
        
        super(ShowListPeriodHistoryResponse, self).__init__()

        self._total = None
        self._history_records = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if history_records is not None:
            self.history_records = history_records

    @property
    def total(self):
        r"""Gets the total of this ShowListPeriodHistoryResponse.

        记录总数

        :return: The total of this ShowListPeriodHistoryResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowListPeriodHistoryResponse.

        记录总数

        :param total: The total of this ShowListPeriodHistoryResponse.
        :type total: int
        """
        self._total = total

    @property
    def history_records(self):
        r"""Gets the history_records of this ShowListPeriodHistoryResponse.

        构建历史列表

        :return: The history_records of this ShowListPeriodHistoryResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.HistoryRecord1`]
        """
        return self._history_records

    @history_records.setter
    def history_records(self, history_records):
        r"""Sets the history_records of this ShowListPeriodHistoryResponse.

        构建历史列表

        :param history_records: The history_records of this ShowListPeriodHistoryResponse.
        :type history_records: list[:class:`huaweicloudsdkcodeartsbuild.v3.HistoryRecord1`]
        """
        self._history_records = history_records

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
        if not isinstance(other, ShowListPeriodHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
