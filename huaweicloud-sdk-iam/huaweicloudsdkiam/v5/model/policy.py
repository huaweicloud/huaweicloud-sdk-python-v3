# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_type': 'PolicyType',
        'policy_name': 'str',
        'policy_id': 'str',
        'urn': 'str',
        'path': 'str',
        'default_version_id': 'str',
        'attachment_count': 'int',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'policy_type': 'policy_type',
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'urn': 'urn',
        'path': 'path',
        'default_version_id': 'default_version_id',
        'attachment_count': 'attachment_count',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, policy_type=None, policy_name=None, policy_id=None, urn=None, path=None, default_version_id=None, attachment_count=None, description=None, created_at=None, updated_at=None):
        r"""Policy

        The model defined in huaweicloud sdk

        :param policy_type: 
        :type policy_type: :class:`huaweicloudsdkiam.v5.PolicyType`
        :param policy_name: 身份策略名称，长度为1到128个字符，只包含字母、数字、\&quot;_\&quot;、\&quot;+\&quot;、\&quot;&#x3D;\&quot;、\&quot;.\&quot;、\&quot;@\&quot;和\&quot;-\&quot;的字符串。
        :type policy_name: str
        :param policy_id: 身份策略ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type policy_id: str
        :param urn: 统一资源名称。
        :type urn: str
        :param path: 资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\&quot;.\&quot;、\&quot;,\&quot;、\&quot;+\&quot;、\&quot;@\&quot;、\&quot;&#x3D;\&quot;、\&quot;_\&quot;或\&quot;-\&quot;，并以\&quot;/\&quot;结尾，例如\&quot;foo/bar/\&quot;。
        :type path: str
        :param default_version_id: 默认版本号。
        :type default_version_id: str
        :param attachment_count: 附加了本身份策略的实体数量。
        :type attachment_count: int
        :param description: 身份策略描述。
        :type description: str
        :param created_at: 身份策略创建时间。
        :type created_at: datetime
        :param updated_at: 身份策略默认版本最近一次的更新时间。
        :type updated_at: datetime
        """
        
        

        self._policy_type = None
        self._policy_name = None
        self._policy_id = None
        self._urn = None
        self._path = None
        self._default_version_id = None
        self._attachment_count = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.policy_type = policy_type
        self.policy_name = policy_name
        self.policy_id = policy_id
        self.urn = urn
        self.path = path
        self.default_version_id = default_version_id
        self.attachment_count = attachment_count
        if description is not None:
            self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def policy_type(self):
        r"""Gets the policy_type of this Policy.

        :return: The policy_type of this Policy.
        :rtype: :class:`huaweicloudsdkiam.v5.PolicyType`
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this Policy.

        :param policy_type: The policy_type of this Policy.
        :type policy_type: :class:`huaweicloudsdkiam.v5.PolicyType`
        """
        self._policy_type = policy_type

    @property
    def policy_name(self):
        r"""Gets the policy_name of this Policy.

        身份策略名称，长度为1到128个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\".\"、\"@\"和\"-\"的字符串。

        :return: The policy_name of this Policy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this Policy.

        身份策略名称，长度为1到128个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\".\"、\"@\"和\"-\"的字符串。

        :param policy_name: The policy_name of this Policy.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this Policy.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The policy_id of this Policy.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this Policy.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param policy_id: The policy_id of this Policy.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def urn(self):
        r"""Gets the urn of this Policy.

        统一资源名称。

        :return: The urn of this Policy.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this Policy.

        统一资源名称。

        :param urn: The urn of this Policy.
        :type urn: str
        """
        self._urn = urn

    @property
    def path(self):
        r"""Gets the path of this Policy.

        资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :return: The path of this Policy.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this Policy.

        资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :param path: The path of this Policy.
        :type path: str
        """
        self._path = path

    @property
    def default_version_id(self):
        r"""Gets the default_version_id of this Policy.

        默认版本号。

        :return: The default_version_id of this Policy.
        :rtype: str
        """
        return self._default_version_id

    @default_version_id.setter
    def default_version_id(self, default_version_id):
        r"""Sets the default_version_id of this Policy.

        默认版本号。

        :param default_version_id: The default_version_id of this Policy.
        :type default_version_id: str
        """
        self._default_version_id = default_version_id

    @property
    def attachment_count(self):
        r"""Gets the attachment_count of this Policy.

        附加了本身份策略的实体数量。

        :return: The attachment_count of this Policy.
        :rtype: int
        """
        return self._attachment_count

    @attachment_count.setter
    def attachment_count(self, attachment_count):
        r"""Sets the attachment_count of this Policy.

        附加了本身份策略的实体数量。

        :param attachment_count: The attachment_count of this Policy.
        :type attachment_count: int
        """
        self._attachment_count = attachment_count

    @property
    def description(self):
        r"""Gets the description of this Policy.

        身份策略描述。

        :return: The description of this Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Policy.

        身份策略描述。

        :param description: The description of this Policy.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this Policy.

        身份策略创建时间。

        :return: The created_at of this Policy.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Policy.

        身份策略创建时间。

        :param created_at: The created_at of this Policy.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Policy.

        身份策略默认版本最近一次的更新时间。

        :return: The updated_at of this Policy.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Policy.

        身份策略默认版本最近一次的更新时间。

        :param updated_at: The updated_at of this Policy.
        :type updated_at: datetime
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
