# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_size': 'int',
        'detail_list': 'list[GetUpgradeDetailInfo]'
    }

    attribute_map = {
        'total_size': 'totalSize',
        'detail_list': 'detailList'
    }

    def __init__(self, total_size=None, detail_list=None):
        r"""UpgradeDetailResponse

        The model defined in huaweicloud sdk

        :param total_size: 下发执行接口次数。
        :type total_size: int
        :param detail_list: 
        :type detail_list: list[:class:`huaweicloudsdkcss.v1.GetUpgradeDetailInfo`]
        """
        
        super(UpgradeDetailResponse, self).__init__()

        self._total_size = None
        self._detail_list = None
        self.discriminator = None

        if total_size is not None:
            self.total_size = total_size
        if detail_list is not None:
            self.detail_list = detail_list

    @property
    def total_size(self):
        r"""Gets the total_size of this UpgradeDetailResponse.

        下发执行接口次数。

        :return: The total_size of this UpgradeDetailResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this UpgradeDetailResponse.

        下发执行接口次数。

        :param total_size: The total_size of this UpgradeDetailResponse.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def detail_list(self):
        r"""Gets the detail_list of this UpgradeDetailResponse.

        :return: The detail_list of this UpgradeDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.GetUpgradeDetailInfo`]
        """
        return self._detail_list

    @detail_list.setter
    def detail_list(self, detail_list):
        r"""Sets the detail_list of this UpgradeDetailResponse.

        :param detail_list: The detail_list of this UpgradeDetailResponse.
        :type detail_list: list[:class:`huaweicloudsdkcss.v1.GetUpgradeDetailInfo`]
        """
        self._detail_list = detail_list

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
        if not isinstance(other, UpgradeDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
