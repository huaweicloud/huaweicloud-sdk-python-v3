# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateDatapanelObjectsRequest:

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
        'dataclass': 'str',
        'body': 'DataObjectBatchCreateForm'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataclass': 'dataclass',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, dataclass=None, body=None):
        r"""BatchCreateDatapanelObjectsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type workspace_id: str
        :param dataclass: 数据类ID, 您可通过调用[查询数据类列表](ListDataclass.xml)接口获取数据类ID
        :type dataclass: str
        :param body: Body of the BatchCreateDatapanelObjectsRequest
        :type body: :class:`huaweicloudsdksecmaster.v1.DataObjectBatchCreateForm`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._dataclass = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.dataclass = dataclass
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchCreateDatapanelObjectsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this BatchCreateDatapanelObjectsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchCreateDatapanelObjectsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this BatchCreateDatapanelObjectsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this BatchCreateDatapanelObjectsRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The workspace_id of this BatchCreateDatapanelObjectsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this BatchCreateDatapanelObjectsRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param workspace_id: The workspace_id of this BatchCreateDatapanelObjectsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass(self):
        r"""Gets the dataclass of this BatchCreateDatapanelObjectsRequest.

        数据类ID, 您可通过调用[查询数据类列表](ListDataclass.xml)接口获取数据类ID

        :return: The dataclass of this BatchCreateDatapanelObjectsRequest.
        :rtype: str
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        r"""Sets the dataclass of this BatchCreateDatapanelObjectsRequest.

        数据类ID, 您可通过调用[查询数据类列表](ListDataclass.xml)接口获取数据类ID

        :param dataclass: The dataclass of this BatchCreateDatapanelObjectsRequest.
        :type dataclass: str
        """
        self._dataclass = dataclass

    @property
    def body(self):
        r"""Gets the body of this BatchCreateDatapanelObjectsRequest.

        :return: The body of this BatchCreateDatapanelObjectsRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DataObjectBatchCreateForm`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateDatapanelObjectsRequest.

        :param body: The body of this BatchCreateDatapanelObjectsRequest.
        :type body: :class:`huaweicloudsdksecmaster.v1.DataObjectBatchCreateForm`
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
        if not isinstance(other, BatchCreateDatapanelObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
