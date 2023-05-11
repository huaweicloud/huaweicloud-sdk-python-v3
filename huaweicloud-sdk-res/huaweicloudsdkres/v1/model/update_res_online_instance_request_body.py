# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResOnlineInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'description': 'str',
        'job_config': 'JobConfig',
        'job_name': 'str',
        'job_type': 'str',
        'schedule': 'str'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'job_config': 'job_config',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'schedule': 'schedule'
    }

    def __init__(self, category=None, description=None, job_config=None, job_name=None, job_type=None, schedule=None):
        """UpdateResOnlineInstanceRequestBody

        The model defined in huaweicloud sdk

        :param category: 类别。
        :type category: str
        :param description: 描述。
        :type description: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkres.v1.JobConfig`
        :param job_name: 作业名称。
        :type job_name: str
        :param job_type: 作业类型。
        :type job_type: str
        :param schedule: 调度参数。
        :type schedule: str
        """
        
        

        self._category = None
        self._description = None
        self._job_config = None
        self._job_name = None
        self._job_type = None
        self._schedule = None
        self.discriminator = None

        self.category = category
        if description is not None:
            self.description = description
        self.job_config = job_config
        self.job_name = job_name
        self.job_type = job_type
        self.schedule = schedule

    @property
    def category(self):
        """Gets the category of this UpdateResOnlineInstanceRequestBody.

        类别。

        :return: The category of this UpdateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this UpdateResOnlineInstanceRequestBody.

        类别。

        :param category: The category of this UpdateResOnlineInstanceRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        """Gets the description of this UpdateResOnlineInstanceRequestBody.

        描述。

        :return: The description of this UpdateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateResOnlineInstanceRequestBody.

        描述。

        :param description: The description of this UpdateResOnlineInstanceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def job_config(self):
        """Gets the job_config of this UpdateResOnlineInstanceRequestBody.

        :return: The job_config of this UpdateResOnlineInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        """Sets the job_config of this UpdateResOnlineInstanceRequestBody.

        :param job_config: The job_config of this UpdateResOnlineInstanceRequestBody.
        :type job_config: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        self._job_config = job_config

    @property
    def job_name(self):
        """Gets the job_name of this UpdateResOnlineInstanceRequestBody.

        作业名称。

        :return: The job_name of this UpdateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this UpdateResOnlineInstanceRequestBody.

        作业名称。

        :param job_name: The job_name of this UpdateResOnlineInstanceRequestBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this UpdateResOnlineInstanceRequestBody.

        作业类型。

        :return: The job_type of this UpdateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this UpdateResOnlineInstanceRequestBody.

        作业类型。

        :param job_type: The job_type of this UpdateResOnlineInstanceRequestBody.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def schedule(self):
        """Gets the schedule of this UpdateResOnlineInstanceRequestBody.

        调度参数。

        :return: The schedule of this UpdateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this UpdateResOnlineInstanceRequestBody.

        调度参数。

        :param schedule: The schedule of this UpdateResOnlineInstanceRequestBody.
        :type schedule: str
        """
        self._schedule = schedule

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
        if not isinstance(other, UpdateResOnlineInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
