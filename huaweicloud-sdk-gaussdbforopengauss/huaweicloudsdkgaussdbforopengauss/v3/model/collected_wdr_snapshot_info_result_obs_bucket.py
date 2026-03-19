# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectedWdrSnapshotInfoResultObsBucket:

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
        'type': 'str',
        'url': 'str',
        'port': 'int',
        'domain_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'url': 'url',
        'port': 'port',
        'domain_id': 'domain_id'
    }

    def __init__(self, name=None, type=None, url=None, port=None, domain_id=None):
        r"""CollectedWdrSnapshotInfoResultObsBucket

        The model defined in huaweicloud sdk

        :param name: **参数解释**： OBS桶名称。 **取值范围**： 不涉及。
        :type name: str
        :param type: **参数解释**： OBS桶类型。 **取值范围**： - common：公共桶。 - aps：智能运维专用桶。
        :type type: str
        :param url: **参数解释**： OBS服务访问地址。 **取值范围**： 不涉及。
        :type url: str
        :param port: **参数解释**： OBS服务端口号。 **取值范围**： 不涉及。
        :type port: int
        :param domain_id: **参数解释**： 最终租户ID。 **取值范围**： 不涉及。
        :type domain_id: str
        """
        
        

        self._name = None
        self._type = None
        self._url = None
        self._port = None
        self._domain_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if port is not None:
            self.port = port
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS桶名称。 **取值范围**： 不涉及。

        :return: The name of this CollectedWdrSnapshotInfoResultObsBucket.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS桶名称。 **取值范围**： 不涉及。

        :param name: The name of this CollectedWdrSnapshotInfoResultObsBucket.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS桶类型。 **取值范围**： - common：公共桶。 - aps：智能运维专用桶。

        :return: The type of this CollectedWdrSnapshotInfoResultObsBucket.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS桶类型。 **取值范围**： - common：公共桶。 - aps：智能运维专用桶。

        :param type: The type of this CollectedWdrSnapshotInfoResultObsBucket.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        r"""Gets the url of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS服务访问地址。 **取值范围**： 不涉及。

        :return: The url of this CollectedWdrSnapshotInfoResultObsBucket.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS服务访问地址。 **取值范围**： 不涉及。

        :param url: The url of this CollectedWdrSnapshotInfoResultObsBucket.
        :type url: str
        """
        self._url = url

    @property
    def port(self):
        r"""Gets the port of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS服务端口号。 **取值范围**： 不涉及。

        :return: The port of this CollectedWdrSnapshotInfoResultObsBucket.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： OBS服务端口号。 **取值范围**： 不涉及。

        :param port: The port of this CollectedWdrSnapshotInfoResultObsBucket.
        :type port: int
        """
        self._port = port

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： 最终租户ID。 **取值范围**： 不涉及。

        :return: The domain_id of this CollectedWdrSnapshotInfoResultObsBucket.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CollectedWdrSnapshotInfoResultObsBucket.

        **参数解释**： 最终租户ID。 **取值范围**： 不涉及。

        :param domain_id: The domain_id of this CollectedWdrSnapshotInfoResultObsBucket.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, CollectedWdrSnapshotInfoResultObsBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
