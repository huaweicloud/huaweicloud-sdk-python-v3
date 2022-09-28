# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRunDesktopsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'failed_operation_list': 'list[VmOperateResult]',
        'job_id': 'str'
    }

    attribute_map = {
        'failed_operation_list': 'failed_operation_list',
        'job_id': 'job_id'
    }

    def __init__(self, failed_operation_list=None, job_id=None):
        """BatchRunDesktopsResponse

        The model defined in huaweicloud sdk

        :param failed_operation_list: 操作失败桌面列表。
        :type failed_operation_list: list[:class:`huaweicloudsdkworkspace.v2.VmOperateResult`]
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        super(BatchRunDesktopsResponse, self).__init__()

        self._failed_operation_list = None
        self._job_id = None
        self.discriminator = None

        if failed_operation_list is not None:
            self.failed_operation_list = failed_operation_list
        if job_id is not None:
            self.job_id = job_id

    @property
    def failed_operation_list(self):
        """Gets the failed_operation_list of this BatchRunDesktopsResponse.

        操作失败桌面列表。

        :return: The failed_operation_list of this BatchRunDesktopsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VmOperateResult`]
        """
        return self._failed_operation_list

    @failed_operation_list.setter
    def failed_operation_list(self, failed_operation_list):
        """Sets the failed_operation_list of this BatchRunDesktopsResponse.

        操作失败桌面列表。

        :param failed_operation_list: The failed_operation_list of this BatchRunDesktopsResponse.
        :type failed_operation_list: list[:class:`huaweicloudsdkworkspace.v2.VmOperateResult`]
        """
        self._failed_operation_list = failed_operation_list

    @property
    def job_id(self):
        """Gets the job_id of this BatchRunDesktopsResponse.

        任务ID。

        :return: The job_id of this BatchRunDesktopsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BatchRunDesktopsResponse.

        任务ID。

        :param job_id: The job_id of this BatchRunDesktopsResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, BatchRunDesktopsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
