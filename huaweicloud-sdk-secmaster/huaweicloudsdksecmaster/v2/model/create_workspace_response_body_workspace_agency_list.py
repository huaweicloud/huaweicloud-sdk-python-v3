# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkspaceResponseBodyWorkspaceAgencyList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'id': 'str',
        'name': 'str',
        'region_id': 'str',
        'workspace_attribution': 'str',
        'agency_version': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'iam_agency_id': 'str',
        'iam_agency_name': 'str',
        'resource_spec_code': 'list[str]',
        'selected': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'id': 'id',
        'name': 'name',
        'region_id': 'region_id',
        'workspace_attribution': 'workspace_attribution',
        'agency_version': 'agency_version',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'iam_agency_id': 'iam_agency_id',
        'iam_agency_name': 'iam_agency_name',
        'resource_spec_code': 'resource_spec_code',
        'selected': 'selected'
    }

    def __init__(self, project_id=None, id=None, name=None, region_id=None, workspace_attribution=None, agency_version=None, domain_id=None, domain_name=None, iam_agency_id=None, iam_agency_name=None, resource_spec_code=None, selected=None):
        r"""CreateWorkspaceResponseBodyWorkspaceAgencyList

        The model defined in huaweicloud sdk

        :param project_id: 委托空间所属项目id
        :type project_id: str
        :param id: 空间委托id
        :type id: str
        :param name: 空间委托名称
        :type name: str
        :param region_id: 委托空间所属region id
        :type region_id: str
        :param workspace_attribution: THIS_ACCOUNT:本账号空间,CROSS_ACCOUNT:跨账号空间
        :type workspace_attribution: str
        :param agency_version: 委托版本
        :type agency_version: str
        :param domain_id: 委托租户id
        :type domain_id: str
        :param domain_name: 委托租户名称
        :type domain_name: str
        :param iam_agency_id: iam委托id
        :type iam_agency_id: str
        :param iam_agency_name: iam委托名称
        :type iam_agency_name: str
        :param resource_spec_code: 委托空间购买版本
        :type resource_spec_code: list[str]
        :param selected: 是否被视图选中
        :type selected: bool
        """
        
        

        self._project_id = None
        self._id = None
        self._name = None
        self._region_id = None
        self._workspace_attribution = None
        self._agency_version = None
        self._domain_id = None
        self._domain_name = None
        self._iam_agency_id = None
        self._iam_agency_name = None
        self._resource_spec_code = None
        self._selected = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if workspace_attribution is not None:
            self.workspace_attribution = workspace_attribution
        if agency_version is not None:
            self.agency_version = agency_version
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if iam_agency_id is not None:
            self.iam_agency_id = iam_agency_id
        if iam_agency_name is not None:
            self.iam_agency_name = iam_agency_name
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if selected is not None:
            self.selected = selected

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托空间所属项目id

        :return: The project_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托空间所属项目id

        :param project_id: The project_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def id(self):
        r"""Gets the id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        空间委托id

        :return: The id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        空间委托id

        :param id: The id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        空间委托名称

        :return: The name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        空间委托名称

        :param name: The name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托空间所属region id

        :return: The region_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托空间所属region id

        :param region_id: The region_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def workspace_attribution(self):
        r"""Gets the workspace_attribution of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        THIS_ACCOUNT:本账号空间,CROSS_ACCOUNT:跨账号空间

        :return: The workspace_attribution of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._workspace_attribution

    @workspace_attribution.setter
    def workspace_attribution(self, workspace_attribution):
        r"""Sets the workspace_attribution of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        THIS_ACCOUNT:本账号空间,CROSS_ACCOUNT:跨账号空间

        :param workspace_attribution: The workspace_attribution of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type workspace_attribution: str
        """
        self._workspace_attribution = workspace_attribution

    @property
    def agency_version(self):
        r"""Gets the agency_version of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托版本

        :return: The agency_version of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._agency_version

    @agency_version.setter
    def agency_version(self, agency_version):
        r"""Sets the agency_version of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托版本

        :param agency_version: The agency_version of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type agency_version: str
        """
        self._agency_version = agency_version

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托租户id

        :return: The domain_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托租户id

        :param domain_id: The domain_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托租户名称

        :return: The domain_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托租户名称

        :param domain_name: The domain_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def iam_agency_id(self):
        r"""Gets the iam_agency_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        iam委托id

        :return: The iam_agency_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._iam_agency_id

    @iam_agency_id.setter
    def iam_agency_id(self, iam_agency_id):
        r"""Sets the iam_agency_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        iam委托id

        :param iam_agency_id: The iam_agency_id of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type iam_agency_id: str
        """
        self._iam_agency_id = iam_agency_id

    @property
    def iam_agency_name(self):
        r"""Gets the iam_agency_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        iam委托名称

        :return: The iam_agency_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: str
        """
        return self._iam_agency_name

    @iam_agency_name.setter
    def iam_agency_name(self, iam_agency_name):
        r"""Sets the iam_agency_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        iam委托名称

        :param iam_agency_name: The iam_agency_name of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type iam_agency_name: str
        """
        self._iam_agency_name = iam_agency_name

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托空间购买版本

        :return: The resource_spec_code of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: list[str]
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        委托空间购买版本

        :param resource_spec_code: The resource_spec_code of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type resource_spec_code: list[str]
        """
        self._resource_spec_code = resource_spec_code

    @property
    def selected(self):
        r"""Gets the selected of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        是否被视图选中

        :return: The selected of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        r"""Sets the selected of this CreateWorkspaceResponseBodyWorkspaceAgencyList.

        是否被视图选中

        :param selected: The selected of this CreateWorkspaceResponseBodyWorkspaceAgencyList.
        :type selected: bool
        """
        self._selected = selected

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
        if not isinstance(other, CreateWorkspaceResponseBodyWorkspaceAgencyList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
