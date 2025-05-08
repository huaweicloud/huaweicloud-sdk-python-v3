# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKafkaReassignmentTaskResponse(SdkResponse):

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
        'reassignment_time': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'reassignment_time': 'reassignment_time'
    }

    def __init__(self, job_id=None, reassignment_time=None):
        r"""CreateKafkaReassignmentTaskResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID（当执行分区平衡任务时仅返回job_id）。
        :type job_id: str
        :param reassignment_time: 预估时间，单位为秒（当执行预估时间任务时仅返回reassignment_time）。
        :type reassignment_time: int
        """
        
        super(CreateKafkaReassignmentTaskResponse, self).__init__()

        self._job_id = None
        self._reassignment_time = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if reassignment_time is not None:
            self.reassignment_time = reassignment_time

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateKafkaReassignmentTaskResponse.

        任务ID（当执行分区平衡任务时仅返回job_id）。

        :return: The job_id of this CreateKafkaReassignmentTaskResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateKafkaReassignmentTaskResponse.

        任务ID（当执行分区平衡任务时仅返回job_id）。

        :param job_id: The job_id of this CreateKafkaReassignmentTaskResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def reassignment_time(self):
        r"""Gets the reassignment_time of this CreateKafkaReassignmentTaskResponse.

        预估时间，单位为秒（当执行预估时间任务时仅返回reassignment_time）。

        :return: The reassignment_time of this CreateKafkaReassignmentTaskResponse.
        :rtype: int
        """
        return self._reassignment_time

    @reassignment_time.setter
    def reassignment_time(self, reassignment_time):
        r"""Sets the reassignment_time of this CreateKafkaReassignmentTaskResponse.

        预估时间，单位为秒（当执行预估时间任务时仅返回reassignment_time）。

        :param reassignment_time: The reassignment_time of this CreateKafkaReassignmentTaskResponse.
        :type reassignment_time: int
        """
        self._reassignment_time = reassignment_time

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
        if not isinstance(other, CreateKafkaReassignmentTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
