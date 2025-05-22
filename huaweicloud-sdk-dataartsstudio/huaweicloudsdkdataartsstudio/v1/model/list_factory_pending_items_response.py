# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryPendingItemsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[ListFactoryPendingItemsRespData]',
        'total': 'int'
    }

    attribute_map = {
        'data': 'data',
        'total': 'total'
    }

    def __init__(self, data=None, total=None):
        r"""ListFactoryPendingItemsResponse

        The model defined in huaweicloud sdk

        :param data: 待发布包信息
        :type data: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryPendingItemsRespData`]
        :param total: 待发布包数量
        :type total: int
        """
        
        super(ListFactoryPendingItemsResponse, self).__init__()

        self._data = None
        self._total = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total is not None:
            self.total = total

    @property
    def data(self):
        r"""Gets the data of this ListFactoryPendingItemsResponse.

        待发布包信息

        :return: The data of this ListFactoryPendingItemsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryPendingItemsRespData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListFactoryPendingItemsResponse.

        待发布包信息

        :param data: The data of this ListFactoryPendingItemsResponse.
        :type data: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryPendingItemsRespData`]
        """
        self._data = data

    @property
    def total(self):
        r"""Gets the total of this ListFactoryPendingItemsResponse.

        待发布包数量

        :return: The total of this ListFactoryPendingItemsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFactoryPendingItemsResponse.

        待发布包数量

        :param total: The total of this ListFactoryPendingItemsResponse.
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
        if not isinstance(other, ListFactoryPendingItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
