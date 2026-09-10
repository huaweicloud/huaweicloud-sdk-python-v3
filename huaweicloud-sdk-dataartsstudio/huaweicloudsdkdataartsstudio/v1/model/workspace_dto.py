# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkspaceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bad_record_location_name': 'str',
        'description': 'str',
        'job_log_location_name': 'str',
        'name': 'str',
        'eps_id': 'str',
        'mode': 'str',
        'status': 'str'
    }

    attribute_map = {
        'bad_record_location_name': 'bad_record_location_name',
        'description': 'description',
        'job_log_location_name': 'job_log_location_name',
        'name': 'name',
        'eps_id': 'eps_id',
        'mode': 'mode',
        'status': 'status'
    }

    def __init__(self, bad_record_location_name=None, description=None, job_log_location_name=None, name=None, eps_id=None, mode=None, status=None):
        r"""WorkspaceDto

        The model defined in huaweicloud sdk

        :param bad_record_location_name: DLI脏数据OBS路径
        :type bad_record_location_name: str
        :param description: 工作空间描述
        :type description: str
        :param job_log_location_name: 作业日志OBS路径
        :type job_log_location_name: str
        :param name: 工作空间名称
        :type name: str
        :param eps_id: 企业项目ID
        :type eps_id: str
        :param mode: 工作空间模式。0：简易模式；1：企业模式
        :type mode: str
        :param status: 工作空间状态。0：正常；5：冻结
        :type status: str
        """
        
        

        self._bad_record_location_name = None
        self._description = None
        self._job_log_location_name = None
        self._name = None
        self._eps_id = None
        self._mode = None
        self._status = None
        self.discriminator = None

        if bad_record_location_name is not None:
            self.bad_record_location_name = bad_record_location_name
        if description is not None:
            self.description = description
        if job_log_location_name is not None:
            self.job_log_location_name = job_log_location_name
        self.name = name
        if eps_id is not None:
            self.eps_id = eps_id
        if mode is not None:
            self.mode = mode
        if status is not None:
            self.status = status

    @property
    def bad_record_location_name(self):
        r"""Gets the bad_record_location_name of this WorkspaceDto.

        DLI脏数据OBS路径

        :return: The bad_record_location_name of this WorkspaceDto.
        :rtype: str
        """
        return self._bad_record_location_name

    @bad_record_location_name.setter
    def bad_record_location_name(self, bad_record_location_name):
        r"""Sets the bad_record_location_name of this WorkspaceDto.

        DLI脏数据OBS路径

        :param bad_record_location_name: The bad_record_location_name of this WorkspaceDto.
        :type bad_record_location_name: str
        """
        self._bad_record_location_name = bad_record_location_name

    @property
    def description(self):
        r"""Gets the description of this WorkspaceDto.

        工作空间描述

        :return: The description of this WorkspaceDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkspaceDto.

        工作空间描述

        :param description: The description of this WorkspaceDto.
        :type description: str
        """
        self._description = description

    @property
    def job_log_location_name(self):
        r"""Gets the job_log_location_name of this WorkspaceDto.

        作业日志OBS路径

        :return: The job_log_location_name of this WorkspaceDto.
        :rtype: str
        """
        return self._job_log_location_name

    @job_log_location_name.setter
    def job_log_location_name(self, job_log_location_name):
        r"""Sets the job_log_location_name of this WorkspaceDto.

        作业日志OBS路径

        :param job_log_location_name: The job_log_location_name of this WorkspaceDto.
        :type job_log_location_name: str
        """
        self._job_log_location_name = job_log_location_name

    @property
    def name(self):
        r"""Gets the name of this WorkspaceDto.

        工作空间名称

        :return: The name of this WorkspaceDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkspaceDto.

        工作空间名称

        :param name: The name of this WorkspaceDto.
        :type name: str
        """
        self._name = name

    @property
    def eps_id(self):
        r"""Gets the eps_id of this WorkspaceDto.

        企业项目ID

        :return: The eps_id of this WorkspaceDto.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this WorkspaceDto.

        企业项目ID

        :param eps_id: The eps_id of this WorkspaceDto.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def mode(self):
        r"""Gets the mode of this WorkspaceDto.

        工作空间模式。0：简易模式；1：企业模式

        :return: The mode of this WorkspaceDto.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this WorkspaceDto.

        工作空间模式。0：简易模式；1：企业模式

        :param mode: The mode of this WorkspaceDto.
        :type mode: str
        """
        self._mode = mode

    @property
    def status(self):
        r"""Gets the status of this WorkspaceDto.

        工作空间状态。0：正常；5：冻结

        :return: The status of this WorkspaceDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkspaceDto.

        工作空间状态。0：正常；5：冻结

        :param status: The status of this WorkspaceDto.
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
        if not isinstance(other, WorkspaceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
