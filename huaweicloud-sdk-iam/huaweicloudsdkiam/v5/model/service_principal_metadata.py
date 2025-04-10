# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServicePrincipalMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_principal': 'str',
        'service_catalog': 'str',
        'display_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'service_principal': 'service_principal',
        'service_catalog': 'service_catalog',
        'display_name': 'display_name',
        'description': 'description'
    }

    def __init__(self, service_principal=None, service_catalog=None, display_name=None, description=None):
        r"""ServicePrincipalMetadata

        The model defined in huaweicloud sdk

        :param service_principal: 服务主体，由\&quot;service.\&quot;开头，后跟一个长度为1到56个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type service_principal: str
        :param service_catalog: 云服务名称。
        :type service_catalog: str
        :param display_name: 用于显示的服务主体名称。
        :type display_name: str
        :param description: 服务主体的描述。
        :type description: str
        """
        
        

        self._service_principal = None
        self._service_catalog = None
        self._display_name = None
        self._description = None
        self.discriminator = None

        self.service_principal = service_principal
        self.service_catalog = service_catalog
        self.display_name = display_name
        self.description = description

    @property
    def service_principal(self):
        r"""Gets the service_principal of this ServicePrincipalMetadata.

        服务主体，由\"service.\"开头，后跟一个长度为1到56个字符，只包含字母、数字和\"-\"的字符串。

        :return: The service_principal of this ServicePrincipalMetadata.
        :rtype: str
        """
        return self._service_principal

    @service_principal.setter
    def service_principal(self, service_principal):
        r"""Sets the service_principal of this ServicePrincipalMetadata.

        服务主体，由\"service.\"开头，后跟一个长度为1到56个字符，只包含字母、数字和\"-\"的字符串。

        :param service_principal: The service_principal of this ServicePrincipalMetadata.
        :type service_principal: str
        """
        self._service_principal = service_principal

    @property
    def service_catalog(self):
        r"""Gets the service_catalog of this ServicePrincipalMetadata.

        云服务名称。

        :return: The service_catalog of this ServicePrincipalMetadata.
        :rtype: str
        """
        return self._service_catalog

    @service_catalog.setter
    def service_catalog(self, service_catalog):
        r"""Sets the service_catalog of this ServicePrincipalMetadata.

        云服务名称。

        :param service_catalog: The service_catalog of this ServicePrincipalMetadata.
        :type service_catalog: str
        """
        self._service_catalog = service_catalog

    @property
    def display_name(self):
        r"""Gets the display_name of this ServicePrincipalMetadata.

        用于显示的服务主体名称。

        :return: The display_name of this ServicePrincipalMetadata.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ServicePrincipalMetadata.

        用于显示的服务主体名称。

        :param display_name: The display_name of this ServicePrincipalMetadata.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this ServicePrincipalMetadata.

        服务主体的描述。

        :return: The description of this ServicePrincipalMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServicePrincipalMetadata.

        服务主体的描述。

        :param description: The description of this ServicePrincipalMetadata.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ServicePrincipalMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
