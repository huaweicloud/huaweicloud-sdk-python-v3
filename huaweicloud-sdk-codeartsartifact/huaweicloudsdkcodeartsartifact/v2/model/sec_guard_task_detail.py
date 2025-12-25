# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecGuardTaskDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'scan_path': 'str',
        'file_name': 'str',
        'display_name': 'str',
        'path': 'str',
        'created_time': 'str',
        'opensource': 'OpensourceCount',
        'virus': 'int',
        'malware': 'MalwareCount',
        'status': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'scan_path': 'scan_path',
        'file_name': 'file_name',
        'display_name': 'display_name',
        'path': 'path',
        'created_time': 'created_time',
        'opensource': 'opensource',
        'virus': 'virus',
        'malware': 'malware',
        'status': 'status'
    }

    def __init__(self, task_id=None, task_name=None, scan_path=None, file_name=None, display_name=None, path=None, created_time=None, opensource=None, virus=None, malware=None, status=None):
        r"""SecGuardTaskDetail

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**: 任务id。 **取值范围**: 不涉及。
        :type task_id: str
        :param task_name: **参数解释**: 任务名。 **取值范围**: 不涉及。
        :type task_name: str
        :param scan_path: **参数解释**: 文件扫描路径。 **取值范围**: 不涉及。
        :type scan_path: str
        :param file_name: **参数解释**: 文件名。 **取值范围**: 不涉及。
        :type file_name: str
        :param display_name: **参数解释**: 展示名称。 **取值范围**: 不涉及。
        :type display_name: str
        :param path: **参数解释**: 路径。 **取值范围**: 不涉及。
        :type path: str
        :param created_time: **参数解释**: 创建时间。 **取值范围**: 不涉及。
        :type created_time: str
        :param opensource: 
        :type opensource: :class:`huaweicloudsdkcodeartsartifact.v2.OpensourceCount`
        :param virus: **参数解释**: 病毒文件数。 **取值范围**: 不涉及。
        :type virus: int
        :param malware: 
        :type malware: :class:`huaweicloudsdkcodeartsartifact.v2.MalwareCount`
        :param status: **参数解释**: 状态。 **取值范围**: 不涉及。
        :type status: str
        """
        
        

        self._task_id = None
        self._task_name = None
        self._scan_path = None
        self._file_name = None
        self._display_name = None
        self._path = None
        self._created_time = None
        self._opensource = None
        self._virus = None
        self._malware = None
        self._status = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if scan_path is not None:
            self.scan_path = scan_path
        if file_name is not None:
            self.file_name = file_name
        if display_name is not None:
            self.display_name = display_name
        if path is not None:
            self.path = path
        if created_time is not None:
            self.created_time = created_time
        if opensource is not None:
            self.opensource = opensource
        if virus is not None:
            self.virus = virus
        if malware is not None:
            self.malware = malware
        if status is not None:
            self.status = status

    @property
    def task_id(self):
        r"""Gets the task_id of this SecGuardTaskDetail.

        **参数解释**: 任务id。 **取值范围**: 不涉及。

        :return: The task_id of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SecGuardTaskDetail.

        **参数解释**: 任务id。 **取值范围**: 不涉及。

        :param task_id: The task_id of this SecGuardTaskDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this SecGuardTaskDetail.

        **参数解释**: 任务名。 **取值范围**: 不涉及。

        :return: The task_name of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this SecGuardTaskDetail.

        **参数解释**: 任务名。 **取值范围**: 不涉及。

        :param task_name: The task_name of this SecGuardTaskDetail.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def scan_path(self):
        r"""Gets the scan_path of this SecGuardTaskDetail.

        **参数解释**: 文件扫描路径。 **取值范围**: 不涉及。

        :return: The scan_path of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._scan_path

    @scan_path.setter
    def scan_path(self, scan_path):
        r"""Sets the scan_path of this SecGuardTaskDetail.

        **参数解释**: 文件扫描路径。 **取值范围**: 不涉及。

        :param scan_path: The scan_path of this SecGuardTaskDetail.
        :type scan_path: str
        """
        self._scan_path = scan_path

    @property
    def file_name(self):
        r"""Gets the file_name of this SecGuardTaskDetail.

        **参数解释**: 文件名。 **取值范围**: 不涉及。

        :return: The file_name of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this SecGuardTaskDetail.

        **参数解释**: 文件名。 **取值范围**: 不涉及。

        :param file_name: The file_name of this SecGuardTaskDetail.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def display_name(self):
        r"""Gets the display_name of this SecGuardTaskDetail.

        **参数解释**: 展示名称。 **取值范围**: 不涉及。

        :return: The display_name of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this SecGuardTaskDetail.

        **参数解释**: 展示名称。 **取值范围**: 不涉及。

        :param display_name: The display_name of this SecGuardTaskDetail.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def path(self):
        r"""Gets the path of this SecGuardTaskDetail.

        **参数解释**: 路径。 **取值范围**: 不涉及。

        :return: The path of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this SecGuardTaskDetail.

        **参数解释**: 路径。 **取值范围**: 不涉及。

        :param path: The path of this SecGuardTaskDetail.
        :type path: str
        """
        self._path = path

    @property
    def created_time(self):
        r"""Gets the created_time of this SecGuardTaskDetail.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。

        :return: The created_time of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this SecGuardTaskDetail.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。

        :param created_time: The created_time of this SecGuardTaskDetail.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def opensource(self):
        r"""Gets the opensource of this SecGuardTaskDetail.

        :return: The opensource of this SecGuardTaskDetail.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.OpensourceCount`
        """
        return self._opensource

    @opensource.setter
    def opensource(self, opensource):
        r"""Sets the opensource of this SecGuardTaskDetail.

        :param opensource: The opensource of this SecGuardTaskDetail.
        :type opensource: :class:`huaweicloudsdkcodeartsartifact.v2.OpensourceCount`
        """
        self._opensource = opensource

    @property
    def virus(self):
        r"""Gets the virus of this SecGuardTaskDetail.

        **参数解释**: 病毒文件数。 **取值范围**: 不涉及。

        :return: The virus of this SecGuardTaskDetail.
        :rtype: int
        """
        return self._virus

    @virus.setter
    def virus(self, virus):
        r"""Sets the virus of this SecGuardTaskDetail.

        **参数解释**: 病毒文件数。 **取值范围**: 不涉及。

        :param virus: The virus of this SecGuardTaskDetail.
        :type virus: int
        """
        self._virus = virus

    @property
    def malware(self):
        r"""Gets the malware of this SecGuardTaskDetail.

        :return: The malware of this SecGuardTaskDetail.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.MalwareCount`
        """
        return self._malware

    @malware.setter
    def malware(self, malware):
        r"""Sets the malware of this SecGuardTaskDetail.

        :param malware: The malware of this SecGuardTaskDetail.
        :type malware: :class:`huaweicloudsdkcodeartsartifact.v2.MalwareCount`
        """
        self._malware = malware

    @property
    def status(self):
        r"""Gets the status of this SecGuardTaskDetail.

        **参数解释**: 状态。 **取值范围**: 不涉及。

        :return: The status of this SecGuardTaskDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SecGuardTaskDetail.

        **参数解释**: 状态。 **取值范围**: 不涉及。

        :param status: The status of this SecGuardTaskDetail.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, SecGuardTaskDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
