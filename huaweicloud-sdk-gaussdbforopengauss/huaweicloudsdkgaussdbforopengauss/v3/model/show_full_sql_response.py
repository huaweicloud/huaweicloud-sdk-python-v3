# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFullSqlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_statistics': 'object',
        'components': 'list[FullSqlComponetResult]'
    }

    attribute_map = {
        'trace_statistics': 'trace_statistics',
        'components': 'components'
    }

    def __init__(self, trace_statistics=None, components=None):
        r"""ShowFullSqlResponse

        The model defined in huaweicloud sdk

        :param trace_statistics: **参数解释**: 链路详情。
        :type trace_statistics: object
        :param components: **参数解释**: 组件上SQL执行记录列表。
        :type components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlComponetResult`]
        """
        
        super().__init__()

        self._trace_statistics = None
        self._components = None
        self.discriminator = None

        if trace_statistics is not None:
            self.trace_statistics = trace_statistics
        if components is not None:
            self.components = components

    @property
    def trace_statistics(self):
        r"""Gets the trace_statistics of this ShowFullSqlResponse.

        **参数解释**: 链路详情。

        :return: The trace_statistics of this ShowFullSqlResponse.
        :rtype: object
        """
        return self._trace_statistics

    @trace_statistics.setter
    def trace_statistics(self, trace_statistics):
        r"""Sets the trace_statistics of this ShowFullSqlResponse.

        **参数解释**: 链路详情。

        :param trace_statistics: The trace_statistics of this ShowFullSqlResponse.
        :type trace_statistics: object
        """
        self._trace_statistics = trace_statistics

    @property
    def components(self):
        r"""Gets the components of this ShowFullSqlResponse.

        **参数解释**: 组件上SQL执行记录列表。

        :return: The components of this ShowFullSqlResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlComponetResult`]
        """
        return self._components

    @components.setter
    def components(self, components):
        r"""Sets the components of this ShowFullSqlResponse.

        **参数解释**: 组件上SQL执行记录列表。

        :param components: The components of this ShowFullSqlResponse.
        :type components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlComponetResult`]
        """
        self._components = components

    def to_dict(self):
        import warnings
        warnings.warn("ShowFullSqlResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFullSqlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
