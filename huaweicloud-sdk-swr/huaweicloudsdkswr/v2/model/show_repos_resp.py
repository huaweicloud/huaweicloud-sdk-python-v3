# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReposResp:

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
        'category': 'str',
        'description': 'str',
        'size': 'int',
        'is_public': 'bool',
        'num_images': 'int',
        'num_download': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'logo': 'str',
        'url': 'str',
        'path': 'str',
        'internal_path': 'str',
        'domain_name': 'str',
        'namespace': 'str',
        'tags': 'list[str]',
        'status': 'bool',
        'total_range': 'int'
    }

    attribute_map = {
        'name': 'name',
        'category': 'category',
        'description': 'description',
        'size': 'size',
        'is_public': 'is_public',
        'num_images': 'num_images',
        'num_download': 'num_download',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'logo': 'logo',
        'url': 'url',
        'path': 'path',
        'internal_path': 'internal_path',
        'domain_name': 'domain_name',
        'namespace': 'namespace',
        'tags': 'tags',
        'status': 'status',
        'total_range': 'total_range'
    }

    def __init__(self, name=None, category=None, description=None, size=None, is_public=None, num_images=None, num_download=None, created_at=None, updated_at=None, logo=None, url=None, path=None, internal_path=None, domain_name=None, namespace=None, tags=None, status=None, total_range=None):
        """ShowReposResp

        The model defined in huaweicloud sdk

        :param name: 仓库名称
        :type name: str
        :param category: 仓库类型（计划改造，每个镜像会有多个lable标示）
        :type category: str
        :param description: 仓库描述信息
        :type description: str
        :param size: 仓库大小 
        :type size: int
        :param is_public: 仓库是否为公共仓库，值为true或false
        :type is_public: bool
        :param num_images: 仓库中镜像个数，0 ~ 9223372036854775807
        :type num_images: int
        :param num_download: 仓库下载次数
        :type num_download: int
        :param created_at: 仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type created_at: str
        :param updated_at: 仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type updated_at: str
        :param logo: 仓库logo地址（暂时未用）
        :type logo: str
        :param url: 仓库logo图片的URL，URL格式。（暂时未用）
        :type url: str
        :param path: 镜像pull路径，格式为 swr.cn-north-1.myhuaweicloud.com/namespace/repository
        :type path: str
        :param internal_path: 镜像pull路径，格式为 10.125.0.198:20202/namespace/repository
        :type internal_path: str
        :param domain_name: 租户名
        :type domain_name: str
        :param namespace: 租户的组织名称
        :type namespace: str
        :param tags: 镜像版本列表
        :type tags: list[str]
        :param status: 查询他人共享镜像：共享是否过期 查询我共享的镜像：默认为false,无意义
        :type status: bool
        :param total_range: 总记录条数
        :type total_range: int
        """
        
        

        self._name = None
        self._category = None
        self._description = None
        self._size = None
        self._is_public = None
        self._num_images = None
        self._num_download = None
        self._created_at = None
        self._updated_at = None
        self._logo = None
        self._url = None
        self._path = None
        self._internal_path = None
        self._domain_name = None
        self._namespace = None
        self._tags = None
        self._status = None
        self._total_range = None
        self.discriminator = None

        self.name = name
        self.category = category
        self.description = description
        self.size = size
        self.is_public = is_public
        self.num_images = num_images
        self.num_download = num_download
        self.created_at = created_at
        self.updated_at = updated_at
        self.logo = logo
        self.url = url
        self.path = path
        self.internal_path = internal_path
        self.domain_name = domain_name
        self.namespace = namespace
        self.tags = tags
        self.status = status
        self.total_range = total_range

    @property
    def name(self):
        """Gets the name of this ShowReposResp.

        仓库名称

        :return: The name of this ShowReposResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowReposResp.

        仓库名称

        :param name: The name of this ShowReposResp.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        """Gets the category of this ShowReposResp.

        仓库类型（计划改造，每个镜像会有多个lable标示）

        :return: The category of this ShowReposResp.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ShowReposResp.

        仓库类型（计划改造，每个镜像会有多个lable标示）

        :param category: The category of this ShowReposResp.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        """Gets the description of this ShowReposResp.

        仓库描述信息

        :return: The description of this ShowReposResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowReposResp.

        仓库描述信息

        :param description: The description of this ShowReposResp.
        :type description: str
        """
        self._description = description

    @property
    def size(self):
        """Gets the size of this ShowReposResp.

        仓库大小 

        :return: The size of this ShowReposResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowReposResp.

        仓库大小 

        :param size: The size of this ShowReposResp.
        :type size: int
        """
        self._size = size

    @property
    def is_public(self):
        """Gets the is_public of this ShowReposResp.

        仓库是否为公共仓库，值为true或false

        :return: The is_public of this ShowReposResp.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ShowReposResp.

        仓库是否为公共仓库，值为true或false

        :param is_public: The is_public of this ShowReposResp.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def num_images(self):
        """Gets the num_images of this ShowReposResp.

        仓库中镜像个数，0 ~ 9223372036854775807

        :return: The num_images of this ShowReposResp.
        :rtype: int
        """
        return self._num_images

    @num_images.setter
    def num_images(self, num_images):
        """Sets the num_images of this ShowReposResp.

        仓库中镜像个数，0 ~ 9223372036854775807

        :param num_images: The num_images of this ShowReposResp.
        :type num_images: int
        """
        self._num_images = num_images

    @property
    def num_download(self):
        """Gets the num_download of this ShowReposResp.

        仓库下载次数

        :return: The num_download of this ShowReposResp.
        :rtype: int
        """
        return self._num_download

    @num_download.setter
    def num_download(self, num_download):
        """Sets the num_download of this ShowReposResp.

        仓库下载次数

        :param num_download: The num_download of this ShowReposResp.
        :type num_download: int
        """
        self._num_download = num_download

    @property
    def created_at(self):
        """Gets the created_at of this ShowReposResp.

        仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The created_at of this ShowReposResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowReposResp.

        仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param created_at: The created_at of this ShowReposResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowReposResp.

        仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The updated_at of this ShowReposResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowReposResp.

        仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param updated_at: The updated_at of this ShowReposResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def logo(self):
        """Gets the logo of this ShowReposResp.

        仓库logo地址（暂时未用）

        :return: The logo of this ShowReposResp.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this ShowReposResp.

        仓库logo地址（暂时未用）

        :param logo: The logo of this ShowReposResp.
        :type logo: str
        """
        self._logo = logo

    @property
    def url(self):
        """Gets the url of this ShowReposResp.

        仓库logo图片的URL，URL格式。（暂时未用）

        :return: The url of this ShowReposResp.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowReposResp.

        仓库logo图片的URL，URL格式。（暂时未用）

        :param url: The url of this ShowReposResp.
        :type url: str
        """
        self._url = url

    @property
    def path(self):
        """Gets the path of this ShowReposResp.

        镜像pull路径，格式为 swr.cn-north-1.myhuaweicloud.com/namespace/repository

        :return: The path of this ShowReposResp.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowReposResp.

        镜像pull路径，格式为 swr.cn-north-1.myhuaweicloud.com/namespace/repository

        :param path: The path of this ShowReposResp.
        :type path: str
        """
        self._path = path

    @property
    def internal_path(self):
        """Gets the internal_path of this ShowReposResp.

        镜像pull路径，格式为 10.125.0.198:20202/namespace/repository

        :return: The internal_path of this ShowReposResp.
        :rtype: str
        """
        return self._internal_path

    @internal_path.setter
    def internal_path(self, internal_path):
        """Sets the internal_path of this ShowReposResp.

        镜像pull路径，格式为 10.125.0.198:20202/namespace/repository

        :param internal_path: The internal_path of this ShowReposResp.
        :type internal_path: str
        """
        self._internal_path = internal_path

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowReposResp.

        租户名

        :return: The domain_name of this ShowReposResp.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowReposResp.

        租户名

        :param domain_name: The domain_name of this ShowReposResp.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def namespace(self):
        """Gets the namespace of this ShowReposResp.

        租户的组织名称

        :return: The namespace of this ShowReposResp.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowReposResp.

        租户的组织名称

        :param namespace: The namespace of this ShowReposResp.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def tags(self):
        """Gets the tags of this ShowReposResp.

        镜像版本列表

        :return: The tags of this ShowReposResp.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowReposResp.

        镜像版本列表

        :param tags: The tags of this ShowReposResp.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this ShowReposResp.

        查询他人共享镜像：共享是否过期 查询我共享的镜像：默认为false,无意义

        :return: The status of this ShowReposResp.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowReposResp.

        查询他人共享镜像：共享是否过期 查询我共享的镜像：默认为false,无意义

        :param status: The status of this ShowReposResp.
        :type status: bool
        """
        self._status = status

    @property
    def total_range(self):
        """Gets the total_range of this ShowReposResp.

        总记录条数

        :return: The total_range of this ShowReposResp.
        :rtype: int
        """
        return self._total_range

    @total_range.setter
    def total_range(self, total_range):
        """Sets the total_range of this ShowReposResp.

        总记录条数

        :param total_range: The total_range of this ShowReposResp.
        :type total_range: int
        """
        self._total_range = total_range

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
        if not isinstance(other, ShowReposResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
