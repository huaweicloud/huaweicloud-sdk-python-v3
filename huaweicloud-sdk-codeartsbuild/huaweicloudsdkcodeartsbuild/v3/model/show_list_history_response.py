# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowListHistoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'history_records': 'list[HistoryRecord]',
        'total': 'int'
    }

    attribute_map = {
        'history_records': 'history_records',
        'total': 'total'
    }

    def __init__(self, history_records=None, total=None):
        """ShowListHistoryResponse

        The model defined in huaweicloud sdk

        :param history_records: 构建历史列表
        :type history_records: list[:class:`huaweicloudsdkcodeartsbuild.v3.HistoryRecord`]
        :param total: 记录总数
        :type total: int
        """
        
        super(ShowListHistoryResponse, self).__init__()

        self._history_records = None
        self._total = None
        self.discriminator = None

        if history_records is not None:
            self.history_records = history_records
        if total is not None:
            self.total = total

    @property
    def history_records(self):
        """Gets the history_records of this ShowListHistoryResponse.

        构建历史列表

        :return: The history_records of this ShowListHistoryResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.HistoryRecord`]
        """
        return self._history_records

    @history_records.setter
    def history_records(self, history_records):
        """Sets the history_records of this ShowListHistoryResponse.

        构建历史列表

        :param history_records: The history_records of this ShowListHistoryResponse.
        :type history_records: list[:class:`huaweicloudsdkcodeartsbuild.v3.HistoryRecord`]
        """
        self._history_records = history_records

    @property
    def total(self):
        """Gets the total of this ShowListHistoryResponse.

        记录总数

        :return: The total of this ShowListHistoryResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowListHistoryResponse.

        记录总数

        :param total: The total of this ShowListHistoryResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ShowListHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
