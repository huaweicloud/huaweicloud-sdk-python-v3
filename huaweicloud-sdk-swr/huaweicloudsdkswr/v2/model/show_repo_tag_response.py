# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepoTagResponse(SdkResponse):

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
        'repo_id': 'int',
        'tag': 'str',
        'image_id': 'str',
        'manifest': 'str',
        'digest': 'str',
        'schema': 'int',
        'path': 'str',
        'internal_path': 'str',
        'size': 'int',
        'is_trusted': 'bool',
        'created': 'str',
        'updated': 'str',
        'domain_id': 'str',
        'tag_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'repo_id': 'repo_id',
        'tag': 'tag',
        'image_id': 'image_id',
        'manifest': 'manifest',
        'digest': 'digest',
        'schema': 'schema',
        'path': 'path',
        'internal_path': 'internal_path',
        'size': 'size',
        'is_trusted': 'is_trusted',
        'created': 'created',
        'updated': 'updated',
        'domain_id': 'domain_id',
        'tag_type': 'tag_type'
    }

    def __init__(self, id=None, repo_id=None, tag=None, image_id=None, manifest=None, digest=None, schema=None, path=None, internal_path=None, size=None, is_trusted=None, created=None, updated=None, domain_id=None, tag_type=None):
        r"""ShowRepoTagResponse

        The model defined in huaweicloud sdk

        :param id: tag编号
        :type id: int
        :param repo_id: 仓库编号
        :type repo_id: int
        :param tag: tag版本名称
        :type tag: str
        :param image_id: 镜像id
        :type image_id: str
        :param manifest: 镜像manifest
        :type manifest: str
        :param digest: 镜像hash值
        :type digest: str
        :param schema: docker协议版本，值为1或2
        :type schema: int
        :param path: 镜像pull地址，格式为swr.cn-north-1.myhuaweicloud.com/namespace/repository:tag
        :type path: str
        :param internal_path: cce集群内镜像pull路径，格式为 10.125.0.198:20202/namespace/repository:tag
        :type internal_path: str
        :param size: 镜像大小，0 ~ 9223372036854775807
        :type size: int
        :param is_trusted: 默认值为false
        :type is_trusted: bool
        :param created: 镜像创建时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type created: str
        :param updated: 镜像更新时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type updated: str
        :param domain_id: 帐号ID
        :type domain_id: str
        :param tag_type: 0：manifest类型；1：manifest list类型
        :type tag_type: int
        """
        
        super(ShowRepoTagResponse, self).__init__()

        self._id = None
        self._repo_id = None
        self._tag = None
        self._image_id = None
        self._manifest = None
        self._digest = None
        self._schema = None
        self._path = None
        self._internal_path = None
        self._size = None
        self._is_trusted = None
        self._created = None
        self._updated = None
        self._domain_id = None
        self._tag_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repo_id is not None:
            self.repo_id = repo_id
        if tag is not None:
            self.tag = tag
        if image_id is not None:
            self.image_id = image_id
        if manifest is not None:
            self.manifest = manifest
        if digest is not None:
            self.digest = digest
        if schema is not None:
            self.schema = schema
        if path is not None:
            self.path = path
        if internal_path is not None:
            self.internal_path = internal_path
        if size is not None:
            self.size = size
        if is_trusted is not None:
            self.is_trusted = is_trusted
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if domain_id is not None:
            self.domain_id = domain_id
        if tag_type is not None:
            self.tag_type = tag_type

    @property
    def id(self):
        r"""Gets the id of this ShowRepoTagResponse.

        tag编号

        :return: The id of this ShowRepoTagResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowRepoTagResponse.

        tag编号

        :param id: The id of this ShowRepoTagResponse.
        :type id: int
        """
        self._id = id

    @property
    def repo_id(self):
        r"""Gets the repo_id of this ShowRepoTagResponse.

        仓库编号

        :return: The repo_id of this ShowRepoTagResponse.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this ShowRepoTagResponse.

        仓库编号

        :param repo_id: The repo_id of this ShowRepoTagResponse.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def tag(self):
        r"""Gets the tag of this ShowRepoTagResponse.

        tag版本名称

        :return: The tag of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ShowRepoTagResponse.

        tag版本名称

        :param tag: The tag of this ShowRepoTagResponse.
        :type tag: str
        """
        self._tag = tag

    @property
    def image_id(self):
        r"""Gets the image_id of this ShowRepoTagResponse.

        镜像id

        :return: The image_id of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ShowRepoTagResponse.

        镜像id

        :param image_id: The image_id of this ShowRepoTagResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def manifest(self):
        r"""Gets the manifest of this ShowRepoTagResponse.

        镜像manifest

        :return: The manifest of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        r"""Sets the manifest of this ShowRepoTagResponse.

        镜像manifest

        :param manifest: The manifest of this ShowRepoTagResponse.
        :type manifest: str
        """
        self._manifest = manifest

    @property
    def digest(self):
        r"""Gets the digest of this ShowRepoTagResponse.

        镜像hash值

        :return: The digest of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this ShowRepoTagResponse.

        镜像hash值

        :param digest: The digest of this ShowRepoTagResponse.
        :type digest: str
        """
        self._digest = digest

    @property
    def schema(self):
        r"""Gets the schema of this ShowRepoTagResponse.

        docker协议版本，值为1或2

        :return: The schema of this ShowRepoTagResponse.
        :rtype: int
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowRepoTagResponse.

        docker协议版本，值为1或2

        :param schema: The schema of this ShowRepoTagResponse.
        :type schema: int
        """
        self._schema = schema

    @property
    def path(self):
        r"""Gets the path of this ShowRepoTagResponse.

        镜像pull地址，格式为swr.cn-north-1.myhuaweicloud.com/namespace/repository:tag

        :return: The path of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowRepoTagResponse.

        镜像pull地址，格式为swr.cn-north-1.myhuaweicloud.com/namespace/repository:tag

        :param path: The path of this ShowRepoTagResponse.
        :type path: str
        """
        self._path = path

    @property
    def internal_path(self):
        r"""Gets the internal_path of this ShowRepoTagResponse.

        cce集群内镜像pull路径，格式为 10.125.0.198:20202/namespace/repository:tag

        :return: The internal_path of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._internal_path

    @internal_path.setter
    def internal_path(self, internal_path):
        r"""Sets the internal_path of this ShowRepoTagResponse.

        cce集群内镜像pull路径，格式为 10.125.0.198:20202/namespace/repository:tag

        :param internal_path: The internal_path of this ShowRepoTagResponse.
        :type internal_path: str
        """
        self._internal_path = internal_path

    @property
    def size(self):
        r"""Gets the size of this ShowRepoTagResponse.

        镜像大小，0 ~ 9223372036854775807

        :return: The size of this ShowRepoTagResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowRepoTagResponse.

        镜像大小，0 ~ 9223372036854775807

        :param size: The size of this ShowRepoTagResponse.
        :type size: int
        """
        self._size = size

    @property
    def is_trusted(self):
        r"""Gets the is_trusted of this ShowRepoTagResponse.

        默认值为false

        :return: The is_trusted of this ShowRepoTagResponse.
        :rtype: bool
        """
        return self._is_trusted

    @is_trusted.setter
    def is_trusted(self, is_trusted):
        r"""Sets the is_trusted of this ShowRepoTagResponse.

        默认值为false

        :param is_trusted: The is_trusted of this ShowRepoTagResponse.
        :type is_trusted: bool
        """
        self._is_trusted = is_trusted

    @property
    def created(self):
        r"""Gets the created of this ShowRepoTagResponse.

        镜像创建时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The created of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ShowRepoTagResponse.

        镜像创建时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param created: The created of this ShowRepoTagResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ShowRepoTagResponse.

        镜像更新时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The updated of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowRepoTagResponse.

        镜像更新时间，UTC时间格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param updated: The updated of this ShowRepoTagResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowRepoTagResponse.

        帐号ID

        :return: The domain_id of this ShowRepoTagResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowRepoTagResponse.

        帐号ID

        :param domain_id: The domain_id of this ShowRepoTagResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def tag_type(self):
        r"""Gets the tag_type of this ShowRepoTagResponse.

        0：manifest类型；1：manifest list类型

        :return: The tag_type of this ShowRepoTagResponse.
        :rtype: int
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this ShowRepoTagResponse.

        0：manifest类型；1：manifest list类型

        :param tag_type: The tag_type of this ShowRepoTagResponse.
        :type tag_type: int
        """
        self._tag_type = tag_type

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
        if not isinstance(other, ShowRepoTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
