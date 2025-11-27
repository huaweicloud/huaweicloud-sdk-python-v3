# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExportTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_tasks': 'list[ExportTask]',
        'page': 'Page'
    }

    attribute_map = {
        'export_tasks': 'export_tasks',
        'page': 'page'
    }

    def __init__(self, export_tasks=None, page=None):
        r"""ListExportTasksResponse

        The model defined in huaweicloud sdk

        :param export_tasks: 导出任务列表。
        :type export_tasks: list[:class:`huaweicloudsdkiotda.v5.ExportTask`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super().__init__()

        self._export_tasks = None
        self._page = None
        self.discriminator = None

        if export_tasks is not None:
            self.export_tasks = export_tasks
        if page is not None:
            self.page = page

    @property
    def export_tasks(self):
        r"""Gets the export_tasks of this ListExportTasksResponse.

        导出任务列表。

        :return: The export_tasks of this ListExportTasksResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ExportTask`]
        """
        return self._export_tasks

    @export_tasks.setter
    def export_tasks(self, export_tasks):
        r"""Sets the export_tasks of this ListExportTasksResponse.

        导出任务列表。

        :param export_tasks: The export_tasks of this ListExportTasksResponse.
        :type export_tasks: list[:class:`huaweicloudsdkiotda.v5.ExportTask`]
        """
        self._export_tasks = export_tasks

    @property
    def page(self):
        r"""Gets the page of this ListExportTasksResponse.

        :return: The page of this ListExportTasksResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListExportTasksResponse.

        :param page: The page of this ListExportTasksResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

    def to_dict(self):
        import warnings
        warnings.warn("ListExportTasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListExportTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
