# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemUserWhiteListResponse(SdkResponse):

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
        'remain_num': 'int',
        'limit_num': 'int',
        'data_list': 'list[SystemUserWhiteListResponseInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'remain_num': 'remain_num',
        'limit_num': 'limit_num',
        'data_list': 'data_list'
    }

    def __init__(self, total_num=None, remain_num=None, limit_num=None, data_list=None):
        r"""ListSystemUserWhiteListResponse

        The model defined in huaweicloud sdk

        :param total_num: **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        :param remain_num: 可继续添加的白名单数量
        :type remain_num: int
        :param limit_num: 白名单数量上限
        :type limit_num: int
        :param data_list: 系统用户白名单详情
        :type data_list: list[:class:`huaweicloudsdkhss.v5.SystemUserWhiteListResponseInfo`]
        """
        
        super(ListSystemUserWhiteListResponse, self).__init__()

        self._total_num = None
        self._remain_num = None
        self._limit_num = None
        self._data_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if remain_num is not None:
            self.remain_num = remain_num
        if limit_num is not None:
            self.limit_num = limit_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListSystemUserWhiteListResponse.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this ListSystemUserWhiteListResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListSystemUserWhiteListResponse.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this ListSystemUserWhiteListResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def remain_num(self):
        r"""Gets the remain_num of this ListSystemUserWhiteListResponse.

        可继续添加的白名单数量

        :return: The remain_num of this ListSystemUserWhiteListResponse.
        :rtype: int
        """
        return self._remain_num

    @remain_num.setter
    def remain_num(self, remain_num):
        r"""Sets the remain_num of this ListSystemUserWhiteListResponse.

        可继续添加的白名单数量

        :param remain_num: The remain_num of this ListSystemUserWhiteListResponse.
        :type remain_num: int
        """
        self._remain_num = remain_num

    @property
    def limit_num(self):
        r"""Gets the limit_num of this ListSystemUserWhiteListResponse.

        白名单数量上限

        :return: The limit_num of this ListSystemUserWhiteListResponse.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        r"""Sets the limit_num of this ListSystemUserWhiteListResponse.

        白名单数量上限

        :param limit_num: The limit_num of this ListSystemUserWhiteListResponse.
        :type limit_num: int
        """
        self._limit_num = limit_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListSystemUserWhiteListResponse.

        系统用户白名单详情

        :return: The data_list of this ListSystemUserWhiteListResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SystemUserWhiteListResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListSystemUserWhiteListResponse.

        系统用户白名单详情

        :param data_list: The data_list of this ListSystemUserWhiteListResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.SystemUserWhiteListResponseInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListSystemUserWhiteListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
