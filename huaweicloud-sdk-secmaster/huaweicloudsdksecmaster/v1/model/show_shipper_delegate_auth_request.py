# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShipperDelegateAuthRequest:

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
        'workspace_id': 'str',
        'domain_id': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'domain_id': 'domain_id',
        'agency_name': 'agency_name'
    }

    def __init__(self, project_id=None, workspace_id=None, domain_id=None, agency_name=None):
        r"""ShowShipperDelegateAuthRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param agency_name: 委托的名称。委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务器的临时凭证。
        :type agency_name: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._domain_id = None
        self._agency_name = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.domain_id = domain_id
        self.agency_name = agency_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowShipperDelegateAuthRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ShowShipperDelegateAuthRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowShipperDelegateAuthRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ShowShipperDelegateAuthRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowShipperDelegateAuthRequest.

        工作空间ID

        :return: The workspace_id of this ShowShipperDelegateAuthRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowShipperDelegateAuthRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ShowShipperDelegateAuthRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowShipperDelegateAuthRequest.

        账号ID

        :return: The domain_id of this ShowShipperDelegateAuthRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowShipperDelegateAuthRequest.

        账号ID

        :param domain_id: The domain_id of this ShowShipperDelegateAuthRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShowShipperDelegateAuthRequest.

        委托的名称。委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务器的临时凭证。

        :return: The agency_name of this ShowShipperDelegateAuthRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShowShipperDelegateAuthRequest.

        委托的名称。委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务器的临时凭证。

        :param agency_name: The agency_name of this ShowShipperDelegateAuthRequest.
        :type agency_name: str
        """
        self._agency_name = agency_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowShipperDelegateAuthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
