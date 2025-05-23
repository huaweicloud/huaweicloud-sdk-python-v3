# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRefundOrderDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'refund_infos': 'list[OrderRefundInfoV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'refund_infos': 'refund_infos'
    }

    def __init__(self, total_count=None, refund_infos=None):
        r"""ShowRefundOrderDetailsResponse

        The model defined in huaweicloud sdk

        :param total_count: 查询总数。
        :type total_count: int
        :param refund_infos: 资源信息列表。 具体请参见表2。
        :type refund_infos: list[:class:`huaweicloudsdkbssintl.v2.OrderRefundInfoV2`]
        """
        
        super(ShowRefundOrderDetailsResponse, self).__init__()

        self._total_count = None
        self._refund_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if refund_infos is not None:
            self.refund_infos = refund_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowRefundOrderDetailsResponse.

        查询总数。

        :return: The total_count of this ShowRefundOrderDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowRefundOrderDetailsResponse.

        查询总数。

        :param total_count: The total_count of this ShowRefundOrderDetailsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def refund_infos(self):
        r"""Gets the refund_infos of this ShowRefundOrderDetailsResponse.

        资源信息列表。 具体请参见表2。

        :return: The refund_infos of this ShowRefundOrderDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.OrderRefundInfoV2`]
        """
        return self._refund_infos

    @refund_infos.setter
    def refund_infos(self, refund_infos):
        r"""Sets the refund_infos of this ShowRefundOrderDetailsResponse.

        资源信息列表。 具体请参见表2。

        :param refund_infos: The refund_infos of this ShowRefundOrderDetailsResponse.
        :type refund_infos: list[:class:`huaweicloudsdkbssintl.v2.OrderRefundInfoV2`]
        """
        self._refund_infos = refund_infos

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
        if not isinstance(other, ShowRefundOrderDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
