# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsResponse(SdkResponse):

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
        'data': 'list[FlavorBrief]'
    }

    attribute_map = {
        'total': 'total',
        'data': 'data'
    }

    def __init__(self, total=None, data=None):
        r"""ListFlavorsResponse

        The model defined in huaweicloud sdk

        :param total: 微服务引擎规格总个数
        :type total: int
        :param data: 微服务引擎规格详情
        :type data: list[:class:`huaweicloudsdkcse.v1.FlavorBrief`]
        """
        
        super(ListFlavorsResponse, self).__init__()

        self._total = None
        self._data = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if data is not None:
            self.data = data

    @property
    def total(self):
        r"""Gets the total of this ListFlavorsResponse.

        微服务引擎规格总个数

        :return: The total of this ListFlavorsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFlavorsResponse.

        微服务引擎规格总个数

        :param total: The total of this ListFlavorsResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        r"""Gets the data of this ListFlavorsResponse.

        微服务引擎规格详情

        :return: The data of this ListFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkcse.v1.FlavorBrief`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListFlavorsResponse.

        微服务引擎规格详情

        :param data: The data of this ListFlavorsResponse.
        :type data: list[:class:`huaweicloudsdkcse.v1.FlavorBrief`]
        """
        self._data = data

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
        if not isinstance(other, ListFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
