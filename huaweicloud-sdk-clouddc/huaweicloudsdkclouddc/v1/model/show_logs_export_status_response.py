# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogsExportStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_id': 'str',
        'status': 'str',
        'percentage': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'export_id': 'export_id',
        'status': 'status',
        'percentage': 'percentage',
        'created_at': 'created_at'
    }

    def __init__(self, export_id=None, status=None, percentage=None, created_at=None):
        r"""ShowLogsExportStatusResponse

        The model defined in huaweicloud sdk

        :param export_id: export task id
        :type export_id: str
        :param status: 导出进度
        :type status: str
        :param percentage: 导出进度百分比，范围0-100，如\&quot;10%\&quot;
        :type percentage: str
        :param created_at: 导出开始时间，时间戳格式为ISO 8601，例如：2025-03-20T02:48:06+00:00
        :type created_at: datetime
        """
        
        super(ShowLogsExportStatusResponse, self).__init__()

        self._export_id = None
        self._status = None
        self._percentage = None
        self._created_at = None
        self.discriminator = None

        if export_id is not None:
            self.export_id = export_id
        if status is not None:
            self.status = status
        if percentage is not None:
            self.percentage = percentage
        if created_at is not None:
            self.created_at = created_at

    @property
    def export_id(self):
        r"""Gets the export_id of this ShowLogsExportStatusResponse.

        export task id

        :return: The export_id of this ShowLogsExportStatusResponse.
        :rtype: str
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        r"""Sets the export_id of this ShowLogsExportStatusResponse.

        export task id

        :param export_id: The export_id of this ShowLogsExportStatusResponse.
        :type export_id: str
        """
        self._export_id = export_id

    @property
    def status(self):
        r"""Gets the status of this ShowLogsExportStatusResponse.

        导出进度

        :return: The status of this ShowLogsExportStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowLogsExportStatusResponse.

        导出进度

        :param status: The status of this ShowLogsExportStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def percentage(self):
        r"""Gets the percentage of this ShowLogsExportStatusResponse.

        导出进度百分比，范围0-100，如\"10%\"

        :return: The percentage of this ShowLogsExportStatusResponse.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this ShowLogsExportStatusResponse.

        导出进度百分比，范围0-100，如\"10%\"

        :param percentage: The percentage of this ShowLogsExportStatusResponse.
        :type percentage: str
        """
        self._percentage = percentage

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowLogsExportStatusResponse.

        导出开始时间，时间戳格式为ISO 8601，例如：2025-03-20T02:48:06+00:00

        :return: The created_at of this ShowLogsExportStatusResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowLogsExportStatusResponse.

        导出开始时间，时间戳格式为ISO 8601，例如：2025-03-20T02:48:06+00:00

        :param created_at: The created_at of this ShowLogsExportStatusResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowLogsExportStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
