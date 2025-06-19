# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'octopus_job_name': 'str',
        'actual_build_number': 'str',
        'daily_build_number': 'str'
    }

    attribute_map = {
        'octopus_job_name': 'octopus_job_name',
        'actual_build_number': 'actual_build_number',
        'daily_build_number': 'daily_build_number'
    }

    def __init__(self, octopus_job_name=None, actual_build_number=None, daily_build_number=None):
        r"""ExecuteJobResponse

        The model defined in huaweicloud sdk

        :param octopus_job_name: 临时任务名称
        :type octopus_job_name: str
        :param actual_build_number: 实际构建次数
        :type actual_build_number: str
        :param daily_build_number: 构建每日编号
        :type daily_build_number: str
        """
        
        super(ExecuteJobResponse, self).__init__()

        self._octopus_job_name = None
        self._actual_build_number = None
        self._daily_build_number = None
        self.discriminator = None

        if octopus_job_name is not None:
            self.octopus_job_name = octopus_job_name
        if actual_build_number is not None:
            self.actual_build_number = actual_build_number
        if daily_build_number is not None:
            self.daily_build_number = daily_build_number

    @property
    def octopus_job_name(self):
        r"""Gets the octopus_job_name of this ExecuteJobResponse.

        临时任务名称

        :return: The octopus_job_name of this ExecuteJobResponse.
        :rtype: str
        """
        return self._octopus_job_name

    @octopus_job_name.setter
    def octopus_job_name(self, octopus_job_name):
        r"""Sets the octopus_job_name of this ExecuteJobResponse.

        临时任务名称

        :param octopus_job_name: The octopus_job_name of this ExecuteJobResponse.
        :type octopus_job_name: str
        """
        self._octopus_job_name = octopus_job_name

    @property
    def actual_build_number(self):
        r"""Gets the actual_build_number of this ExecuteJobResponse.

        实际构建次数

        :return: The actual_build_number of this ExecuteJobResponse.
        :rtype: str
        """
        return self._actual_build_number

    @actual_build_number.setter
    def actual_build_number(self, actual_build_number):
        r"""Sets the actual_build_number of this ExecuteJobResponse.

        实际构建次数

        :param actual_build_number: The actual_build_number of this ExecuteJobResponse.
        :type actual_build_number: str
        """
        self._actual_build_number = actual_build_number

    @property
    def daily_build_number(self):
        r"""Gets the daily_build_number of this ExecuteJobResponse.

        构建每日编号

        :return: The daily_build_number of this ExecuteJobResponse.
        :rtype: str
        """
        return self._daily_build_number

    @daily_build_number.setter
    def daily_build_number(self, daily_build_number):
        r"""Sets the daily_build_number of this ExecuteJobResponse.

        构建每日编号

        :param daily_build_number: The daily_build_number of this ExecuteJobResponse.
        :type daily_build_number: str
        """
        self._daily_build_number = daily_build_number

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
        if not isinstance(other, ExecuteJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
