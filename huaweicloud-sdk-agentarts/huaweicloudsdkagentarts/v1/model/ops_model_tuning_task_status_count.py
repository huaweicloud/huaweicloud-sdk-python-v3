# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsModelTuningTaskStatusCount:

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
        'training': 'int',
        'stopping': 'int',
        'stopped': 'int',
        'success': 'int',
        'fail': 'int',
        'deleting': 'int'
    }

    attribute_map = {
        'draft': 'draft',
        'training': 'training',
        'stopping': 'stopping',
        'stopped': 'stopped',
        'success': 'success',
        'fail': 'fail',
        'deleting': 'deleting'
    }

    def __init__(self, draft=None, training=None, stopping=None, stopped=None, success=None, fail=None, deleting=None):
        r"""OpsModelTuningTaskStatusCount

        The model defined in huaweicloud sdk

        :param draft: **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。
        :type draft: int
        :param training: **参数解释：** 训练中任务个数。  **取值范围：** 0-1000的整数。
        :type training: int
        :param stopping: **参数解释：** 停止中任务个数。  **取值范围：** 0-1000的整数。
        :type stopping: int
        :param stopped: **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。
        :type stopped: int
        :param success: **参数解释：** 成功任务个数。  **取值范围：** 0-1000的整数。
        :type success: int
        :param fail: **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。
        :type fail: int
        :param deleting: **参数解释：** 删除中任务个数。  **取值范围：** 0-1000的整数。
        :type deleting: int
        """
        
        

        self._draft = None
        self._training = None
        self._stopping = None
        self._stopped = None
        self._success = None
        self._fail = None
        self._deleting = None
        self.discriminator = None

        if draft is not None:
            self.draft = draft
        if training is not None:
            self.training = training
        if stopping is not None:
            self.stopping = stopping
        if stopped is not None:
            self.stopped = stopped
        if success is not None:
            self.success = success
        if fail is not None:
            self.fail = fail
        if deleting is not None:
            self.deleting = deleting

    @property
    def draft(self):
        r"""Gets the draft of this OpsModelTuningTaskStatusCount.

        **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。

        :return: The draft of this OpsModelTuningTaskStatusCount.
        :rtype: int
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        r"""Sets the draft of this OpsModelTuningTaskStatusCount.

        **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。

        :param draft: The draft of this OpsModelTuningTaskStatusCount.
        :type draft: int
        """
        self._draft = draft

    @property
    def training(self):
        r"""Gets the training of this OpsModelTuningTaskStatusCount.

        **参数解释：** 训练中任务个数。  **取值范围：** 0-1000的整数。

        :return: The training of this OpsModelTuningTaskStatusCount.
        :rtype: int
        """
        return self._training

    @training.setter
    def training(self, training):
        r"""Sets the training of this OpsModelTuningTaskStatusCount.

        **参数解释：** 训练中任务个数。  **取值范围：** 0-1000的整数。

        :param training: The training of this OpsModelTuningTaskStatusCount.
        :type training: int
        """
        self._training = training

    @property
    def stopping(self):
        r"""Gets the stopping of this OpsModelTuningTaskStatusCount.

        **参数解释：** 停止中任务个数。  **取值范围：** 0-1000的整数。

        :return: The stopping of this OpsModelTuningTaskStatusCount.
        :rtype: int
        """
        return self._stopping

    @stopping.setter
    def stopping(self, stopping):
        r"""Sets the stopping of this OpsModelTuningTaskStatusCount.

        **参数解释：** 停止中任务个数。  **取值范围：** 0-1000的整数。

        :param stopping: The stopping of this OpsModelTuningTaskStatusCount.
        :type stopping: int
        """
        self._stopping = stopping

    @property
    def stopped(self):
        r"""Gets the stopped of this OpsModelTuningTaskStatusCount.

        **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。

        :return: The stopped of this OpsModelTuningTaskStatusCount.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this OpsModelTuningTaskStatusCount.

        **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。

        :param stopped: The stopped of this OpsModelTuningTaskStatusCount.
        :type stopped: int
        """
        self._stopped = stopped

    @property
    def success(self):
        r"""Gets the success of this OpsModelTuningTaskStatusCount.

        **参数解释：** 成功任务个数。  **取值范围：** 0-1000的整数。

        :return: The success of this OpsModelTuningTaskStatusCount.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this OpsModelTuningTaskStatusCount.

        **参数解释：** 成功任务个数。  **取值范围：** 0-1000的整数。

        :param success: The success of this OpsModelTuningTaskStatusCount.
        :type success: int
        """
        self._success = success

    @property
    def fail(self):
        r"""Gets the fail of this OpsModelTuningTaskStatusCount.

        **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。

        :return: The fail of this OpsModelTuningTaskStatusCount.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this OpsModelTuningTaskStatusCount.

        **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。

        :param fail: The fail of this OpsModelTuningTaskStatusCount.
        :type fail: int
        """
        self._fail = fail

    @property
    def deleting(self):
        r"""Gets the deleting of this OpsModelTuningTaskStatusCount.

        **参数解释：** 删除中任务个数。  **取值范围：** 0-1000的整数。

        :return: The deleting of this OpsModelTuningTaskStatusCount.
        :rtype: int
        """
        return self._deleting

    @deleting.setter
    def deleting(self, deleting):
        r"""Sets the deleting of this OpsModelTuningTaskStatusCount.

        **参数解释：** 删除中任务个数。  **取值范围：** 0-1000的整数。

        :param deleting: The deleting of this OpsModelTuningTaskStatusCount.
        :type deleting: int
        """
        self._deleting = deleting

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
        if not isinstance(other, OpsModelTuningTaskStatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
