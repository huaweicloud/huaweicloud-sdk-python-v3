# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobFilterDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'job_node_labels': 'list[str]'
    }

    attribute_map = {
        'job_name': 'job_name',
        'job_node_labels': 'job_node_labels'
    }

    def __init__(self, job_name=None, job_node_labels=None):
        """JobFilterDto

        The model defined in huaweicloud sdk

        :param job_name: 作业名称
        :type job_name: str
        :param job_node_labels: 计算节点标签
        :type job_node_labels: list[str]
        """
        
        

        self._job_name = None
        self._job_node_labels = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if job_node_labels is not None:
            self.job_node_labels = job_node_labels

    @property
    def job_name(self):
        """Gets the job_name of this JobFilterDto.

        作业名称

        :return: The job_name of this JobFilterDto.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobFilterDto.

        作业名称

        :param job_name: The job_name of this JobFilterDto.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_node_labels(self):
        """Gets the job_node_labels of this JobFilterDto.

        计算节点标签

        :return: The job_node_labels of this JobFilterDto.
        :rtype: list[str]
        """
        return self._job_node_labels

    @job_node_labels.setter
    def job_node_labels(self, job_node_labels):
        """Sets the job_node_labels of this JobFilterDto.

        计算节点标签

        :param job_node_labels: The job_node_labels of this JobFilterDto.
        :type job_node_labels: list[str]
        """
        self._job_node_labels = job_node_labels

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
        if not isinstance(other, JobFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
