# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowProcessNodeVO:

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
        'category': 'str',
        'process_instance_id': 'str',
        'workflow_activity_id': 'str',
        'code': 'str',
        'config': 'WorkItemFlowNodeConfigVO',
        'enable_suspend': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'process_instance_id': 'process_instance_id',
        'workflow_activity_id': 'workflow_activity_id',
        'code': 'code',
        'config': 'config',
        'enable_suspend': 'enable_suspend'
    }

    def __init__(self, id=None, category=None, process_instance_id=None, workflow_activity_id=None, code=None, config=None, enable_suspend=None):
        r"""WorkItemFlowProcessNodeVO

        The model defined in huaweicloud sdk

        :param id: 节点ID
        :type id: str
        :param category: 节点类别
        :type category: str
        :param process_instance_id: 工作流实例ID
        :type process_instance_id: str
        :param workflow_activity_id: 工作流活动ID
        :type workflow_activity_id: str
        :param code: 节点编码
        :type code: str
        :param config: 
        :type config: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowNodeConfigVO`
        :param enable_suspend: 是否允许挂起
        :type enable_suspend: bool
        """
        
        

        self._id = None
        self._category = None
        self._process_instance_id = None
        self._workflow_activity_id = None
        self._code = None
        self._config = None
        self._enable_suspend = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if process_instance_id is not None:
            self.process_instance_id = process_instance_id
        if workflow_activity_id is not None:
            self.workflow_activity_id = workflow_activity_id
        if code is not None:
            self.code = code
        if config is not None:
            self.config = config
        if enable_suspend is not None:
            self.enable_suspend = enable_suspend

    @property
    def id(self):
        r"""Gets the id of this WorkItemFlowProcessNodeVO.

        节点ID

        :return: The id of this WorkItemFlowProcessNodeVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkItemFlowProcessNodeVO.

        节点ID

        :param id: The id of this WorkItemFlowProcessNodeVO.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this WorkItemFlowProcessNodeVO.

        节点类别

        :return: The category of this WorkItemFlowProcessNodeVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this WorkItemFlowProcessNodeVO.

        节点类别

        :param category: The category of this WorkItemFlowProcessNodeVO.
        :type category: str
        """
        self._category = category

    @property
    def process_instance_id(self):
        r"""Gets the process_instance_id of this WorkItemFlowProcessNodeVO.

        工作流实例ID

        :return: The process_instance_id of this WorkItemFlowProcessNodeVO.
        :rtype: str
        """
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, process_instance_id):
        r"""Sets the process_instance_id of this WorkItemFlowProcessNodeVO.

        工作流实例ID

        :param process_instance_id: The process_instance_id of this WorkItemFlowProcessNodeVO.
        :type process_instance_id: str
        """
        self._process_instance_id = process_instance_id

    @property
    def workflow_activity_id(self):
        r"""Gets the workflow_activity_id of this WorkItemFlowProcessNodeVO.

        工作流活动ID

        :return: The workflow_activity_id of this WorkItemFlowProcessNodeVO.
        :rtype: str
        """
        return self._workflow_activity_id

    @workflow_activity_id.setter
    def workflow_activity_id(self, workflow_activity_id):
        r"""Sets the workflow_activity_id of this WorkItemFlowProcessNodeVO.

        工作流活动ID

        :param workflow_activity_id: The workflow_activity_id of this WorkItemFlowProcessNodeVO.
        :type workflow_activity_id: str
        """
        self._workflow_activity_id = workflow_activity_id

    @property
    def code(self):
        r"""Gets the code of this WorkItemFlowProcessNodeVO.

        节点编码

        :return: The code of this WorkItemFlowProcessNodeVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this WorkItemFlowProcessNodeVO.

        节点编码

        :param code: The code of this WorkItemFlowProcessNodeVO.
        :type code: str
        """
        self._code = code

    @property
    def config(self):
        r"""Gets the config of this WorkItemFlowProcessNodeVO.

        :return: The config of this WorkItemFlowProcessNodeVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowNodeConfigVO`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this WorkItemFlowProcessNodeVO.

        :param config: The config of this WorkItemFlowProcessNodeVO.
        :type config: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowNodeConfigVO`
        """
        self._config = config

    @property
    def enable_suspend(self):
        r"""Gets the enable_suspend of this WorkItemFlowProcessNodeVO.

        是否允许挂起

        :return: The enable_suspend of this WorkItemFlowProcessNodeVO.
        :rtype: bool
        """
        return self._enable_suspend

    @enable_suspend.setter
    def enable_suspend(self, enable_suspend):
        r"""Sets the enable_suspend of this WorkItemFlowProcessNodeVO.

        是否允许挂起

        :param enable_suspend: The enable_suspend of this WorkItemFlowProcessNodeVO.
        :type enable_suspend: bool
        """
        self._enable_suspend = enable_suspend

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
        if not isinstance(other, WorkItemFlowProcessNodeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
