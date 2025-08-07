# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReposRespV3:

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
        'category': 'str',
        'description': 'str',
        'size': 'int',
        'is_public': 'bool',
        'num_images': 'int',
        'num_download': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'domain_name': 'str',
        'namespace_name': 'str',
        'status': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category': 'category',
        'description': 'description',
        'size': 'size',
        'is_public': 'is_public',
        'num_images': 'num_images',
        'num_download': 'num_download',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_name': 'domain_name',
        'namespace_name': 'namespace_name',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, category=None, description=None, size=None, is_public=None, num_images=None, num_download=None, created_at=None, updated_at=None, domain_name=None, namespace_name=None, status=None):
        r"""ShowReposRespV3

        The model defined in huaweicloud sdk

        :param id: 仓库ID
        :type id: int
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
        :param domain_name: 仓库所属租户
        :type domain_name: str
        :param namespace_name: 租户的组织名称
        :type namespace_name: str
        :param status: 查询他人共享镜像：共享是否过期 查询我共享的镜像：默认为false,无意义
        :type status: bool
        """
        
        

        self._id = None
        self._name = None
        self._category = None
        self._description = None
        self._size = None
        self._is_public = None
        self._num_images = None
        self._num_download = None
        self._created_at = None
        self._updated_at = None
        self._domain_name = None
        self._namespace_name = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.size = size
        self.is_public = is_public
        self.num_images = num_images
        self.num_download = num_download
        self.created_at = created_at
        self.updated_at = updated_at
        self.domain_name = domain_name
        self.namespace_name = namespace_name
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this ShowReposRespV3.

        仓库ID

        :return: The id of this ShowReposRespV3.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowReposRespV3.

        仓库ID

        :param id: The id of this ShowReposRespV3.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowReposRespV3.

        仓库名称

        :return: The name of this ShowReposRespV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowReposRespV3.

        仓库名称

        :param name: The name of this ShowReposRespV3.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        r"""Gets the category of this ShowReposRespV3.

        仓库类型（计划改造，每个镜像会有多个lable标示）

        :return: The category of this ShowReposRespV3.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowReposRespV3.

        仓库类型（计划改造，每个镜像会有多个lable标示）

        :param category: The category of this ShowReposRespV3.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this ShowReposRespV3.

        仓库描述信息

        :return: The description of this ShowReposRespV3.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowReposRespV3.

        仓库描述信息

        :param description: The description of this ShowReposRespV3.
        :type description: str
        """
        self._description = description

    @property
    def size(self):
        r"""Gets the size of this ShowReposRespV3.

        仓库大小

        :return: The size of this ShowReposRespV3.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowReposRespV3.

        仓库大小

        :param size: The size of this ShowReposRespV3.
        :type size: int
        """
        self._size = size

    @property
    def is_public(self):
        r"""Gets the is_public of this ShowReposRespV3.

        仓库是否为公共仓库，值为true或false

        :return: The is_public of this ShowReposRespV3.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this ShowReposRespV3.

        仓库是否为公共仓库，值为true或false

        :param is_public: The is_public of this ShowReposRespV3.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def num_images(self):
        r"""Gets the num_images of this ShowReposRespV3.

        仓库中镜像个数，0 ~ 9223372036854775807

        :return: The num_images of this ShowReposRespV3.
        :rtype: int
        """
        return self._num_images

    @num_images.setter
    def num_images(self, num_images):
        r"""Sets the num_images of this ShowReposRespV3.

        仓库中镜像个数，0 ~ 9223372036854775807

        :param num_images: The num_images of this ShowReposRespV3.
        :type num_images: int
        """
        self._num_images = num_images

    @property
    def num_download(self):
        r"""Gets the num_download of this ShowReposRespV3.

        仓库下载次数

        :return: The num_download of this ShowReposRespV3.
        :rtype: int
        """
        return self._num_download

    @num_download.setter
    def num_download(self, num_download):
        r"""Sets the num_download of this ShowReposRespV3.

        仓库下载次数

        :param num_download: The num_download of this ShowReposRespV3.
        :type num_download: int
        """
        self._num_download = num_download

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowReposRespV3.

        仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The created_at of this ShowReposRespV3.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowReposRespV3.

        仓库创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param created_at: The created_at of this ShowReposRespV3.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowReposRespV3.

        仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The updated_at of this ShowReposRespV3.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowReposRespV3.

        仓库更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param updated_at: The updated_at of this ShowReposRespV3.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowReposRespV3.

        仓库所属租户

        :return: The domain_name of this ShowReposRespV3.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowReposRespV3.

        仓库所属租户

        :param domain_name: The domain_name of this ShowReposRespV3.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ShowReposRespV3.

        租户的组织名称

        :return: The namespace_name of this ShowReposRespV3.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ShowReposRespV3.

        租户的组织名称

        :param namespace_name: The namespace_name of this ShowReposRespV3.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def status(self):
        r"""Gets the status of this ShowReposRespV3.

        查询他人共享镜像：共享是否过期 查询我共享的镜像：默认为false,无意义

        :return: The status of this ShowReposRespV3.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowReposRespV3.

        查询他人共享镜像：共享是否过期 查询我共享的镜像：默认为false,无意义

        :param status: The status of this ShowReposRespV3.
        :type status: bool
        """
        self._status = status

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
        if not isinstance(other, ShowReposRespV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
