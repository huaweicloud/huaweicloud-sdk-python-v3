# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessoryListAccessories:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'domain_id': 'str',
        'namespace_name': 'str',
        'repo_name': 'str',
        'sig_tag': 'str',
        'sig_digest': 'str',
        'target_digest': 'str',
        'size': 'int',
        'type': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'namespace_name': 'namespace_name',
        'repo_name': 'repo_name',
        'sig_tag': 'sig_tag',
        'sig_digest': 'sig_digest',
        'target_digest': 'target_digest',
        'size': 'size',
        'type': 'type',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, domain_id=None, namespace_name=None, repo_name=None, sig_tag=None, sig_digest=None, target_digest=None, size=None, type=None, created_at=None, updated_at=None):
        r"""AccessoryListAccessories

        The model defined in huaweicloud sdk

        :param id: 附件编号
        :type id: int
        :param domain_id: 附件所属的租户ID
        :type domain_id: str
        :param namespace_name: 附件所属的组织
        :type namespace_name: str
        :param repo_name: 附件所属的仓库
        :type repo_name: str
        :param sig_tag: 附件镜像的版本
        :type sig_tag: str
        :param sig_digest: 附件镜像的hash值
        :type sig_digest: str
        :param target_digest: 附件关联镜像的hash值
        :type target_digest: str
        :param size: 附件镜像的大小
        :type size: int
        :param type: 附件的类型
        :type type: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._domain_id = None
        self._namespace_name = None
        self._repo_name = None
        self._sig_tag = None
        self._sig_digest = None
        self._target_digest = None
        self._size = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if repo_name is not None:
            self.repo_name = repo_name
        if sig_tag is not None:
            self.sig_tag = sig_tag
        if sig_digest is not None:
            self.sig_digest = sig_digest
        if target_digest is not None:
            self.target_digest = target_digest
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this AccessoryListAccessories.

        附件编号

        :return: The id of this AccessoryListAccessories.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AccessoryListAccessories.

        附件编号

        :param id: The id of this AccessoryListAccessories.
        :type id: int
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AccessoryListAccessories.

        附件所属的租户ID

        :return: The domain_id of this AccessoryListAccessories.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AccessoryListAccessories.

        附件所属的租户ID

        :param domain_id: The domain_id of this AccessoryListAccessories.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this AccessoryListAccessories.

        附件所属的组织

        :return: The namespace_name of this AccessoryListAccessories.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this AccessoryListAccessories.

        附件所属的组织

        :param namespace_name: The namespace_name of this AccessoryListAccessories.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def repo_name(self):
        r"""Gets the repo_name of this AccessoryListAccessories.

        附件所属的仓库

        :return: The repo_name of this AccessoryListAccessories.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this AccessoryListAccessories.

        附件所属的仓库

        :param repo_name: The repo_name of this AccessoryListAccessories.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def sig_tag(self):
        r"""Gets the sig_tag of this AccessoryListAccessories.

        附件镜像的版本

        :return: The sig_tag of this AccessoryListAccessories.
        :rtype: str
        """
        return self._sig_tag

    @sig_tag.setter
    def sig_tag(self, sig_tag):
        r"""Sets the sig_tag of this AccessoryListAccessories.

        附件镜像的版本

        :param sig_tag: The sig_tag of this AccessoryListAccessories.
        :type sig_tag: str
        """
        self._sig_tag = sig_tag

    @property
    def sig_digest(self):
        r"""Gets the sig_digest of this AccessoryListAccessories.

        附件镜像的hash值

        :return: The sig_digest of this AccessoryListAccessories.
        :rtype: str
        """
        return self._sig_digest

    @sig_digest.setter
    def sig_digest(self, sig_digest):
        r"""Sets the sig_digest of this AccessoryListAccessories.

        附件镜像的hash值

        :param sig_digest: The sig_digest of this AccessoryListAccessories.
        :type sig_digest: str
        """
        self._sig_digest = sig_digest

    @property
    def target_digest(self):
        r"""Gets the target_digest of this AccessoryListAccessories.

        附件关联镜像的hash值

        :return: The target_digest of this AccessoryListAccessories.
        :rtype: str
        """
        return self._target_digest

    @target_digest.setter
    def target_digest(self, target_digest):
        r"""Sets the target_digest of this AccessoryListAccessories.

        附件关联镜像的hash值

        :param target_digest: The target_digest of this AccessoryListAccessories.
        :type target_digest: str
        """
        self._target_digest = target_digest

    @property
    def size(self):
        r"""Gets the size of this AccessoryListAccessories.

        附件镜像的大小

        :return: The size of this AccessoryListAccessories.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this AccessoryListAccessories.

        附件镜像的大小

        :param size: The size of this AccessoryListAccessories.
        :type size: int
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this AccessoryListAccessories.

        附件的类型

        :return: The type of this AccessoryListAccessories.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AccessoryListAccessories.

        附件的类型

        :param type: The type of this AccessoryListAccessories.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        r"""Gets the created_at of this AccessoryListAccessories.

        创建时间

        :return: The created_at of this AccessoryListAccessories.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AccessoryListAccessories.

        创建时间

        :param created_at: The created_at of this AccessoryListAccessories.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AccessoryListAccessories.

        更新时间

        :return: The updated_at of this AccessoryListAccessories.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AccessoryListAccessories.

        更新时间

        :param updated_at: The updated_at of this AccessoryListAccessories.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, AccessoryListAccessories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
