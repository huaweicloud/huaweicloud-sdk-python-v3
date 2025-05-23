# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAimMsgTemplateVariableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[VariableAttributesResponse]',
        'total': 'int'
    }

    attribute_map = {
        'results': 'results',
        'total': 'total'
    }

    def __init__(self, results=None, total=None):
        r"""ShowAimMsgTemplateVariableResponse

        The model defined in huaweicloud sdk

        :param results: 返回结果列表。
        :type results: list[:class:`huaweicloudsdkkoomessage.v1.VariableAttributesResponse`]
        :param total: 总数。
        :type total: int
        """
        
        super(ShowAimMsgTemplateVariableResponse, self).__init__()

        self._results = None
        self._total = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if total is not None:
            self.total = total

    @property
    def results(self):
        r"""Gets the results of this ShowAimMsgTemplateVariableResponse.

        返回结果列表。

        :return: The results of this ShowAimMsgTemplateVariableResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.VariableAttributesResponse`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this ShowAimMsgTemplateVariableResponse.

        返回结果列表。

        :param results: The results of this ShowAimMsgTemplateVariableResponse.
        :type results: list[:class:`huaweicloudsdkkoomessage.v1.VariableAttributesResponse`]
        """
        self._results = results

    @property
    def total(self):
        r"""Gets the total of this ShowAimMsgTemplateVariableResponse.

        总数。

        :return: The total of this ShowAimMsgTemplateVariableResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowAimMsgTemplateVariableResponse.

        总数。

        :param total: The total of this ShowAimMsgTemplateVariableResponse.
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
        if not isinstance(other, ShowAimMsgTemplateVariableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
