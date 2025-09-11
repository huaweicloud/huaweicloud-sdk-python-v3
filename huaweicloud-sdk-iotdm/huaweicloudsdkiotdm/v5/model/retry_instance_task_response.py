# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryInstanceTaskResponse(SdkResponse):

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
        'type': 'str',
        'status': 'str',
        'status_detail': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'target_config': 'TargetConfig',
        'operate_window': 'OperateWindow',
        'progress': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'type': 'type',
        'status': 'status',
        'status_detail': 'status_detail',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'target_config': 'target_config',
        'operate_window': 'operate_window',
        'progress': 'progress'
    }

    def __init__(self, task_id=None, type=None, status=None, status_detail=None, create_time=None, start_time=None, end_time=None, target_config=None, operate_window=None, progress=None):
        r"""RetryInstanceTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务Id
        :type task_id: str
        :param type: **参数说明**：实例任务类型。 **取值范围**： - CREATE：创建实例任务 - MODIFY：实例规格变更任务 - DELETE：实例删除任务 - FREEZE：实例冻结任务 - UNFREEZE：实例解冻任务 - UPDATE_ACCESS_CONFIG：修改实例接入信息任务 - UPDATE_ALLOW_LISTS： 修改实例接入白名单任务 - OPEN_SNAT：启用实例SNAT配置任务 
        :type type: str
        :param status: **参数说明**：任务状态。 **取值范围**： - PENDING：等待执行 - RUNNING：执行中 - SUCCESS：执行成功 - FAILED：执行失败 
        :type status: str
        :param status_detail: **参数说明**：任务状态描述。 
        :type status_detail: str
        :param create_time: **参数说明**：实例任务的创建时间。格式为：\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;\&quot; 
        :type create_time: str
        :param start_time: **参数说明**：实例任务的开始时间。格式为：\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;\&quot; 
        :type start_time: str
        :param end_time: **参数说明**：实例任务的结束时间。格式为：\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;\&quot; 
        :type end_time: str
        :param target_config: 
        :type target_config: :class:`huaweicloudsdkiotdm.v5.TargetConfig`
        :param operate_window: 
        :type operate_window: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        :param progress: **参数说明**：任务进度\&quot; 
        :type progress: int
        """
        
        super(RetryInstanceTaskResponse, self).__init__()

        self._task_id = None
        self._type = None
        self._status = None
        self._status_detail = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._target_config = None
        self._operate_window = None
        self._progress = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if status_detail is not None:
            self.status_detail = status_detail
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if target_config is not None:
            self.target_config = target_config
        if operate_window is not None:
            self.operate_window = operate_window
        if progress is not None:
            self.progress = progress

    @property
    def task_id(self):
        r"""Gets the task_id of this RetryInstanceTaskResponse.

        任务Id

        :return: The task_id of this RetryInstanceTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this RetryInstanceTaskResponse.

        任务Id

        :param task_id: The task_id of this RetryInstanceTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def type(self):
        r"""Gets the type of this RetryInstanceTaskResponse.

        **参数说明**：实例任务类型。 **取值范围**： - CREATE：创建实例任务 - MODIFY：实例规格变更任务 - DELETE：实例删除任务 - FREEZE：实例冻结任务 - UNFREEZE：实例解冻任务 - UPDATE_ACCESS_CONFIG：修改实例接入信息任务 - UPDATE_ALLOW_LISTS： 修改实例接入白名单任务 - OPEN_SNAT：启用实例SNAT配置任务 

        :return: The type of this RetryInstanceTaskResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RetryInstanceTaskResponse.

        **参数说明**：实例任务类型。 **取值范围**： - CREATE：创建实例任务 - MODIFY：实例规格变更任务 - DELETE：实例删除任务 - FREEZE：实例冻结任务 - UNFREEZE：实例解冻任务 - UPDATE_ACCESS_CONFIG：修改实例接入信息任务 - UPDATE_ALLOW_LISTS： 修改实例接入白名单任务 - OPEN_SNAT：启用实例SNAT配置任务 

        :param type: The type of this RetryInstanceTaskResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this RetryInstanceTaskResponse.

        **参数说明**：任务状态。 **取值范围**： - PENDING：等待执行 - RUNNING：执行中 - SUCCESS：执行成功 - FAILED：执行失败 

        :return: The status of this RetryInstanceTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RetryInstanceTaskResponse.

        **参数说明**：任务状态。 **取值范围**： - PENDING：等待执行 - RUNNING：执行中 - SUCCESS：执行成功 - FAILED：执行失败 

        :param status: The status of this RetryInstanceTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_detail(self):
        r"""Gets the status_detail of this RetryInstanceTaskResponse.

        **参数说明**：任务状态描述。 

        :return: The status_detail of this RetryInstanceTaskResponse.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        r"""Sets the status_detail of this RetryInstanceTaskResponse.

        **参数说明**：任务状态描述。 

        :param status_detail: The status_detail of this RetryInstanceTaskResponse.
        :type status_detail: str
        """
        self._status_detail = status_detail

    @property
    def create_time(self):
        r"""Gets the create_time of this RetryInstanceTaskResponse.

        **参数说明**：实例任务的创建时间。格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\" 

        :return: The create_time of this RetryInstanceTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this RetryInstanceTaskResponse.

        **参数说明**：实例任务的创建时间。格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\" 

        :param create_time: The create_time of this RetryInstanceTaskResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this RetryInstanceTaskResponse.

        **参数说明**：实例任务的开始时间。格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\" 

        :return: The start_time of this RetryInstanceTaskResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RetryInstanceTaskResponse.

        **参数说明**：实例任务的开始时间。格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\" 

        :param start_time: The start_time of this RetryInstanceTaskResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RetryInstanceTaskResponse.

        **参数说明**：实例任务的结束时间。格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\" 

        :return: The end_time of this RetryInstanceTaskResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RetryInstanceTaskResponse.

        **参数说明**：实例任务的结束时间。格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\" 

        :param end_time: The end_time of this RetryInstanceTaskResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def target_config(self):
        r"""Gets the target_config of this RetryInstanceTaskResponse.

        :return: The target_config of this RetryInstanceTaskResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.TargetConfig`
        """
        return self._target_config

    @target_config.setter
    def target_config(self, target_config):
        r"""Sets the target_config of this RetryInstanceTaskResponse.

        :param target_config: The target_config of this RetryInstanceTaskResponse.
        :type target_config: :class:`huaweicloudsdkiotdm.v5.TargetConfig`
        """
        self._target_config = target_config

    @property
    def operate_window(self):
        r"""Gets the operate_window of this RetryInstanceTaskResponse.

        :return: The operate_window of this RetryInstanceTaskResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        """
        return self._operate_window

    @operate_window.setter
    def operate_window(self, operate_window):
        r"""Sets the operate_window of this RetryInstanceTaskResponse.

        :param operate_window: The operate_window of this RetryInstanceTaskResponse.
        :type operate_window: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        """
        self._operate_window = operate_window

    @property
    def progress(self):
        r"""Gets the progress of this RetryInstanceTaskResponse.

        **参数说明**：任务进度\" 

        :return: The progress of this RetryInstanceTaskResponse.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this RetryInstanceTaskResponse.

        **参数说明**：任务进度\" 

        :param progress: The progress of this RetryInstanceTaskResponse.
        :type progress: int
        """
        self._progress = progress

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
        if not isinstance(other, RetryInstanceTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
