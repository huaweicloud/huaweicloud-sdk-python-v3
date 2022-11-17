# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCaseOperateLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'incident_operate_log_list': 'list[IncidentOperateLogV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'incident_operate_log_list': 'incident_operate_log_list'
    }

    def __init__(self, total_count=None, incident_operate_log_list=None):
        """ListCaseOperateLogsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param incident_operate_log_list: 工单操作日志列表
        :type incident_operate_log_list: list[:class:`huaweicloudsdkosm.v2.IncidentOperateLogV2`]
        """
        
        super(ListCaseOperateLogsResponse, self).__init__()

        self._total_count = None
        self._incident_operate_log_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if incident_operate_log_list is not None:
            self.incident_operate_log_list = incident_operate_log_list

    @property
    def total_count(self):
        """Gets the total_count of this ListCaseOperateLogsResponse.

        总数

        :return: The total_count of this ListCaseOperateLogsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCaseOperateLogsResponse.

        总数

        :param total_count: The total_count of this ListCaseOperateLogsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def incident_operate_log_list(self):
        """Gets the incident_operate_log_list of this ListCaseOperateLogsResponse.

        工单操作日志列表

        :return: The incident_operate_log_list of this ListCaseOperateLogsResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.IncidentOperateLogV2`]
        """
        return self._incident_operate_log_list

    @incident_operate_log_list.setter
    def incident_operate_log_list(self, incident_operate_log_list):
        """Sets the incident_operate_log_list of this ListCaseOperateLogsResponse.

        工单操作日志列表

        :param incident_operate_log_list: The incident_operate_log_list of this ListCaseOperateLogsResponse.
        :type incident_operate_log_list: list[:class:`huaweicloudsdkosm.v2.IncidentOperateLogV2`]
        """
        self._incident_operate_log_list = incident_operate_log_list

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
        if not isinstance(other, ListCaseOperateLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
