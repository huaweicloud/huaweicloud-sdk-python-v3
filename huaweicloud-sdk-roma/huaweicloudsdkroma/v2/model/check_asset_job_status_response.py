# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckAssetJobStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'status': 'str',
        'reasons': 'list[AssetJobReason]',
        'progress_percent': 'float',
        'archive_id': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'reasons': 'reasons',
        'progress_percent': 'progress_percent',
        'archive_id': 'archive_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, type=None, status=None, reasons=None, progress_percent=None, archive_id=None, begin_time=None, end_time=None):
        """CheckAssetJobStatusResponse

        The model defined in huaweicloud sdk

        :param id: 作业ID
        :type id: str
        :param type: 作业类型
        :type type: str
        :param status: 作业状态 - RUNNING : 作业正在执行 - SUCCEEDED : 作业执行成功，对于导出作业，用户可以通过archive_id来下载资产包 - FAILED : 作业执行失败，通过reason字段查看具体错误原因
        :type status: str
        :param reasons: 导致作业失败的错误原因
        :type reasons: list[:class:`huaweicloudsdkroma.v2.AssetJobReason`]
        :param progress_percent: 作业进度百分比
        :type progress_percent: float
        :param archive_id: 导出作业成功时，供下载的资产包ID
        :type archive_id: str
        :param begin_time: 作业开始时间
        :type begin_time: str
        :param end_time: 作业结束时间
        :type end_time: str
        """
        
        super(CheckAssetJobStatusResponse, self).__init__()

        self._id = None
        self._type = None
        self._status = None
        self._reasons = None
        self._progress_percent = None
        self._archive_id = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if reasons is not None:
            self.reasons = reasons
        if progress_percent is not None:
            self.progress_percent = progress_percent
        if archive_id is not None:
            self.archive_id = archive_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this CheckAssetJobStatusResponse.

        作业ID

        :return: The id of this CheckAssetJobStatusResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckAssetJobStatusResponse.

        作业ID

        :param id: The id of this CheckAssetJobStatusResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this CheckAssetJobStatusResponse.

        作业类型

        :return: The type of this CheckAssetJobStatusResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckAssetJobStatusResponse.

        作业类型

        :param type: The type of this CheckAssetJobStatusResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this CheckAssetJobStatusResponse.

        作业状态 - RUNNING : 作业正在执行 - SUCCEEDED : 作业执行成功，对于导出作业，用户可以通过archive_id来下载资产包 - FAILED : 作业执行失败，通过reason字段查看具体错误原因

        :return: The status of this CheckAssetJobStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckAssetJobStatusResponse.

        作业状态 - RUNNING : 作业正在执行 - SUCCEEDED : 作业执行成功，对于导出作业，用户可以通过archive_id来下载资产包 - FAILED : 作业执行失败，通过reason字段查看具体错误原因

        :param status: The status of this CheckAssetJobStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def reasons(self):
        """Gets the reasons of this CheckAssetJobStatusResponse.

        导致作业失败的错误原因

        :return: The reasons of this CheckAssetJobStatusResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.AssetJobReason`]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this CheckAssetJobStatusResponse.

        导致作业失败的错误原因

        :param reasons: The reasons of this CheckAssetJobStatusResponse.
        :type reasons: list[:class:`huaweicloudsdkroma.v2.AssetJobReason`]
        """
        self._reasons = reasons

    @property
    def progress_percent(self):
        """Gets the progress_percent of this CheckAssetJobStatusResponse.

        作业进度百分比

        :return: The progress_percent of this CheckAssetJobStatusResponse.
        :rtype: float
        """
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, progress_percent):
        """Sets the progress_percent of this CheckAssetJobStatusResponse.

        作业进度百分比

        :param progress_percent: The progress_percent of this CheckAssetJobStatusResponse.
        :type progress_percent: float
        """
        self._progress_percent = progress_percent

    @property
    def archive_id(self):
        """Gets the archive_id of this CheckAssetJobStatusResponse.

        导出作业成功时，供下载的资产包ID

        :return: The archive_id of this CheckAssetJobStatusResponse.
        :rtype: str
        """
        return self._archive_id

    @archive_id.setter
    def archive_id(self, archive_id):
        """Sets the archive_id of this CheckAssetJobStatusResponse.

        导出作业成功时，供下载的资产包ID

        :param archive_id: The archive_id of this CheckAssetJobStatusResponse.
        :type archive_id: str
        """
        self._archive_id = archive_id

    @property
    def begin_time(self):
        """Gets the begin_time of this CheckAssetJobStatusResponse.

        作业开始时间

        :return: The begin_time of this CheckAssetJobStatusResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this CheckAssetJobStatusResponse.

        作业开始时间

        :param begin_time: The begin_time of this CheckAssetJobStatusResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this CheckAssetJobStatusResponse.

        作业结束时间

        :return: The end_time of this CheckAssetJobStatusResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CheckAssetJobStatusResponse.

        作业结束时间

        :param end_time: The end_time of this CheckAssetJobStatusResponse.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, CheckAssetJobStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
