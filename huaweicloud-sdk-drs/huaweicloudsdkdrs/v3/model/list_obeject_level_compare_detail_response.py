# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObejectLevelCompareDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'compare_detail': 'list[ObjectsCompareDetailInfo]'
    }

    attribute_map = {
        'count': 'count',
        'compare_detail': 'compare_detail'
    }

    def __init__(self, count=None, compare_detail=None):
        r"""ListObejectLevelCompareDetailResponse

        The model defined in huaweicloud sdk

        :param count: 对比数量。
        :type count: int
        :param compare_detail: 对象级对比详情。
        :type compare_detail: list[:class:`huaweicloudsdkdrs.v3.ObjectsCompareDetailInfo`]
        """
        
        super(ListObejectLevelCompareDetailResponse, self).__init__()

        self._count = None
        self._compare_detail = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if compare_detail is not None:
            self.compare_detail = compare_detail

    @property
    def count(self):
        r"""Gets the count of this ListObejectLevelCompareDetailResponse.

        对比数量。

        :return: The count of this ListObejectLevelCompareDetailResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListObejectLevelCompareDetailResponse.

        对比数量。

        :param count: The count of this ListObejectLevelCompareDetailResponse.
        :type count: int
        """
        self._count = count

    @property
    def compare_detail(self):
        r"""Gets the compare_detail of this ListObejectLevelCompareDetailResponse.

        对象级对比详情。

        :return: The compare_detail of this ListObejectLevelCompareDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ObjectsCompareDetailInfo`]
        """
        return self._compare_detail

    @compare_detail.setter
    def compare_detail(self, compare_detail):
        r"""Sets the compare_detail of this ListObejectLevelCompareDetailResponse.

        对象级对比详情。

        :param compare_detail: The compare_detail of this ListObejectLevelCompareDetailResponse.
        :type compare_detail: list[:class:`huaweicloudsdkdrs.v3.ObjectsCompareDetailInfo`]
        """
        self._compare_detail = compare_detail

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
        if not isinstance(other, ListObejectLevelCompareDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
