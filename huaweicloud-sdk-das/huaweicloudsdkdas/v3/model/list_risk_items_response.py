# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRiskItemsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'items': 'list[QueryRiskItemsItems]'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'items': 'items'
    }

    def __init__(self, datastore_type=None, items=None):
        r"""ListRiskItemsResponse

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param items: 风险指标项
        :type items: list[:class:`huaweicloudsdkdas.v3.QueryRiskItemsItems`]
        """
        
        super(ListRiskItemsResponse, self).__init__()

        self._datastore_type = None
        self._items = None
        self.discriminator = None

        if datastore_type is not None:
            self.datastore_type = datastore_type
        if items is not None:
            self.items = items

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListRiskItemsResponse.

        数据库类型

        :return: The datastore_type of this ListRiskItemsResponse.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListRiskItemsResponse.

        数据库类型

        :param datastore_type: The datastore_type of this ListRiskItemsResponse.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def items(self):
        r"""Gets the items of this ListRiskItemsResponse.

        风险指标项

        :return: The items of this ListRiskItemsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.QueryRiskItemsItems`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListRiskItemsResponse.

        风险指标项

        :param items: The items of this ListRiskItemsResponse.
        :type items: list[:class:`huaweicloudsdkdas.v3.QueryRiskItemsItems`]
        """
        self._items = items

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
        if not isinstance(other, ListRiskItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
