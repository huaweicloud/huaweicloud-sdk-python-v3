# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComponentTemplateRequest:

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
        'template_id': 'str',
        'body': 'CreateTemplateReq'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'template_id': 'template_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, template_id=None, body=None):
        r"""UpdateComponentTemplateRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param template_id: 插件配置模板ID
        :type template_id: str
        :param body: Body of the UpdateComponentTemplateRequest
        :type body: :class:`huaweicloudsdksecmaster.v1.CreateTemplateReq`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._template_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.template_id = template_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateComponentTemplateRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this UpdateComponentTemplateRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateComponentTemplateRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this UpdateComponentTemplateRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateComponentTemplateRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this UpdateComponentTemplateRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateComponentTemplateRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this UpdateComponentTemplateRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateComponentTemplateRequest.

        插件配置模板ID

        :return: The template_id of this UpdateComponentTemplateRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateComponentTemplateRequest.

        插件配置模板ID

        :param template_id: The template_id of this UpdateComponentTemplateRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def body(self):
        r"""Gets the body of this UpdateComponentTemplateRequest.

        :return: The body of this UpdateComponentTemplateRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateTemplateReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateComponentTemplateRequest.

        :param body: The body of this UpdateComponentTemplateRequest.
        :type body: :class:`huaweicloudsdksecmaster.v1.CreateTemplateReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateComponentTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
