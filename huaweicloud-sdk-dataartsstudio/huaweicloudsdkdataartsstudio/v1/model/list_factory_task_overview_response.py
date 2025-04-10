# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryTaskOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fail_count': 'int',
        'force_success_count': 'int',
        'freeze_count': 'int',
        'ignore_success_count': 'int',
        'manual_stop_count': 'int',
        'pause_count': 'int',
        'running_count': 'int',
        'running_exception_count': 'int',
        'skip_count': 'int',
        'success_count': 'int',
        'total_count': 'int',
        'waiting_confirm_count': 'int',
        'waiting_count': 'int'
    }

    attribute_map = {
        'fail_count': 'fail_count',
        'force_success_count': 'force_success_count',
        'freeze_count': 'freeze_count',
        'ignore_success_count': 'ignore_success_count',
        'manual_stop_count': 'manual_stop_count',
        'pause_count': 'pause_count',
        'running_count': 'running_count',
        'running_exception_count': 'running_exception_count',
        'skip_count': 'skip_count',
        'success_count': 'success_count',
        'total_count': 'total_count',
        'waiting_confirm_count': 'waiting_confirm_count',
        'waiting_count': 'waiting_count'
    }

    def __init__(self, fail_count=None, force_success_count=None, freeze_count=None, ignore_success_count=None, manual_stop_count=None, pause_count=None, running_count=None, running_exception_count=None, skip_count=None, success_count=None, total_count=None, waiting_confirm_count=None, waiting_count=None):
        r"""ListFactoryTaskOverviewResponse

        The model defined in huaweicloud sdk

        :param fail_count: 失败的实例数量
        :type fail_count: int
        :param force_success_count: 强制成功的实例数量
        :type force_success_count: int
        :param freeze_count: 冻结的实例数量
        :type freeze_count: int
        :param ignore_success_count: 忽略失败的实例数量
        :type ignore_success_count: int
        :param manual_stop_count: 取消的实例数量
        :type manual_stop_count: int
        :param pause_count: 暂时的实例数量
        :type pause_count: int
        :param running_count: 运行中的实例数量
        :type running_count: int
        :param running_exception_count: 异常的实例数量
        :type running_exception_count: int
        :param skip_count: 跳过的实例数量
        :type skip_count: int
        :param success_count: 运行成功的实例数量
        :type success_count: int
        :param total_count: 实例总数
        :type total_count: int
        :param waiting_confirm_count: 待确认执行的实例数量
        :type waiting_confirm_count: int
        :param waiting_count: 等待运行的实例数量
        :type waiting_count: int
        """
        
        super(ListFactoryTaskOverviewResponse, self).__init__()

        self._fail_count = None
        self._force_success_count = None
        self._freeze_count = None
        self._ignore_success_count = None
        self._manual_stop_count = None
        self._pause_count = None
        self._running_count = None
        self._running_exception_count = None
        self._skip_count = None
        self._success_count = None
        self._total_count = None
        self._waiting_confirm_count = None
        self._waiting_count = None
        self.discriminator = None

        if fail_count is not None:
            self.fail_count = fail_count
        if force_success_count is not None:
            self.force_success_count = force_success_count
        if freeze_count is not None:
            self.freeze_count = freeze_count
        if ignore_success_count is not None:
            self.ignore_success_count = ignore_success_count
        if manual_stop_count is not None:
            self.manual_stop_count = manual_stop_count
        if pause_count is not None:
            self.pause_count = pause_count
        if running_count is not None:
            self.running_count = running_count
        if running_exception_count is not None:
            self.running_exception_count = running_exception_count
        if skip_count is not None:
            self.skip_count = skip_count
        if success_count is not None:
            self.success_count = success_count
        if total_count is not None:
            self.total_count = total_count
        if waiting_confirm_count is not None:
            self.waiting_confirm_count = waiting_confirm_count
        if waiting_count is not None:
            self.waiting_count = waiting_count

    @property
    def fail_count(self):
        r"""Gets the fail_count of this ListFactoryTaskOverviewResponse.

        失败的实例数量

        :return: The fail_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        r"""Sets the fail_count of this ListFactoryTaskOverviewResponse.

        失败的实例数量

        :param fail_count: The fail_count of this ListFactoryTaskOverviewResponse.
        :type fail_count: int
        """
        self._fail_count = fail_count

    @property
    def force_success_count(self):
        r"""Gets the force_success_count of this ListFactoryTaskOverviewResponse.

        强制成功的实例数量

        :return: The force_success_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._force_success_count

    @force_success_count.setter
    def force_success_count(self, force_success_count):
        r"""Sets the force_success_count of this ListFactoryTaskOverviewResponse.

        强制成功的实例数量

        :param force_success_count: The force_success_count of this ListFactoryTaskOverviewResponse.
        :type force_success_count: int
        """
        self._force_success_count = force_success_count

    @property
    def freeze_count(self):
        r"""Gets the freeze_count of this ListFactoryTaskOverviewResponse.

        冻结的实例数量

        :return: The freeze_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._freeze_count

    @freeze_count.setter
    def freeze_count(self, freeze_count):
        r"""Sets the freeze_count of this ListFactoryTaskOverviewResponse.

        冻结的实例数量

        :param freeze_count: The freeze_count of this ListFactoryTaskOverviewResponse.
        :type freeze_count: int
        """
        self._freeze_count = freeze_count

    @property
    def ignore_success_count(self):
        r"""Gets the ignore_success_count of this ListFactoryTaskOverviewResponse.

        忽略失败的实例数量

        :return: The ignore_success_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._ignore_success_count

    @ignore_success_count.setter
    def ignore_success_count(self, ignore_success_count):
        r"""Sets the ignore_success_count of this ListFactoryTaskOverviewResponse.

        忽略失败的实例数量

        :param ignore_success_count: The ignore_success_count of this ListFactoryTaskOverviewResponse.
        :type ignore_success_count: int
        """
        self._ignore_success_count = ignore_success_count

    @property
    def manual_stop_count(self):
        r"""Gets the manual_stop_count of this ListFactoryTaskOverviewResponse.

        取消的实例数量

        :return: The manual_stop_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._manual_stop_count

    @manual_stop_count.setter
    def manual_stop_count(self, manual_stop_count):
        r"""Sets the manual_stop_count of this ListFactoryTaskOverviewResponse.

        取消的实例数量

        :param manual_stop_count: The manual_stop_count of this ListFactoryTaskOverviewResponse.
        :type manual_stop_count: int
        """
        self._manual_stop_count = manual_stop_count

    @property
    def pause_count(self):
        r"""Gets the pause_count of this ListFactoryTaskOverviewResponse.

        暂时的实例数量

        :return: The pause_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._pause_count

    @pause_count.setter
    def pause_count(self, pause_count):
        r"""Sets the pause_count of this ListFactoryTaskOverviewResponse.

        暂时的实例数量

        :param pause_count: The pause_count of this ListFactoryTaskOverviewResponse.
        :type pause_count: int
        """
        self._pause_count = pause_count

    @property
    def running_count(self):
        r"""Gets the running_count of this ListFactoryTaskOverviewResponse.

        运行中的实例数量

        :return: The running_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        r"""Sets the running_count of this ListFactoryTaskOverviewResponse.

        运行中的实例数量

        :param running_count: The running_count of this ListFactoryTaskOverviewResponse.
        :type running_count: int
        """
        self._running_count = running_count

    @property
    def running_exception_count(self):
        r"""Gets the running_exception_count of this ListFactoryTaskOverviewResponse.

        异常的实例数量

        :return: The running_exception_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._running_exception_count

    @running_exception_count.setter
    def running_exception_count(self, running_exception_count):
        r"""Sets the running_exception_count of this ListFactoryTaskOverviewResponse.

        异常的实例数量

        :param running_exception_count: The running_exception_count of this ListFactoryTaskOverviewResponse.
        :type running_exception_count: int
        """
        self._running_exception_count = running_exception_count

    @property
    def skip_count(self):
        r"""Gets the skip_count of this ListFactoryTaskOverviewResponse.

        跳过的实例数量

        :return: The skip_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._skip_count

    @skip_count.setter
    def skip_count(self, skip_count):
        r"""Sets the skip_count of this ListFactoryTaskOverviewResponse.

        跳过的实例数量

        :param skip_count: The skip_count of this ListFactoryTaskOverviewResponse.
        :type skip_count: int
        """
        self._skip_count = skip_count

    @property
    def success_count(self):
        r"""Gets the success_count of this ListFactoryTaskOverviewResponse.

        运行成功的实例数量

        :return: The success_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ListFactoryTaskOverviewResponse.

        运行成功的实例数量

        :param success_count: The success_count of this ListFactoryTaskOverviewResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def total_count(self):
        r"""Gets the total_count of this ListFactoryTaskOverviewResponse.

        实例总数

        :return: The total_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListFactoryTaskOverviewResponse.

        实例总数

        :param total_count: The total_count of this ListFactoryTaskOverviewResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def waiting_confirm_count(self):
        r"""Gets the waiting_confirm_count of this ListFactoryTaskOverviewResponse.

        待确认执行的实例数量

        :return: The waiting_confirm_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._waiting_confirm_count

    @waiting_confirm_count.setter
    def waiting_confirm_count(self, waiting_confirm_count):
        r"""Sets the waiting_confirm_count of this ListFactoryTaskOverviewResponse.

        待确认执行的实例数量

        :param waiting_confirm_count: The waiting_confirm_count of this ListFactoryTaskOverviewResponse.
        :type waiting_confirm_count: int
        """
        self._waiting_confirm_count = waiting_confirm_count

    @property
    def waiting_count(self):
        r"""Gets the waiting_count of this ListFactoryTaskOverviewResponse.

        等待运行的实例数量

        :return: The waiting_count of this ListFactoryTaskOverviewResponse.
        :rtype: int
        """
        return self._waiting_count

    @waiting_count.setter
    def waiting_count(self, waiting_count):
        r"""Sets the waiting_count of this ListFactoryTaskOverviewResponse.

        等待运行的实例数量

        :param waiting_count: The waiting_count of this ListFactoryTaskOverviewResponse.
        :type waiting_count: int
        """
        self._waiting_count = waiting_count

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
        if not isinstance(other, ListFactoryTaskOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
