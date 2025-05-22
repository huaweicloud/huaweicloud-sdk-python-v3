# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRunningStatusResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_job_id': 'str',
        'last_build_no': 'str',
        'last_build_status': 'str',
        'is_running': 'bool'
    }

    attribute_map = {
        'last_job_id': 'last_job_id',
        'last_build_no': 'last_build_no',
        'last_build_status': 'last_build_status',
        'is_running': 'is_running'
    }

    def __init__(self, last_job_id=None, last_build_no=None, last_build_status=None, is_running=None):
        r"""ShowRunningStatusResult

        The model defined in huaweicloud sdk

        :param last_job_id: 任务ID
        :type last_job_id: str
        :param last_build_no: 最新构建编号
        :type last_build_no: str
        :param last_build_status: 最新构建状态
        :type last_build_status: str
        :param is_running: 是否在运行中
        :type is_running: bool
        """
        
        

        self._last_job_id = None
        self._last_build_no = None
        self._last_build_status = None
        self._is_running = None
        self.discriminator = None

        if last_job_id is not None:
            self.last_job_id = last_job_id
        if last_build_no is not None:
            self.last_build_no = last_build_no
        if last_build_status is not None:
            self.last_build_status = last_build_status
        if is_running is not None:
            self.is_running = is_running

    @property
    def last_job_id(self):
        r"""Gets the last_job_id of this ShowRunningStatusResult.

        任务ID

        :return: The last_job_id of this ShowRunningStatusResult.
        :rtype: str
        """
        return self._last_job_id

    @last_job_id.setter
    def last_job_id(self, last_job_id):
        r"""Sets the last_job_id of this ShowRunningStatusResult.

        任务ID

        :param last_job_id: The last_job_id of this ShowRunningStatusResult.
        :type last_job_id: str
        """
        self._last_job_id = last_job_id

    @property
    def last_build_no(self):
        r"""Gets the last_build_no of this ShowRunningStatusResult.

        最新构建编号

        :return: The last_build_no of this ShowRunningStatusResult.
        :rtype: str
        """
        return self._last_build_no

    @last_build_no.setter
    def last_build_no(self, last_build_no):
        r"""Sets the last_build_no of this ShowRunningStatusResult.

        最新构建编号

        :param last_build_no: The last_build_no of this ShowRunningStatusResult.
        :type last_build_no: str
        """
        self._last_build_no = last_build_no

    @property
    def last_build_status(self):
        r"""Gets the last_build_status of this ShowRunningStatusResult.

        最新构建状态

        :return: The last_build_status of this ShowRunningStatusResult.
        :rtype: str
        """
        return self._last_build_status

    @last_build_status.setter
    def last_build_status(self, last_build_status):
        r"""Sets the last_build_status of this ShowRunningStatusResult.

        最新构建状态

        :param last_build_status: The last_build_status of this ShowRunningStatusResult.
        :type last_build_status: str
        """
        self._last_build_status = last_build_status

    @property
    def is_running(self):
        r"""Gets the is_running of this ShowRunningStatusResult.

        是否在运行中

        :return: The is_running of this ShowRunningStatusResult.
        :rtype: bool
        """
        return self._is_running

    @is_running.setter
    def is_running(self, is_running):
        r"""Sets the is_running of this ShowRunningStatusResult.

        是否在运行中

        :param is_running: The is_running of this ShowRunningStatusResult.
        :type is_running: bool
        """
        self._is_running = is_running

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
        if not isinstance(other, ShowRunningStatusResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
