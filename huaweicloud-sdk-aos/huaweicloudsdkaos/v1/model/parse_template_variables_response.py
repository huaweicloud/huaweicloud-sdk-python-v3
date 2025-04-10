# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseTemplateVariablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'variables': 'list[VariableResponse]'
    }

    attribute_map = {
        'variables': 'variables'
    }

    def __init__(self, variables=None):
        r"""ParseTemplateVariablesResponse

        The model defined in huaweicloud sdk

        :param variables: 解析模板得到的参数列表
        :type variables: list[:class:`huaweicloudsdkaos.v1.VariableResponse`]
        """
        
        super(ParseTemplateVariablesResponse, self).__init__()

        self._variables = None
        self.discriminator = None

        if variables is not None:
            self.variables = variables

    @property
    def variables(self):
        r"""Gets the variables of this ParseTemplateVariablesResponse.

        解析模板得到的参数列表

        :return: The variables of this ParseTemplateVariablesResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VariableResponse`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this ParseTemplateVariablesResponse.

        解析模板得到的参数列表

        :param variables: The variables of this ParseTemplateVariablesResponse.
        :type variables: list[:class:`huaweicloudsdkaos.v1.VariableResponse`]
        """
        self._variables = variables

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
        if not isinstance(other, ParseTemplateVariablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
