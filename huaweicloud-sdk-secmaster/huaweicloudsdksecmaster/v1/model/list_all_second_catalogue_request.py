# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllSecondCatalogueRequest:

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
        'catalogue_type': 'str',
        'catalogue_code': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'catalogue_type': 'catalogue_type',
        'catalogue_code': 'catalogue_code'
    }

    def __init__(self, project_id=None, workspace_id=None, catalogue_type=None, catalogue_code=None):
        r"""ListAllSecondCatalogueRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type workspace_id: str
        :param catalogue_type: 目录类型（内置或自定义）
        :type catalogue_type: str
        :param catalogue_code: 目录编码
        :type catalogue_code: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._catalogue_type = None
        self._catalogue_code = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if catalogue_type is not None:
            self.catalogue_type = catalogue_type
        if catalogue_code is not None:
            self.catalogue_code = catalogue_code

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAllSecondCatalogueRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListAllSecondCatalogueRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAllSecondCatalogueRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListAllSecondCatalogueRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAllSecondCatalogueRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The workspace_id of this ListAllSecondCatalogueRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAllSecondCatalogueRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param workspace_id: The workspace_id of this ListAllSecondCatalogueRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def catalogue_type(self):
        r"""Gets the catalogue_type of this ListAllSecondCatalogueRequest.

        目录类型（内置或自定义）

        :return: The catalogue_type of this ListAllSecondCatalogueRequest.
        :rtype: str
        """
        return self._catalogue_type

    @catalogue_type.setter
    def catalogue_type(self, catalogue_type):
        r"""Sets the catalogue_type of this ListAllSecondCatalogueRequest.

        目录类型（内置或自定义）

        :param catalogue_type: The catalogue_type of this ListAllSecondCatalogueRequest.
        :type catalogue_type: str
        """
        self._catalogue_type = catalogue_type

    @property
    def catalogue_code(self):
        r"""Gets the catalogue_code of this ListAllSecondCatalogueRequest.

        目录编码

        :return: The catalogue_code of this ListAllSecondCatalogueRequest.
        :rtype: str
        """
        return self._catalogue_code

    @catalogue_code.setter
    def catalogue_code(self, catalogue_code):
        r"""Sets the catalogue_code of this ListAllSecondCatalogueRequest.

        目录编码

        :param catalogue_code: The catalogue_code of this ListAllSecondCatalogueRequest.
        :type catalogue_code: str
        """
        self._catalogue_code = catalogue_code

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
        if not isinstance(other, ListAllSecondCatalogueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
