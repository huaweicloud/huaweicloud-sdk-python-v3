# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Artifact:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'digest': 'str',
        'id': 'int',
        'repository_id': 'int',
        'repository_name': 'str',
        'type': 'str',
        'namespace_id': 'int',
        'media_type': 'str',
        'manifest_media_type': 'str',
        'pull_time': 'str',
        'push_time': 'str',
        'size': 'int',
        'tags': 'list[ArtifactTag]'
    }

    attribute_map = {
        'digest': 'digest',
        'id': 'id',
        'repository_id': 'repository_id',
        'repository_name': 'repository_name',
        'type': 'type',
        'namespace_id': 'namespace_id',
        'media_type': 'media_type',
        'manifest_media_type': 'manifest_media_type',
        'pull_time': 'pull_time',
        'push_time': 'push_time',
        'size': 'size',
        'tags': 'tags'
    }

    def __init__(self, digest=None, id=None, repository_id=None, repository_name=None, type=None, namespace_id=None, media_type=None, manifest_media_type=None, pull_time=None, push_time=None, size=None, tags=None):
        r"""Artifact

        The model defined in huaweicloud sdk

        :param digest: 制品摘要
        :type digest: str
        :param id: 制品ID
        :type id: int
        :param repository_id: 仓库ID
        :type repository_id: int
        :param repository_name: 仓库名称
        :type repository_name: str
        :param type: 制品类型
        :type type: str
        :param namespace_id: 命名空间ID
        :type namespace_id: int
        :param media_type: 制品MIME类型
        :type media_type: str
        :param manifest_media_type: 制品元数据MIME类型
        :type manifest_media_type: str
        :param pull_time: 最近一次拉取时间
        :type pull_time: str
        :param push_time: 最近一次上传时间
        :type push_time: str
        :param size: 制品大小，单位：Byte
        :type size: int
        :param tags: 制品版本的Tag列表
        :type tags: list[:class:`huaweicloudsdkswr.v2.ArtifactTag`]
        """
        
        

        self._digest = None
        self._id = None
        self._repository_id = None
        self._repository_name = None
        self._type = None
        self._namespace_id = None
        self._media_type = None
        self._manifest_media_type = None
        self._pull_time = None
        self._push_time = None
        self._size = None
        self._tags = None
        self.discriminator = None

        if digest is not None:
            self.digest = digest
        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if repository_name is not None:
            self.repository_name = repository_name
        if type is not None:
            self.type = type
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if media_type is not None:
            self.media_type = media_type
        if manifest_media_type is not None:
            self.manifest_media_type = manifest_media_type
        if pull_time is not None:
            self.pull_time = pull_time
        if push_time is not None:
            self.push_time = push_time
        if size is not None:
            self.size = size
        if tags is not None:
            self.tags = tags

    @property
    def digest(self):
        r"""Gets the digest of this Artifact.

        制品摘要

        :return: The digest of this Artifact.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this Artifact.

        制品摘要

        :param digest: The digest of this Artifact.
        :type digest: str
        """
        self._digest = digest

    @property
    def id(self):
        r"""Gets the id of this Artifact.

        制品ID

        :return: The id of this Artifact.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Artifact.

        制品ID

        :param id: The id of this Artifact.
        :type id: int
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this Artifact.

        仓库ID

        :return: The repository_id of this Artifact.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this Artifact.

        仓库ID

        :param repository_id: The repository_id of this Artifact.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def repository_name(self):
        r"""Gets the repository_name of this Artifact.

        仓库名称

        :return: The repository_name of this Artifact.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this Artifact.

        仓库名称

        :param repository_name: The repository_name of this Artifact.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def type(self):
        r"""Gets the type of this Artifact.

        制品类型

        :return: The type of this Artifact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Artifact.

        制品类型

        :param type: The type of this Artifact.
        :type type: str
        """
        self._type = type

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this Artifact.

        命名空间ID

        :return: The namespace_id of this Artifact.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this Artifact.

        命名空间ID

        :param namespace_id: The namespace_id of this Artifact.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def media_type(self):
        r"""Gets the media_type of this Artifact.

        制品MIME类型

        :return: The media_type of this Artifact.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        r"""Sets the media_type of this Artifact.

        制品MIME类型

        :param media_type: The media_type of this Artifact.
        :type media_type: str
        """
        self._media_type = media_type

    @property
    def manifest_media_type(self):
        r"""Gets the manifest_media_type of this Artifact.

        制品元数据MIME类型

        :return: The manifest_media_type of this Artifact.
        :rtype: str
        """
        return self._manifest_media_type

    @manifest_media_type.setter
    def manifest_media_type(self, manifest_media_type):
        r"""Sets the manifest_media_type of this Artifact.

        制品元数据MIME类型

        :param manifest_media_type: The manifest_media_type of this Artifact.
        :type manifest_media_type: str
        """
        self._manifest_media_type = manifest_media_type

    @property
    def pull_time(self):
        r"""Gets the pull_time of this Artifact.

        最近一次拉取时间

        :return: The pull_time of this Artifact.
        :rtype: str
        """
        return self._pull_time

    @pull_time.setter
    def pull_time(self, pull_time):
        r"""Sets the pull_time of this Artifact.

        最近一次拉取时间

        :param pull_time: The pull_time of this Artifact.
        :type pull_time: str
        """
        self._pull_time = pull_time

    @property
    def push_time(self):
        r"""Gets the push_time of this Artifact.

        最近一次上传时间

        :return: The push_time of this Artifact.
        :rtype: str
        """
        return self._push_time

    @push_time.setter
    def push_time(self, push_time):
        r"""Sets the push_time of this Artifact.

        最近一次上传时间

        :param push_time: The push_time of this Artifact.
        :type push_time: str
        """
        self._push_time = push_time

    @property
    def size(self):
        r"""Gets the size of this Artifact.

        制品大小，单位：Byte

        :return: The size of this Artifact.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Artifact.

        制品大小，单位：Byte

        :param size: The size of this Artifact.
        :type size: int
        """
        self._size = size

    @property
    def tags(self):
        r"""Gets the tags of this Artifact.

        制品版本的Tag列表

        :return: The tags of this Artifact.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ArtifactTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Artifact.

        制品版本的Tag列表

        :param tags: The tags of this Artifact.
        :type tags: list[:class:`huaweicloudsdkswr.v2.ArtifactTag`]
        """
        self._tags = tags

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
        if not isinstance(other, Artifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
