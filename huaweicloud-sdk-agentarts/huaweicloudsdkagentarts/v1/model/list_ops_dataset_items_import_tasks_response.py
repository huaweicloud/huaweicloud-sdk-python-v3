# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsDatasetItemsImportTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'import_tasks': 'list[OpsImportTaskOutput]'
    }

    attribute_map = {
        'import_tasks': 'import_tasks'
    }

    def __init__(self, import_tasks=None):
        r"""ListOpsDatasetItemsImportTasksResponse

        The model defined in huaweicloud sdk

        :param import_tasks: **参数解释：** 包含多个导入任务详细执行状态的集合。 **取值范围：** 符合 OpsImportTaskOutput 结构的对象数组。 
        :type import_tasks: list[:class:`huaweicloudsdkagentarts.v1.OpsImportTaskOutput`]
        """
        
        super().__init__()

        self._import_tasks = None
        self.discriminator = None

        if import_tasks is not None:
            self.import_tasks = import_tasks

    @property
    def import_tasks(self):
        r"""Gets the import_tasks of this ListOpsDatasetItemsImportTasksResponse.

        **参数解释：** 包含多个导入任务详细执行状态的集合。 **取值范围：** 符合 OpsImportTaskOutput 结构的对象数组。 

        :return: The import_tasks of this ListOpsDatasetItemsImportTasksResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsImportTaskOutput`]
        """
        return self._import_tasks

    @import_tasks.setter
    def import_tasks(self, import_tasks):
        r"""Sets the import_tasks of this ListOpsDatasetItemsImportTasksResponse.

        **参数解释：** 包含多个导入任务详细执行状态的集合。 **取值范围：** 符合 OpsImportTaskOutput 结构的对象数组。 

        :param import_tasks: The import_tasks of this ListOpsDatasetItemsImportTasksResponse.
        :type import_tasks: list[:class:`huaweicloudsdkagentarts.v1.OpsImportTaskOutput`]
        """
        self._import_tasks = import_tasks

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsDatasetItemsImportTasksResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListOpsDatasetItemsImportTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
