# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartInfo:

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
        'start_time': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'start_time': 'start_time'
    }

    def __init__(self, job_id=None, start_time=None):
        """StartInfo

        The model defined in huaweicloud sdk

        :param job_id: 任务id。 
        :type job_id: str
        :param start_time: 任务启动时间，时间戳格式精确到秒，例如：1614078283，取值为空代表立即启动。
        :type start_time: str
        """
        
        

        self._job_id = None
        self._start_time = None
        self.discriminator = None

        self.job_id = job_id
        if start_time is not None:
            self.start_time = start_time

    @property
    def job_id(self):
        """Gets the job_id of this StartInfo.

        任务id。 

        :return: The job_id of this StartInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StartInfo.

        任务id。 

        :param job_id: The job_id of this StartInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def start_time(self):
        """Gets the start_time of this StartInfo.

        任务启动时间，时间戳格式精确到秒，例如：1614078283，取值为空代表立即启动。

        :return: The start_time of this StartInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this StartInfo.

        任务启动时间，时间戳格式精确到秒，例如：1614078283，取值为空代表立即启动。

        :param start_time: The start_time of this StartInfo.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, StartInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
