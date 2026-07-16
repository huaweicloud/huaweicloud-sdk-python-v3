# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsDatasetItemsImportTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_id': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'dataset_id': 'dataset_id',
        'task_id': 'task_id'
    }

    def __init__(self, dataset_id=None, task_id=None):
        r"""ListOpsDatasetItemsImportTasksRequest

        The model defined in huaweicloud sdk

        :param dataset_id: **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 
        :type dataset_id: str
        :param task_id: **参数解释：** 导入任务的唯一标识符（ID）。通过此参数可以筛选出特定导入任务产生的评测集记录。 **约束限制：** 长度为0到100个字符。 **取值范围：** 符合UUID标准的字符串。 **默认取值：** 不涉及。
        :type task_id: str
        """
        
        

        self._dataset_id = None
        self._task_id = None
        self.discriminator = None

        self.dataset_id = dataset_id
        if task_id is not None:
            self.task_id = task_id

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this ListOpsDatasetItemsImportTasksRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :return: The dataset_id of this ListOpsDatasetItemsImportTasksRequest.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this ListOpsDatasetItemsImportTasksRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :param dataset_id: The dataset_id of this ListOpsDatasetItemsImportTasksRequest.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ListOpsDatasetItemsImportTasksRequest.

        **参数解释：** 导入任务的唯一标识符（ID）。通过此参数可以筛选出特定导入任务产生的评测集记录。 **约束限制：** 长度为0到100个字符。 **取值范围：** 符合UUID标准的字符串。 **默认取值：** 不涉及。

        :return: The task_id of this ListOpsDatasetItemsImportTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListOpsDatasetItemsImportTasksRequest.

        **参数解释：** 导入任务的唯一标识符（ID）。通过此参数可以筛选出特定导入任务产生的评测集记录。 **约束限制：** 长度为0到100个字符。 **取值范围：** 符合UUID标准的字符串。 **默认取值：** 不涉及。

        :param task_id: The task_id of this ListOpsDatasetItemsImportTasksRequest.
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
        if not isinstance(other, ListOpsDatasetItemsImportTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
