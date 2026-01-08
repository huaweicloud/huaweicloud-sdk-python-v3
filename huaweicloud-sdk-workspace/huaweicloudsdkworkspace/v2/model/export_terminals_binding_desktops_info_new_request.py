# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTerminalsBindingDesktopsInfoNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'computer_name': 'str',
        'mac': 'str'
    }

    attribute_map = {
        'language': 'language',
        'computer_name': 'computer_name',
        'mac': 'mac'
    }

    def __init__(self, language=None, computer_name=None, mac=None):
        r"""ExportTerminalsBindingDesktopsInfoNewRequest

        The model defined in huaweicloud sdk

        :param language: 语言。  - zh_CN：中文 - en_US：英文
        :type language: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param mac: mac地址。
        :type mac: str
        """
        
        

        self._language = None
        self._computer_name = None
        self._mac = None
        self.discriminator = None

        self.language = language
        if computer_name is not None:
            self.computer_name = computer_name
        if mac is not None:
            self.mac = mac

    @property
    def language(self):
        r"""Gets the language of this ExportTerminalsBindingDesktopsInfoNewRequest.

        语言。  - zh_CN：中文 - en_US：英文

        :return: The language of this ExportTerminalsBindingDesktopsInfoNewRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportTerminalsBindingDesktopsInfoNewRequest.

        语言。  - zh_CN：中文 - en_US：英文

        :param language: The language of this ExportTerminalsBindingDesktopsInfoNewRequest.
        :type language: str
        """
        self._language = language

    @property
    def computer_name(self):
        r"""Gets the computer_name of this ExportTerminalsBindingDesktopsInfoNewRequest.

        桌面名。

        :return: The computer_name of this ExportTerminalsBindingDesktopsInfoNewRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this ExportTerminalsBindingDesktopsInfoNewRequest.

        桌面名。

        :param computer_name: The computer_name of this ExportTerminalsBindingDesktopsInfoNewRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def mac(self):
        r"""Gets the mac of this ExportTerminalsBindingDesktopsInfoNewRequest.

        mac地址。

        :return: The mac of this ExportTerminalsBindingDesktopsInfoNewRequest.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        r"""Sets the mac of this ExportTerminalsBindingDesktopsInfoNewRequest.

        mac地址。

        :param mac: The mac of this ExportTerminalsBindingDesktopsInfoNewRequest.
        :type mac: str
        """
        self._mac = mac

    def to_dict(self):
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
        if not isinstance(other, ExportTerminalsBindingDesktopsInfoNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
