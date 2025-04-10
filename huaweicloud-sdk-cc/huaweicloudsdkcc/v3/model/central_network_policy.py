# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkPolicy:

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
        'created_at': 'datetime',
        'domain_id': 'str',
        'state': 'CentralNetworkPolicyStateEnum',
        'central_network_id': 'str',
        'document_template_version': 'DocumentTemplateVersionEnum',
        'is_applied': 'bool',
        'version': 'int',
        'document': 'CentralNetworkPolicyDocument'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'domain_id': 'domain_id',
        'state': 'state',
        'central_network_id': 'central_network_id',
        'document_template_version': 'document_template_version',
        'is_applied': 'is_applied',
        'version': 'version',
        'document': 'document'
    }

    def __init__(self, id=None, created_at=None, domain_id=None, state=None, central_network_id=None, document_template_version=None, is_applied=None, version=None, document=None):
        r"""CentralNetworkPolicy

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicyStateEnum`
        :param central_network_id: 中心网络ID。
        :type central_network_id: str
        :param document_template_version: 
        :type document_template_version: :class:`huaweicloudsdkcc.v3.DocumentTemplateVersionEnum`
        :param is_applied: 是否被应用。
        :type is_applied: bool
        :param version: 中心网络策略的版本。
        :type version: int
        :param document: 
        :type document: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicyDocument`
        """
        
        

        self._id = None
        self._created_at = None
        self._domain_id = None
        self._state = None
        self._central_network_id = None
        self._document_template_version = None
        self._is_applied = None
        self._version = None
        self._document = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        self.domain_id = domain_id
        self.state = state
        self.central_network_id = central_network_id
        self.document_template_version = document_template_version
        self.is_applied = is_applied
        self.version = version
        self.document = document

    @property
    def id(self):
        r"""Gets the id of this CentralNetworkPolicy.

        实例ID。

        :return: The id of this CentralNetworkPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CentralNetworkPolicy.

        实例ID。

        :param id: The id of this CentralNetworkPolicy.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this CentralNetworkPolicy.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this CentralNetworkPolicy.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CentralNetworkPolicy.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this CentralNetworkPolicy.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CentralNetworkPolicy.

        实例所属账号ID。

        :return: The domain_id of this CentralNetworkPolicy.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CentralNetworkPolicy.

        实例所属账号ID。

        :param domain_id: The domain_id of this CentralNetworkPolicy.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def state(self):
        r"""Gets the state of this CentralNetworkPolicy.

        :return: The state of this CentralNetworkPolicy.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicyStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CentralNetworkPolicy.

        :param state: The state of this CentralNetworkPolicy.
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicyStateEnum`
        """
        self._state = state

    @property
    def central_network_id(self):
        r"""Gets the central_network_id of this CentralNetworkPolicy.

        中心网络ID。

        :return: The central_network_id of this CentralNetworkPolicy.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        r"""Sets the central_network_id of this CentralNetworkPolicy.

        中心网络ID。

        :param central_network_id: The central_network_id of this CentralNetworkPolicy.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def document_template_version(self):
        r"""Gets the document_template_version of this CentralNetworkPolicy.

        :return: The document_template_version of this CentralNetworkPolicy.
        :rtype: :class:`huaweicloudsdkcc.v3.DocumentTemplateVersionEnum`
        """
        return self._document_template_version

    @document_template_version.setter
    def document_template_version(self, document_template_version):
        r"""Sets the document_template_version of this CentralNetworkPolicy.

        :param document_template_version: The document_template_version of this CentralNetworkPolicy.
        :type document_template_version: :class:`huaweicloudsdkcc.v3.DocumentTemplateVersionEnum`
        """
        self._document_template_version = document_template_version

    @property
    def is_applied(self):
        r"""Gets the is_applied of this CentralNetworkPolicy.

        是否被应用。

        :return: The is_applied of this CentralNetworkPolicy.
        :rtype: bool
        """
        return self._is_applied

    @is_applied.setter
    def is_applied(self, is_applied):
        r"""Sets the is_applied of this CentralNetworkPolicy.

        是否被应用。

        :param is_applied: The is_applied of this CentralNetworkPolicy.
        :type is_applied: bool
        """
        self._is_applied = is_applied

    @property
    def version(self):
        r"""Gets the version of this CentralNetworkPolicy.

        中心网络策略的版本。

        :return: The version of this CentralNetworkPolicy.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CentralNetworkPolicy.

        中心网络策略的版本。

        :param version: The version of this CentralNetworkPolicy.
        :type version: int
        """
        self._version = version

    @property
    def document(self):
        r"""Gets the document of this CentralNetworkPolicy.

        :return: The document of this CentralNetworkPolicy.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicyDocument`
        """
        return self._document

    @document.setter
    def document(self, document):
        r"""Sets the document of this CentralNetworkPolicy.

        :param document: The document of this CentralNetworkPolicy.
        :type document: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicyDocument`
        """
        self._document = document

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
        if not isinstance(other, CentralNetworkPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
