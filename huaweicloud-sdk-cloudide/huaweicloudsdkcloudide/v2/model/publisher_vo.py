# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublisherVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_repo': 'str',
        'created_time': 'datetime',
        'description': 'str',
        'eamap_info': 'str',
        'email': 'str',
        'espase_group': 'str',
        'extension_count': 'int',
        'id': 'str',
        'identifier': 'str',
        'is_open': 'bool',
        'is_org': 'bool',
        'logo_url': 'str',
        'member_count': 'int',
        'name': 'str',
        'official': 'bool',
        'owners': 'list[MemberRoleVo]',
        'publisher_review': 'bool',
        'role': 'str',
        'status': 'bool',
        'suite_count': 'int',
        'support_url': 'str',
        'system_review': 'bool',
        'updated_time': 'datetime',
        'web_url': 'str'
    }

    attribute_map = {
        'code_repo': 'code_repo',
        'created_time': 'created_time',
        'description': 'description',
        'eamap_info': 'eamap_info',
        'email': 'email',
        'espase_group': 'espase_group',
        'extension_count': 'extension_count',
        'id': 'id',
        'identifier': 'identifier',
        'is_open': 'is_open',
        'is_org': 'is_org',
        'logo_url': 'logo_url',
        'member_count': 'member_count',
        'name': 'name',
        'official': 'official',
        'owners': 'owners',
        'publisher_review': 'publisher_review',
        'role': 'role',
        'status': 'status',
        'suite_count': 'suite_count',
        'support_url': 'support_url',
        'system_review': 'system_review',
        'updated_time': 'updated_time',
        'web_url': 'web_url'
    }

    def __init__(self, code_repo=None, created_time=None, description=None, eamap_info=None, email=None, espase_group=None, extension_count=None, id=None, identifier=None, is_open=None, is_org=None, logo_url=None, member_count=None, name=None, official=None, owners=None, publisher_review=None, role=None, status=None, suite_count=None, support_url=None, system_review=None, updated_time=None, web_url=None):
        """PublisherVO

        The model defined in huaweicloud sdk

        :param code_repo: 代码地址
        :type code_repo: str
        :param created_time: 创建时间
        :type created_time: datetime
        :param description: 发布商描述
        :type description: str
        :param eamap_info: EAMAP注册信息
        :type eamap_info: str
        :param email: 邮箱
        :type email: str
        :param espase_group: espase交流群号
        :type espase_group: str
        :param extension_count: 插件数量
        :type extension_count: int
        :param id: 发布商ID
        :type id: str
        :param identifier: 唯一标志
        :type identifier: str
        :param is_open: 开源发布商,0:非开源; 1:开源;
        :type is_open: bool
        :param is_org: 发布商或组织,0:发布商; 1:组织;
        :type is_org: bool
        :param logo_url: 发布商logo
        :type logo_url: str
        :param member_count: 成员数量
        :type member_count: int
        :param name: 发布商名称
        :type name: str
        :param official: 是否是官方发布商
        :type official: bool
        :param owners: 成员角色
        :type owners: list[:class:`huaweicloudsdkcloudide.v2.MemberRoleVo`]
        :param publisher_review: 是否开启发布商审核,1:开启；0:关闭
        :type publisher_review: bool
        :param role: 角色
        :type role: str
        :param status: 状态,0:禁用; 1:正常;
        :type status: bool
        :param suite_count: 匹配数量
        :type suite_count: int
        :param support_url: 支持地址
        :type support_url: str
        :param system_review: 是否忽略系统审核,1:忽略；0:不忽略
        :type system_review: bool
        :param updated_time: 更新时间
        :type updated_time: datetime
        :param web_url: 官网地址
        :type web_url: str
        """
        
        

        self._code_repo = None
        self._created_time = None
        self._description = None
        self._eamap_info = None
        self._email = None
        self._espase_group = None
        self._extension_count = None
        self._id = None
        self._identifier = None
        self._is_open = None
        self._is_org = None
        self._logo_url = None
        self._member_count = None
        self._name = None
        self._official = None
        self._owners = None
        self._publisher_review = None
        self._role = None
        self._status = None
        self._suite_count = None
        self._support_url = None
        self._system_review = None
        self._updated_time = None
        self._web_url = None
        self.discriminator = None

        if code_repo is not None:
            self.code_repo = code_repo
        if created_time is not None:
            self.created_time = created_time
        if description is not None:
            self.description = description
        if eamap_info is not None:
            self.eamap_info = eamap_info
        if email is not None:
            self.email = email
        if espase_group is not None:
            self.espase_group = espase_group
        if extension_count is not None:
            self.extension_count = extension_count
        if id is not None:
            self.id = id
        if identifier is not None:
            self.identifier = identifier
        if is_open is not None:
            self.is_open = is_open
        if is_org is not None:
            self.is_org = is_org
        if logo_url is not None:
            self.logo_url = logo_url
        if member_count is not None:
            self.member_count = member_count
        if name is not None:
            self.name = name
        if official is not None:
            self.official = official
        if owners is not None:
            self.owners = owners
        if publisher_review is not None:
            self.publisher_review = publisher_review
        if role is not None:
            self.role = role
        if status is not None:
            self.status = status
        if suite_count is not None:
            self.suite_count = suite_count
        if support_url is not None:
            self.support_url = support_url
        if system_review is not None:
            self.system_review = system_review
        if updated_time is not None:
            self.updated_time = updated_time
        if web_url is not None:
            self.web_url = web_url

    @property
    def code_repo(self):
        """Gets the code_repo of this PublisherVO.

        代码地址

        :return: The code_repo of this PublisherVO.
        :rtype: str
        """
        return self._code_repo

    @code_repo.setter
    def code_repo(self, code_repo):
        """Sets the code_repo of this PublisherVO.

        代码地址

        :param code_repo: The code_repo of this PublisherVO.
        :type code_repo: str
        """
        self._code_repo = code_repo

    @property
    def created_time(self):
        """Gets the created_time of this PublisherVO.

        创建时间

        :return: The created_time of this PublisherVO.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this PublisherVO.

        创建时间

        :param created_time: The created_time of this PublisherVO.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def description(self):
        """Gets the description of this PublisherVO.

        发布商描述

        :return: The description of this PublisherVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublisherVO.

        发布商描述

        :param description: The description of this PublisherVO.
        :type description: str
        """
        self._description = description

    @property
    def eamap_info(self):
        """Gets the eamap_info of this PublisherVO.

        EAMAP注册信息

        :return: The eamap_info of this PublisherVO.
        :rtype: str
        """
        return self._eamap_info

    @eamap_info.setter
    def eamap_info(self, eamap_info):
        """Sets the eamap_info of this PublisherVO.

        EAMAP注册信息

        :param eamap_info: The eamap_info of this PublisherVO.
        :type eamap_info: str
        """
        self._eamap_info = eamap_info

    @property
    def email(self):
        """Gets the email of this PublisherVO.

        邮箱

        :return: The email of this PublisherVO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PublisherVO.

        邮箱

        :param email: The email of this PublisherVO.
        :type email: str
        """
        self._email = email

    @property
    def espase_group(self):
        """Gets the espase_group of this PublisherVO.

        espase交流群号

        :return: The espase_group of this PublisherVO.
        :rtype: str
        """
        return self._espase_group

    @espase_group.setter
    def espase_group(self, espase_group):
        """Sets the espase_group of this PublisherVO.

        espase交流群号

        :param espase_group: The espase_group of this PublisherVO.
        :type espase_group: str
        """
        self._espase_group = espase_group

    @property
    def extension_count(self):
        """Gets the extension_count of this PublisherVO.

        插件数量

        :return: The extension_count of this PublisherVO.
        :rtype: int
        """
        return self._extension_count

    @extension_count.setter
    def extension_count(self, extension_count):
        """Sets the extension_count of this PublisherVO.

        插件数量

        :param extension_count: The extension_count of this PublisherVO.
        :type extension_count: int
        """
        self._extension_count = extension_count

    @property
    def id(self):
        """Gets the id of this PublisherVO.

        发布商ID

        :return: The id of this PublisherVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublisherVO.

        发布商ID

        :param id: The id of this PublisherVO.
        :type id: str
        """
        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this PublisherVO.

        唯一标志

        :return: The identifier of this PublisherVO.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PublisherVO.

        唯一标志

        :param identifier: The identifier of this PublisherVO.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def is_open(self):
        """Gets the is_open of this PublisherVO.

        开源发布商,0:非开源; 1:开源;

        :return: The is_open of this PublisherVO.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        """Sets the is_open of this PublisherVO.

        开源发布商,0:非开源; 1:开源;

        :param is_open: The is_open of this PublisherVO.
        :type is_open: bool
        """
        self._is_open = is_open

    @property
    def is_org(self):
        """Gets the is_org of this PublisherVO.

        发布商或组织,0:发布商; 1:组织;

        :return: The is_org of this PublisherVO.
        :rtype: bool
        """
        return self._is_org

    @is_org.setter
    def is_org(self, is_org):
        """Sets the is_org of this PublisherVO.

        发布商或组织,0:发布商; 1:组织;

        :param is_org: The is_org of this PublisherVO.
        :type is_org: bool
        """
        self._is_org = is_org

    @property
    def logo_url(self):
        """Gets the logo_url of this PublisherVO.

        发布商logo

        :return: The logo_url of this PublisherVO.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this PublisherVO.

        发布商logo

        :param logo_url: The logo_url of this PublisherVO.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def member_count(self):
        """Gets the member_count of this PublisherVO.

        成员数量

        :return: The member_count of this PublisherVO.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this PublisherVO.

        成员数量

        :param member_count: The member_count of this PublisherVO.
        :type member_count: int
        """
        self._member_count = member_count

    @property
    def name(self):
        """Gets the name of this PublisherVO.

        发布商名称

        :return: The name of this PublisherVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublisherVO.

        发布商名称

        :param name: The name of this PublisherVO.
        :type name: str
        """
        self._name = name

    @property
    def official(self):
        """Gets the official of this PublisherVO.

        是否是官方发布商

        :return: The official of this PublisherVO.
        :rtype: bool
        """
        return self._official

    @official.setter
    def official(self, official):
        """Sets the official of this PublisherVO.

        是否是官方发布商

        :param official: The official of this PublisherVO.
        :type official: bool
        """
        self._official = official

    @property
    def owners(self):
        """Gets the owners of this PublisherVO.

        成员角色

        :return: The owners of this PublisherVO.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.MemberRoleVo`]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this PublisherVO.

        成员角色

        :param owners: The owners of this PublisherVO.
        :type owners: list[:class:`huaweicloudsdkcloudide.v2.MemberRoleVo`]
        """
        self._owners = owners

    @property
    def publisher_review(self):
        """Gets the publisher_review of this PublisherVO.

        是否开启发布商审核,1:开启；0:关闭

        :return: The publisher_review of this PublisherVO.
        :rtype: bool
        """
        return self._publisher_review

    @publisher_review.setter
    def publisher_review(self, publisher_review):
        """Sets the publisher_review of this PublisherVO.

        是否开启发布商审核,1:开启；0:关闭

        :param publisher_review: The publisher_review of this PublisherVO.
        :type publisher_review: bool
        """
        self._publisher_review = publisher_review

    @property
    def role(self):
        """Gets the role of this PublisherVO.

        角色

        :return: The role of this PublisherVO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this PublisherVO.

        角色

        :param role: The role of this PublisherVO.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        """Gets the status of this PublisherVO.

        状态,0:禁用; 1:正常;

        :return: The status of this PublisherVO.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublisherVO.

        状态,0:禁用; 1:正常;

        :param status: The status of this PublisherVO.
        :type status: bool
        """
        self._status = status

    @property
    def suite_count(self):
        """Gets the suite_count of this PublisherVO.

        匹配数量

        :return: The suite_count of this PublisherVO.
        :rtype: int
        """
        return self._suite_count

    @suite_count.setter
    def suite_count(self, suite_count):
        """Sets the suite_count of this PublisherVO.

        匹配数量

        :param suite_count: The suite_count of this PublisherVO.
        :type suite_count: int
        """
        self._suite_count = suite_count

    @property
    def support_url(self):
        """Gets the support_url of this PublisherVO.

        支持地址

        :return: The support_url of this PublisherVO.
        :rtype: str
        """
        return self._support_url

    @support_url.setter
    def support_url(self, support_url):
        """Sets the support_url of this PublisherVO.

        支持地址

        :param support_url: The support_url of this PublisherVO.
        :type support_url: str
        """
        self._support_url = support_url

    @property
    def system_review(self):
        """Gets the system_review of this PublisherVO.

        是否忽略系统审核,1:忽略；0:不忽略

        :return: The system_review of this PublisherVO.
        :rtype: bool
        """
        return self._system_review

    @system_review.setter
    def system_review(self, system_review):
        """Sets the system_review of this PublisherVO.

        是否忽略系统审核,1:忽略；0:不忽略

        :param system_review: The system_review of this PublisherVO.
        :type system_review: bool
        """
        self._system_review = system_review

    @property
    def updated_time(self):
        """Gets the updated_time of this PublisherVO.

        更新时间

        :return: The updated_time of this PublisherVO.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this PublisherVO.

        更新时间

        :param updated_time: The updated_time of this PublisherVO.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def web_url(self):
        """Gets the web_url of this PublisherVO.

        官网地址

        :return: The web_url of this PublisherVO.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this PublisherVO.

        官网地址

        :param web_url: The web_url of this PublisherVO.
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
        if not isinstance(other, PublisherVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
