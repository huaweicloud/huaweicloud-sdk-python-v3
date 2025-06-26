# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Execution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'policy_id': 'int',
        'status': 'str',
        'status_text': 'str',
        'total': 'int',
        'failed': 'int',
        'succeed': 'int',
        'in_progress': 'int',
        'stopped': 'int',
        'trigger': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policy_id': 'policy_id',
        'status': 'status',
        'status_text': 'status_text',
        'total': 'total',
        'failed': 'failed',
        'succeed': 'succeed',
        'in_progress': 'in_progress',
        'stopped': 'stopped',
        'trigger': 'trigger',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, policy_id=None, status=None, status_text=None, total=None, failed=None, succeed=None, in_progress=None, stopped=None, trigger=None, created_at=None, updated_at=None):
        r"""Execution

        The model defined in huaweicloud sdk

        :param id: 记录ID
        :type id: int
        :param policy_id: 策略ID
        :type policy_id: int
        :param status: 状态
        :type status: str
        :param status_text: 状态详情
        :type status_text: str
        :param total: 总数
        :type total: int
        :param failed: 失败数
        :type failed: int
        :param succeed: 成功数
        :type succeed: int
        :param in_progress: 进行中的数量
        :type in_progress: int
        :param stopped: 停止数
        :type stopped: int
        :param trigger: 触发类型
        :type trigger: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._policy_id = None
        self._status = None
        self._status_text = None
        self._total = None
        self._failed = None
        self._succeed = None
        self._in_progress = None
        self._stopped = None
        self._trigger = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.policy_id = policy_id
        self.status = status
        self.status_text = status_text
        self.total = total
        self.failed = failed
        self.succeed = succeed
        self.in_progress = in_progress
        self.stopped = stopped
        self.trigger = trigger
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this Execution.

        记录ID

        :return: The id of this Execution.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Execution.

        记录ID

        :param id: The id of this Execution.
        :type id: int
        """
        self._id = id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this Execution.

        策略ID

        :return: The policy_id of this Execution.
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this Execution.

        策略ID

        :param policy_id: The policy_id of this Execution.
        :type policy_id: int
        """
        self._policy_id = policy_id

    @property
    def status(self):
        r"""Gets the status of this Execution.

        状态

        :return: The status of this Execution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Execution.

        状态

        :param status: The status of this Execution.
        :type status: str
        """
        self._status = status

    @property
    def status_text(self):
        r"""Gets the status_text of this Execution.

        状态详情

        :return: The status_text of this Execution.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        r"""Sets the status_text of this Execution.

        状态详情

        :param status_text: The status_text of this Execution.
        :type status_text: str
        """
        self._status_text = status_text

    @property
    def total(self):
        r"""Gets the total of this Execution.

        总数

        :return: The total of this Execution.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this Execution.

        总数

        :param total: The total of this Execution.
        :type total: int
        """
        self._total = total

    @property
    def failed(self):
        r"""Gets the failed of this Execution.

        失败数

        :return: The failed of this Execution.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this Execution.

        失败数

        :param failed: The failed of this Execution.
        :type failed: int
        """
        self._failed = failed

    @property
    def succeed(self):
        r"""Gets the succeed of this Execution.

        成功数

        :return: The succeed of this Execution.
        :rtype: int
        """
        return self._succeed

    @succeed.setter
    def succeed(self, succeed):
        r"""Sets the succeed of this Execution.

        成功数

        :param succeed: The succeed of this Execution.
        :type succeed: int
        """
        self._succeed = succeed

    @property
    def in_progress(self):
        r"""Gets the in_progress of this Execution.

        进行中的数量

        :return: The in_progress of this Execution.
        :rtype: int
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        r"""Sets the in_progress of this Execution.

        进行中的数量

        :param in_progress: The in_progress of this Execution.
        :type in_progress: int
        """
        self._in_progress = in_progress

    @property
    def stopped(self):
        r"""Gets the stopped of this Execution.

        停止数

        :return: The stopped of this Execution.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this Execution.

        停止数

        :param stopped: The stopped of this Execution.
        :type stopped: int
        """
        self._stopped = stopped

    @property
    def trigger(self):
        r"""Gets the trigger of this Execution.

        触发类型

        :return: The trigger of this Execution.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this Execution.

        触发类型

        :param trigger: The trigger of this Execution.
        :type trigger: str
        """
        self._trigger = trigger

    @property
    def created_at(self):
        r"""Gets the created_at of this Execution.

        创建时间

        :return: The created_at of this Execution.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Execution.

        创建时间

        :param created_at: The created_at of this Execution.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Execution.

        更新时间

        :return: The updated_at of this Execution.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Execution.

        更新时间

        :param updated_at: The updated_at of this Execution.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Execution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
