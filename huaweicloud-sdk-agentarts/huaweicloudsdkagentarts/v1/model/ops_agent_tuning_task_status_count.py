# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsAgentTuningTaskStatusCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'draft': 'int',
        'running': 'int',
        'stopped': 'int',
        'success': 'int',
        'fail': 'int'
    }

    attribute_map = {
        'draft': 'draft',
        'running': 'running',
        'stopped': 'stopped',
        'success': 'success',
        'fail': 'fail'
    }

    def __init__(self, draft=None, running=None, stopped=None, success=None, fail=None):
        r"""OpsAgentTuningTaskStatusCount

        The model defined in huaweicloud sdk

        :param draft: **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。
        :type draft: int
        :param running: **参数解释：** 运行中任务个数。  **取值范围：** 0-1000的整数。
        :type running: int
        :param stopped: **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。
        :type stopped: int
        :param success: **参数解释：** 成功任务个数。  **取值范围：** 0-1000的整数。
        :type success: int
        :param fail: **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。
        :type fail: int
        """
        
        

        self._draft = None
        self._running = None
        self._stopped = None
        self._success = None
        self._fail = None
        self.discriminator = None

        if draft is not None:
            self.draft = draft
        if running is not None:
            self.running = running
        if stopped is not None:
            self.stopped = stopped
        if success is not None:
            self.success = success
        if fail is not None:
            self.fail = fail

    @property
    def draft(self):
        r"""Gets the draft of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。

        :return: The draft of this OpsAgentTuningTaskStatusCount.
        :rtype: int
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        r"""Sets the draft of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。

        :param draft: The draft of this OpsAgentTuningTaskStatusCount.
        :type draft: int
        """
        self._draft = draft

    @property
    def running(self):
        r"""Gets the running of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 运行中任务个数。  **取值范围：** 0-1000的整数。

        :return: The running of this OpsAgentTuningTaskStatusCount.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 运行中任务个数。  **取值范围：** 0-1000的整数。

        :param running: The running of this OpsAgentTuningTaskStatusCount.
        :type running: int
        """
        self._running = running

    @property
    def stopped(self):
        r"""Gets the stopped of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。

        :return: The stopped of this OpsAgentTuningTaskStatusCount.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。

        :param stopped: The stopped of this OpsAgentTuningTaskStatusCount.
        :type stopped: int
        """
        self._stopped = stopped

    @property
    def success(self):
        r"""Gets the success of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 成功任务个数。  **取值范围：** 0-1000的整数。

        :return: The success of this OpsAgentTuningTaskStatusCount.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 成功任务个数。  **取值范围：** 0-1000的整数。

        :param success: The success of this OpsAgentTuningTaskStatusCount.
        :type success: int
        """
        self._success = success

    @property
    def fail(self):
        r"""Gets the fail of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。

        :return: The fail of this OpsAgentTuningTaskStatusCount.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this OpsAgentTuningTaskStatusCount.

        **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。

        :param fail: The fail of this OpsAgentTuningTaskStatusCount.
        :type fail: int
        """
        self._fail = fail

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
        if not isinstance(other, OpsAgentTuningTaskStatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
