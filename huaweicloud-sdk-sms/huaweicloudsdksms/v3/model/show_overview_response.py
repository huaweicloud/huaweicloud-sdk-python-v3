# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'waiting': 'int',
        'replicate': 'int',
        'syncing': 'int',
        'stopped': 'int',
        'deleting': 'int',
        'cutovering': 'int',
        'unavailable': 'int',
        'stopping': 'int',
        'skipping': 'int',
        'finished': 'int',
        'initialize': 'int',
        'error': 'int',
        'cloning': 'int',
        'unconfigured': 'int'
    }

    attribute_map = {
        'waiting': 'waiting',
        'replicate': 'replicate',
        'syncing': 'syncing',
        'stopped': 'stopped',
        'deleting': 'deleting',
        'cutovering': 'cutovering',
        'unavailable': 'unavailable',
        'stopping': 'stopping',
        'skipping': 'skipping',
        'finished': 'finished',
        'initialize': 'initialize',
        'error': 'error',
        'cloning': 'cloning',
        'unconfigured': 'unconfigured'
    }

    def __init__(self, waiting=None, replicate=None, syncing=None, stopped=None, deleting=None, cutovering=None, unavailable=None, stopping=None, skipping=None, finished=None, initialize=None, error=None, cloning=None, unconfigured=None):
        r"""ShowOverviewResponse

        The model defined in huaweicloud sdk

        :param waiting: 等待中
        :type waiting: int
        :param replicate: 复制中
        :type replicate: int
        :param syncing: 同步中
        :type syncing: int
        :param stopped: 已暂停
        :type stopped: int
        :param deleting: 删除中
        :type deleting: int
        :param cutovering: 启动目的端中
        :type cutovering: int
        :param unavailable: 环境校验不通过
        :type unavailable: int
        :param stopping: 暂停中
        :type stopping: int
        :param skipping: 跳过中
        :type skipping: int
        :param finished: 启动目的端完成
        :type finished: int
        :param initialize: 初始化
        :type initialize: int
        :param error: 错误
        :type error: int
        :param cloning: 等待克隆完成
        :type cloning: int
        :param unconfigured: 未配置目的端
        :type unconfigured: int
        """
        
        super(ShowOverviewResponse, self).__init__()

        self._waiting = None
        self._replicate = None
        self._syncing = None
        self._stopped = None
        self._deleting = None
        self._cutovering = None
        self._unavailable = None
        self._stopping = None
        self._skipping = None
        self._finished = None
        self._initialize = None
        self._error = None
        self._cloning = None
        self._unconfigured = None
        self.discriminator = None

        if waiting is not None:
            self.waiting = waiting
        if replicate is not None:
            self.replicate = replicate
        if syncing is not None:
            self.syncing = syncing
        if stopped is not None:
            self.stopped = stopped
        if deleting is not None:
            self.deleting = deleting
        if cutovering is not None:
            self.cutovering = cutovering
        if unavailable is not None:
            self.unavailable = unavailable
        if stopping is not None:
            self.stopping = stopping
        if skipping is not None:
            self.skipping = skipping
        if finished is not None:
            self.finished = finished
        if initialize is not None:
            self.initialize = initialize
        if error is not None:
            self.error = error
        if cloning is not None:
            self.cloning = cloning
        if unconfigured is not None:
            self.unconfigured = unconfigured

    @property
    def waiting(self):
        r"""Gets the waiting of this ShowOverviewResponse.

        等待中

        :return: The waiting of this ShowOverviewResponse.
        :rtype: int
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        r"""Sets the waiting of this ShowOverviewResponse.

        等待中

        :param waiting: The waiting of this ShowOverviewResponse.
        :type waiting: int
        """
        self._waiting = waiting

    @property
    def replicate(self):
        r"""Gets the replicate of this ShowOverviewResponse.

        复制中

        :return: The replicate of this ShowOverviewResponse.
        :rtype: int
        """
        return self._replicate

    @replicate.setter
    def replicate(self, replicate):
        r"""Sets the replicate of this ShowOverviewResponse.

        复制中

        :param replicate: The replicate of this ShowOverviewResponse.
        :type replicate: int
        """
        self._replicate = replicate

    @property
    def syncing(self):
        r"""Gets the syncing of this ShowOverviewResponse.

        同步中

        :return: The syncing of this ShowOverviewResponse.
        :rtype: int
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        r"""Sets the syncing of this ShowOverviewResponse.

        同步中

        :param syncing: The syncing of this ShowOverviewResponse.
        :type syncing: int
        """
        self._syncing = syncing

    @property
    def stopped(self):
        r"""Gets the stopped of this ShowOverviewResponse.

        已暂停

        :return: The stopped of this ShowOverviewResponse.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this ShowOverviewResponse.

        已暂停

        :param stopped: The stopped of this ShowOverviewResponse.
        :type stopped: int
        """
        self._stopped = stopped

    @property
    def deleting(self):
        r"""Gets the deleting of this ShowOverviewResponse.

        删除中

        :return: The deleting of this ShowOverviewResponse.
        :rtype: int
        """
        return self._deleting

    @deleting.setter
    def deleting(self, deleting):
        r"""Sets the deleting of this ShowOverviewResponse.

        删除中

        :param deleting: The deleting of this ShowOverviewResponse.
        :type deleting: int
        """
        self._deleting = deleting

    @property
    def cutovering(self):
        r"""Gets the cutovering of this ShowOverviewResponse.

        启动目的端中

        :return: The cutovering of this ShowOverviewResponse.
        :rtype: int
        """
        return self._cutovering

    @cutovering.setter
    def cutovering(self, cutovering):
        r"""Sets the cutovering of this ShowOverviewResponse.

        启动目的端中

        :param cutovering: The cutovering of this ShowOverviewResponse.
        :type cutovering: int
        """
        self._cutovering = cutovering

    @property
    def unavailable(self):
        r"""Gets the unavailable of this ShowOverviewResponse.

        环境校验不通过

        :return: The unavailable of this ShowOverviewResponse.
        :rtype: int
        """
        return self._unavailable

    @unavailable.setter
    def unavailable(self, unavailable):
        r"""Sets the unavailable of this ShowOverviewResponse.

        环境校验不通过

        :param unavailable: The unavailable of this ShowOverviewResponse.
        :type unavailable: int
        """
        self._unavailable = unavailable

    @property
    def stopping(self):
        r"""Gets the stopping of this ShowOverviewResponse.

        暂停中

        :return: The stopping of this ShowOverviewResponse.
        :rtype: int
        """
        return self._stopping

    @stopping.setter
    def stopping(self, stopping):
        r"""Sets the stopping of this ShowOverviewResponse.

        暂停中

        :param stopping: The stopping of this ShowOverviewResponse.
        :type stopping: int
        """
        self._stopping = stopping

    @property
    def skipping(self):
        r"""Gets the skipping of this ShowOverviewResponse.

        跳过中

        :return: The skipping of this ShowOverviewResponse.
        :rtype: int
        """
        return self._skipping

    @skipping.setter
    def skipping(self, skipping):
        r"""Sets the skipping of this ShowOverviewResponse.

        跳过中

        :param skipping: The skipping of this ShowOverviewResponse.
        :type skipping: int
        """
        self._skipping = skipping

    @property
    def finished(self):
        r"""Gets the finished of this ShowOverviewResponse.

        启动目的端完成

        :return: The finished of this ShowOverviewResponse.
        :rtype: int
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        r"""Sets the finished of this ShowOverviewResponse.

        启动目的端完成

        :param finished: The finished of this ShowOverviewResponse.
        :type finished: int
        """
        self._finished = finished

    @property
    def initialize(self):
        r"""Gets the initialize of this ShowOverviewResponse.

        初始化

        :return: The initialize of this ShowOverviewResponse.
        :rtype: int
        """
        return self._initialize

    @initialize.setter
    def initialize(self, initialize):
        r"""Sets the initialize of this ShowOverviewResponse.

        初始化

        :param initialize: The initialize of this ShowOverviewResponse.
        :type initialize: int
        """
        self._initialize = initialize

    @property
    def error(self):
        r"""Gets the error of this ShowOverviewResponse.

        错误

        :return: The error of this ShowOverviewResponse.
        :rtype: int
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowOverviewResponse.

        错误

        :param error: The error of this ShowOverviewResponse.
        :type error: int
        """
        self._error = error

    @property
    def cloning(self):
        r"""Gets the cloning of this ShowOverviewResponse.

        等待克隆完成

        :return: The cloning of this ShowOverviewResponse.
        :rtype: int
        """
        return self._cloning

    @cloning.setter
    def cloning(self, cloning):
        r"""Sets the cloning of this ShowOverviewResponse.

        等待克隆完成

        :param cloning: The cloning of this ShowOverviewResponse.
        :type cloning: int
        """
        self._cloning = cloning

    @property
    def unconfigured(self):
        r"""Gets the unconfigured of this ShowOverviewResponse.

        未配置目的端

        :return: The unconfigured of this ShowOverviewResponse.
        :rtype: int
        """
        return self._unconfigured

    @unconfigured.setter
    def unconfigured(self, unconfigured):
        r"""Sets the unconfigured of this ShowOverviewResponse.

        未配置目的端

        :param unconfigured: The unconfigured of this ShowOverviewResponse.
        :type unconfigured: int
        """
        self._unconfigured = unconfigured

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
        if not isinstance(other, ShowOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
