# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowsResponse(SdkResponse):

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
        'flows': 'list[ListFlowRespItem]'
    }

    attribute_map = {
        'total': 'total',
        'flows': 'flows'
    }

    def __init__(self, total=None, flows=None):
        r"""ListFlowsResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param flows: 流列表
        :type flows: list[:class:`huaweicloudsdklive.v1.ListFlowRespItem`]
        """
        
        super(ListFlowsResponse, self).__init__()

        self._total = None
        self._flows = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if flows is not None:
            self.flows = flows

    @property
    def total(self):
        r"""Gets the total of this ListFlowsResponse.

        总数

        :return: The total of this ListFlowsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFlowsResponse.

        总数

        :param total: The total of this ListFlowsResponse.
        :type total: int
        """
        self._total = total

    @property
    def flows(self):
        r"""Gets the flows of this ListFlowsResponse.

        流列表

        :return: The flows of this ListFlowsResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.ListFlowRespItem`]
        """
        return self._flows

    @flows.setter
    def flows(self, flows):
        r"""Sets the flows of this ListFlowsResponse.

        流列表

        :param flows: The flows of this ListFlowsResponse.
        :type flows: list[:class:`huaweicloudsdklive.v1.ListFlowRespItem`]
        """
        self._flows = flows

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
        if not isinstance(other, ListFlowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
