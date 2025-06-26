# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceRepositoryResponse(SdkResponse):

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
        'name': 'str',
        'namespace_name': 'str',
        'namespace_id': 'int',
        'tag_count': 'int',
        'pull_count': 'int',
        'artifact_count': 'int',
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'namespace_name': 'namespace_name',
        'namespace_id': 'namespace_id',
        'tag_count': 'tag_count',
        'pull_count': 'pull_count',
        'artifact_count': 'artifact_count',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, namespace_name=None, namespace_id=None, tag_count=None, pull_count=None, artifact_count=None, description=None, created_at=None, updated_at=None):
        r"""ShowInstanceRepositoryResponse

        The model defined in huaweicloud sdk

        :param id: 仓库ID
        :type id: int
        :param name: 仓库名称
        :type name: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param namespace_id: 命名空间ID
        :type namespace_id: int
        :param tag_count: 仓库内的制品版本数量
        :type tag_count: int
        :param pull_count: 被下载总次数
        :type pull_count: int
        :param artifact_count: 制品包总数
        :type artifact_count: int
        :param description: 描述
        :type description: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        super(ShowInstanceRepositoryResponse, self).__init__()

        self._id = None
        self._name = None
        self._namespace_name = None
        self._namespace_id = None
        self._tag_count = None
        self._pull_count = None
        self._artifact_count = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if tag_count is not None:
            self.tag_count = tag_count
        if pull_count is not None:
            self.pull_count = pull_count
        if artifact_count is not None:
            self.artifact_count = artifact_count
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceRepositoryResponse.

        仓库ID

        :return: The id of this ShowInstanceRepositoryResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceRepositoryResponse.

        仓库ID

        :param id: The id of this ShowInstanceRepositoryResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceRepositoryResponse.

        仓库名称

        :return: The name of this ShowInstanceRepositoryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceRepositoryResponse.

        仓库名称

        :param name: The name of this ShowInstanceRepositoryResponse.
        :type name: str
        """
        self._name = name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ShowInstanceRepositoryResponse.

        命名空间名称

        :return: The namespace_name of this ShowInstanceRepositoryResponse.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ShowInstanceRepositoryResponse.

        命名空间名称

        :param namespace_name: The namespace_name of this ShowInstanceRepositoryResponse.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this ShowInstanceRepositoryResponse.

        命名空间ID

        :return: The namespace_id of this ShowInstanceRepositoryResponse.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this ShowInstanceRepositoryResponse.

        命名空间ID

        :param namespace_id: The namespace_id of this ShowInstanceRepositoryResponse.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def tag_count(self):
        r"""Gets the tag_count of this ShowInstanceRepositoryResponse.

        仓库内的制品版本数量

        :return: The tag_count of this ShowInstanceRepositoryResponse.
        :rtype: int
        """
        return self._tag_count

    @tag_count.setter
    def tag_count(self, tag_count):
        r"""Sets the tag_count of this ShowInstanceRepositoryResponse.

        仓库内的制品版本数量

        :param tag_count: The tag_count of this ShowInstanceRepositoryResponse.
        :type tag_count: int
        """
        self._tag_count = tag_count

    @property
    def pull_count(self):
        r"""Gets the pull_count of this ShowInstanceRepositoryResponse.

        被下载总次数

        :return: The pull_count of this ShowInstanceRepositoryResponse.
        :rtype: int
        """
        return self._pull_count

    @pull_count.setter
    def pull_count(self, pull_count):
        r"""Sets the pull_count of this ShowInstanceRepositoryResponse.

        被下载总次数

        :param pull_count: The pull_count of this ShowInstanceRepositoryResponse.
        :type pull_count: int
        """
        self._pull_count = pull_count

    @property
    def artifact_count(self):
        r"""Gets the artifact_count of this ShowInstanceRepositoryResponse.

        制品包总数

        :return: The artifact_count of this ShowInstanceRepositoryResponse.
        :rtype: int
        """
        return self._artifact_count

    @artifact_count.setter
    def artifact_count(self, artifact_count):
        r"""Sets the artifact_count of this ShowInstanceRepositoryResponse.

        制品包总数

        :param artifact_count: The artifact_count of this ShowInstanceRepositoryResponse.
        :type artifact_count: int
        """
        self._artifact_count = artifact_count

    @property
    def description(self):
        r"""Gets the description of this ShowInstanceRepositoryResponse.

        描述

        :return: The description of this ShowInstanceRepositoryResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowInstanceRepositoryResponse.

        描述

        :param description: The description of this ShowInstanceRepositoryResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowInstanceRepositoryResponse.

        创建时间

        :return: The created_at of this ShowInstanceRepositoryResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowInstanceRepositoryResponse.

        创建时间

        :param created_at: The created_at of this ShowInstanceRepositoryResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowInstanceRepositoryResponse.

        更新时间

        :return: The updated_at of this ShowInstanceRepositoryResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowInstanceRepositoryResponse.

        更新时间

        :param updated_at: The updated_at of this ShowInstanceRepositoryResponse.
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
        if not isinstance(other, ShowInstanceRepositoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
