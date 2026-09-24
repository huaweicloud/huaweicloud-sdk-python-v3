# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluationTaskSummary:

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
        'name': 'str',
        'description': 'str',
        'eval_mode': 'str',
        'status': 'str',
        'dataset_id': 'str',
        'dataset_name': 'str',
        'input_source_type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'tags': 'list[OpsTmsTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'eval_mode': 'eval_mode',
        'status': 'status',
        'dataset_id': 'dataset_id',
        'dataset_name': 'dataset_name',
        'input_source_type': 'input_source_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, eval_mode=None, status=None, dataset_id=None, dataset_name=None, input_source_type=None, created_at=None, updated_at=None, tags=None):
        r"""OpsEvaluationTaskSummary

        The model defined in huaweicloud sdk

        :param id: 评估任务的唯一标识符。
        :type id: str
        :param name: 评估任务名称。
        :type name: str
        :param description: 评估任务描述。
        :type description: str
        :param eval_mode: 评估模式（OFFLINE/ONLINE）。
        :type eval_mode: str
        :param status: 任务状态（PENDING/RUNNING/COMPLETED/STOPPED等）。
        :type status: str
        :param dataset_id: 关联的评测集ID。
        :type dataset_id: str
        :param dataset_name: 关联的评测集名称。
        :type dataset_name: str
        :param input_source_type: 输入源类型（DATASET_STATIC/DATASET_DYNAMIC/TRACE_STREAM）。
        :type input_source_type: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        :param tags: **参数解释：** 评估任务绑定的TMS标签列表。 **取值范围：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._eval_mode = None
        self._status = None
        self._dataset_id = None
        self._dataset_name = None
        self._input_source_type = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if eval_mode is not None:
            self.eval_mode = eval_mode
        if status is not None:
            self.status = status
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if input_source_type is not None:
            self.input_source_type = input_source_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this OpsEvaluationTaskSummary.

        评估任务的唯一标识符。

        :return: The id of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsEvaluationTaskSummary.

        评估任务的唯一标识符。

        :param id: The id of this OpsEvaluationTaskSummary.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OpsEvaluationTaskSummary.

        评估任务名称。

        :return: The name of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsEvaluationTaskSummary.

        评估任务名称。

        :param name: The name of this OpsEvaluationTaskSummary.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this OpsEvaluationTaskSummary.

        评估任务描述。

        :return: The description of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsEvaluationTaskSummary.

        评估任务描述。

        :param description: The description of this OpsEvaluationTaskSummary.
        :type description: str
        """
        self._description = description

    @property
    def eval_mode(self):
        r"""Gets the eval_mode of this OpsEvaluationTaskSummary.

        评估模式（OFFLINE/ONLINE）。

        :return: The eval_mode of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._eval_mode

    @eval_mode.setter
    def eval_mode(self, eval_mode):
        r"""Sets the eval_mode of this OpsEvaluationTaskSummary.

        评估模式（OFFLINE/ONLINE）。

        :param eval_mode: The eval_mode of this OpsEvaluationTaskSummary.
        :type eval_mode: str
        """
        self._eval_mode = eval_mode

    @property
    def status(self):
        r"""Gets the status of this OpsEvaluationTaskSummary.

        任务状态（PENDING/RUNNING/COMPLETED/STOPPED等）。

        :return: The status of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OpsEvaluationTaskSummary.

        任务状态（PENDING/RUNNING/COMPLETED/STOPPED等）。

        :param status: The status of this OpsEvaluationTaskSummary.
        :type status: str
        """
        self._status = status

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this OpsEvaluationTaskSummary.

        关联的评测集ID。

        :return: The dataset_id of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this OpsEvaluationTaskSummary.

        关联的评测集ID。

        :param dataset_id: The dataset_id of this OpsEvaluationTaskSummary.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this OpsEvaluationTaskSummary.

        关联的评测集名称。

        :return: The dataset_name of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this OpsEvaluationTaskSummary.

        关联的评测集名称。

        :param dataset_name: The dataset_name of this OpsEvaluationTaskSummary.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def input_source_type(self):
        r"""Gets the input_source_type of this OpsEvaluationTaskSummary.

        输入源类型（DATASET_STATIC/DATASET_DYNAMIC/TRACE_STREAM）。

        :return: The input_source_type of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._input_source_type

    @input_source_type.setter
    def input_source_type(self, input_source_type):
        r"""Sets the input_source_type of this OpsEvaluationTaskSummary.

        输入源类型（DATASET_STATIC/DATASET_DYNAMIC/TRACE_STREAM）。

        :param input_source_type: The input_source_type of this OpsEvaluationTaskSummary.
        :type input_source_type: str
        """
        self._input_source_type = input_source_type

    @property
    def created_at(self):
        r"""Gets the created_at of this OpsEvaluationTaskSummary.

        创建时间。

        :return: The created_at of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OpsEvaluationTaskSummary.

        创建时间。

        :param created_at: The created_at of this OpsEvaluationTaskSummary.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this OpsEvaluationTaskSummary.

        更新时间。

        :return: The updated_at of this OpsEvaluationTaskSummary.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this OpsEvaluationTaskSummary.

        更新时间。

        :param updated_at: The updated_at of this OpsEvaluationTaskSummary.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this OpsEvaluationTaskSummary.

        **参数解释：** 评估任务绑定的TMS标签列表。 **取值范围：** 不涉及。 

        :return: The tags of this OpsEvaluationTaskSummary.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpsEvaluationTaskSummary.

        **参数解释：** 评估任务绑定的TMS标签列表。 **取值范围：** 不涉及。 

        :param tags: The tags of this OpsEvaluationTaskSummary.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        self._tags = tags

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
        if not isinstance(other, OpsEvaluationTaskSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
