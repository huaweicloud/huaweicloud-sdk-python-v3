# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsDeployTaskStatusCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploying': 'int',
        'running': 'int',
        'stopping': 'int',
        'stopped': 'int',
        'starting': 'int',
        'fail': 'int',
        'deleting': 'int',
        'access_fail': 'int'
    }

    attribute_map = {
        'deploying': 'deploying',
        'running': 'running',
        'stopping': 'stopping',
        'stopped': 'stopped',
        'starting': 'starting',
        'fail': 'fail',
        'deleting': 'deleting',
        'access_fail': 'access_fail'
    }

    def __init__(self, deploying=None, running=None, stopping=None, stopped=None, starting=None, fail=None, deleting=None, access_fail=None):
        r"""OpsDeployTaskStatusCount

        The model defined in huaweicloud sdk

        :param deploying: **参数解释：** 部署中任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type deploying: int
        :param running: **参数解释：** 运行中任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type running: int
        :param stopping: **参数解释：** 停止中任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type stopping: int
        :param stopped: **参数解释：** 已停止任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type stopped: int
        :param starting: **参数解释：** 启动中任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type starting: int
        :param fail: **参数解释：** 部署失败任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type fail: int
        :param deleting: **参数解释：** 删除中任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type deleting: int
        :param access_fail: **参数解释：** 接入失败任务个数，单位：个。  **取值范围：** 0-1000的整数。
        :type access_fail: int
        """
        
        

        self._deploying = None
        self._running = None
        self._stopping = None
        self._stopped = None
        self._starting = None
        self._fail = None
        self._deleting = None
        self._access_fail = None
        self.discriminator = None

        if deploying is not None:
            self.deploying = deploying
        if running is not None:
            self.running = running
        if stopping is not None:
            self.stopping = stopping
        if stopped is not None:
            self.stopped = stopped
        if starting is not None:
            self.starting = starting
        if fail is not None:
            self.fail = fail
        if deleting is not None:
            self.deleting = deleting
        if access_fail is not None:
            self.access_fail = access_fail

    @property
    def deploying(self):
        r"""Gets the deploying of this OpsDeployTaskStatusCount.

        **参数解释：** 部署中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The deploying of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._deploying

    @deploying.setter
    def deploying(self, deploying):
        r"""Sets the deploying of this OpsDeployTaskStatusCount.

        **参数解释：** 部署中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param deploying: The deploying of this OpsDeployTaskStatusCount.
        :type deploying: int
        """
        self._deploying = deploying

    @property
    def running(self):
        r"""Gets the running of this OpsDeployTaskStatusCount.

        **参数解释：** 运行中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The running of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this OpsDeployTaskStatusCount.

        **参数解释：** 运行中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param running: The running of this OpsDeployTaskStatusCount.
        :type running: int
        """
        self._running = running

    @property
    def stopping(self):
        r"""Gets the stopping of this OpsDeployTaskStatusCount.

        **参数解释：** 停止中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The stopping of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._stopping

    @stopping.setter
    def stopping(self, stopping):
        r"""Sets the stopping of this OpsDeployTaskStatusCount.

        **参数解释：** 停止中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param stopping: The stopping of this OpsDeployTaskStatusCount.
        :type stopping: int
        """
        self._stopping = stopping

    @property
    def stopped(self):
        r"""Gets the stopped of this OpsDeployTaskStatusCount.

        **参数解释：** 已停止任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The stopped of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this OpsDeployTaskStatusCount.

        **参数解释：** 已停止任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param stopped: The stopped of this OpsDeployTaskStatusCount.
        :type stopped: int
        """
        self._stopped = stopped

    @property
    def starting(self):
        r"""Gets the starting of this OpsDeployTaskStatusCount.

        **参数解释：** 启动中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The starting of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._starting

    @starting.setter
    def starting(self, starting):
        r"""Sets the starting of this OpsDeployTaskStatusCount.

        **参数解释：** 启动中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param starting: The starting of this OpsDeployTaskStatusCount.
        :type starting: int
        """
        self._starting = starting

    @property
    def fail(self):
        r"""Gets the fail of this OpsDeployTaskStatusCount.

        **参数解释：** 部署失败任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The fail of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this OpsDeployTaskStatusCount.

        **参数解释：** 部署失败任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param fail: The fail of this OpsDeployTaskStatusCount.
        :type fail: int
        """
        self._fail = fail

    @property
    def deleting(self):
        r"""Gets the deleting of this OpsDeployTaskStatusCount.

        **参数解释：** 删除中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The deleting of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._deleting

    @deleting.setter
    def deleting(self, deleting):
        r"""Sets the deleting of this OpsDeployTaskStatusCount.

        **参数解释：** 删除中任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param deleting: The deleting of this OpsDeployTaskStatusCount.
        :type deleting: int
        """
        self._deleting = deleting

    @property
    def access_fail(self):
        r"""Gets the access_fail of this OpsDeployTaskStatusCount.

        **参数解释：** 接入失败任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :return: The access_fail of this OpsDeployTaskStatusCount.
        :rtype: int
        """
        return self._access_fail

    @access_fail.setter
    def access_fail(self, access_fail):
        r"""Sets the access_fail of this OpsDeployTaskStatusCount.

        **参数解释：** 接入失败任务个数，单位：个。  **取值范围：** 0-1000的整数。

        :param access_fail: The access_fail of this OpsDeployTaskStatusCount.
        :type access_fail: int
        """
        self._access_fail = access_fail

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
        if not isinstance(other, OpsDeployTaskStatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
