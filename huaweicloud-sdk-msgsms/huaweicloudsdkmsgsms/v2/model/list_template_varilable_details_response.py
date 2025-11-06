# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateVarilableDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[ApiTemplateVariable]',
        'total': 'int'
    }

    attribute_map = {
        'results': 'results',
        'total': 'total'
    }

    def __init__(self, results=None, total=None):
        r"""ListTemplateVarilableDetailsResponse

        The model defined in huaweicloud sdk

        :param results: 查询结果
        :type results: list[:class:`huaweicloudsdkmsgsms.v2.ApiTemplateVariable`]
        :param total: 总数
        :type total: int
        """
        
        super().__init__()

        self._results = None
        self._total = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if total is not None:
            self.total = total

    @property
    def results(self):
        r"""Gets the results of this ListTemplateVarilableDetailsResponse.

        查询结果

        :return: The results of this ListTemplateVarilableDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkmsgsms.v2.ApiTemplateVariable`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this ListTemplateVarilableDetailsResponse.

        查询结果

        :param results: The results of this ListTemplateVarilableDetailsResponse.
        :type results: list[:class:`huaweicloudsdkmsgsms.v2.ApiTemplateVariable`]
        """
        self._results = results

    @property
    def total(self):
        r"""Gets the total of this ListTemplateVarilableDetailsResponse.

        总数

        :return: The total of this ListTemplateVarilableDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTemplateVarilableDetailsResponse.

        总数

        :param total: The total of this ListTemplateVarilableDetailsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListTemplateVarilableDetailsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTemplateVarilableDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
