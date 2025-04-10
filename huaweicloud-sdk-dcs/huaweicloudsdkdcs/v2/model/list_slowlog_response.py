# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowlogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'count': 'int',
        'slowlogs': 'list[SlowlogItem]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'count': 'count',
        'slowlogs': 'slowlogs'
    }

    def __init__(self, total_num=None, count=None, slowlogs=None):
        r"""ListSlowlogResponse

        The model defined in huaweicloud sdk

        :param total_num: 慢日志总条数
        :type total_num: int
        :param count: 总数
        :type count: int
        :param slowlogs: 慢日志列表
        :type slowlogs: list[:class:`huaweicloudsdkdcs.v2.SlowlogItem`]
        """
        
        super(ListSlowlogResponse, self).__init__()

        self._total_num = None
        self._count = None
        self._slowlogs = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if count is not None:
            self.count = count
        if slowlogs is not None:
            self.slowlogs = slowlogs

    @property
    def total_num(self):
        r"""Gets the total_num of this ListSlowlogResponse.

        慢日志总条数

        :return: The total_num of this ListSlowlogResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListSlowlogResponse.

        慢日志总条数

        :param total_num: The total_num of this ListSlowlogResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def count(self):
        r"""Gets the count of this ListSlowlogResponse.

        总数

        :return: The count of this ListSlowlogResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSlowlogResponse.

        总数

        :param count: The count of this ListSlowlogResponse.
        :type count: int
        """
        self._count = count

    @property
    def slowlogs(self):
        r"""Gets the slowlogs of this ListSlowlogResponse.

        慢日志列表

        :return: The slowlogs of this ListSlowlogResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.SlowlogItem`]
        """
        return self._slowlogs

    @slowlogs.setter
    def slowlogs(self, slowlogs):
        r"""Sets the slowlogs of this ListSlowlogResponse.

        慢日志列表

        :param slowlogs: The slowlogs of this ListSlowlogResponse.
        :type slowlogs: list[:class:`huaweicloudsdkdcs.v2.SlowlogItem`]
        """
        self._slowlogs = slowlogs

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
        if not isinstance(other, ListSlowlogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
