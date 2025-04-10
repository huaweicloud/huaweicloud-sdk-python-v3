# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainRoleAssignmentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'role_id': 'str',
        'subject': 'str',
        'subject_user_id': 'str',
        'subject_group_id': 'str',
        'subject_agency_id': 'str',
        'scope': 'str',
        'scope_project_id': 'str',
        'scope_domain_id': 'str',
        'scope_enterprise_projects_id': 'str',
        'is_inherited': 'bool',
        'include_group': 'bool',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'role_id': 'role_id',
        'subject': 'subject',
        'subject_user_id': 'subject.user_id',
        'subject_group_id': 'subject.group_id',
        'subject_agency_id': 'subject.agency_id',
        'scope': 'scope',
        'scope_project_id': 'scope.project_id',
        'scope_domain_id': 'scope.domain_id',
        'scope_enterprise_projects_id': 'scope.enterprise_projects_id',
        'is_inherited': 'is_inherited',
        'include_group': 'include_group',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, domain_id=None, role_id=None, subject=None, subject_user_id=None, subject_group_id=None, subject_agency_id=None, scope=None, scope_project_id=None, scope_domain_id=None, scope_enterprise_projects_id=None, is_inherited=None, include_group=None, page=None, per_page=None):
        r"""ShowDomainRoleAssignmentsRequest

        The model defined in huaweicloud sdk

        :param domain_id: 待查询账号ID。
        :type domain_id: str
        :param role_id: 策略ID。
        :type role_id: str
        :param subject: 授权主体,取值范围：user、group、agency。该参数与subject.user_id、subject.group_id、subject.agency_id只能选择一个。
        :type subject: str
        :param subject_user_id: 授权的IAM用户ID。
        :type subject_user_id: str
        :param subject_group_id: 授权的用户组ID。
        :type subject_group_id: str
        :param subject_agency_id: 授权的委托ID。
        :type subject_agency_id: str
        :param scope: 授权范围，取值范围：project、domain、enterprise_project。该参数与scope.project_id、scope.domain_id、scope.enterprise_projects_id只能选择一个。 &gt; - 如需查看全局服务授权记录，scope取值domain或填写scope.domain_id。 &gt; - 如需查看基于所有资源的授权记录，scope取值为domain，且is_inherited取值为true &gt; - 如需查看基于项目的授权记录，scope取值为project或填写scope.project_id。 &gt; - 如需查看基于企业项目的授权记录，scope取值为enterprise_project或填写scope.enterprise_project_id。
        :type scope: str
        :param scope_project_id: 授权的项目ID。
        :type scope_project_id: str
        :param scope_domain_id: 待查询账号ID。
        :type scope_domain_id: str
        :param scope_enterprise_projects_id: 授权的企业项目ID。
        :type scope_enterprise_projects_id: str
        :param is_inherited: 是否包含基于所有项目授权的记录，默认为false。当参数scope&#x3D;domain或者scope.domain_id存在时生效。true：查询基于所有项目授权的记录。 false：查询基于全局服务授权的记录。
        :type is_inherited: bool
        :param include_group: 是否包含基于IAM用户所属用户组授权的记录，默认为true。当参数subject&#x3D;user或者subject.user_id存在时生效。true：查询基于IAM用户授权、IAM用户所属用户组授权的记录。 false：仅查询基于IAM用户授权的记录。
        :type include_group: bool
        :param page: 分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。
        :type page: int
        :param per_page: 分页查询时每页的数据个数，取值范围为[1,50]。需要与page同时存在。
        :type per_page: int
        """
        
        

        self._domain_id = None
        self._role_id = None
        self._subject = None
        self._subject_user_id = None
        self._subject_group_id = None
        self._subject_agency_id = None
        self._scope = None
        self._scope_project_id = None
        self._scope_domain_id = None
        self._scope_enterprise_projects_id = None
        self._is_inherited = None
        self._include_group = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        self.domain_id = domain_id
        if role_id is not None:
            self.role_id = role_id
        if subject is not None:
            self.subject = subject
        if subject_user_id is not None:
            self.subject_user_id = subject_user_id
        if subject_group_id is not None:
            self.subject_group_id = subject_group_id
        if subject_agency_id is not None:
            self.subject_agency_id = subject_agency_id
        if scope is not None:
            self.scope = scope
        if scope_project_id is not None:
            self.scope_project_id = scope_project_id
        if scope_domain_id is not None:
            self.scope_domain_id = scope_domain_id
        if scope_enterprise_projects_id is not None:
            self.scope_enterprise_projects_id = scope_enterprise_projects_id
        if is_inherited is not None:
            self.is_inherited = is_inherited
        if include_group is not None:
            self.include_group = include_group
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainRoleAssignmentsRequest.

        待查询账号ID。

        :return: The domain_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainRoleAssignmentsRequest.

        待查询账号ID。

        :param domain_id: The domain_id of this ShowDomainRoleAssignmentsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def role_id(self):
        r"""Gets the role_id of this ShowDomainRoleAssignmentsRequest.

        策略ID。

        :return: The role_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ShowDomainRoleAssignmentsRequest.

        策略ID。

        :param role_id: The role_id of this ShowDomainRoleAssignmentsRequest.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def subject(self):
        r"""Gets the subject of this ShowDomainRoleAssignmentsRequest.

        授权主体,取值范围：user、group、agency。该参数与subject.user_id、subject.group_id、subject.agency_id只能选择一个。

        :return: The subject of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ShowDomainRoleAssignmentsRequest.

        授权主体,取值范围：user、group、agency。该参数与subject.user_id、subject.group_id、subject.agency_id只能选择一个。

        :param subject: The subject of this ShowDomainRoleAssignmentsRequest.
        :type subject: str
        """
        self._subject = subject

    @property
    def subject_user_id(self):
        r"""Gets the subject_user_id of this ShowDomainRoleAssignmentsRequest.

        授权的IAM用户ID。

        :return: The subject_user_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._subject_user_id

    @subject_user_id.setter
    def subject_user_id(self, subject_user_id):
        r"""Sets the subject_user_id of this ShowDomainRoleAssignmentsRequest.

        授权的IAM用户ID。

        :param subject_user_id: The subject_user_id of this ShowDomainRoleAssignmentsRequest.
        :type subject_user_id: str
        """
        self._subject_user_id = subject_user_id

    @property
    def subject_group_id(self):
        r"""Gets the subject_group_id of this ShowDomainRoleAssignmentsRequest.

        授权的用户组ID。

        :return: The subject_group_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._subject_group_id

    @subject_group_id.setter
    def subject_group_id(self, subject_group_id):
        r"""Sets the subject_group_id of this ShowDomainRoleAssignmentsRequest.

        授权的用户组ID。

        :param subject_group_id: The subject_group_id of this ShowDomainRoleAssignmentsRequest.
        :type subject_group_id: str
        """
        self._subject_group_id = subject_group_id

    @property
    def subject_agency_id(self):
        r"""Gets the subject_agency_id of this ShowDomainRoleAssignmentsRequest.

        授权的委托ID。

        :return: The subject_agency_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._subject_agency_id

    @subject_agency_id.setter
    def subject_agency_id(self, subject_agency_id):
        r"""Sets the subject_agency_id of this ShowDomainRoleAssignmentsRequest.

        授权的委托ID。

        :param subject_agency_id: The subject_agency_id of this ShowDomainRoleAssignmentsRequest.
        :type subject_agency_id: str
        """
        self._subject_agency_id = subject_agency_id

    @property
    def scope(self):
        r"""Gets the scope of this ShowDomainRoleAssignmentsRequest.

        授权范围，取值范围：project、domain、enterprise_project。该参数与scope.project_id、scope.domain_id、scope.enterprise_projects_id只能选择一个。 > - 如需查看全局服务授权记录，scope取值domain或填写scope.domain_id。 > - 如需查看基于所有资源的授权记录，scope取值为domain，且is_inherited取值为true > - 如需查看基于项目的授权记录，scope取值为project或填写scope.project_id。 > - 如需查看基于企业项目的授权记录，scope取值为enterprise_project或填写scope.enterprise_project_id。

        :return: The scope of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ShowDomainRoleAssignmentsRequest.

        授权范围，取值范围：project、domain、enterprise_project。该参数与scope.project_id、scope.domain_id、scope.enterprise_projects_id只能选择一个。 > - 如需查看全局服务授权记录，scope取值domain或填写scope.domain_id。 > - 如需查看基于所有资源的授权记录，scope取值为domain，且is_inherited取值为true > - 如需查看基于项目的授权记录，scope取值为project或填写scope.project_id。 > - 如需查看基于企业项目的授权记录，scope取值为enterprise_project或填写scope.enterprise_project_id。

        :param scope: The scope of this ShowDomainRoleAssignmentsRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def scope_project_id(self):
        r"""Gets the scope_project_id of this ShowDomainRoleAssignmentsRequest.

        授权的项目ID。

        :return: The scope_project_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._scope_project_id

    @scope_project_id.setter
    def scope_project_id(self, scope_project_id):
        r"""Sets the scope_project_id of this ShowDomainRoleAssignmentsRequest.

        授权的项目ID。

        :param scope_project_id: The scope_project_id of this ShowDomainRoleAssignmentsRequest.
        :type scope_project_id: str
        """
        self._scope_project_id = scope_project_id

    @property
    def scope_domain_id(self):
        r"""Gets the scope_domain_id of this ShowDomainRoleAssignmentsRequest.

        待查询账号ID。

        :return: The scope_domain_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._scope_domain_id

    @scope_domain_id.setter
    def scope_domain_id(self, scope_domain_id):
        r"""Sets the scope_domain_id of this ShowDomainRoleAssignmentsRequest.

        待查询账号ID。

        :param scope_domain_id: The scope_domain_id of this ShowDomainRoleAssignmentsRequest.
        :type scope_domain_id: str
        """
        self._scope_domain_id = scope_domain_id

    @property
    def scope_enterprise_projects_id(self):
        r"""Gets the scope_enterprise_projects_id of this ShowDomainRoleAssignmentsRequest.

        授权的企业项目ID。

        :return: The scope_enterprise_projects_id of this ShowDomainRoleAssignmentsRequest.
        :rtype: str
        """
        return self._scope_enterprise_projects_id

    @scope_enterprise_projects_id.setter
    def scope_enterprise_projects_id(self, scope_enterprise_projects_id):
        r"""Sets the scope_enterprise_projects_id of this ShowDomainRoleAssignmentsRequest.

        授权的企业项目ID。

        :param scope_enterprise_projects_id: The scope_enterprise_projects_id of this ShowDomainRoleAssignmentsRequest.
        :type scope_enterprise_projects_id: str
        """
        self._scope_enterprise_projects_id = scope_enterprise_projects_id

    @property
    def is_inherited(self):
        r"""Gets the is_inherited of this ShowDomainRoleAssignmentsRequest.

        是否包含基于所有项目授权的记录，默认为false。当参数scope=domain或者scope.domain_id存在时生效。true：查询基于所有项目授权的记录。 false：查询基于全局服务授权的记录。

        :return: The is_inherited of this ShowDomainRoleAssignmentsRequest.
        :rtype: bool
        """
        return self._is_inherited

    @is_inherited.setter
    def is_inherited(self, is_inherited):
        r"""Sets the is_inherited of this ShowDomainRoleAssignmentsRequest.

        是否包含基于所有项目授权的记录，默认为false。当参数scope=domain或者scope.domain_id存在时生效。true：查询基于所有项目授权的记录。 false：查询基于全局服务授权的记录。

        :param is_inherited: The is_inherited of this ShowDomainRoleAssignmentsRequest.
        :type is_inherited: bool
        """
        self._is_inherited = is_inherited

    @property
    def include_group(self):
        r"""Gets the include_group of this ShowDomainRoleAssignmentsRequest.

        是否包含基于IAM用户所属用户组授权的记录，默认为true。当参数subject=user或者subject.user_id存在时生效。true：查询基于IAM用户授权、IAM用户所属用户组授权的记录。 false：仅查询基于IAM用户授权的记录。

        :return: The include_group of this ShowDomainRoleAssignmentsRequest.
        :rtype: bool
        """
        return self._include_group

    @include_group.setter
    def include_group(self, include_group):
        r"""Sets the include_group of this ShowDomainRoleAssignmentsRequest.

        是否包含基于IAM用户所属用户组授权的记录，默认为true。当参数subject=user或者subject.user_id存在时生效。true：查询基于IAM用户授权、IAM用户所属用户组授权的记录。 false：仅查询基于IAM用户授权的记录。

        :param include_group: The include_group of this ShowDomainRoleAssignmentsRequest.
        :type include_group: bool
        """
        self._include_group = include_group

    @property
    def page(self):
        r"""Gets the page of this ShowDomainRoleAssignmentsRequest.

        分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。

        :return: The page of this ShowDomainRoleAssignmentsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowDomainRoleAssignmentsRequest.

        分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。

        :param page: The page of this ShowDomainRoleAssignmentsRequest.
        :type page: int
        """
        self._page = page

    @property
    def per_page(self):
        r"""Gets the per_page of this ShowDomainRoleAssignmentsRequest.

        分页查询时每页的数据个数，取值范围为[1,50]。需要与page同时存在。

        :return: The per_page of this ShowDomainRoleAssignmentsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ShowDomainRoleAssignmentsRequest.

        分页查询时每页的数据个数，取值范围为[1,50]。需要与page同时存在。

        :param per_page: The per_page of this ShowDomainRoleAssignmentsRequest.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ShowDomainRoleAssignmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
