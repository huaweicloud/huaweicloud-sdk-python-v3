# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigHistoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'history_num': 'int',
        'histories': 'list[HistoryInfo]'
    }

    attribute_map = {
        'history_num': 'history_num',
        'histories': 'histories'
    }

    def __init__(self, history_num=None, histories=None):
        r"""ListConfigHistoriesResponse

        The model defined in huaweicloud sdk

        :param history_num: 实例参数修改记录个数
        :type history_num: int
        :param histories: 实力参数修改记录详情
        :type histories: list[:class:`huaweicloudsdkdcs.v2.HistoryInfo`]
        """
        
        super(ListConfigHistoriesResponse, self).__init__()

        self._history_num = None
        self._histories = None
        self.discriminator = None

        if history_num is not None:
            self.history_num = history_num
        if histories is not None:
            self.histories = histories

    @property
    def history_num(self):
        r"""Gets the history_num of this ListConfigHistoriesResponse.

        实例参数修改记录个数

        :return: The history_num of this ListConfigHistoriesResponse.
        :rtype: int
        """
        return self._history_num

    @history_num.setter
    def history_num(self, history_num):
        r"""Sets the history_num of this ListConfigHistoriesResponse.

        实例参数修改记录个数

        :param history_num: The history_num of this ListConfigHistoriesResponse.
        :type history_num: int
        """
        self._history_num = history_num

    @property
    def histories(self):
        r"""Gets the histories of this ListConfigHistoriesResponse.

        实力参数修改记录详情

        :return: The histories of this ListConfigHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.HistoryInfo`]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        r"""Sets the histories of this ListConfigHistoriesResponse.

        实力参数修改记录详情

        :param histories: The histories of this ListConfigHistoriesResponse.
        :type histories: list[:class:`huaweicloudsdkdcs.v2.HistoryInfo`]
        """
        self._histories = histories

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
        if not isinstance(other, ListConfigHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
