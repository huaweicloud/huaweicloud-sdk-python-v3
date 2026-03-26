# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLockBlockingRelationshipResponse(SdkResponse):

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
        'detail_list': 'list[ListLockBlockingDetailRespDetailList]'
    }

    attribute_map = {
        'total': 'total',
        'detail_list': 'detail_list'
    }

    def __init__(self, total=None, detail_list=None):
        r"""ListLockBlockingRelationshipResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param detail_list: 锁阻塞明细列表
        :type detail_list: list[:class:`huaweicloudsdkdas.v3.ListLockBlockingDetailRespDetailList`]
        """
        
        super().__init__()

        self._total = None
        self._detail_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if detail_list is not None:
            self.detail_list = detail_list

    @property
    def total(self):
        r"""Gets the total of this ListLockBlockingRelationshipResponse.

        总数

        :return: The total of this ListLockBlockingRelationshipResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListLockBlockingRelationshipResponse.

        总数

        :param total: The total of this ListLockBlockingRelationshipResponse.
        :type total: int
        """
        self._total = total

    @property
    def detail_list(self):
        r"""Gets the detail_list of this ListLockBlockingRelationshipResponse.

        锁阻塞明细列表

        :return: The detail_list of this ListLockBlockingRelationshipResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ListLockBlockingDetailRespDetailList`]
        """
        return self._detail_list

    @detail_list.setter
    def detail_list(self, detail_list):
        r"""Sets the detail_list of this ListLockBlockingRelationshipResponse.

        锁阻塞明细列表

        :param detail_list: The detail_list of this ListLockBlockingRelationshipResponse.
        :type detail_list: list[:class:`huaweicloudsdkdas.v3.ListLockBlockingDetailRespDetailList`]
        """
        self._detail_list = detail_list

    def to_dict(self):
        import warnings
        warnings.warn("ListLockBlockingRelationshipResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListLockBlockingRelationshipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
