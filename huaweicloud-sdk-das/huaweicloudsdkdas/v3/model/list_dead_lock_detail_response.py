# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeadLockDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail_list': 'list[DeadLockDetail]',
        'total': 'int'
    }

    attribute_map = {
        'detail_list': 'detail_list',
        'total': 'total'
    }

    def __init__(self, detail_list=None, total=None):
        r"""ListDeadLockDetailResponse

        The model defined in huaweicloud sdk

        :param detail_list: 死锁明细列表
        :type detail_list: list[:class:`huaweicloudsdkdas.v3.DeadLockDetail`]
        :param total: 总数
        :type total: int
        """
        
        super().__init__()

        self._detail_list = None
        self._total = None
        self.discriminator = None

        if detail_list is not None:
            self.detail_list = detail_list
        if total is not None:
            self.total = total

    @property
    def detail_list(self):
        r"""Gets the detail_list of this ListDeadLockDetailResponse.

        死锁明细列表

        :return: The detail_list of this ListDeadLockDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DeadLockDetail`]
        """
        return self._detail_list

    @detail_list.setter
    def detail_list(self, detail_list):
        r"""Sets the detail_list of this ListDeadLockDetailResponse.

        死锁明细列表

        :param detail_list: The detail_list of this ListDeadLockDetailResponse.
        :type detail_list: list[:class:`huaweicloudsdkdas.v3.DeadLockDetail`]
        """
        self._detail_list = detail_list

    @property
    def total(self):
        r"""Gets the total of this ListDeadLockDetailResponse.

        总数

        :return: The total of this ListDeadLockDetailResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDeadLockDetailResponse.

        总数

        :param total: The total of this ListDeadLockDetailResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListDeadLockDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDeadLockDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
