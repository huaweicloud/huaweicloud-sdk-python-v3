# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAimSendTaskResponse(SdkResponse):

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
        'sms_channel': 'SmsChannel',
        'resolve_task': 'AIMResolveTaskRequestMode',
        'task_id': 'str',
        'task_state': 'str',
        'creation_time': 'datetime',
        'submission_count': 'int',
        'send_count': 'int',
        'resolve_count': 'int',
        'support_resolve_count': 'int',
        'failed_short_chains': 'list[CreateResolveTaskParamMode]'
    }

    attribute_map = {
        'task_name': 'task_name',
        'sms_channel': 'sms_channel',
        'resolve_task': 'resolve_task',
        'task_id': 'task_id',
        'task_state': 'task_state',
        'creation_time': 'creation_time',
        'submission_count': 'submission_count',
        'send_count': 'send_count',
        'resolve_count': 'resolve_count',
        'support_resolve_count': 'support_resolve_count',
        'failed_short_chains': 'failed_short_chains'
    }

    def __init__(self, task_name=None, sms_channel=None, resolve_task=None, task_id=None, task_state=None, creation_time=None, submission_count=None, send_count=None, resolve_count=None, support_resolve_count=None, failed_short_chains=None):
        r"""CreateAimSendTaskResponse

        The model defined in huaweicloud sdk

        :param task_name: 智能信息发送任务名称。
        :type task_name: str
        :param sms_channel: 
        :type sms_channel: :class:`huaweicloudsdkkoomessage.v1.SmsChannel`
        :param resolve_task: 
        :type resolve_task: :class:`huaweicloudsdkkoomessage.v1.AIMResolveTaskRequestMode`
        :param task_id: 任务ID。
        :type task_id: str
        :param task_state: 任务状态。  - Success：发送成功 - Failed：发送失败  &gt; 此状态仅代表任务提交状态，不代表智能信息发送结果。用户手机接收智能信息结果请以收到的回执结果为准，也可通过查询智能信息发送明细API获取或登录KooMessage控制台查看。 
        :type task_state: str
        :param creation_time: 创建时间。样例：2019-10-12T07:20:50.522Z。
        :type creation_time: datetime
        :param submission_count: 提交的手机号码总数。
        :type submission_count: int
        :param send_count: 发送数量。
        :type send_count: int
        :param resolve_count: 智能信息解析成功的手机号码总数。 
        :type resolve_count: int
        :param support_resolve_count: 支持智能信息解析的手机号码总数。  &gt;通过API发送的智能信息任务不做解析能力判断，返回-1作为标识。 
        :type support_resolve_count: int
        :param failed_short_chains: 短链生成失败列表。 
        :type failed_short_chains: list[:class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskParamMode`]
        """
        
        super(CreateAimSendTaskResponse, self).__init__()

        self._task_name = None
        self._sms_channel = None
        self._resolve_task = None
        self._task_id = None
        self._task_state = None
        self._creation_time = None
        self._submission_count = None
        self._send_count = None
        self._resolve_count = None
        self._support_resolve_count = None
        self._failed_short_chains = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if sms_channel is not None:
            self.sms_channel = sms_channel
        if resolve_task is not None:
            self.resolve_task = resolve_task
        if task_id is not None:
            self.task_id = task_id
        if task_state is not None:
            self.task_state = task_state
        if creation_time is not None:
            self.creation_time = creation_time
        if submission_count is not None:
            self.submission_count = submission_count
        if send_count is not None:
            self.send_count = send_count
        if resolve_count is not None:
            self.resolve_count = resolve_count
        if support_resolve_count is not None:
            self.support_resolve_count = support_resolve_count
        if failed_short_chains is not None:
            self.failed_short_chains = failed_short_chains

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateAimSendTaskResponse.

        智能信息发送任务名称。

        :return: The task_name of this CreateAimSendTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateAimSendTaskResponse.

        智能信息发送任务名称。

        :param task_name: The task_name of this CreateAimSendTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def sms_channel(self):
        r"""Gets the sms_channel of this CreateAimSendTaskResponse.

        :return: The sms_channel of this CreateAimSendTaskResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.SmsChannel`
        """
        return self._sms_channel

    @sms_channel.setter
    def sms_channel(self, sms_channel):
        r"""Sets the sms_channel of this CreateAimSendTaskResponse.

        :param sms_channel: The sms_channel of this CreateAimSendTaskResponse.
        :type sms_channel: :class:`huaweicloudsdkkoomessage.v1.SmsChannel`
        """
        self._sms_channel = sms_channel

    @property
    def resolve_task(self):
        r"""Gets the resolve_task of this CreateAimSendTaskResponse.

        :return: The resolve_task of this CreateAimSendTaskResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.AIMResolveTaskRequestMode`
        """
        return self._resolve_task

    @resolve_task.setter
    def resolve_task(self, resolve_task):
        r"""Sets the resolve_task of this CreateAimSendTaskResponse.

        :param resolve_task: The resolve_task of this CreateAimSendTaskResponse.
        :type resolve_task: :class:`huaweicloudsdkkoomessage.v1.AIMResolveTaskRequestMode`
        """
        self._resolve_task = resolve_task

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateAimSendTaskResponse.

        任务ID。

        :return: The task_id of this CreateAimSendTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateAimSendTaskResponse.

        任务ID。

        :param task_id: The task_id of this CreateAimSendTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_state(self):
        r"""Gets the task_state of this CreateAimSendTaskResponse.

        任务状态。  - Success：发送成功 - Failed：发送失败  > 此状态仅代表任务提交状态，不代表智能信息发送结果。用户手机接收智能信息结果请以收到的回执结果为准，也可通过查询智能信息发送明细API获取或登录KooMessage控制台查看。 

        :return: The task_state of this CreateAimSendTaskResponse.
        :rtype: str
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        r"""Sets the task_state of this CreateAimSendTaskResponse.

        任务状态。  - Success：发送成功 - Failed：发送失败  > 此状态仅代表任务提交状态，不代表智能信息发送结果。用户手机接收智能信息结果请以收到的回执结果为准，也可通过查询智能信息发送明细API获取或登录KooMessage控制台查看。 

        :param task_state: The task_state of this CreateAimSendTaskResponse.
        :type task_state: str
        """
        self._task_state = task_state

    @property
    def creation_time(self):
        r"""Gets the creation_time of this CreateAimSendTaskResponse.

        创建时间。样例：2019-10-12T07:20:50.522Z。

        :return: The creation_time of this CreateAimSendTaskResponse.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this CreateAimSendTaskResponse.

        创建时间。样例：2019-10-12T07:20:50.522Z。

        :param creation_time: The creation_time of this CreateAimSendTaskResponse.
        :type creation_time: datetime
        """
        self._creation_time = creation_time

    @property
    def submission_count(self):
        r"""Gets the submission_count of this CreateAimSendTaskResponse.

        提交的手机号码总数。

        :return: The submission_count of this CreateAimSendTaskResponse.
        :rtype: int
        """
        return self._submission_count

    @submission_count.setter
    def submission_count(self, submission_count):
        r"""Sets the submission_count of this CreateAimSendTaskResponse.

        提交的手机号码总数。

        :param submission_count: The submission_count of this CreateAimSendTaskResponse.
        :type submission_count: int
        """
        self._submission_count = submission_count

    @property
    def send_count(self):
        r"""Gets the send_count of this CreateAimSendTaskResponse.

        发送数量。

        :return: The send_count of this CreateAimSendTaskResponse.
        :rtype: int
        """
        return self._send_count

    @send_count.setter
    def send_count(self, send_count):
        r"""Sets the send_count of this CreateAimSendTaskResponse.

        发送数量。

        :param send_count: The send_count of this CreateAimSendTaskResponse.
        :type send_count: int
        """
        self._send_count = send_count

    @property
    def resolve_count(self):
        r"""Gets the resolve_count of this CreateAimSendTaskResponse.

        智能信息解析成功的手机号码总数。 

        :return: The resolve_count of this CreateAimSendTaskResponse.
        :rtype: int
        """
        return self._resolve_count

    @resolve_count.setter
    def resolve_count(self, resolve_count):
        r"""Sets the resolve_count of this CreateAimSendTaskResponse.

        智能信息解析成功的手机号码总数。 

        :param resolve_count: The resolve_count of this CreateAimSendTaskResponse.
        :type resolve_count: int
        """
        self._resolve_count = resolve_count

    @property
    def support_resolve_count(self):
        r"""Gets the support_resolve_count of this CreateAimSendTaskResponse.

        支持智能信息解析的手机号码总数。  >通过API发送的智能信息任务不做解析能力判断，返回-1作为标识。 

        :return: The support_resolve_count of this CreateAimSendTaskResponse.
        :rtype: int
        """
        return self._support_resolve_count

    @support_resolve_count.setter
    def support_resolve_count(self, support_resolve_count):
        r"""Sets the support_resolve_count of this CreateAimSendTaskResponse.

        支持智能信息解析的手机号码总数。  >通过API发送的智能信息任务不做解析能力判断，返回-1作为标识。 

        :param support_resolve_count: The support_resolve_count of this CreateAimSendTaskResponse.
        :type support_resolve_count: int
        """
        self._support_resolve_count = support_resolve_count

    @property
    def failed_short_chains(self):
        r"""Gets the failed_short_chains of this CreateAimSendTaskResponse.

        短链生成失败列表。 

        :return: The failed_short_chains of this CreateAimSendTaskResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskParamMode`]
        """
        return self._failed_short_chains

    @failed_short_chains.setter
    def failed_short_chains(self, failed_short_chains):
        r"""Sets the failed_short_chains of this CreateAimSendTaskResponse.

        短链生成失败列表。 

        :param failed_short_chains: The failed_short_chains of this CreateAimSendTaskResponse.
        :type failed_short_chains: list[:class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskParamMode`]
        """
        self._failed_short_chains = failed_short_chains

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
        if not isinstance(other, CreateAimSendTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
