# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShipperParamRequest:

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
        'param_type': 'str',
        'param': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'param_type': 'param_type',
        'param': 'param'
    }

    def __init__(self, project_id=None, workspace_id=None, param_type=None, param=None):
        r"""ShowShipperParamRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param param_type: 参数类型
        :type param_type: str
        :param param: 根据param的传参决定，传类型的一级菜单id，如：(lts_group_id)是一串id
        :type param: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._param_type = None
        self._param = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.param_type = param_type
        if param is not None:
            self.param = param

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowShipperParamRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ShowShipperParamRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowShipperParamRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ShowShipperParamRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowShipperParamRequest.

        工作空间ID

        :return: The workspace_id of this ShowShipperParamRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowShipperParamRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ShowShipperParamRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def param_type(self):
        r"""Gets the param_type of this ShowShipperParamRequest.

        参数类型

        :return: The param_type of this ShowShipperParamRequest.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        r"""Sets the param_type of this ShowShipperParamRequest.

        参数类型

        :param param_type: The param_type of this ShowShipperParamRequest.
        :type param_type: str
        """
        self._param_type = param_type

    @property
    def param(self):
        r"""Gets the param of this ShowShipperParamRequest.

        根据param的传参决定，传类型的一级菜单id，如：(lts_group_id)是一串id

        :return: The param of this ShowShipperParamRequest.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this ShowShipperParamRequest.

        根据param的传参决定，传类型的一级菜单id，如：(lts_group_id)是一串id

        :param param: The param of this ShowShipperParamRequest.
        :type param: str
        """
        self._param = param

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
        if not isinstance(other, ShowShipperParamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
