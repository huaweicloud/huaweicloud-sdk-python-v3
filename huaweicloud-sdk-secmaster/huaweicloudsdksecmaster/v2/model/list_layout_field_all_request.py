# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLayoutFieldAllRequest:

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
        'name': 'str',
        'is_built_in': 'bool',
        'business_code': 'str',
        'layout_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'name': 'name',
        'is_built_in': 'is_built_in',
        'business_code': 'business_code',
        'layout_id': 'layout_id'
    }

    def __init__(self, project_id=None, workspace_id=None, name=None, is_built_in=None, business_code=None, layout_id=None):
        r"""ListLayoutFieldAllRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type workspace_id: str
        :param name: 名称查询
        :type name: str
        :param is_built_in: 是否内置
        :type is_built_in: bool
        :param business_code: 数据类业务编码
        :type business_code: str
        :param layout_id: 布局id
        :type layout_id: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._name = None
        self._is_built_in = None
        self._business_code = None
        self._layout_id = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if name is not None:
            self.name = name
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if business_code is not None:
            self.business_code = business_code
        if layout_id is not None:
            self.layout_id = layout_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListLayoutFieldAllRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListLayoutFieldAllRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListLayoutFieldAllRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListLayoutFieldAllRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListLayoutFieldAllRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The workspace_id of this ListLayoutFieldAllRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListLayoutFieldAllRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param workspace_id: The workspace_id of this ListLayoutFieldAllRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def name(self):
        r"""Gets the name of this ListLayoutFieldAllRequest.

        名称查询

        :return: The name of this ListLayoutFieldAllRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListLayoutFieldAllRequest.

        名称查询

        :param name: The name of this ListLayoutFieldAllRequest.
        :type name: str
        """
        self._name = name

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this ListLayoutFieldAllRequest.

        是否内置

        :return: The is_built_in of this ListLayoutFieldAllRequest.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this ListLayoutFieldAllRequest.

        是否内置

        :param is_built_in: The is_built_in of this ListLayoutFieldAllRequest.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def business_code(self):
        r"""Gets the business_code of this ListLayoutFieldAllRequest.

        数据类业务编码

        :return: The business_code of this ListLayoutFieldAllRequest.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        r"""Sets the business_code of this ListLayoutFieldAllRequest.

        数据类业务编码

        :param business_code: The business_code of this ListLayoutFieldAllRequest.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def layout_id(self):
        r"""Gets the layout_id of this ListLayoutFieldAllRequest.

        布局id

        :return: The layout_id of this ListLayoutFieldAllRequest.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this ListLayoutFieldAllRequest.

        布局id

        :param layout_id: The layout_id of this ListLayoutFieldAllRequest.
        :type layout_id: str
        """
        self._layout_id = layout_id

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
        if not isinstance(other, ListLayoutFieldAllRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
