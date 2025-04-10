# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'backups': 'str',
        'flavor': 'str',
        'floatingips': 'list[str]',
        'interface': 'str',
        'ports': 'list[str]',
        'server': 'str',
        'volumes': 'list[str]'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'backups': 'backups',
        'flavor': 'flavor',
        'floatingips': 'floatingips',
        'interface': 'interface',
        'ports': 'ports',
        'server': 'server',
        'volumes': 'volumes'
    }

    def __init__(self, backup_id=None, backups=None, flavor=None, floatingips=None, interface=None, ports=None, server=None, volumes=None):
        r"""ShowMetadataResponse

        The model defined in huaweicloud sdk

        :param backup_id: 备份ID
        :type backup_id: str
        :param backups: 云服务器备份信息
        :type backups: str
        :param flavor: 云服务器规格信息
        :type flavor: str
        :param floatingips: 云服务器浮动IP信息
        :type floatingips: list[str]
        :param interface: 云服务器接口信息
        :type interface: str
        :param ports: 云服务器端口信息
        :type ports: list[str]
        :param server: 云服务器信息
        :type server: str
        :param volumes: 云服务器卷信息
        :type volumes: list[str]
        """
        
        super(ShowMetadataResponse, self).__init__()

        self._backup_id = None
        self._backups = None
        self._flavor = None
        self._floatingips = None
        self._interface = None
        self._ports = None
        self._server = None
        self._volumes = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if backups is not None:
            self.backups = backups
        if flavor is not None:
            self.flavor = flavor
        if floatingips is not None:
            self.floatingips = floatingips
        if interface is not None:
            self.interface = interface
        if ports is not None:
            self.ports = ports
        if server is not None:
            self.server = server
        if volumes is not None:
            self.volumes = volumes

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ShowMetadataResponse.

        备份ID

        :return: The backup_id of this ShowMetadataResponse.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ShowMetadataResponse.

        备份ID

        :param backup_id: The backup_id of this ShowMetadataResponse.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backups(self):
        r"""Gets the backups of this ShowMetadataResponse.

        云服务器备份信息

        :return: The backups of this ShowMetadataResponse.
        :rtype: str
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        r"""Sets the backups of this ShowMetadataResponse.

        云服务器备份信息

        :param backups: The backups of this ShowMetadataResponse.
        :type backups: str
        """
        self._backups = backups

    @property
    def flavor(self):
        r"""Gets the flavor of this ShowMetadataResponse.

        云服务器规格信息

        :return: The flavor of this ShowMetadataResponse.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ShowMetadataResponse.

        云服务器规格信息

        :param flavor: The flavor of this ShowMetadataResponse.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def floatingips(self):
        r"""Gets the floatingips of this ShowMetadataResponse.

        云服务器浮动IP信息

        :return: The floatingips of this ShowMetadataResponse.
        :rtype: list[str]
        """
        return self._floatingips

    @floatingips.setter
    def floatingips(self, floatingips):
        r"""Sets the floatingips of this ShowMetadataResponse.

        云服务器浮动IP信息

        :param floatingips: The floatingips of this ShowMetadataResponse.
        :type floatingips: list[str]
        """
        self._floatingips = floatingips

    @property
    def interface(self):
        r"""Gets the interface of this ShowMetadataResponse.

        云服务器接口信息

        :return: The interface of this ShowMetadataResponse.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        r"""Sets the interface of this ShowMetadataResponse.

        云服务器接口信息

        :param interface: The interface of this ShowMetadataResponse.
        :type interface: str
        """
        self._interface = interface

    @property
    def ports(self):
        r"""Gets the ports of this ShowMetadataResponse.

        云服务器端口信息

        :return: The ports of this ShowMetadataResponse.
        :rtype: list[str]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this ShowMetadataResponse.

        云服务器端口信息

        :param ports: The ports of this ShowMetadataResponse.
        :type ports: list[str]
        """
        self._ports = ports

    @property
    def server(self):
        r"""Gets the server of this ShowMetadataResponse.

        云服务器信息

        :return: The server of this ShowMetadataResponse.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        r"""Sets the server of this ShowMetadataResponse.

        云服务器信息

        :param server: The server of this ShowMetadataResponse.
        :type server: str
        """
        self._server = server

    @property
    def volumes(self):
        r"""Gets the volumes of this ShowMetadataResponse.

        云服务器卷信息

        :return: The volumes of this ShowMetadataResponse.
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this ShowMetadataResponse.

        云服务器卷信息

        :param volumes: The volumes of this ShowMetadataResponse.
        :type volumes: list[str]
        """
        self._volumes = volumes

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
        if not isinstance(other, ShowMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
