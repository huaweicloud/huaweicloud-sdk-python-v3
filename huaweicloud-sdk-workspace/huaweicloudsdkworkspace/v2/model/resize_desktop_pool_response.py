# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeDesktopPoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'error_policy': 'str',
        'jobs': 'list[ResizeDesktopPoolJobResponse]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'error_policy': 'error_policy',
        'jobs': 'jobs'
    }

    def __init__(self, job_id=None, error_policy=None, jobs=None):
        """ResizeDesktopPoolResponse

        The model defined in huaweicloud sdk

        :param job_id: 创建云桌面总任务id
        :type job_id: str
        :param error_policy: 变更订单错误处理策略。cbc调用返回值。设置为 NO_WORKORDER。云运营平台会认为无法开通成功，退费给客户后，不会再发运维工单给云服务，而由云服务自己去闭环处理对应问题。
        :type error_policy: str
        :param jobs: 按需桌面变更规格返回的任务信息。
        :type jobs: list[:class:`huaweicloudsdkworkspace.v2.ResizeDesktopPoolJobResponse`]
        """
        
        super(ResizeDesktopPoolResponse, self).__init__()

        self._job_id = None
        self._error_policy = None
        self._jobs = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if error_policy is not None:
            self.error_policy = error_policy
        if jobs is not None:
            self.jobs = jobs

    @property
    def job_id(self):
        """Gets the job_id of this ResizeDesktopPoolResponse.

        创建云桌面总任务id

        :return: The job_id of this ResizeDesktopPoolResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ResizeDesktopPoolResponse.

        创建云桌面总任务id

        :param job_id: The job_id of this ResizeDesktopPoolResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def error_policy(self):
        """Gets the error_policy of this ResizeDesktopPoolResponse.

        变更订单错误处理策略。cbc调用返回值。设置为 NO_WORKORDER。云运营平台会认为无法开通成功，退费给客户后，不会再发运维工单给云服务，而由云服务自己去闭环处理对应问题。

        :return: The error_policy of this ResizeDesktopPoolResponse.
        :rtype: str
        """
        return self._error_policy

    @error_policy.setter
    def error_policy(self, error_policy):
        """Sets the error_policy of this ResizeDesktopPoolResponse.

        变更订单错误处理策略。cbc调用返回值。设置为 NO_WORKORDER。云运营平台会认为无法开通成功，退费给客户后，不会再发运维工单给云服务，而由云服务自己去闭环处理对应问题。

        :param error_policy: The error_policy of this ResizeDesktopPoolResponse.
        :type error_policy: str
        """
        self._error_policy = error_policy

    @property
    def jobs(self):
        """Gets the jobs of this ResizeDesktopPoolResponse.

        按需桌面变更规格返回的任务信息。

        :return: The jobs of this ResizeDesktopPoolResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ResizeDesktopPoolJobResponse`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ResizeDesktopPoolResponse.

        按需桌面变更规格返回的任务信息。

        :param jobs: The jobs of this ResizeDesktopPoolResponse.
        :type jobs: list[:class:`huaweicloudsdkworkspace.v2.ResizeDesktopPoolJobResponse`]
        """
        self._jobs = jobs

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
        if not isinstance(other, ResizeDesktopPoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
