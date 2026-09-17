# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportedService:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'service_name': 'service_name',
        'display_name': 'display_name'
    }

    def __init__(self, service_name=None, display_name=None):
        r"""SupportedService

        The model defined in huaweicloud sdk

        :param service_name: 云服务名称。
        :type service_name: str
        :param display_name: 关联的服务的展示名称（受语言控制）。
        :type display_name: str
        """
        
        

        self._service_name = None
        self._display_name = None
        self.discriminator = None

        self.service_name = service_name
        self.display_name = display_name

    @property
    def service_name(self):
        r"""Gets the service_name of this SupportedService.

        云服务名称。

        :return: The service_name of this SupportedService.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this SupportedService.

        云服务名称。

        :param service_name: The service_name of this SupportedService.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def display_name(self):
        r"""Gets the display_name of this SupportedService.

        关联的服务的展示名称（受语言控制）。

        :return: The display_name of this SupportedService.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this SupportedService.

        关联的服务的展示名称（受语言控制）。

        :param display_name: The display_name of this SupportedService.
        :type display_name: str
        """
        self._display_name = display_name

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
        if not isinstance(other, SupportedService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
