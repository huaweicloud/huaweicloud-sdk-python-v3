# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStatusStatisticRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'iteration_id': 'int',
        'tracker_id': 'int',
        'status_id': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'iteration_id': 'iteration_id',
        'tracker_id': 'tracker_id',
        'status_id': 'status_id'
    }

    def __init__(self, project_id=None, iteration_id=None, tracker_id=None, status_id=None):
        """ListStatusStatisticRequest

        The model defined in huaweicloud sdk

        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param iteration_id: 迭代数字id
        :type iteration_id: int
        :param tracker_id: 自定义字段支持的工作项类型 2任务/Task,3缺陷/Bug,7Story
        :type tracker_id: int
        :param status_id: 工作项状态数字id
        :type status_id: int
        """
        
        

        self._project_id = None
        self._iteration_id = None
        self._tracker_id = None
        self._status_id = None
        self.discriminator = None

        self.project_id = project_id
        self.iteration_id = iteration_id
        self.tracker_id = tracker_id
        self.status_id = status_id

    @property
    def project_id(self):
        """Gets the project_id of this ListStatusStatisticRequest.

        devcloud项目的32位id

        :return: The project_id of this ListStatusStatisticRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListStatusStatisticRequest.

        devcloud项目的32位id

        :param project_id: The project_id of this ListStatusStatisticRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def iteration_id(self):
        """Gets the iteration_id of this ListStatusStatisticRequest.

        迭代数字id

        :return: The iteration_id of this ListStatusStatisticRequest.
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this ListStatusStatisticRequest.

        迭代数字id

        :param iteration_id: The iteration_id of this ListStatusStatisticRequest.
        :type iteration_id: int
        """
        self._iteration_id = iteration_id

    @property
    def tracker_id(self):
        """Gets the tracker_id of this ListStatusStatisticRequest.

        自定义字段支持的工作项类型 2任务/Task,3缺陷/Bug,7Story

        :return: The tracker_id of this ListStatusStatisticRequest.
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this ListStatusStatisticRequest.

        自定义字段支持的工作项类型 2任务/Task,3缺陷/Bug,7Story

        :param tracker_id: The tracker_id of this ListStatusStatisticRequest.
        :type tracker_id: int
        """
        self._tracker_id = tracker_id

    @property
    def status_id(self):
        """Gets the status_id of this ListStatusStatisticRequest.

        工作项状态数字id

        :return: The status_id of this ListStatusStatisticRequest.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this ListStatusStatisticRequest.

        工作项状态数字id

        :param status_id: The status_id of this ListStatusStatisticRequest.
        :type status_id: int
        """
        self._status_id = status_id

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
        if not isinstance(other, ListStatusStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
