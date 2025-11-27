# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReplicationErrorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'errors': 'list[ListReplicationErrorsResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'errors': 'errors',
        'total_count': 'total_count'
    }

    def __init__(self, errors=None, total_count=None):
        r"""ListReplicationErrorsResponse

        The model defined in huaweicloud sdk

        :param errors: 报错列表。
        :type errors: list[:class:`huaweicloudsdkrds.v3.ListReplicationErrorsResult`]
        :param total_count: 报错总数。
        :type total_count: int
        """
        
        super().__init__()

        self._errors = None
        self._total_count = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if total_count is not None:
            self.total_count = total_count

    @property
    def errors(self):
        r"""Gets the errors of this ListReplicationErrorsResponse.

        报错列表。

        :return: The errors of this ListReplicationErrorsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ListReplicationErrorsResult`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this ListReplicationErrorsResponse.

        报错列表。

        :param errors: The errors of this ListReplicationErrorsResponse.
        :type errors: list[:class:`huaweicloudsdkrds.v3.ListReplicationErrorsResult`]
        """
        self._errors = errors

    @property
    def total_count(self):
        r"""Gets the total_count of this ListReplicationErrorsResponse.

        报错总数。

        :return: The total_count of this ListReplicationErrorsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListReplicationErrorsResponse.

        报错总数。

        :param total_count: The total_count of this ListReplicationErrorsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListReplicationErrorsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListReplicationErrorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
