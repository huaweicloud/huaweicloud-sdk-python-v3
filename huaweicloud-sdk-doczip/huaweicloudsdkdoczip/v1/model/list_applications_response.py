# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_list': 'list[Application]',
        'total': 'int',
        'x_trace_id': 'str'
    }

    attribute_map = {
        'application_list': 'application_list',
        'total': 'total',
        'x_trace_id': 'X-Trace-Id'
    }

    def __init__(self, application_list=None, total=None, x_trace_id=None):
        r"""ListApplicationsResponse

        The model defined in huaweicloud sdk

        :param application_list: **参数解释**： 返回的应用列表信息。 **取值范围**： 不涉及。
        :type application_list: list[:class:`huaweicloudsdkdoczip.v1.Application`]
        :param total: **参数解释**： 总数。 **取值范围**： 不涉及。
        :type total: int
        :param x_trace_id: 
        :type x_trace_id: str
        """
        
        super().__init__()

        self._application_list = None
        self._total = None
        self._x_trace_id = None
        self.discriminator = None

        if application_list is not None:
            self.application_list = application_list
        if total is not None:
            self.total = total
        if x_trace_id is not None:
            self.x_trace_id = x_trace_id

    @property
    def application_list(self):
        r"""Gets the application_list of this ListApplicationsResponse.

        **参数解释**： 返回的应用列表信息。 **取值范围**： 不涉及。

        :return: The application_list of this ListApplicationsResponse.
        :rtype: list[:class:`huaweicloudsdkdoczip.v1.Application`]
        """
        return self._application_list

    @application_list.setter
    def application_list(self, application_list):
        r"""Sets the application_list of this ListApplicationsResponse.

        **参数解释**： 返回的应用列表信息。 **取值范围**： 不涉及。

        :param application_list: The application_list of this ListApplicationsResponse.
        :type application_list: list[:class:`huaweicloudsdkdoczip.v1.Application`]
        """
        self._application_list = application_list

    @property
    def total(self):
        r"""Gets the total of this ListApplicationsResponse.

        **参数解释**： 总数。 **取值范围**： 不涉及。

        :return: The total of this ListApplicationsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListApplicationsResponse.

        **参数解释**： 总数。 **取值范围**： 不涉及。

        :param total: The total of this ListApplicationsResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_trace_id(self):
        r"""Gets the x_trace_id of this ListApplicationsResponse.

        :return: The x_trace_id of this ListApplicationsResponse.
        :rtype: str
        """
        return self._x_trace_id

    @x_trace_id.setter
    def x_trace_id(self, x_trace_id):
        r"""Sets the x_trace_id of this ListApplicationsResponse.

        :param x_trace_id: The x_trace_id of this ListApplicationsResponse.
        :type x_trace_id: str
        """
        self._x_trace_id = x_trace_id

    def to_dict(self):
        import warnings
        warnings.warn("ListApplicationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListApplicationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
