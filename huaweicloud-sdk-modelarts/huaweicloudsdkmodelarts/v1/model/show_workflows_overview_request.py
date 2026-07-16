# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowsOverviewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'search_type': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'search_type': 'search_type',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, workspace_id=None, search_type=None, name=None, description=None):
        r"""ShowWorkflowsOverviewRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param search_type: 过滤方式。可选值如下： - equal表示精确匹配。 - contain表示模糊匹配。  具体过滤的字段，由各个接口额外定义参数。例如Workflow支持按照名称（name）进行过滤，则相应的过滤字段为name。name&#x3D;workflow&amp;search_type&#x3D;contain表示查询名称中含有Workflow字样的所有工作流。
        :type search_type: str
        :param name: 工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。
        :type name: str
        :param description: 工作流描述信息。
        :type description: str
        """
        
        

        self._workspace_id = None
        self._search_type = None
        self._name = None
        self._description = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if search_type is not None:
            self.search_type = search_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowWorkflowsOverviewRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this ShowWorkflowsOverviewRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowWorkflowsOverviewRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this ShowWorkflowsOverviewRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def search_type(self):
        r"""Gets the search_type of this ShowWorkflowsOverviewRequest.

        过滤方式。可选值如下： - equal表示精确匹配。 - contain表示模糊匹配。  具体过滤的字段，由各个接口额外定义参数。例如Workflow支持按照名称（name）进行过滤，则相应的过滤字段为name。name=workflow&search_type=contain表示查询名称中含有Workflow字样的所有工作流。

        :return: The search_type of this ShowWorkflowsOverviewRequest.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this ShowWorkflowsOverviewRequest.

        过滤方式。可选值如下： - equal表示精确匹配。 - contain表示模糊匹配。  具体过滤的字段，由各个接口额外定义参数。例如Workflow支持按照名称（name）进行过滤，则相应的过滤字段为name。name=workflow&search_type=contain表示查询名称中含有Workflow字样的所有工作流。

        :param search_type: The search_type of this ShowWorkflowsOverviewRequest.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def name(self):
        r"""Gets the name of this ShowWorkflowsOverviewRequest.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :return: The name of this ShowWorkflowsOverviewRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowWorkflowsOverviewRequest.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :param name: The name of this ShowWorkflowsOverviewRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowWorkflowsOverviewRequest.

        工作流描述信息。

        :return: The description of this ShowWorkflowsOverviewRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowWorkflowsOverviewRequest.

        工作流描述信息。

        :param description: The description of this ShowWorkflowsOverviewRequest.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ShowWorkflowsOverviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
