# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerConsoleOutputResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output': 'str'
    }

    attribute_map = {
        'output': 'output'
    }

    def __init__(self, output=None):
        r"""ShowServerConsoleOutputResponse

        The model defined in huaweicloud sdk

        :param output: 云服务器控制台日志。
        :type output: str
        """
        
        super().__init__()

        self._output = None
        self.discriminator = None

        if output is not None:
            self.output = output

    @property
    def output(self):
        r"""Gets the output of this ShowServerConsoleOutputResponse.

        云服务器控制台日志。

        :return: The output of this ShowServerConsoleOutputResponse.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ShowServerConsoleOutputResponse.

        云服务器控制台日志。

        :param output: The output of this ShowServerConsoleOutputResponse.
        :type output: str
        """
        self._output = output

    def to_dict(self):
        import warnings
        warnings.warn("ShowServerConsoleOutputResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowServerConsoleOutputResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
