# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryResponse(SdkResponse):

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
        'ns_id': 'int',
        'name': 'str',
        'category': 'str',
        'description': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'size': 'int',
        'is_public': 'bool',
        'num_images': 'int',
        'num_download': 'int',
        'url': 'str',
        'path': 'str',
        'internal_path': 'str',
        'created': 'str',
        'updated': 'str',
        'domain_id': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'id': 'id',
        'ns_id': 'ns_id',
        'name': 'name',
        'category': 'category',
        'description': 'description',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'size': 'size',
        'is_public': 'is_public',
        'num_images': 'num_images',
        'num_download': 'num_download',
        'url': 'url',
        'path': 'path',
        'internal_path': 'internal_path',
        'created': 'created',
        'updated': 'updated',
        'domain_id': 'domain_id',
        'priority': 'priority'
    }

    def __init__(self, id=None, ns_id=None, name=None, category=None, description=None, creator_id=None, creator_name=None, size=None, is_public=None, num_images=None, num_download=None, url=None, path=None, internal_path=None, created=None, updated=None, domain_id=None, priority=None):
        """ShowRepositoryResponse

        The model defined in huaweicloud sdk

        :param id: 仓库编号
        :type id: int
        :param ns_id: 组织编号
        :type ns_id: int
        :param name: 仓库名称
        :type name: str
        :param category: 仓库类型（计划改造，每个镜像会有多个lable标示）
        :type category: str
        :param description: 仓库描述信息
        :type description: str
        :param creator_id: 仓库创建者id
        :type creator_id: str
        :param creator_name: 仓库创建者
        :type creator_name: str
        :param size: 仓库大小 
        :type size: int
        :param is_public: 仓库是否为公共仓库，值为true或false
        :type is_public: bool
        :param num_images: 仓库中镜像个数，0 ~ 9223372036854775807
        :type num_images: int
        :param num_download: 仓库下载次数
        :type num_download: int
        :param url: 仓库logo图片的URL，URL格式。（暂时未用）
        :type url: str
        :param path: 镜像pull路径，格式为 swr.cn-north-1.myhuaweicloud.com/namespace/repository
        :type path: str
        :param internal_path: 镜像pull路径，格式为 10.125.0.198:20202/namespace/repository
        :type internal_path: str
        :param created: 仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type created: str
        :param updated: 仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type updated: str
        :param domain_id: 帐号ID
        :type domain_id: str
        :param priority: 镜像排序优先级
        :type priority: int
        """
        
        super(ShowRepositoryResponse, self).__init__()

        self._id = None
        self._ns_id = None
        self._name = None
        self._category = None
        self._description = None
        self._creator_id = None
        self._creator_name = None
        self._size = None
        self._is_public = None
        self._num_images = None
        self._num_download = None
        self._url = None
        self._path = None
        self._internal_path = None
        self._created = None
        self._updated = None
        self._domain_id = None
        self._priority = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ns_id is not None:
            self.ns_id = ns_id
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if size is not None:
            self.size = size
        if is_public is not None:
            self.is_public = is_public
        if num_images is not None:
            self.num_images = num_images
        if num_download is not None:
            self.num_download = num_download
        if url is not None:
            self.url = url
        if path is not None:
            self.path = path
        if internal_path is not None:
            self.internal_path = internal_path
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if domain_id is not None:
            self.domain_id = domain_id
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        """Gets the id of this ShowRepositoryResponse.

        仓库编号

        :return: The id of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowRepositoryResponse.

        仓库编号

        :param id: The id of this ShowRepositoryResponse.
        :type id: int
        """
        self._id = id

    @property
    def ns_id(self):
        """Gets the ns_id of this ShowRepositoryResponse.

        组织编号

        :return: The ns_id of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._ns_id

    @ns_id.setter
    def ns_id(self, ns_id):
        """Sets the ns_id of this ShowRepositoryResponse.

        组织编号

        :param ns_id: The ns_id of this ShowRepositoryResponse.
        :type ns_id: int
        """
        self._ns_id = ns_id

    @property
    def name(self):
        """Gets the name of this ShowRepositoryResponse.

        仓库名称

        :return: The name of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowRepositoryResponse.

        仓库名称

        :param name: The name of this ShowRepositoryResponse.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        """Gets the category of this ShowRepositoryResponse.

        仓库类型（计划改造，每个镜像会有多个lable标示）

        :return: The category of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ShowRepositoryResponse.

        仓库类型（计划改造，每个镜像会有多个lable标示）

        :param category: The category of this ShowRepositoryResponse.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        """Gets the description of this ShowRepositoryResponse.

        仓库描述信息

        :return: The description of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowRepositoryResponse.

        仓库描述信息

        :param description: The description of this ShowRepositoryResponse.
        :type description: str
        """
        self._description = description

    @property
    def creator_id(self):
        """Gets the creator_id of this ShowRepositoryResponse.

        仓库创建者id

        :return: The creator_id of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ShowRepositoryResponse.

        仓库创建者id

        :param creator_id: The creator_id of this ShowRepositoryResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowRepositoryResponse.

        仓库创建者

        :return: The creator_name of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowRepositoryResponse.

        仓库创建者

        :param creator_name: The creator_name of this ShowRepositoryResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def size(self):
        """Gets the size of this ShowRepositoryResponse.

        仓库大小 

        :return: The size of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowRepositoryResponse.

        仓库大小 

        :param size: The size of this ShowRepositoryResponse.
        :type size: int
        """
        self._size = size

    @property
    def is_public(self):
        """Gets the is_public of this ShowRepositoryResponse.

        仓库是否为公共仓库，值为true或false

        :return: The is_public of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ShowRepositoryResponse.

        仓库是否为公共仓库，值为true或false

        :param is_public: The is_public of this ShowRepositoryResponse.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def num_images(self):
        """Gets the num_images of this ShowRepositoryResponse.

        仓库中镜像个数，0 ~ 9223372036854775807

        :return: The num_images of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._num_images

    @num_images.setter
    def num_images(self, num_images):
        """Sets the num_images of this ShowRepositoryResponse.

        仓库中镜像个数，0 ~ 9223372036854775807

        :param num_images: The num_images of this ShowRepositoryResponse.
        :type num_images: int
        """
        self._num_images = num_images

    @property
    def num_download(self):
        """Gets the num_download of this ShowRepositoryResponse.

        仓库下载次数

        :return: The num_download of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._num_download

    @num_download.setter
    def num_download(self, num_download):
        """Sets the num_download of this ShowRepositoryResponse.

        仓库下载次数

        :param num_download: The num_download of this ShowRepositoryResponse.
        :type num_download: int
        """
        self._num_download = num_download

    @property
    def url(self):
        """Gets the url of this ShowRepositoryResponse.

        仓库logo图片的URL，URL格式。（暂时未用）

        :return: The url of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowRepositoryResponse.

        仓库logo图片的URL，URL格式。（暂时未用）

        :param url: The url of this ShowRepositoryResponse.
        :type url: str
        """
        self._url = url

    @property
    def path(self):
        """Gets the path of this ShowRepositoryResponse.

        镜像pull路径，格式为 swr.cn-north-1.myhuaweicloud.com/namespace/repository

        :return: The path of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowRepositoryResponse.

        镜像pull路径，格式为 swr.cn-north-1.myhuaweicloud.com/namespace/repository

        :param path: The path of this ShowRepositoryResponse.
        :type path: str
        """
        self._path = path

    @property
    def internal_path(self):
        """Gets the internal_path of this ShowRepositoryResponse.

        镜像pull路径，格式为 10.125.0.198:20202/namespace/repository

        :return: The internal_path of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._internal_path

    @internal_path.setter
    def internal_path(self, internal_path):
        """Sets the internal_path of this ShowRepositoryResponse.

        镜像pull路径，格式为 10.125.0.198:20202/namespace/repository

        :param internal_path: The internal_path of this ShowRepositoryResponse.
        :type internal_path: str
        """
        self._internal_path = internal_path

    @property
    def created(self):
        """Gets the created of this ShowRepositoryResponse.

        仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The created of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowRepositoryResponse.

        仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param created: The created of this ShowRepositoryResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowRepositoryResponse.

        仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The updated of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowRepositoryResponse.

        仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param updated: The updated of this ShowRepositoryResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowRepositoryResponse.

        帐号ID

        :return: The domain_id of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowRepositoryResponse.

        帐号ID

        :param domain_id: The domain_id of this ShowRepositoryResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def priority(self):
        """Gets the priority of this ShowRepositoryResponse.

        镜像排序优先级

        :return: The priority of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ShowRepositoryResponse.

        镜像排序优先级

        :param priority: The priority of this ShowRepositoryResponse.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, ShowRepositoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
