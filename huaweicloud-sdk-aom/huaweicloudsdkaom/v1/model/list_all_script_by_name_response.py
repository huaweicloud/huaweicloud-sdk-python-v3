# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllScriptByNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elements': 'list[Script]',
        'total_elements': 'int'
    }

    attribute_map = {
        'elements': 'elements',
        'total_elements': 'total_elements'
    }

    def __init__(self, elements=None, total_elements=None):
        r"""ListAllScriptByNameResponse

        The model defined in huaweicloud sdk

        :param elements: 查询结果集合。
        :type elements: list[:class:`huaweicloudsdkaom.v1.Script`]
        :param total_elements: 查询到的结果数量。
        :type total_elements: int
        """
        
        super(ListAllScriptByNameResponse, self).__init__()

        self._elements = None
        self._total_elements = None
        self.discriminator = None

        if elements is not None:
            self.elements = elements
        if total_elements is not None:
            self.total_elements = total_elements

    @property
    def elements(self):
        r"""Gets the elements of this ListAllScriptByNameResponse.

        查询结果集合。

        :return: The elements of this ListAllScriptByNameResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Script`]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        r"""Sets the elements of this ListAllScriptByNameResponse.

        查询结果集合。

        :param elements: The elements of this ListAllScriptByNameResponse.
        :type elements: list[:class:`huaweicloudsdkaom.v1.Script`]
        """
        self._elements = elements

    @property
    def total_elements(self):
        r"""Gets the total_elements of this ListAllScriptByNameResponse.

        查询到的结果数量。

        :return: The total_elements of this ListAllScriptByNameResponse.
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        r"""Sets the total_elements of this ListAllScriptByNameResponse.

        查询到的结果数量。

        :param total_elements: The total_elements of this ListAllScriptByNameResponse.
        :type total_elements: int
        """
        self._total_elements = total_elements

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
        if not isinstance(other, ListAllScriptByNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
