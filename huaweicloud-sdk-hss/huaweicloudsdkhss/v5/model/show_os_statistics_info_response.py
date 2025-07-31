# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOsStatisticsInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'win_num': 'int',
        'linux_num': 'int',
        'os_list': 'list[OsStatisticsInfo]'
    }

    attribute_map = {
        'win_num': 'win_num',
        'linux_num': 'linux_num',
        'os_list': 'os_list'
    }

    def __init__(self, win_num=None, linux_num=None, os_list=None):
        r"""ShowOsStatisticsInfoResponse

        The model defined in huaweicloud sdk

        :param win_num: win_num
        :type win_num: int
        :param linux_num: linux_num
        :type linux_num: int
        :param os_list: 操作系统统计数据列表
        :type os_list: list[:class:`huaweicloudsdkhss.v5.OsStatisticsInfo`]
        """
        
        super(ShowOsStatisticsInfoResponse, self).__init__()

        self._win_num = None
        self._linux_num = None
        self._os_list = None
        self.discriminator = None

        if win_num is not None:
            self.win_num = win_num
        if linux_num is not None:
            self.linux_num = linux_num
        if os_list is not None:
            self.os_list = os_list

    @property
    def win_num(self):
        r"""Gets the win_num of this ShowOsStatisticsInfoResponse.

        win_num

        :return: The win_num of this ShowOsStatisticsInfoResponse.
        :rtype: int
        """
        return self._win_num

    @win_num.setter
    def win_num(self, win_num):
        r"""Sets the win_num of this ShowOsStatisticsInfoResponse.

        win_num

        :param win_num: The win_num of this ShowOsStatisticsInfoResponse.
        :type win_num: int
        """
        self._win_num = win_num

    @property
    def linux_num(self):
        r"""Gets the linux_num of this ShowOsStatisticsInfoResponse.

        linux_num

        :return: The linux_num of this ShowOsStatisticsInfoResponse.
        :rtype: int
        """
        return self._linux_num

    @linux_num.setter
    def linux_num(self, linux_num):
        r"""Sets the linux_num of this ShowOsStatisticsInfoResponse.

        linux_num

        :param linux_num: The linux_num of this ShowOsStatisticsInfoResponse.
        :type linux_num: int
        """
        self._linux_num = linux_num

    @property
    def os_list(self):
        r"""Gets the os_list of this ShowOsStatisticsInfoResponse.

        操作系统统计数据列表

        :return: The os_list of this ShowOsStatisticsInfoResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.OsStatisticsInfo`]
        """
        return self._os_list

    @os_list.setter
    def os_list(self, os_list):
        r"""Sets the os_list of this ShowOsStatisticsInfoResponse.

        操作系统统计数据列表

        :param os_list: The os_list of this ShowOsStatisticsInfoResponse.
        :type os_list: list[:class:`huaweicloudsdkhss.v5.OsStatisticsInfo`]
        """
        self._os_list = os_list

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
        if not isinstance(other, ShowOsStatisticsInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
