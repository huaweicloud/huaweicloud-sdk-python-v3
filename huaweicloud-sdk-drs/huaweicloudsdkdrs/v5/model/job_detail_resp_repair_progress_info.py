# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDetailRespRepairProgressInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'progress': 'str',
        'error_msg': 'str',
        'count': 'int',
        'repair_progress_details': 'JobDetailRespRepairProgressInfoRepairProgressDetails'
    }

    attribute_map = {
        'status': 'status',
        'progress': 'progress',
        'error_msg': 'error_msg',
        'count': 'count',
        'repair_progress_details': 'repair_progress_details'
    }

    def __init__(self, status=None, progress=None, error_msg=None, count=None, repair_progress_details=None):
        r"""JobDetailRespRepairProgressInfo

        The model defined in huaweicloud sdk

        :param status: 修复状态。
        :type status: str
        :param progress: 修复进度，百分比。
        :type progress: str
        :param error_msg: 错误信息。
        :type error_msg: str
        :param count: 总数。
        :type count: int
        :param repair_progress_details: 
        :type repair_progress_details: :class:`huaweicloudsdkdrs.v5.JobDetailRespRepairProgressInfoRepairProgressDetails`
        """
        
        

        self._status = None
        self._progress = None
        self._error_msg = None
        self._count = None
        self._repair_progress_details = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if error_msg is not None:
            self.error_msg = error_msg
        if count is not None:
            self.count = count
        if repair_progress_details is not None:
            self.repair_progress_details = repair_progress_details

    @property
    def status(self):
        r"""Gets the status of this JobDetailRespRepairProgressInfo.

        修复状态。

        :return: The status of this JobDetailRespRepairProgressInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobDetailRespRepairProgressInfo.

        修复状态。

        :param status: The status of this JobDetailRespRepairProgressInfo.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this JobDetailRespRepairProgressInfo.

        修复进度，百分比。

        :return: The progress of this JobDetailRespRepairProgressInfo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this JobDetailRespRepairProgressInfo.

        修复进度，百分比。

        :param progress: The progress of this JobDetailRespRepairProgressInfo.
        :type progress: str
        """
        self._progress = progress

    @property
    def error_msg(self):
        r"""Gets the error_msg of this JobDetailRespRepairProgressInfo.

        错误信息。

        :return: The error_msg of this JobDetailRespRepairProgressInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this JobDetailRespRepairProgressInfo.

        错误信息。

        :param error_msg: The error_msg of this JobDetailRespRepairProgressInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def count(self):
        r"""Gets the count of this JobDetailRespRepairProgressInfo.

        总数。

        :return: The count of this JobDetailRespRepairProgressInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this JobDetailRespRepairProgressInfo.

        总数。

        :param count: The count of this JobDetailRespRepairProgressInfo.
        :type count: int
        """
        self._count = count

    @property
    def repair_progress_details(self):
        r"""Gets the repair_progress_details of this JobDetailRespRepairProgressInfo.

        :return: The repair_progress_details of this JobDetailRespRepairProgressInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobDetailRespRepairProgressInfoRepairProgressDetails`
        """
        return self._repair_progress_details

    @repair_progress_details.setter
    def repair_progress_details(self, repair_progress_details):
        r"""Sets the repair_progress_details of this JobDetailRespRepairProgressInfo.

        :param repair_progress_details: The repair_progress_details of this JobDetailRespRepairProgressInfo.
        :type repair_progress_details: :class:`huaweicloudsdkdrs.v5.JobDetailRespRepairProgressInfoRepairProgressDetails`
        """
        self._repair_progress_details = repair_progress_details

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
        if not isinstance(other, JobDetailRespRepairProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
