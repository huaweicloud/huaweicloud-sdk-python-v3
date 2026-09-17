# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluationTaskResultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'session_id': 'str',
        'dataset_id': 'str',
        'dataset_version': 'str',
        'dataset_name': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'item_data': 'list[object]',
        'agent_output': 'list[str]',
        'trace_ids': 'list[str]',
        'evaluations': 'list[OpsEvaluationItemEvaluation]',
        'annotations': 'list[object]'
    }

    attribute_map = {
        'item_id': 'item_id',
        'session_id': 'session_id',
        'dataset_id': 'dataset_id',
        'dataset_version': 'dataset_version',
        'dataset_name': 'dataset_name',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'item_data': 'item_data',
        'agent_output': 'agent_output',
        'trace_ids': 'trace_ids',
        'evaluations': 'evaluations',
        'annotations': 'annotations'
    }

    def __init__(self, item_id=None, session_id=None, dataset_id=None, dataset_version=None, dataset_name=None, task_id=None, task_name=None, item_data=None, agent_output=None, trace_ids=None, evaluations=None, annotations=None):
        r"""OpsEvaluationTaskResultItem

        The model defined in huaweicloud sdk

        :param item_id: 数据条目ID。
        :type item_id: str
        :param session_id: 会话ID。
        :type session_id: str
        :param dataset_id: 数据集ID。
        :type dataset_id: str
        :param dataset_version: 数据集版本。
        :type dataset_version: str
        :param dataset_name: 数据集名称。
        :type dataset_name: str
        :param task_id: 任务ID。
        :type task_id: str
        :param task_name: 任务名称。
        :type task_name: str
        :param item_data: 数据条目原始数据。
        :type item_data: list[object]
        :param agent_output: 智能体输出列表。
        :type agent_output: list[str]
        :param trace_ids: 轨迹ID列表。
        :type trace_ids: list[str]
        :param evaluations: 各评估器的评估结果列表。
        :type evaluations: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluationItemEvaluation`]
        :param annotations: 人工标注列表。
        :type annotations: list[object]
        """
        
        

        self._item_id = None
        self._session_id = None
        self._dataset_id = None
        self._dataset_version = None
        self._dataset_name = None
        self._task_id = None
        self._task_name = None
        self._item_data = None
        self._agent_output = None
        self._trace_ids = None
        self._evaluations = None
        self._annotations = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if session_id is not None:
            self.session_id = session_id
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_version is not None:
            self.dataset_version = dataset_version
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if item_data is not None:
            self.item_data = item_data
        if agent_output is not None:
            self.agent_output = agent_output
        if trace_ids is not None:
            self.trace_ids = trace_ids
        if evaluations is not None:
            self.evaluations = evaluations
        if annotations is not None:
            self.annotations = annotations

    @property
    def item_id(self):
        r"""Gets the item_id of this OpsEvaluationTaskResultItem.

        数据条目ID。

        :return: The item_id of this OpsEvaluationTaskResultItem.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this OpsEvaluationTaskResultItem.

        数据条目ID。

        :param item_id: The item_id of this OpsEvaluationTaskResultItem.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def session_id(self):
        r"""Gets the session_id of this OpsEvaluationTaskResultItem.

        会话ID。

        :return: The session_id of this OpsEvaluationTaskResultItem.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this OpsEvaluationTaskResultItem.

        会话ID。

        :param session_id: The session_id of this OpsEvaluationTaskResultItem.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this OpsEvaluationTaskResultItem.

        数据集ID。

        :return: The dataset_id of this OpsEvaluationTaskResultItem.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this OpsEvaluationTaskResultItem.

        数据集ID。

        :param dataset_id: The dataset_id of this OpsEvaluationTaskResultItem.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def dataset_version(self):
        r"""Gets the dataset_version of this OpsEvaluationTaskResultItem.

        数据集版本。

        :return: The dataset_version of this OpsEvaluationTaskResultItem.
        :rtype: str
        """
        return self._dataset_version

    @dataset_version.setter
    def dataset_version(self, dataset_version):
        r"""Sets the dataset_version of this OpsEvaluationTaskResultItem.

        数据集版本。

        :param dataset_version: The dataset_version of this OpsEvaluationTaskResultItem.
        :type dataset_version: str
        """
        self._dataset_version = dataset_version

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this OpsEvaluationTaskResultItem.

        数据集名称。

        :return: The dataset_name of this OpsEvaluationTaskResultItem.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this OpsEvaluationTaskResultItem.

        数据集名称。

        :param dataset_name: The dataset_name of this OpsEvaluationTaskResultItem.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def task_id(self):
        r"""Gets the task_id of this OpsEvaluationTaskResultItem.

        任务ID。

        :return: The task_id of this OpsEvaluationTaskResultItem.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this OpsEvaluationTaskResultItem.

        任务ID。

        :param task_id: The task_id of this OpsEvaluationTaskResultItem.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this OpsEvaluationTaskResultItem.

        任务名称。

        :return: The task_name of this OpsEvaluationTaskResultItem.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this OpsEvaluationTaskResultItem.

        任务名称。

        :param task_name: The task_name of this OpsEvaluationTaskResultItem.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def item_data(self):
        r"""Gets the item_data of this OpsEvaluationTaskResultItem.

        数据条目原始数据。

        :return: The item_data of this OpsEvaluationTaskResultItem.
        :rtype: list[object]
        """
        return self._item_data

    @item_data.setter
    def item_data(self, item_data):
        r"""Sets the item_data of this OpsEvaluationTaskResultItem.

        数据条目原始数据。

        :param item_data: The item_data of this OpsEvaluationTaskResultItem.
        :type item_data: list[object]
        """
        self._item_data = item_data

    @property
    def agent_output(self):
        r"""Gets the agent_output of this OpsEvaluationTaskResultItem.

        智能体输出列表。

        :return: The agent_output of this OpsEvaluationTaskResultItem.
        :rtype: list[str]
        """
        return self._agent_output

    @agent_output.setter
    def agent_output(self, agent_output):
        r"""Sets the agent_output of this OpsEvaluationTaskResultItem.

        智能体输出列表。

        :param agent_output: The agent_output of this OpsEvaluationTaskResultItem.
        :type agent_output: list[str]
        """
        self._agent_output = agent_output

    @property
    def trace_ids(self):
        r"""Gets the trace_ids of this OpsEvaluationTaskResultItem.

        轨迹ID列表。

        :return: The trace_ids of this OpsEvaluationTaskResultItem.
        :rtype: list[str]
        """
        return self._trace_ids

    @trace_ids.setter
    def trace_ids(self, trace_ids):
        r"""Sets the trace_ids of this OpsEvaluationTaskResultItem.

        轨迹ID列表。

        :param trace_ids: The trace_ids of this OpsEvaluationTaskResultItem.
        :type trace_ids: list[str]
        """
        self._trace_ids = trace_ids

    @property
    def evaluations(self):
        r"""Gets the evaluations of this OpsEvaluationTaskResultItem.

        各评估器的评估结果列表。

        :return: The evaluations of this OpsEvaluationTaskResultItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluationItemEvaluation`]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        r"""Sets the evaluations of this OpsEvaluationTaskResultItem.

        各评估器的评估结果列表。

        :param evaluations: The evaluations of this OpsEvaluationTaskResultItem.
        :type evaluations: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluationItemEvaluation`]
        """
        self._evaluations = evaluations

    @property
    def annotations(self):
        r"""Gets the annotations of this OpsEvaluationTaskResultItem.

        人工标注列表。

        :return: The annotations of this OpsEvaluationTaskResultItem.
        :rtype: list[object]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this OpsEvaluationTaskResultItem.

        人工标注列表。

        :param annotations: The annotations of this OpsEvaluationTaskResultItem.
        :type annotations: list[object]
        """
        self._annotations = annotations

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
        if not isinstance(other, OpsEvaluationTaskResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
