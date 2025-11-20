# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'need_restart': 'bool'
    }

    attribute_map = {
        'need_restart': 'need_restart'
    }

    def __init__(self, need_restart=None):
        r"""ModifyConfigurationResponse

        The model defined in huaweicloud sdk

        :param need_restart: 是否需要重启。
        :type need_restart: bool
        """
        
        super().__init__()

        self._need_restart = None
        self.discriminator = None

        if need_restart is not None:
            self.need_restart = need_restart

    @property
    def need_restart(self):
        r"""Gets the need_restart of this ModifyConfigurationResponse.

        是否需要重启。

        :return: The need_restart of this ModifyConfigurationResponse.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        r"""Sets the need_restart of this ModifyConfigurationResponse.

        是否需要重启。

        :param need_restart: The need_restart of this ModifyConfigurationResponse.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    def to_dict(self):
        import warnings
        warnings.warn("ModifyConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ModifyConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
