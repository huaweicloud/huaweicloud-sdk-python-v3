# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkspaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'name': 'str',
        'description': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'is_view': 'bool',
        'region_id': 'str',
        'view_bind_id': 'str',
        'view_bind_name': 'str',
        'workspace_agency_list': 'list[CreateWorkspaceResponseBodyWorkspaceAgencyList]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'description': 'description',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'is_view': 'is_view',
        'region_id': 'region_id',
        'view_bind_id': 'view_bind_id',
        'view_bind_name': 'view_bind_name',
        'workspace_agency_list': 'workspace_agency_list'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, description=None, creator_id=None, creator_name=None, modifier_id=None, modifier_name=None, project_id=None, project_name=None, domain_id=None, domain_name=None, enterprise_project_id=None, enterprise_project_name=None, is_view=None, region_id=None, view_bind_id=None, view_bind_name=None, workspace_agency_list=None):
        r"""UpdateWorkspaceResponse

        The model defined in huaweicloud sdk

        :param id: 工作空间id
        :type id: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param name: 工作空间名称
        :type name: str
        :param description: 工作空间描述
        :type description: str
        :param creator_id: 创建人id
        :type creator_id: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param modifier_id: 修改人id
        :type modifier_id: str
        :param modifier_name: 修改人名称
        :type modifier_name: str
        :param project_id: 所属项目id
        :type project_id: str
        :param project_name: 所属项目名称
        :type project_name: str
        :param domain_id: 所属租户id
        :type domain_id: str
        :param domain_name: 所属租户名称
        :type domain_name: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param is_view: 是否是视图
        :type is_view: bool
        :param region_id: 区域id
        :type region_id: str
        :param view_bind_id: 视图绑定的空间id
        :type view_bind_id: str
        :param view_bind_name: 视图绑定的空间名称
        :type view_bind_name: str
        :param workspace_agency_list: 纳管空间列表
        :type workspace_agency_list: list[:class:`huaweicloudsdksecmaster.v2.CreateWorkspaceResponseBodyWorkspaceAgencyList`]
        """
        
        super(UpdateWorkspaceResponse, self).__init__()

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._description = None
        self._creator_id = None
        self._creator_name = None
        self._modifier_id = None
        self._modifier_name = None
        self._project_id = None
        self._project_name = None
        self._domain_id = None
        self._domain_name = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._is_view = None
        self._region_id = None
        self._view_bind_id = None
        self._view_bind_name = None
        self._workspace_agency_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if is_view is not None:
            self.is_view = is_view
        if region_id is not None:
            self.region_id = region_id
        if view_bind_id is not None:
            self.view_bind_id = view_bind_id
        if view_bind_name is not None:
            self.view_bind_name = view_bind_name
        if workspace_agency_list is not None:
            self.workspace_agency_list = workspace_agency_list

    @property
    def id(self):
        r"""Gets the id of this UpdateWorkspaceResponse.

        工作空间id

        :return: The id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateWorkspaceResponse.

        工作空间id

        :param id: The id of this UpdateWorkspaceResponse.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateWorkspaceResponse.

        创建时间

        :return: The create_time of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateWorkspaceResponse.

        创建时间

        :param create_time: The create_time of this UpdateWorkspaceResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateWorkspaceResponse.

        更新时间

        :return: The update_time of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateWorkspaceResponse.

        更新时间

        :param update_time: The update_time of this UpdateWorkspaceResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def name(self):
        r"""Gets the name of this UpdateWorkspaceResponse.

        工作空间名称

        :return: The name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateWorkspaceResponse.

        工作空间名称

        :param name: The name of this UpdateWorkspaceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateWorkspaceResponse.

        工作空间描述

        :return: The description of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateWorkspaceResponse.

        工作空间描述

        :param description: The description of this UpdateWorkspaceResponse.
        :type description: str
        """
        self._description = description

    @property
    def creator_id(self):
        r"""Gets the creator_id of this UpdateWorkspaceResponse.

        创建人id

        :return: The creator_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this UpdateWorkspaceResponse.

        创建人id

        :param creator_id: The creator_id of this UpdateWorkspaceResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this UpdateWorkspaceResponse.

        创建人名称

        :return: The creator_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this UpdateWorkspaceResponse.

        创建人名称

        :param creator_name: The creator_name of this UpdateWorkspaceResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this UpdateWorkspaceResponse.

        修改人id

        :return: The modifier_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this UpdateWorkspaceResponse.

        修改人id

        :param modifier_id: The modifier_id of this UpdateWorkspaceResponse.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this UpdateWorkspaceResponse.

        修改人名称

        :return: The modifier_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this UpdateWorkspaceResponse.

        修改人名称

        :param modifier_name: The modifier_name of this UpdateWorkspaceResponse.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateWorkspaceResponse.

        所属项目id

        :return: The project_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateWorkspaceResponse.

        所属项目id

        :param project_id: The project_id of this UpdateWorkspaceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this UpdateWorkspaceResponse.

        所属项目名称

        :return: The project_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this UpdateWorkspaceResponse.

        所属项目名称

        :param project_name: The project_name of this UpdateWorkspaceResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateWorkspaceResponse.

        所属租户id

        :return: The domain_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateWorkspaceResponse.

        所属租户id

        :param domain_id: The domain_id of this UpdateWorkspaceResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateWorkspaceResponse.

        所属租户名称

        :return: The domain_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateWorkspaceResponse.

        所属租户名称

        :param domain_name: The domain_name of this UpdateWorkspaceResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateWorkspaceResponse.

        企业项目id

        :return: The enterprise_project_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateWorkspaceResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this UpdateWorkspaceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this UpdateWorkspaceResponse.

        企业项目名称

        :return: The enterprise_project_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this UpdateWorkspaceResponse.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this UpdateWorkspaceResponse.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def is_view(self):
        r"""Gets the is_view of this UpdateWorkspaceResponse.

        是否是视图

        :return: The is_view of this UpdateWorkspaceResponse.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        r"""Sets the is_view of this UpdateWorkspaceResponse.

        是否是视图

        :param is_view: The is_view of this UpdateWorkspaceResponse.
        :type is_view: bool
        """
        self._is_view = is_view

    @property
    def region_id(self):
        r"""Gets the region_id of this UpdateWorkspaceResponse.

        区域id

        :return: The region_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this UpdateWorkspaceResponse.

        区域id

        :param region_id: The region_id of this UpdateWorkspaceResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def view_bind_id(self):
        r"""Gets the view_bind_id of this UpdateWorkspaceResponse.

        视图绑定的空间id

        :return: The view_bind_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._view_bind_id

    @view_bind_id.setter
    def view_bind_id(self, view_bind_id):
        r"""Sets the view_bind_id of this UpdateWorkspaceResponse.

        视图绑定的空间id

        :param view_bind_id: The view_bind_id of this UpdateWorkspaceResponse.
        :type view_bind_id: str
        """
        self._view_bind_id = view_bind_id

    @property
    def view_bind_name(self):
        r"""Gets the view_bind_name of this UpdateWorkspaceResponse.

        视图绑定的空间名称

        :return: The view_bind_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._view_bind_name

    @view_bind_name.setter
    def view_bind_name(self, view_bind_name):
        r"""Sets the view_bind_name of this UpdateWorkspaceResponse.

        视图绑定的空间名称

        :param view_bind_name: The view_bind_name of this UpdateWorkspaceResponse.
        :type view_bind_name: str
        """
        self._view_bind_name = view_bind_name

    @property
    def workspace_agency_list(self):
        r"""Gets the workspace_agency_list of this UpdateWorkspaceResponse.

        纳管空间列表

        :return: The workspace_agency_list of this UpdateWorkspaceResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CreateWorkspaceResponseBodyWorkspaceAgencyList`]
        """
        return self._workspace_agency_list

    @workspace_agency_list.setter
    def workspace_agency_list(self, workspace_agency_list):
        r"""Sets the workspace_agency_list of this UpdateWorkspaceResponse.

        纳管空间列表

        :param workspace_agency_list: The workspace_agency_list of this UpdateWorkspaceResponse.
        :type workspace_agency_list: list[:class:`huaweicloudsdksecmaster.v2.CreateWorkspaceResponseBodyWorkspaceAgencyList`]
        """
        self._workspace_agency_list = workspace_agency_list

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
        if not isinstance(other, UpdateWorkspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
