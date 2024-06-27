# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicAwLib:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'datetime',
        'create_time_stamp': 'int',
        'create_time_string': 'str',
        'create_user': 'str',
        'document_link': 'str',
        'id': 'str',
        'name': 'str',
        'net_area': 'list[str]',
        'obs_temp_url': 'str',
        'product_line': 'str',
        'repo_branch': 'str',
        'repo_lib_path': 'str',
        'repo_password': 'str',
        'repo_private_key': 'str',
        'repo_url': 'str',
        'repo_username': 'str',
        'update_time': 'datetime',
        'update_time_stamp': 'int',
        'update_time_string': 'str',
        'update_user': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'create_time_stamp': 'create_time_stamp',
        'create_time_string': 'create_time_string',
        'create_user': 'create_user',
        'document_link': 'document_link',
        'id': 'id',
        'name': 'name',
        'net_area': 'net_area',
        'obs_temp_url': 'obs_temp_url',
        'product_line': 'product_line',
        'repo_branch': 'repo_branch',
        'repo_lib_path': 'repo_lib_path',
        'repo_password': 'repo_password',
        'repo_private_key': 'repo_private_key',
        'repo_url': 'repo_url',
        'repo_username': 'repo_username',
        'update_time': 'update_time',
        'update_time_stamp': 'update_time_stamp',
        'update_time_string': 'update_time_string',
        'update_user': 'update_user'
    }

    def __init__(self, create_time=None, create_time_stamp=None, create_time_string=None, create_user=None, document_link=None, id=None, name=None, net_area=None, obs_temp_url=None, product_line=None, repo_branch=None, repo_lib_path=None, repo_password=None, repo_private_key=None, repo_url=None, repo_username=None, update_time=None, update_time_stamp=None, update_time_string=None, update_user=None):
        """PublicAwLib

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: datetime
        :param create_time_stamp: 创建时间戳
        :type create_time_stamp: int
        :param create_time_string: 创建时间字符串
        :type create_time_string: str
        :param create_user: 创建人
        :type create_user: str
        :param document_link: 文档链接
        :type document_link: str
        :param id: id
        :type id: str
        :param name: 名称
        :type name: str
        :param net_area: 蓝区:Blue,绿区:Green,黄区:Yellow
        :type net_area: list[str]
        :param obs_temp_url: obs临时url
        :type obs_temp_url: str
        :param product_line: 产品线
        :type product_line: str
        :param repo_branch: 仓库分支
        :type repo_branch: str
        :param repo_lib_path: 存公共aw依赖jar包的目录
        :type repo_lib_path: str
        :param repo_password: 仓库密码
        :type repo_password: str
        :param repo_private_key: 仓库秘钥
        :type repo_private_key: str
        :param repo_url: 仓库地址
        :type repo_url: str
        :param repo_username: 仓库用户名
        :type repo_username: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param update_time_stamp: 更新时间戳
        :type update_time_stamp: int
        :param update_time_string: 更新时间字符串
        :type update_time_string: str
        :param update_user: 更新人
        :type update_user: str
        """
        
        

        self._create_time = None
        self._create_time_stamp = None
        self._create_time_string = None
        self._create_user = None
        self._document_link = None
        self._id = None
        self._name = None
        self._net_area = None
        self._obs_temp_url = None
        self._product_line = None
        self._repo_branch = None
        self._repo_lib_path = None
        self._repo_password = None
        self._repo_private_key = None
        self._repo_url = None
        self._repo_username = None
        self._update_time = None
        self._update_time_stamp = None
        self._update_time_string = None
        self._update_user = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if create_time_string is not None:
            self.create_time_string = create_time_string
        if create_user is not None:
            self.create_user = create_user
        if document_link is not None:
            self.document_link = document_link
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if net_area is not None:
            self.net_area = net_area
        if obs_temp_url is not None:
            self.obs_temp_url = obs_temp_url
        if product_line is not None:
            self.product_line = product_line
        if repo_branch is not None:
            self.repo_branch = repo_branch
        if repo_lib_path is not None:
            self.repo_lib_path = repo_lib_path
        if repo_password is not None:
            self.repo_password = repo_password
        if repo_private_key is not None:
            self.repo_private_key = repo_private_key
        if repo_url is not None:
            self.repo_url = repo_url
        if repo_username is not None:
            self.repo_username = repo_username
        if update_time is not None:
            self.update_time = update_time
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp
        if update_time_string is not None:
            self.update_time_string = update_time_string
        if update_user is not None:
            self.update_user = update_user

    @property
    def create_time(self):
        """Gets the create_time of this PublicAwLib.

        创建时间

        :return: The create_time of this PublicAwLib.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PublicAwLib.

        创建时间

        :param create_time: The create_time of this PublicAwLib.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_time_stamp(self):
        """Gets the create_time_stamp of this PublicAwLib.

        创建时间戳

        :return: The create_time_stamp of this PublicAwLib.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        """Sets the create_time_stamp of this PublicAwLib.

        创建时间戳

        :param create_time_stamp: The create_time_stamp of this PublicAwLib.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def create_time_string(self):
        """Gets the create_time_string of this PublicAwLib.

        创建时间字符串

        :return: The create_time_string of this PublicAwLib.
        :rtype: str
        """
        return self._create_time_string

    @create_time_string.setter
    def create_time_string(self, create_time_string):
        """Sets the create_time_string of this PublicAwLib.

        创建时间字符串

        :param create_time_string: The create_time_string of this PublicAwLib.
        :type create_time_string: str
        """
        self._create_time_string = create_time_string

    @property
    def create_user(self):
        """Gets the create_user of this PublicAwLib.

        创建人

        :return: The create_user of this PublicAwLib.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this PublicAwLib.

        创建人

        :param create_user: The create_user of this PublicAwLib.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def document_link(self):
        """Gets the document_link of this PublicAwLib.

        文档链接

        :return: The document_link of this PublicAwLib.
        :rtype: str
        """
        return self._document_link

    @document_link.setter
    def document_link(self, document_link):
        """Sets the document_link of this PublicAwLib.

        文档链接

        :param document_link: The document_link of this PublicAwLib.
        :type document_link: str
        """
        self._document_link = document_link

    @property
    def id(self):
        """Gets the id of this PublicAwLib.

        id

        :return: The id of this PublicAwLib.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicAwLib.

        id

        :param id: The id of this PublicAwLib.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PublicAwLib.

        名称

        :return: The name of this PublicAwLib.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicAwLib.

        名称

        :param name: The name of this PublicAwLib.
        :type name: str
        """
        self._name = name

    @property
    def net_area(self):
        """Gets the net_area of this PublicAwLib.

        蓝区:Blue,绿区:Green,黄区:Yellow

        :return: The net_area of this PublicAwLib.
        :rtype: list[str]
        """
        return self._net_area

    @net_area.setter
    def net_area(self, net_area):
        """Sets the net_area of this PublicAwLib.

        蓝区:Blue,绿区:Green,黄区:Yellow

        :param net_area: The net_area of this PublicAwLib.
        :type net_area: list[str]
        """
        self._net_area = net_area

    @property
    def obs_temp_url(self):
        """Gets the obs_temp_url of this PublicAwLib.

        obs临时url

        :return: The obs_temp_url of this PublicAwLib.
        :rtype: str
        """
        return self._obs_temp_url

    @obs_temp_url.setter
    def obs_temp_url(self, obs_temp_url):
        """Sets the obs_temp_url of this PublicAwLib.

        obs临时url

        :param obs_temp_url: The obs_temp_url of this PublicAwLib.
        :type obs_temp_url: str
        """
        self._obs_temp_url = obs_temp_url

    @property
    def product_line(self):
        """Gets the product_line of this PublicAwLib.

        产品线

        :return: The product_line of this PublicAwLib.
        :rtype: str
        """
        return self._product_line

    @product_line.setter
    def product_line(self, product_line):
        """Sets the product_line of this PublicAwLib.

        产品线

        :param product_line: The product_line of this PublicAwLib.
        :type product_line: str
        """
        self._product_line = product_line

    @property
    def repo_branch(self):
        """Gets the repo_branch of this PublicAwLib.

        仓库分支

        :return: The repo_branch of this PublicAwLib.
        :rtype: str
        """
        return self._repo_branch

    @repo_branch.setter
    def repo_branch(self, repo_branch):
        """Sets the repo_branch of this PublicAwLib.

        仓库分支

        :param repo_branch: The repo_branch of this PublicAwLib.
        :type repo_branch: str
        """
        self._repo_branch = repo_branch

    @property
    def repo_lib_path(self):
        """Gets the repo_lib_path of this PublicAwLib.

        存公共aw依赖jar包的目录

        :return: The repo_lib_path of this PublicAwLib.
        :rtype: str
        """
        return self._repo_lib_path

    @repo_lib_path.setter
    def repo_lib_path(self, repo_lib_path):
        """Sets the repo_lib_path of this PublicAwLib.

        存公共aw依赖jar包的目录

        :param repo_lib_path: The repo_lib_path of this PublicAwLib.
        :type repo_lib_path: str
        """
        self._repo_lib_path = repo_lib_path

    @property
    def repo_password(self):
        """Gets the repo_password of this PublicAwLib.

        仓库密码

        :return: The repo_password of this PublicAwLib.
        :rtype: str
        """
        return self._repo_password

    @repo_password.setter
    def repo_password(self, repo_password):
        """Sets the repo_password of this PublicAwLib.

        仓库密码

        :param repo_password: The repo_password of this PublicAwLib.
        :type repo_password: str
        """
        self._repo_password = repo_password

    @property
    def repo_private_key(self):
        """Gets the repo_private_key of this PublicAwLib.

        仓库秘钥

        :return: The repo_private_key of this PublicAwLib.
        :rtype: str
        """
        return self._repo_private_key

    @repo_private_key.setter
    def repo_private_key(self, repo_private_key):
        """Sets the repo_private_key of this PublicAwLib.

        仓库秘钥

        :param repo_private_key: The repo_private_key of this PublicAwLib.
        :type repo_private_key: str
        """
        self._repo_private_key = repo_private_key

    @property
    def repo_url(self):
        """Gets the repo_url of this PublicAwLib.

        仓库地址

        :return: The repo_url of this PublicAwLib.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this PublicAwLib.

        仓库地址

        :param repo_url: The repo_url of this PublicAwLib.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def repo_username(self):
        """Gets the repo_username of this PublicAwLib.

        仓库用户名

        :return: The repo_username of this PublicAwLib.
        :rtype: str
        """
        return self._repo_username

    @repo_username.setter
    def repo_username(self, repo_username):
        """Sets the repo_username of this PublicAwLib.

        仓库用户名

        :param repo_username: The repo_username of this PublicAwLib.
        :type repo_username: str
        """
        self._repo_username = repo_username

    @property
    def update_time(self):
        """Gets the update_time of this PublicAwLib.

        更新时间

        :return: The update_time of this PublicAwLib.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PublicAwLib.

        更新时间

        :param update_time: The update_time of this PublicAwLib.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_time_stamp(self):
        """Gets the update_time_stamp of this PublicAwLib.

        更新时间戳

        :return: The update_time_stamp of this PublicAwLib.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        """Sets the update_time_stamp of this PublicAwLib.

        更新时间戳

        :param update_time_stamp: The update_time_stamp of this PublicAwLib.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

    @property
    def update_time_string(self):
        """Gets the update_time_string of this PublicAwLib.

        更新时间字符串

        :return: The update_time_string of this PublicAwLib.
        :rtype: str
        """
        return self._update_time_string

    @update_time_string.setter
    def update_time_string(self, update_time_string):
        """Sets the update_time_string of this PublicAwLib.

        更新时间字符串

        :param update_time_string: The update_time_string of this PublicAwLib.
        :type update_time_string: str
        """
        self._update_time_string = update_time_string

    @property
    def update_user(self):
        """Gets the update_user of this PublicAwLib.

        更新人

        :return: The update_user of this PublicAwLib.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this PublicAwLib.

        更新人

        :param update_user: The update_user of this PublicAwLib.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, PublicAwLib):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
