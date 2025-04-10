# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeInstancesVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_ids': 'list[str]',
        'succeeded_num': 'int',
        'failed_num': 'int',
        'failed_instance_ids': 'list[str]',
        'error_messages': 'list[str]'
    }

    attribute_map = {
        'job_ids': 'job_ids',
        'succeeded_num': 'succeeded_num',
        'failed_num': 'failed_num',
        'failed_instance_ids': 'failed_instance_ids',
        'error_messages': 'error_messages'
    }

    def __init__(self, job_ids=None, succeeded_num=None, failed_num=None, failed_instance_ids=None, error_messages=None):
        r"""UpgradeInstancesVersionResponse

        The model defined in huaweicloud sdk

        :param job_ids: 任务id。
        :type job_ids: list[str]
        :param succeeded_num: 下发成功的实例数量。
        :type succeeded_num: int
        :param failed_num: 下发失败的实例数量。
        :type failed_num: int
        :param failed_instance_ids: 下发失败的实例ID列表。
        :type failed_instance_ids: list[str]
        :param error_messages: 下发失败错误信息列表。
        :type error_messages: list[str]
        """
        
        super(UpgradeInstancesVersionResponse, self).__init__()

        self._job_ids = None
        self._succeeded_num = None
        self._failed_num = None
        self._failed_instance_ids = None
        self._error_messages = None
        self.discriminator = None

        if job_ids is not None:
            self.job_ids = job_ids
        if succeeded_num is not None:
            self.succeeded_num = succeeded_num
        if failed_num is not None:
            self.failed_num = failed_num
        if failed_instance_ids is not None:
            self.failed_instance_ids = failed_instance_ids
        if error_messages is not None:
            self.error_messages = error_messages

    @property
    def job_ids(self):
        r"""Gets the job_ids of this UpgradeInstancesVersionResponse.

        任务id。

        :return: The job_ids of this UpgradeInstancesVersionResponse.
        :rtype: list[str]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        r"""Sets the job_ids of this UpgradeInstancesVersionResponse.

        任务id。

        :param job_ids: The job_ids of this UpgradeInstancesVersionResponse.
        :type job_ids: list[str]
        """
        self._job_ids = job_ids

    @property
    def succeeded_num(self):
        r"""Gets the succeeded_num of this UpgradeInstancesVersionResponse.

        下发成功的实例数量。

        :return: The succeeded_num of this UpgradeInstancesVersionResponse.
        :rtype: int
        """
        return self._succeeded_num

    @succeeded_num.setter
    def succeeded_num(self, succeeded_num):
        r"""Sets the succeeded_num of this UpgradeInstancesVersionResponse.

        下发成功的实例数量。

        :param succeeded_num: The succeeded_num of this UpgradeInstancesVersionResponse.
        :type succeeded_num: int
        """
        self._succeeded_num = succeeded_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this UpgradeInstancesVersionResponse.

        下发失败的实例数量。

        :return: The failed_num of this UpgradeInstancesVersionResponse.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this UpgradeInstancesVersionResponse.

        下发失败的实例数量。

        :param failed_num: The failed_num of this UpgradeInstancesVersionResponse.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def failed_instance_ids(self):
        r"""Gets the failed_instance_ids of this UpgradeInstancesVersionResponse.

        下发失败的实例ID列表。

        :return: The failed_instance_ids of this UpgradeInstancesVersionResponse.
        :rtype: list[str]
        """
        return self._failed_instance_ids

    @failed_instance_ids.setter
    def failed_instance_ids(self, failed_instance_ids):
        r"""Sets the failed_instance_ids of this UpgradeInstancesVersionResponse.

        下发失败的实例ID列表。

        :param failed_instance_ids: The failed_instance_ids of this UpgradeInstancesVersionResponse.
        :type failed_instance_ids: list[str]
        """
        self._failed_instance_ids = failed_instance_ids

    @property
    def error_messages(self):
        r"""Gets the error_messages of this UpgradeInstancesVersionResponse.

        下发失败错误信息列表。

        :return: The error_messages of this UpgradeInstancesVersionResponse.
        :rtype: list[str]
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        r"""Sets the error_messages of this UpgradeInstancesVersionResponse.

        下发失败错误信息列表。

        :param error_messages: The error_messages of this UpgradeInstancesVersionResponse.
        :type error_messages: list[str]
        """
        self._error_messages = error_messages

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
        if not isinstance(other, UpgradeInstancesVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
