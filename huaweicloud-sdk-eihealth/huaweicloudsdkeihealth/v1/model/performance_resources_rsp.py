# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PerformanceResourcesRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'running_job_count': 'int',
        'schedulable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'running_job_count': 'running_job_count',
        'schedulable': 'schedulable'
    }

    def __init__(self, id=None, name=None, running_job_count=None, schedulable=None):
        """PerformanceResourcesRsp

        The model defined in huaweicloud sdk

        :param id: 性能加速资源id
        :type id: str
        :param name: 性能加速资源名称
        :type name: str
        :param running_job_count: 当前运行中的作业总数
        :type running_job_count: int
        :param schedulable: 资源是否可调度
        :type schedulable: bool
        """
        
        

        self._id = None
        self._name = None
        self._running_job_count = None
        self._schedulable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if running_job_count is not None:
            self.running_job_count = running_job_count
        if schedulable is not None:
            self.schedulable = schedulable

    @property
    def id(self):
        """Gets the id of this PerformanceResourcesRsp.

        性能加速资源id

        :return: The id of this PerformanceResourcesRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PerformanceResourcesRsp.

        性能加速资源id

        :param id: The id of this PerformanceResourcesRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PerformanceResourcesRsp.

        性能加速资源名称

        :return: The name of this PerformanceResourcesRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PerformanceResourcesRsp.

        性能加速资源名称

        :param name: The name of this PerformanceResourcesRsp.
        :type name: str
        """
        self._name = name

    @property
    def running_job_count(self):
        """Gets the running_job_count of this PerformanceResourcesRsp.

        当前运行中的作业总数

        :return: The running_job_count of this PerformanceResourcesRsp.
        :rtype: int
        """
        return self._running_job_count

    @running_job_count.setter
    def running_job_count(self, running_job_count):
        """Sets the running_job_count of this PerformanceResourcesRsp.

        当前运行中的作业总数

        :param running_job_count: The running_job_count of this PerformanceResourcesRsp.
        :type running_job_count: int
        """
        self._running_job_count = running_job_count

    @property
    def schedulable(self):
        """Gets the schedulable of this PerformanceResourcesRsp.

        资源是否可调度

        :return: The schedulable of this PerformanceResourcesRsp.
        :rtype: bool
        """
        return self._schedulable

    @schedulable.setter
    def schedulable(self, schedulable):
        """Sets the schedulable of this PerformanceResourcesRsp.

        资源是否可调度

        :param schedulable: The schedulable of this PerformanceResourcesRsp.
        :type schedulable: bool
        """
        self._schedulable = schedulable

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
        if not isinstance(other, PerformanceResourcesRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
