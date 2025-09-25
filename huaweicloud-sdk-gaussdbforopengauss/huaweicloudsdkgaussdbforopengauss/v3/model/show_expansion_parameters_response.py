# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExpansionParametersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expansion_parameters': 'list[ExpansionParameterResult]'
    }

    attribute_map = {
        'expansion_parameters': 'expansion_parameters'
    }

    def __init__(self, expansion_parameters=None):
        r"""ShowExpansionParametersResponse

        The model defined in huaweicloud sdk

        :param expansion_parameters: **参数解释**: 参数信息。
        :type expansion_parameters: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ExpansionParameterResult`]
        """
        
        super(ShowExpansionParametersResponse, self).__init__()

        self._expansion_parameters = None
        self.discriminator = None

        if expansion_parameters is not None:
            self.expansion_parameters = expansion_parameters

    @property
    def expansion_parameters(self):
        r"""Gets the expansion_parameters of this ShowExpansionParametersResponse.

        **参数解释**: 参数信息。

        :return: The expansion_parameters of this ShowExpansionParametersResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ExpansionParameterResult`]
        """
        return self._expansion_parameters

    @expansion_parameters.setter
    def expansion_parameters(self, expansion_parameters):
        r"""Sets the expansion_parameters of this ShowExpansionParametersResponse.

        **参数解释**: 参数信息。

        :param expansion_parameters: The expansion_parameters of this ShowExpansionParametersResponse.
        :type expansion_parameters: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ExpansionParameterResult`]
        """
        self._expansion_parameters = expansion_parameters

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
        if not isinstance(other, ShowExpansionParametersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
