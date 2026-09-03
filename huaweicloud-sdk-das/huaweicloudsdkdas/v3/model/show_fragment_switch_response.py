# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFragmentSwitchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_name': 'str',
        'open': 'bool'
    }

    attribute_map = {
        'switch_name': 'switch_name',
        'open': 'open'
    }

    def __init__(self, switch_name=None, open=None):
        r"""ShowFragmentSwitchResponse

        The model defined in huaweicloud sdk

        :param switch_name: 开关名称
        :type switch_name: str
        :param open: 是否开启
        :type open: bool
        """
        
        super().__init__()

        self._switch_name = None
        self._open = None
        self.discriminator = None

        if switch_name is not None:
            self.switch_name = switch_name
        if open is not None:
            self.open = open

    @property
    def switch_name(self):
        r"""Gets the switch_name of this ShowFragmentSwitchResponse.

        开关名称

        :return: The switch_name of this ShowFragmentSwitchResponse.
        :rtype: str
        """
        return self._switch_name

    @switch_name.setter
    def switch_name(self, switch_name):
        r"""Sets the switch_name of this ShowFragmentSwitchResponse.

        开关名称

        :param switch_name: The switch_name of this ShowFragmentSwitchResponse.
        :type switch_name: str
        """
        self._switch_name = switch_name

    @property
    def open(self):
        r"""Gets the open of this ShowFragmentSwitchResponse.

        是否开启

        :return: The open of this ShowFragmentSwitchResponse.
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        r"""Sets the open of this ShowFragmentSwitchResponse.

        是否开启

        :param open: The open of this ShowFragmentSwitchResponse.
        :type open: bool
        """
        self._open = open

    def to_dict(self):
        import warnings
        warnings.warn("ShowFragmentSwitchResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFragmentSwitchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
