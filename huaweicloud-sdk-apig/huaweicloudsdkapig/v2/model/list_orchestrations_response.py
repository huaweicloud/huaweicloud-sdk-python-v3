# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrchestrationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'orchestrations': 'list[OrchestrationBaseResp]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'orchestrations': 'orchestrations'
    }

    def __init__(self, size=None, total=None, orchestrations=None):
        """ListOrchestrationsResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param orchestrations: 本次查询到的编排规则列表。
        :type orchestrations: list[:class:`huaweicloudsdkapig.v2.OrchestrationBaseResp`]
        """
        
        super(ListOrchestrationsResponse, self).__init__()

        self._size = None
        self._total = None
        self._orchestrations = None
        self.discriminator = None

        self.size = size
        self.total = total
        if orchestrations is not None:
            self.orchestrations = orchestrations

    @property
    def size(self):
        """Gets the size of this ListOrchestrationsResponse.

        本次返回的列表长度

        :return: The size of this ListOrchestrationsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListOrchestrationsResponse.

        本次返回的列表长度

        :param size: The size of this ListOrchestrationsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        """Gets the total of this ListOrchestrationsResponse.

        满足条件的记录数

        :return: The total of this ListOrchestrationsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListOrchestrationsResponse.

        满足条件的记录数

        :param total: The total of this ListOrchestrationsResponse.
        :type total: int
        """
        self._total = total

    @property
    def orchestrations(self):
        """Gets the orchestrations of this ListOrchestrationsResponse.

        本次查询到的编排规则列表。

        :return: The orchestrations of this ListOrchestrationsResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.OrchestrationBaseResp`]
        """
        return self._orchestrations

    @orchestrations.setter
    def orchestrations(self, orchestrations):
        """Sets the orchestrations of this ListOrchestrationsResponse.

        本次查询到的编排规则列表。

        :param orchestrations: The orchestrations of this ListOrchestrationsResponse.
        :type orchestrations: list[:class:`huaweicloudsdkapig.v2.OrchestrationBaseResp`]
        """
        self._orchestrations = orchestrations

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
        if not isinstance(other, ListOrchestrationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
