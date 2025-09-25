# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQuickAccessDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'message': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'job_id': 'job_id'
    }

    def __init__(self, status=None, message=None, job_id=None):
        r"""CreateQuickAccessDomainResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 异步任务的状态，如RUNNING（运行中）、SUCCESS（成功）、FAILED（失败） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type status: str
        :param message: **参数解释：** 异步任务的描述，说明当前任务的进展或结果 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type message: str
        :param job_id: **参数解释：** 异步任务的ID，用于查询任务进度或结果的唯一标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type job_id: str
        """
        
        super(CreateQuickAccessDomainResponse, self).__init__()

        self._status = None
        self._message = None
        self._job_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this CreateQuickAccessDomainResponse.

        **参数解释：** 异步任务的状态，如RUNNING（运行中）、SUCCESS（成功）、FAILED（失败） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The status of this CreateQuickAccessDomainResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateQuickAccessDomainResponse.

        **参数解释：** 异步任务的状态，如RUNNING（运行中）、SUCCESS（成功）、FAILED（失败） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param status: The status of this CreateQuickAccessDomainResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this CreateQuickAccessDomainResponse.

        **参数解释：** 异步任务的描述，说明当前任务的进展或结果 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The message of this CreateQuickAccessDomainResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateQuickAccessDomainResponse.

        **参数解释：** 异步任务的描述，说明当前任务的进展或结果 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param message: The message of this CreateQuickAccessDomainResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateQuickAccessDomainResponse.

        **参数解释：** 异步任务的ID，用于查询任务进度或结果的唯一标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The job_id of this CreateQuickAccessDomainResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateQuickAccessDomainResponse.

        **参数解释：** 异步任务的ID，用于查询任务进度或结果的唯一标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param job_id: The job_id of this CreateQuickAccessDomainResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, CreateQuickAccessDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
