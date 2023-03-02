# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'creator_name': 'str',
        'domain_name': 'str',
        'group_name': 'str',
        'https_url': 'str',
        'iam_user_uuid': 'str',
        'is_owner': 'int',
        'lfs_size': 'str',
        'project_is_deleted': 'str',
        'project_uuid': 'str',
        'repository_id': 'int',
        'repository_name': 'str',
        'repository_size': 'str',
        'repository_uuid': 'str',
        'ssh_url': 'str',
        'star': 'bool',
        'status': 'int',
        'updated_at': 'str',
        'user_role': 'int',
        'visibility_level': 'int',
        'web_url': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'creator_name': 'creator_name',
        'domain_name': 'domain_name',
        'group_name': 'group_name',
        'https_url': 'https_url',
        'iam_user_uuid': 'iam_user_uuid',
        'is_owner': 'is_owner',
        'lfs_size': 'lfs_size',
        'project_is_deleted': 'project_is_deleted',
        'project_uuid': 'project_uuid',
        'repository_id': 'repository_id',
        'repository_name': 'repository_name',
        'repository_size': 'repository_size',
        'repository_uuid': 'repository_uuid',
        'ssh_url': 'ssh_url',
        'star': 'star',
        'status': 'status',
        'updated_at': 'updated_at',
        'user_role': 'userRole',
        'visibility_level': 'visibility_level',
        'web_url': 'web_url'
    }

    def __init__(self, created_at=None, creator_name=None, domain_name=None, group_name=None, https_url=None, iam_user_uuid=None, is_owner=None, lfs_size=None, project_is_deleted=None, project_uuid=None, repository_id=None, repository_name=None, repository_size=None, repository_uuid=None, ssh_url=None, star=None, status=None, updated_at=None, user_role=None, visibility_level=None, web_url=None):
        """RepoInfoV2

        The model defined in huaweicloud sdk

        :param created_at: 创建时间
        :type created_at: str
        :param creator_name: 创建者的用户名，在用户是租户的情况下，用户名和租户名相等
        :type creator_name: str
        :param domain_name: 创建者的租户名
        :type domain_name: str
        :param group_name: 仓库组名(克隆地址中域名后面项目名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )
        :type group_name: str
        :param https_url: 使用 https 克隆仓库时所使用的 url
        :type https_url: str
        :param iam_user_uuid: 用户的 iam user uuid
        :type iam_user_uuid: str
        :param is_owner: 当前用户是否是仓库的创建者，1：是，0：不是
        :type is_owner: int
        :param lfs_size: 仓库 LFS 容量，单位为M，大于 1024M 则单位为 G
        :type lfs_size: str
        :param project_is_deleted: 项目是否被删除
        :type project_is_deleted: str
        :param project_uuid: 项目的uuid
        :type project_uuid: str
        :param repository_id: 仓库主键id
        :type repository_id: int
        :param repository_name: 仓库名
        :type repository_name: str
        :param repository_size: 仓库总容量 &#x3D; 仓库 LFS 容量 + git 库容量，单位为M，大于 1024M 则单位为 G
        :type repository_size: str
        :param repository_uuid: 仓库uuid(由CreateRepository接口返回)
        :type repository_uuid: str
        :param ssh_url: 使用 ssh 方式克隆仓库时所使用的 url
        :type ssh_url: str
        :param star: 当前用户是否收藏该仓库
        :type star: bool
        :param status: 仓库状态， 0：仓库正常创建成功 1：仓库创建中 2：创建失败 3：仓库冻结 4：仓库已经关闭 
        :type status: int
        :param updated_at: 更新时间
        :type updated_at: str
        :param user_role: 用户在仓库中的权限:20：只读成员 30：普通成员 40：管理员 
        :type user_role: int
        :param visibility_level: 是否可见：0私有仓库，20公有仓库
        :type visibility_level: int
        :param web_url: web url 路径，访问它将跳转至仓库详情页
        :type web_url: str
        """
        
        

        self._created_at = None
        self._creator_name = None
        self._domain_name = None
        self._group_name = None
        self._https_url = None
        self._iam_user_uuid = None
        self._is_owner = None
        self._lfs_size = None
        self._project_is_deleted = None
        self._project_uuid = None
        self._repository_id = None
        self._repository_name = None
        self._repository_size = None
        self._repository_uuid = None
        self._ssh_url = None
        self._star = None
        self._status = None
        self._updated_at = None
        self._user_role = None
        self._visibility_level = None
        self._web_url = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if creator_name is not None:
            self.creator_name = creator_name
        if domain_name is not None:
            self.domain_name = domain_name
        if group_name is not None:
            self.group_name = group_name
        if https_url is not None:
            self.https_url = https_url
        if iam_user_uuid is not None:
            self.iam_user_uuid = iam_user_uuid
        if is_owner is not None:
            self.is_owner = is_owner
        if lfs_size is not None:
            self.lfs_size = lfs_size
        if project_is_deleted is not None:
            self.project_is_deleted = project_is_deleted
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if repository_id is not None:
            self.repository_id = repository_id
        if repository_name is not None:
            self.repository_name = repository_name
        if repository_size is not None:
            self.repository_size = repository_size
        if repository_uuid is not None:
            self.repository_uuid = repository_uuid
        if ssh_url is not None:
            self.ssh_url = ssh_url
        if star is not None:
            self.star = star
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        if user_role is not None:
            self.user_role = user_role
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if web_url is not None:
            self.web_url = web_url

    @property
    def created_at(self):
        """Gets the created_at of this RepoInfoV2.

        创建时间

        :return: The created_at of this RepoInfoV2.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RepoInfoV2.

        创建时间

        :param created_at: The created_at of this RepoInfoV2.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def creator_name(self):
        """Gets the creator_name of this RepoInfoV2.

        创建者的用户名，在用户是租户的情况下，用户名和租户名相等

        :return: The creator_name of this RepoInfoV2.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this RepoInfoV2.

        创建者的用户名，在用户是租户的情况下，用户名和租户名相等

        :param creator_name: The creator_name of this RepoInfoV2.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def domain_name(self):
        """Gets the domain_name of this RepoInfoV2.

        创建者的租户名

        :return: The domain_name of this RepoInfoV2.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this RepoInfoV2.

        创建者的租户名

        :param domain_name: The domain_name of this RepoInfoV2.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def group_name(self):
        """Gets the group_name of this RepoInfoV2.

        仓库组名(克隆地址中域名后面项目名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )

        :return: The group_name of this RepoInfoV2.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this RepoInfoV2.

        仓库组名(克隆地址中域名后面项目名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )

        :param group_name: The group_name of this RepoInfoV2.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def https_url(self):
        """Gets the https_url of this RepoInfoV2.

        使用 https 克隆仓库时所使用的 url

        :return: The https_url of this RepoInfoV2.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        """Sets the https_url of this RepoInfoV2.

        使用 https 克隆仓库时所使用的 url

        :param https_url: The https_url of this RepoInfoV2.
        :type https_url: str
        """
        self._https_url = https_url

    @property
    def iam_user_uuid(self):
        """Gets the iam_user_uuid of this RepoInfoV2.

        用户的 iam user uuid

        :return: The iam_user_uuid of this RepoInfoV2.
        :rtype: str
        """
        return self._iam_user_uuid

    @iam_user_uuid.setter
    def iam_user_uuid(self, iam_user_uuid):
        """Sets the iam_user_uuid of this RepoInfoV2.

        用户的 iam user uuid

        :param iam_user_uuid: The iam_user_uuid of this RepoInfoV2.
        :type iam_user_uuid: str
        """
        self._iam_user_uuid = iam_user_uuid

    @property
    def is_owner(self):
        """Gets the is_owner of this RepoInfoV2.

        当前用户是否是仓库的创建者，1：是，0：不是

        :return: The is_owner of this RepoInfoV2.
        :rtype: int
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        """Sets the is_owner of this RepoInfoV2.

        当前用户是否是仓库的创建者，1：是，0：不是

        :param is_owner: The is_owner of this RepoInfoV2.
        :type is_owner: int
        """
        self._is_owner = is_owner

    @property
    def lfs_size(self):
        """Gets the lfs_size of this RepoInfoV2.

        仓库 LFS 容量，单位为M，大于 1024M 则单位为 G

        :return: The lfs_size of this RepoInfoV2.
        :rtype: str
        """
        return self._lfs_size

    @lfs_size.setter
    def lfs_size(self, lfs_size):
        """Sets the lfs_size of this RepoInfoV2.

        仓库 LFS 容量，单位为M，大于 1024M 则单位为 G

        :param lfs_size: The lfs_size of this RepoInfoV2.
        :type lfs_size: str
        """
        self._lfs_size = lfs_size

    @property
    def project_is_deleted(self):
        """Gets the project_is_deleted of this RepoInfoV2.

        项目是否被删除

        :return: The project_is_deleted of this RepoInfoV2.
        :rtype: str
        """
        return self._project_is_deleted

    @project_is_deleted.setter
    def project_is_deleted(self, project_is_deleted):
        """Sets the project_is_deleted of this RepoInfoV2.

        项目是否被删除

        :param project_is_deleted: The project_is_deleted of this RepoInfoV2.
        :type project_is_deleted: str
        """
        self._project_is_deleted = project_is_deleted

    @property
    def project_uuid(self):
        """Gets the project_uuid of this RepoInfoV2.

        项目的uuid

        :return: The project_uuid of this RepoInfoV2.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this RepoInfoV2.

        项目的uuid

        :param project_uuid: The project_uuid of this RepoInfoV2.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def repository_id(self):
        """Gets the repository_id of this RepoInfoV2.

        仓库主键id

        :return: The repository_id of this RepoInfoV2.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this RepoInfoV2.

        仓库主键id

        :param repository_id: The repository_id of this RepoInfoV2.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def repository_name(self):
        """Gets the repository_name of this RepoInfoV2.

        仓库名

        :return: The repository_name of this RepoInfoV2.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this RepoInfoV2.

        仓库名

        :param repository_name: The repository_name of this RepoInfoV2.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def repository_size(self):
        """Gets the repository_size of this RepoInfoV2.

        仓库总容量 = 仓库 LFS 容量 + git 库容量，单位为M，大于 1024M 则单位为 G

        :return: The repository_size of this RepoInfoV2.
        :rtype: str
        """
        return self._repository_size

    @repository_size.setter
    def repository_size(self, repository_size):
        """Sets the repository_size of this RepoInfoV2.

        仓库总容量 = 仓库 LFS 容量 + git 库容量，单位为M，大于 1024M 则单位为 G

        :param repository_size: The repository_size of this RepoInfoV2.
        :type repository_size: str
        """
        self._repository_size = repository_size

    @property
    def repository_uuid(self):
        """Gets the repository_uuid of this RepoInfoV2.

        仓库uuid(由CreateRepository接口返回)

        :return: The repository_uuid of this RepoInfoV2.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        """Sets the repository_uuid of this RepoInfoV2.

        仓库uuid(由CreateRepository接口返回)

        :param repository_uuid: The repository_uuid of this RepoInfoV2.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

    @property
    def ssh_url(self):
        """Gets the ssh_url of this RepoInfoV2.

        使用 ssh 方式克隆仓库时所使用的 url

        :return: The ssh_url of this RepoInfoV2.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """Sets the ssh_url of this RepoInfoV2.

        使用 ssh 方式克隆仓库时所使用的 url

        :param ssh_url: The ssh_url of this RepoInfoV2.
        :type ssh_url: str
        """
        self._ssh_url = ssh_url

    @property
    def star(self):
        """Gets the star of this RepoInfoV2.

        当前用户是否收藏该仓库

        :return: The star of this RepoInfoV2.
        :rtype: bool
        """
        return self._star

    @star.setter
    def star(self, star):
        """Sets the star of this RepoInfoV2.

        当前用户是否收藏该仓库

        :param star: The star of this RepoInfoV2.
        :type star: bool
        """
        self._star = star

    @property
    def status(self):
        """Gets the status of this RepoInfoV2.

        仓库状态， 0：仓库正常创建成功 1：仓库创建中 2：创建失败 3：仓库冻结 4：仓库已经关闭 

        :return: The status of this RepoInfoV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RepoInfoV2.

        仓库状态， 0：仓库正常创建成功 1：仓库创建中 2：创建失败 3：仓库冻结 4：仓库已经关闭 

        :param status: The status of this RepoInfoV2.
        :type status: int
        """
        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this RepoInfoV2.

        更新时间

        :return: The updated_at of this RepoInfoV2.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RepoInfoV2.

        更新时间

        :param updated_at: The updated_at of this RepoInfoV2.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def user_role(self):
        """Gets the user_role of this RepoInfoV2.

        用户在仓库中的权限:20：只读成员 30：普通成员 40：管理员 

        :return: The user_role of this RepoInfoV2.
        :rtype: int
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this RepoInfoV2.

        用户在仓库中的权限:20：只读成员 30：普通成员 40：管理员 

        :param user_role: The user_role of this RepoInfoV2.
        :type user_role: int
        """
        self._user_role = user_role

    @property
    def visibility_level(self):
        """Gets the visibility_level of this RepoInfoV2.

        是否可见：0私有仓库，20公有仓库

        :return: The visibility_level of this RepoInfoV2.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        """Sets the visibility_level of this RepoInfoV2.

        是否可见：0私有仓库，20公有仓库

        :param visibility_level: The visibility_level of this RepoInfoV2.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def web_url(self):
        """Gets the web_url of this RepoInfoV2.

        web url 路径，访问它将跳转至仓库详情页

        :return: The web_url of this RepoInfoV2.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this RepoInfoV2.

        web url 路径，访问它将跳转至仓库详情页

        :param web_url: The web_url of this RepoInfoV2.
        :type web_url: str
        """
        self._web_url = web_url

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
        if not isinstance(other, RepoInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
