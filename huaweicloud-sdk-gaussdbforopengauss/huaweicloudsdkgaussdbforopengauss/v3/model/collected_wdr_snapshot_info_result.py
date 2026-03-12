# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectedWdrSnapshotInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'wdr_type': 'str',
        'file_size': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'download_url': 'str',
        'status': 'str',
        'notes': 'str',
        'job_create_time': 'str',
        'start_snapshot_id': 'str',
        'end_snapshot_id': 'str',
        'file_name': 'str',
        'file_path': 'str',
        'obs_bucket': 'CollectedWdrSnapshotInfoResultObsBucket'
    }

    attribute_map = {
        'job_id': 'job_id',
        'wdr_type': 'wdr_type',
        'file_size': 'file_size',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'download_url': 'download_url',
        'status': 'status',
        'notes': 'notes',
        'job_create_time': 'job_create_time',
        'start_snapshot_id': 'start_snapshot_id',
        'end_snapshot_id': 'end_snapshot_id',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'obs_bucket': 'obs_bucket'
    }

    def __init__(self, job_id=None, wdr_type=None, file_size=None, start_time=None, end_time=None, download_url=None, status=None, notes=None, job_create_time=None, start_snapshot_id=None, end_snapshot_id=None, file_name=None, file_path=None, obs_bucket=None):
        r"""CollectedWdrSnapshotInfoResult

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**： 任务ID。 **取值范围**： 不涉及。
        :type job_id: str
        :param wdr_type: **参数解释**： 采集类型。 **取值范围**： - 实例级则为cluster。 - 组件级则为component。
        :type wdr_type: str
        :param file_size: **参数解释**： 文件大小单位kb。当status为SUCCESS时，该值不为空。 **取值范围**： 不涉及。
        :type file_size: int
        :param start_time: **参数解释**： 下发采集时填写的开始snapshot时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 下发采集时填写的结束snapshot时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。
        :type end_time: str
        :param download_url: **参数解释**： 报告下载链接，有效时间为30分钟。当status为SUCCESS时，该值不为空。 **取值范围**： 不涉及。
        :type download_url: str
        :param status: **参数解释**： 采集状态。 **取值范围**: - SUCCESS：采集成功。 - FAILED：采集失败。 - EXPORTING：采集中。
        :type status: str
        :param notes: **参数解释**： 备注。采集类型为组件级时，内容包括采集的组件ID。 **取值范围**： 不涉及。
        :type notes: str
        :param job_create_time: **参数解释**： WDR报告生成任务的创建时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，当前时间固定为+0时区。例如，\&quot;2025-07-08T10:57:59+0000\&quot;。 **取值范围**： 不涉及。
        :type job_create_time: str
        :param start_snapshot_id: **参数解释**： 用于生成WDR报告的第一个对比快照ID。例如：\&quot;20024\&quot;。只针对使用报告生成模式为对比快照ID（mode&#x3D;snapshot_id）的采集任务生效；如果该任务使用的是时间区间查询方式（mode&#x3D;time_range），则该字段为空。 **取值范围**： 不涉及。
        :type start_snapshot_id: str
        :param end_snapshot_id: **参数解释**： 用于生成WDR报告的第二个对比快照ID。例如：\&quot;20025\&quot;。只针对使用报告生成模式为对比快照ID（mode&#x3D;snapshot_id）的采集任务生效；如果该任务使用的是时间区间查询方式（mode&#x3D;time_range）来生成的，则该字段为空。 **取值范围**： 不涉及。
        :type end_snapshot_id: str
        :param file_name: **参数解释**： WDR报告临时文件名称。 **取值范围**： 不涉及。
        :type file_name: str
        :param file_path: **参数解释**： WDR报告临时文件保存路径。 **取值范围**： 不涉及。
        :type file_path: str
        :param obs_bucket: 
        :type obs_bucket: :class:`huaweicloudsdkgaussdbforopengauss.v3.CollectedWdrSnapshotInfoResultObsBucket`
        """
        
        

        self._job_id = None
        self._wdr_type = None
        self._file_size = None
        self._start_time = None
        self._end_time = None
        self._download_url = None
        self._status = None
        self._notes = None
        self._job_create_time = None
        self._start_snapshot_id = None
        self._end_snapshot_id = None
        self._file_name = None
        self._file_path = None
        self._obs_bucket = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if wdr_type is not None:
            self.wdr_type = wdr_type
        if file_size is not None:
            self.file_size = file_size
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if download_url is not None:
            self.download_url = download_url
        if status is not None:
            self.status = status
        if notes is not None:
            self.notes = notes
        if job_create_time is not None:
            self.job_create_time = job_create_time
        if start_snapshot_id is not None:
            self.start_snapshot_id = start_snapshot_id
        if end_snapshot_id is not None:
            self.end_snapshot_id = end_snapshot_id
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket

    @property
    def job_id(self):
        r"""Gets the job_id of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :return: The job_id of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :param job_id: The job_id of this CollectedWdrSnapshotInfoResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def wdr_type(self):
        r"""Gets the wdr_type of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 采集类型。 **取值范围**： - 实例级则为cluster。 - 组件级则为component。

        :return: The wdr_type of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._wdr_type

    @wdr_type.setter
    def wdr_type(self, wdr_type):
        r"""Sets the wdr_type of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 采集类型。 **取值范围**： - 实例级则为cluster。 - 组件级则为component。

        :param wdr_type: The wdr_type of this CollectedWdrSnapshotInfoResult.
        :type wdr_type: str
        """
        self._wdr_type = wdr_type

    @property
    def file_size(self):
        r"""Gets the file_size of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 文件大小单位kb。当status为SUCCESS时，该值不为空。 **取值范围**： 不涉及。

        :return: The file_size of this CollectedWdrSnapshotInfoResult.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 文件大小单位kb。当status为SUCCESS时，该值不为空。 **取值范围**： 不涉及。

        :param file_size: The file_size of this CollectedWdrSnapshotInfoResult.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def start_time(self):
        r"""Gets the start_time of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 下发采集时填写的开始snapshot时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。

        :return: The start_time of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 下发采集时填写的开始snapshot时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。

        :param start_time: The start_time of this CollectedWdrSnapshotInfoResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 下发采集时填写的结束snapshot时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。

        :return: The end_time of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 下发采集时填写的结束snapshot时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。

        :param end_time: The end_time of this CollectedWdrSnapshotInfoResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def download_url(self):
        r"""Gets the download_url of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 报告下载链接，有效时间为30分钟。当status为SUCCESS时，该值不为空。 **取值范围**： 不涉及。

        :return: The download_url of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 报告下载链接，有效时间为30分钟。当status为SUCCESS时，该值不为空。 **取值范围**： 不涉及。

        :param download_url: The download_url of this CollectedWdrSnapshotInfoResult.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def status(self):
        r"""Gets the status of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 采集状态。 **取值范围**: - SUCCESS：采集成功。 - FAILED：采集失败。 - EXPORTING：采集中。

        :return: The status of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 采集状态。 **取值范围**: - SUCCESS：采集成功。 - FAILED：采集失败。 - EXPORTING：采集中。

        :param status: The status of this CollectedWdrSnapshotInfoResult.
        :type status: str
        """
        self._status = status

    @property
    def notes(self):
        r"""Gets the notes of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 备注。采集类型为组件级时，内容包括采集的组件ID。 **取值范围**： 不涉及。

        :return: The notes of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 备注。采集类型为组件级时，内容包括采集的组件ID。 **取值范围**： 不涉及。

        :param notes: The notes of this CollectedWdrSnapshotInfoResult.
        :type notes: str
        """
        self._notes = notes

    @property
    def job_create_time(self):
        r"""Gets the job_create_time of this CollectedWdrSnapshotInfoResult.

        **参数解释**： WDR报告生成任务的创建时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，当前时间固定为+0时区。例如，\"2025-07-08T10:57:59+0000\"。 **取值范围**： 不涉及。

        :return: The job_create_time of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._job_create_time

    @job_create_time.setter
    def job_create_time(self, job_create_time):
        r"""Sets the job_create_time of this CollectedWdrSnapshotInfoResult.

        **参数解释**： WDR报告生成任务的创建时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，当前时间固定为+0时区。例如，\"2025-07-08T10:57:59+0000\"。 **取值范围**： 不涉及。

        :param job_create_time: The job_create_time of this CollectedWdrSnapshotInfoResult.
        :type job_create_time: str
        """
        self._job_create_time = job_create_time

    @property
    def start_snapshot_id(self):
        r"""Gets the start_snapshot_id of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 用于生成WDR报告的第一个对比快照ID。例如：\"20024\"。只针对使用报告生成模式为对比快照ID（mode=snapshot_id）的采集任务生效；如果该任务使用的是时间区间查询方式（mode=time_range），则该字段为空。 **取值范围**： 不涉及。

        :return: The start_snapshot_id of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._start_snapshot_id

    @start_snapshot_id.setter
    def start_snapshot_id(self, start_snapshot_id):
        r"""Sets the start_snapshot_id of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 用于生成WDR报告的第一个对比快照ID。例如：\"20024\"。只针对使用报告生成模式为对比快照ID（mode=snapshot_id）的采集任务生效；如果该任务使用的是时间区间查询方式（mode=time_range），则该字段为空。 **取值范围**： 不涉及。

        :param start_snapshot_id: The start_snapshot_id of this CollectedWdrSnapshotInfoResult.
        :type start_snapshot_id: str
        """
        self._start_snapshot_id = start_snapshot_id

    @property
    def end_snapshot_id(self):
        r"""Gets the end_snapshot_id of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 用于生成WDR报告的第二个对比快照ID。例如：\"20025\"。只针对使用报告生成模式为对比快照ID（mode=snapshot_id）的采集任务生效；如果该任务使用的是时间区间查询方式（mode=time_range）来生成的，则该字段为空。 **取值范围**： 不涉及。

        :return: The end_snapshot_id of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._end_snapshot_id

    @end_snapshot_id.setter
    def end_snapshot_id(self, end_snapshot_id):
        r"""Sets the end_snapshot_id of this CollectedWdrSnapshotInfoResult.

        **参数解释**： 用于生成WDR报告的第二个对比快照ID。例如：\"20025\"。只针对使用报告生成模式为对比快照ID（mode=snapshot_id）的采集任务生效；如果该任务使用的是时间区间查询方式（mode=time_range）来生成的，则该字段为空。 **取值范围**： 不涉及。

        :param end_snapshot_id: The end_snapshot_id of this CollectedWdrSnapshotInfoResult.
        :type end_snapshot_id: str
        """
        self._end_snapshot_id = end_snapshot_id

    @property
    def file_name(self):
        r"""Gets the file_name of this CollectedWdrSnapshotInfoResult.

        **参数解释**： WDR报告临时文件名称。 **取值范围**： 不涉及。

        :return: The file_name of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CollectedWdrSnapshotInfoResult.

        **参数解释**： WDR报告临时文件名称。 **取值范围**： 不涉及。

        :param file_name: The file_name of this CollectedWdrSnapshotInfoResult.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this CollectedWdrSnapshotInfoResult.

        **参数解释**： WDR报告临时文件保存路径。 **取值范围**： 不涉及。

        :return: The file_path of this CollectedWdrSnapshotInfoResult.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this CollectedWdrSnapshotInfoResult.

        **参数解释**： WDR报告临时文件保存路径。 **取值范围**： 不涉及。

        :param file_path: The file_path of this CollectedWdrSnapshotInfoResult.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this CollectedWdrSnapshotInfoResult.

        :return: The obs_bucket of this CollectedWdrSnapshotInfoResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CollectedWdrSnapshotInfoResultObsBucket`
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this CollectedWdrSnapshotInfoResult.

        :param obs_bucket: The obs_bucket of this CollectedWdrSnapshotInfoResult.
        :type obs_bucket: :class:`huaweicloudsdkgaussdbforopengauss.v3.CollectedWdrSnapshotInfoResultObsBucket`
        """
        self._obs_bucket = obs_bucket

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
        if not isinstance(other, CollectedWdrSnapshotInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
