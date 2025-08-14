# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntiVirusTaskRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'task_id': 'str',
        'scan_type': 'str',
        'action': 'str',
        'host_ids': 'list[str]'
    }

    attribute_map = {
        'task_name': 'task_name',
        'task_id': 'task_id',
        'scan_type': 'scan_type',
        'action': 'action',
        'host_ids': 'host_ids'
    }

    def __init__(self, task_name=None, task_id=None, scan_type=None, action=None, host_ids=None):
        r"""CreateAntiVirusTaskRequestInfo

        The model defined in huaweicloud sdk

        :param task_name: 任务名称
        :type task_name: str
        :param task_id: 任务ID 创建病毒扫描任务时,task_id是null.重新扫描时，task_id不是null,是当前任务的ID
        :type task_id: str
        :param scan_type: 任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描
        :type scan_type: str
        :param action: 处置动作，包含如下:   - auto：自动处置   - manual：人工处置
        :type action: str
        :param host_ids: 策略管理主机列表
        :type host_ids: list[str]
        """
        
        

        self._task_name = None
        self._task_id = None
        self._scan_type = None
        self._action = None
        self._host_ids = None
        self.discriminator = None

        self.task_name = task_name
        if task_id is not None:
            self.task_id = task_id
        self.scan_type = scan_type
        self.action = action
        self.host_ids = host_ids

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateAntiVirusTaskRequestInfo.

        任务名称

        :return: The task_name of this CreateAntiVirusTaskRequestInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateAntiVirusTaskRequestInfo.

        任务名称

        :param task_name: The task_name of this CreateAntiVirusTaskRequestInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateAntiVirusTaskRequestInfo.

        任务ID 创建病毒扫描任务时,task_id是null.重新扫描时，task_id不是null,是当前任务的ID

        :return: The task_id of this CreateAntiVirusTaskRequestInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateAntiVirusTaskRequestInfo.

        任务ID 创建病毒扫描任务时,task_id是null.重新扫描时，task_id不是null,是当前任务的ID

        :param task_id: The task_id of this CreateAntiVirusTaskRequestInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def scan_type(self):
        r"""Gets the scan_type of this CreateAntiVirusTaskRequestInfo.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :return: The scan_type of this CreateAntiVirusTaskRequestInfo.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this CreateAntiVirusTaskRequestInfo.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :param scan_type: The scan_type of this CreateAntiVirusTaskRequestInfo.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def action(self):
        r"""Gets the action of this CreateAntiVirusTaskRequestInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :return: The action of this CreateAntiVirusTaskRequestInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAntiVirusTaskRequestInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :param action: The action of this CreateAntiVirusTaskRequestInfo.
        :type action: str
        """
        self._action = action

    @property
    def host_ids(self):
        r"""Gets the host_ids of this CreateAntiVirusTaskRequestInfo.

        策略管理主机列表

        :return: The host_ids of this CreateAntiVirusTaskRequestInfo.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this CreateAntiVirusTaskRequestInfo.

        策略管理主机列表

        :param host_ids: The host_ids of this CreateAntiVirusTaskRequestInfo.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

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
        if not isinstance(other, CreateAntiVirusTaskRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
