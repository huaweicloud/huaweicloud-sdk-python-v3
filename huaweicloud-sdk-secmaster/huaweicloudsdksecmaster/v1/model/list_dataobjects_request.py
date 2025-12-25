# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataobjectsRequest:

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
        'dataclass_name': 'str',
        'body': 'DataobjectSearch'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataclass_name': 'dataclass_name',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, dataclass_name=None, body=None):
        r"""ListDataobjectsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type workspace_id: str
        :param dataclass_name: 关联主体数据对象所属数据类名称，小写复数，如告警为alerts，事件为incidents
        :type dataclass_name: str
        :param body: Body of the ListDataobjectsRequest
        :type body: :class:`huaweicloudsdksecmaster.v1.DataobjectSearch`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._dataclass_name = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.dataclass_name = dataclass_name
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this ListDataobjectsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListDataobjectsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListDataobjectsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListDataobjectsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListDataobjectsRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The workspace_id of this ListDataobjectsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListDataobjectsRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param workspace_id: The workspace_id of this ListDataobjectsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this ListDataobjectsRequest.

        关联主体数据对象所属数据类名称，小写复数，如告警为alerts，事件为incidents

        :return: The dataclass_name of this ListDataobjectsRequest.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this ListDataobjectsRequest.

        关联主体数据对象所属数据类名称，小写复数，如告警为alerts，事件为incidents

        :param dataclass_name: The dataclass_name of this ListDataobjectsRequest.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def body(self):
        r"""Gets the body of this ListDataobjectsRequest.

        :return: The body of this ListDataobjectsRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DataobjectSearch`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListDataobjectsRequest.

        :param body: The body of this ListDataobjectsRequest.
        :type body: :class:`huaweicloudsdksecmaster.v1.DataobjectSearch`
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
        if not isinstance(other, ListDataobjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
