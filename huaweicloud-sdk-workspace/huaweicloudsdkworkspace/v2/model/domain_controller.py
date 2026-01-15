# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainController:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dc_ip': 'str',
        'dc_name': 'str'
    }

    attribute_map = {
        'dc_ip': 'dc_ip',
        'dc_name': 'dc_name'
    }

    def __init__(self, dc_ip=None, dc_name=None):
        r"""DomainController

        The model defined in huaweicloud sdk

        :param dc_ip: 域控制器IP地址。
        :type dc_ip: str
        :param dc_name: 域控制器名称。
        :type dc_name: str
        """
        
        

        self._dc_ip = None
        self._dc_name = None
        self.discriminator = None

        self.dc_ip = dc_ip
        self.dc_name = dc_name

    @property
    def dc_ip(self):
        r"""Gets the dc_ip of this DomainController.

        域控制器IP地址。

        :return: The dc_ip of this DomainController.
        :rtype: str
        """
        return self._dc_ip

    @dc_ip.setter
    def dc_ip(self, dc_ip):
        r"""Sets the dc_ip of this DomainController.

        域控制器IP地址。

        :param dc_ip: The dc_ip of this DomainController.
        :type dc_ip: str
        """
        self._dc_ip = dc_ip

    @property
    def dc_name(self):
        r"""Gets the dc_name of this DomainController.

        域控制器名称。

        :return: The dc_name of this DomainController.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        r"""Sets the dc_name of this DomainController.

        域控制器名称。

        :param dc_name: The dc_name of this DomainController.
        :type dc_name: str
        """
        self._dc_name = dc_name

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
        if not isinstance(other, DomainController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
