# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'listeners': 'list[ListenerRef]',
        'protocols': 'list[str]',
        'ciphers': 'list[str]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'listeners': 'listeners',
        'protocols': 'protocols',
        'ciphers': 'ciphers',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, listeners=None, protocols=None, ciphers=None, created_at=None, updated_at=None):
        """SecurityPolicy

        The model defined in huaweicloud sdk

        :param id: 自定义安全安全策略的id。
        :type id: str
        :param project_id: 自定义安全策略的项目id。
        :type project_id: str
        :param name: 自定义安全策略的名称
        :type name: str
        :param description: 自定义安全策略的描述。
        :type description: str
        :param listeners: 自定义安全策略关联的监听器。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        :param protocols: 自定义安全策略的TLS协议列表。
        :type protocols: list[str]
        :param ciphers: 自定义安全策略的加密套件列表。
        :type ciphers: list[str]
        :param created_at: 自定义安全策略的创建时间。
        :type created_at: str
        :param updated_at: 自定义安全策略的更新时间。
        :type updated_at: str
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._listeners = None
        self._protocols = None
        self._ciphers = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.listeners = listeners
        self.protocols = protocols
        self.ciphers = ciphers
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this SecurityPolicy.

        自定义安全安全策略的id。

        :return: The id of this SecurityPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityPolicy.

        自定义安全安全策略的id。

        :param id: The id of this SecurityPolicy.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this SecurityPolicy.

        自定义安全策略的项目id。

        :return: The project_id of this SecurityPolicy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SecurityPolicy.

        自定义安全策略的项目id。

        :param project_id: The project_id of this SecurityPolicy.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this SecurityPolicy.

        自定义安全策略的名称

        :return: The name of this SecurityPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityPolicy.

        自定义安全策略的名称

        :param name: The name of this SecurityPolicy.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecurityPolicy.

        自定义安全策略的描述。

        :return: The description of this SecurityPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityPolicy.

        自定义安全策略的描述。

        :param description: The description of this SecurityPolicy.
        :type description: str
        """
        self._description = description

    @property
    def listeners(self):
        """Gets the listeners of this SecurityPolicy.

        自定义安全策略关联的监听器。

        :return: The listeners of this SecurityPolicy.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this SecurityPolicy.

        自定义安全策略关联的监听器。

        :param listeners: The listeners of this SecurityPolicy.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def protocols(self):
        """Gets the protocols of this SecurityPolicy.

        自定义安全策略的TLS协议列表。

        :return: The protocols of this SecurityPolicy.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this SecurityPolicy.

        自定义安全策略的TLS协议列表。

        :param protocols: The protocols of this SecurityPolicy.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        """Gets the ciphers of this SecurityPolicy.

        自定义安全策略的加密套件列表。

        :return: The ciphers of this SecurityPolicy.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this SecurityPolicy.

        自定义安全策略的加密套件列表。

        :param ciphers: The ciphers of this SecurityPolicy.
        :type ciphers: list[str]
        """
        self._ciphers = ciphers

    @property
    def created_at(self):
        """Gets the created_at of this SecurityPolicy.

        自定义安全策略的创建时间。

        :return: The created_at of this SecurityPolicy.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SecurityPolicy.

        自定义安全策略的创建时间。

        :param created_at: The created_at of this SecurityPolicy.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SecurityPolicy.

        自定义安全策略的更新时间。

        :return: The updated_at of this SecurityPolicy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SecurityPolicy.

        自定义安全策略的更新时间。

        :param updated_at: The updated_at of this SecurityPolicy.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, SecurityPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
