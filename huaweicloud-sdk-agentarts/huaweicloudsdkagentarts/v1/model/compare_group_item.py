# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareGroupItem:

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
        'item_data': 'list[CompareItemData]',
        'dataset_id': 'str',
        'dataset_version': 'str',
        'evaluations': 'list[CompareEvaluation]',
        'task_name': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'item_data': 'item_data',
        'dataset_id': 'dataset_id',
        'dataset_version': 'dataset_version',
        'evaluations': 'evaluations',
        'task_name': 'task_name',
        'task_id': 'task_id'
    }

    def __init__(self, item_id=None, item_data=None, dataset_id=None, dataset_version=None, evaluations=None, task_name=None, task_id=None):
        r"""CompareGroupItem

        The model defined in huaweicloud sdk

        :param item_id: 测试项的唯一标识符（ObjectId格式）。
        :type item_id: str
        :param item_data: 测试数据的原始输入输出对列表，每轮对话或单次测试的明细。
        :type item_data: list[:class:`huaweicloudsdkagentarts.v1.CompareItemData`]
        :param dataset_id: 测试所用数据集的唯一标识符（UUID格式）。
        :type dataset_id: str
        :param dataset_version: 数据集的版本标识符（UUID格式）。
        :type dataset_version: str
        :param evaluations: 对该测试项执行的所有评估器结果列表。
        :type evaluations: list[:class:`huaweicloudsdkagentarts.v1.CompareEvaluation`]
        :param task_name: 测试任务的名称，如“正确性评估-正式测试xxxxx”。
        :type task_name: str
        :param task_id: 测试任务的唯一标识符（UUID 格式）。
        :type task_id: str
        """
        
        

        self._item_id = None
        self._item_data = None
        self._dataset_id = None
        self._dataset_version = None
        self._evaluations = None
        self._task_name = None
        self._task_id = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if item_data is not None:
            self.item_data = item_data
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_version is not None:
            self.dataset_version = dataset_version
        if evaluations is not None:
            self.evaluations = evaluations
        if task_name is not None:
            self.task_name = task_name
        if task_id is not None:
            self.task_id = task_id

    @property
    def item_id(self):
        r"""Gets the item_id of this CompareGroupItem.

        测试项的唯一标识符（ObjectId格式）。

        :return: The item_id of this CompareGroupItem.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this CompareGroupItem.

        测试项的唯一标识符（ObjectId格式）。

        :param item_id: The item_id of this CompareGroupItem.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def item_data(self):
        r"""Gets the item_data of this CompareGroupItem.

        测试数据的原始输入输出对列表，每轮对话或单次测试的明细。

        :return: The item_data of this CompareGroupItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CompareItemData`]
        """
        return self._item_data

    @item_data.setter
    def item_data(self, item_data):
        r"""Sets the item_data of this CompareGroupItem.

        测试数据的原始输入输出对列表，每轮对话或单次测试的明细。

        :param item_data: The item_data of this CompareGroupItem.
        :type item_data: list[:class:`huaweicloudsdkagentarts.v1.CompareItemData`]
        """
        self._item_data = item_data

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this CompareGroupItem.

        测试所用数据集的唯一标识符（UUID格式）。

        :return: The dataset_id of this CompareGroupItem.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this CompareGroupItem.

        测试所用数据集的唯一标识符（UUID格式）。

        :param dataset_id: The dataset_id of this CompareGroupItem.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def dataset_version(self):
        r"""Gets the dataset_version of this CompareGroupItem.

        数据集的版本标识符（UUID格式）。

        :return: The dataset_version of this CompareGroupItem.
        :rtype: str
        """
        return self._dataset_version

    @dataset_version.setter
    def dataset_version(self, dataset_version):
        r"""Sets the dataset_version of this CompareGroupItem.

        数据集的版本标识符（UUID格式）。

        :param dataset_version: The dataset_version of this CompareGroupItem.
        :type dataset_version: str
        """
        self._dataset_version = dataset_version

    @property
    def evaluations(self):
        r"""Gets the evaluations of this CompareGroupItem.

        对该测试项执行的所有评估器结果列表。

        :return: The evaluations of this CompareGroupItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CompareEvaluation`]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        r"""Sets the evaluations of this CompareGroupItem.

        对该测试项执行的所有评估器结果列表。

        :param evaluations: The evaluations of this CompareGroupItem.
        :type evaluations: list[:class:`huaweicloudsdkagentarts.v1.CompareEvaluation`]
        """
        self._evaluations = evaluations

    @property
    def task_name(self):
        r"""Gets the task_name of this CompareGroupItem.

        测试任务的名称，如“正确性评估-正式测试xxxxx”。

        :return: The task_name of this CompareGroupItem.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CompareGroupItem.

        测试任务的名称，如“正确性评估-正式测试xxxxx”。

        :param task_name: The task_name of this CompareGroupItem.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        r"""Gets the task_id of this CompareGroupItem.

        测试任务的唯一标识符（UUID 格式）。

        :return: The task_id of this CompareGroupItem.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CompareGroupItem.

        测试任务的唯一标识符（UUID 格式）。

        :param task_id: The task_id of this CompareGroupItem.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, CompareGroupItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
