# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemSecurityPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'protocols': 'str',
        'ciphers': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'protocols': 'protocols',
        'ciphers': 'ciphers',
        'project_id': 'project_id'
    }

    def __init__(self, name=None, protocols=None, ciphers=None, project_id=None):
        """SystemSecurityPolicy

        The model defined in huaweicloud sdk

        :param name: 系统安全策略的名称。
        :type name: str
        :param protocols: 系统安全策略的TLS协议列表。
        :type protocols: str
        :param ciphers: 系统安全策略的加密套件列表。
        :type ciphers: str
        :param project_id: 项目id。
        :type project_id: str
        """
        
        

        self._name = None
        self._protocols = None
        self._ciphers = None
        self._project_id = None
        self.discriminator = None

        self.name = name
        self.protocols = protocols
        self.ciphers = ciphers
        self.project_id = project_id

    @property
    def name(self):
        """Gets the name of this SystemSecurityPolicy.

        系统安全策略的名称。

        :return: The name of this SystemSecurityPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemSecurityPolicy.

        系统安全策略的名称。

        :param name: The name of this SystemSecurityPolicy.
        :type name: str
        """
        self._name = name

    @property
    def protocols(self):
        """Gets the protocols of this SystemSecurityPolicy.

        系统安全策略的TLS协议列表。

        :return: The protocols of this SystemSecurityPolicy.
        :rtype: str
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this SystemSecurityPolicy.

        系统安全策略的TLS协议列表。

        :param protocols: The protocols of this SystemSecurityPolicy.
        :type protocols: str
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        """Gets the ciphers of this SystemSecurityPolicy.

        系统安全策略的加密套件列表。

        :return: The ciphers of this SystemSecurityPolicy.
        :rtype: str
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this SystemSecurityPolicy.

        系统安全策略的加密套件列表。

        :param ciphers: The ciphers of this SystemSecurityPolicy.
        :type ciphers: str
        """
        self._ciphers = ciphers

    @property
    def project_id(self):
        """Gets the project_id of this SystemSecurityPolicy.

        项目id。

        :return: The project_id of this SystemSecurityPolicy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SystemSecurityPolicy.

        项目id。

        :param project_id: The project_id of this SystemSecurityPolicy.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, SystemSecurityPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
