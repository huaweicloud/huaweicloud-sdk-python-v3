# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceNamespacesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespaces': 'list[Namespace]',
        'total': 'int'
    }

    attribute_map = {
        'namespaces': 'namespaces',
        'total': 'total'
    }

    def __init__(self, namespaces=None, total=None):
        r"""ListInstanceNamespacesResponse

        The model defined in huaweicloud sdk

        :param namespaces: 命名空间列表
        :type namespaces: list[:class:`huaweicloudsdkswr.v2.Namespace`]
        :param total: 命名空间总数
        :type total: int
        """
        
        super(ListInstanceNamespacesResponse, self).__init__()

        self._namespaces = None
        self._total = None
        self.discriminator = None

        if namespaces is not None:
            self.namespaces = namespaces
        if total is not None:
            self.total = total

    @property
    def namespaces(self):
        r"""Gets the namespaces of this ListInstanceNamespacesResponse.

        命名空间列表

        :return: The namespaces of this ListInstanceNamespacesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Namespace`]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this ListInstanceNamespacesResponse.

        命名空间列表

        :param namespaces: The namespaces of this ListInstanceNamespacesResponse.
        :type namespaces: list[:class:`huaweicloudsdkswr.v2.Namespace`]
        """
        self._namespaces = namespaces

    @property
    def total(self):
        r"""Gets the total of this ListInstanceNamespacesResponse.

        命名空间总数

        :return: The total of this ListInstanceNamespacesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceNamespacesResponse.

        命名空间总数

        :param total: The total of this ListInstanceNamespacesResponse.
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
        if not isinstance(other, ListInstanceNamespacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
