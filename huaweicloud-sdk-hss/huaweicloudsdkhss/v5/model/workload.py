# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Workload:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_id': 'str',
        'workload_name': 'str',
        'workload_type': 'str'
    }

    attribute_map = {
        'workload_id': 'workload_id',
        'workload_name': 'workload_name',
        'workload_type': 'workload_type'
    }

    def __init__(self, workload_id=None, workload_name=None, workload_type=None):
        r"""Workload

        The model defined in huaweicloud sdk

        :param workload_id: 工作负载ID
        :type workload_id: str
        :param workload_name: 工作负载名称
        :type workload_name: str
        :param workload_type: 工作负载类型，包含如下：   - deployments：无状态负载   - statefulsets：有状态负载   - daemonsets：守护进程表
        :type workload_type: str
        """
        
        

        self._workload_id = None
        self._workload_name = None
        self._workload_type = None
        self.discriminator = None

        self.workload_id = workload_id
        self.workload_name = workload_name
        self.workload_type = workload_type

    @property
    def workload_id(self):
        r"""Gets the workload_id of this Workload.

        工作负载ID

        :return: The workload_id of this Workload.
        :rtype: str
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        r"""Sets the workload_id of this Workload.

        工作负载ID

        :param workload_id: The workload_id of this Workload.
        :type workload_id: str
        """
        self._workload_id = workload_id

    @property
    def workload_name(self):
        r"""Gets the workload_name of this Workload.

        工作负载名称

        :return: The workload_name of this Workload.
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        r"""Sets the workload_name of this Workload.

        工作负载名称

        :param workload_name: The workload_name of this Workload.
        :type workload_name: str
        """
        self._workload_name = workload_name

    @property
    def workload_type(self):
        r"""Gets the workload_type of this Workload.

        工作负载类型，包含如下：   - deployments：无状态负载   - statefulsets：有状态负载   - daemonsets：守护进程表

        :return: The workload_type of this Workload.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this Workload.

        工作负载类型，包含如下：   - deployments：无状态负载   - statefulsets：有状态负载   - daemonsets：守护进程表

        :param workload_type: The workload_type of this Workload.
        :type workload_type: str
        """
        self._workload_type = workload_type

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
        if not isinstance(other, Workload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
