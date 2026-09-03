# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteExportTaskNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_task_id': 'int'
    }

    attribute_map = {
        'export_task_id': 'export_task_id'
    }

    def __init__(self, export_task_id=None):
        r"""DeleteExportTaskNewRequestBody

        The model defined in huaweicloud sdk

        :param export_task_id: binlog导出任务ID
        :type export_task_id: int
        """
        
        

        self._export_task_id = None
        self.discriminator = None

        self.export_task_id = export_task_id

    @property
    def export_task_id(self):
        r"""Gets the export_task_id of this DeleteExportTaskNewRequestBody.

        binlog导出任务ID

        :return: The export_task_id of this DeleteExportTaskNewRequestBody.
        :rtype: int
        """
        return self._export_task_id

    @export_task_id.setter
    def export_task_id(self, export_task_id):
        r"""Sets the export_task_id of this DeleteExportTaskNewRequestBody.

        binlog导出任务ID

        :param export_task_id: The export_task_id of this DeleteExportTaskNewRequestBody.
        :type export_task_id: int
        """
        self._export_task_id = export_task_id

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
        if not isinstance(other, DeleteExportTaskNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
