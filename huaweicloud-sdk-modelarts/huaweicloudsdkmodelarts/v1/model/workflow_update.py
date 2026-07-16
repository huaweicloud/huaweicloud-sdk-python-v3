# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'data_requirements': 'list[DataRequirement]',
        'parameters': 'list[WorkflowParameter]',
        'storages': 'list[WorkflowStorage]',
        'labels': 'list[str]',
        'smn_switch': 'str',
        'steps': 'list[WorkflowStep]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'data_requirements': 'data_requirements',
        'parameters': 'parameters',
        'storages': 'storages',
        'labels': 'labels',
        'smn_switch': 'smn_switch',
        'steps': 'steps'
    }

    def __init__(self, name=None, description=None, data_requirements=None, parameters=None, storages=None, labels=None, smn_switch=None, steps=None):
        r"""WorkflowUpdate

        The model defined in huaweicloud sdk

        :param name: 工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。
        :type name: str
        :param description: 工作流描述。
        :type description: str
        :param data_requirements: Workflow包含的数据输入项定义。
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        :param parameters: 工作流参数。
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        :param storages: 工作流存储信息。
        :type storages: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStorage`]
        :param labels: 工作流标签。
        :type labels: list[str]
        :param smn_switch: SMN消息订阅开关。
        :type smn_switch: str
        :param steps: 工作流节点。
        :type steps: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStep`]
        """
        
        

        self._name = None
        self._description = None
        self._data_requirements = None
        self._parameters = None
        self._storages = None
        self._labels = None
        self._smn_switch = None
        self._steps = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if data_requirements is not None:
            self.data_requirements = data_requirements
        if parameters is not None:
            self.parameters = parameters
        if storages is not None:
            self.storages = storages
        if labels is not None:
            self.labels = labels
        if smn_switch is not None:
            self.smn_switch = smn_switch
        if steps is not None:
            self.steps = steps

    @property
    def name(self):
        r"""Gets the name of this WorkflowUpdate.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :return: The name of this WorkflowUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowUpdate.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :param name: The name of this WorkflowUpdate.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this WorkflowUpdate.

        工作流描述。

        :return: The description of this WorkflowUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkflowUpdate.

        工作流描述。

        :param description: The description of this WorkflowUpdate.
        :type description: str
        """
        self._description = description

    @property
    def data_requirements(self):
        r"""Gets the data_requirements of this WorkflowUpdate.

        Workflow包含的数据输入项定义。

        :return: The data_requirements of this WorkflowUpdate.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        return self._data_requirements

    @data_requirements.setter
    def data_requirements(self, data_requirements):
        r"""Sets the data_requirements of this WorkflowUpdate.

        Workflow包含的数据输入项定义。

        :param data_requirements: The data_requirements of this WorkflowUpdate.
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        self._data_requirements = data_requirements

    @property
    def parameters(self):
        r"""Gets the parameters of this WorkflowUpdate.

        工作流参数。

        :return: The parameters of this WorkflowUpdate.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this WorkflowUpdate.

        工作流参数。

        :param parameters: The parameters of this WorkflowUpdate.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        self._parameters = parameters

    @property
    def storages(self):
        r"""Gets the storages of this WorkflowUpdate.

        工作流存储信息。

        :return: The storages of this WorkflowUpdate.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStorage`]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        r"""Sets the storages of this WorkflowUpdate.

        工作流存储信息。

        :param storages: The storages of this WorkflowUpdate.
        :type storages: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStorage`]
        """
        self._storages = storages

    @property
    def labels(self):
        r"""Gets the labels of this WorkflowUpdate.

        工作流标签。

        :return: The labels of this WorkflowUpdate.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this WorkflowUpdate.

        工作流标签。

        :param labels: The labels of this WorkflowUpdate.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def smn_switch(self):
        r"""Gets the smn_switch of this WorkflowUpdate.

        SMN消息订阅开关。

        :return: The smn_switch of this WorkflowUpdate.
        :rtype: str
        """
        return self._smn_switch

    @smn_switch.setter
    def smn_switch(self, smn_switch):
        r"""Sets the smn_switch of this WorkflowUpdate.

        SMN消息订阅开关。

        :param smn_switch: The smn_switch of this WorkflowUpdate.
        :type smn_switch: str
        """
        self._smn_switch = smn_switch

    @property
    def steps(self):
        r"""Gets the steps of this WorkflowUpdate.

        工作流节点。

        :return: The steps of this WorkflowUpdate.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStep`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this WorkflowUpdate.

        工作流节点。

        :param steps: The steps of this WorkflowUpdate.
        :type steps: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStep`]
        """
        self._steps = steps

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
        if not isinstance(other, WorkflowUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
