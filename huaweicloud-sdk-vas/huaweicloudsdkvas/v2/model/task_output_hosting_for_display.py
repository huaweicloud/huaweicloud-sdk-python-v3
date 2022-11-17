# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskOutputHostingForDisplay:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs': 'list[TaskOutputHostingForDisplayObs]',
        'result_json_overdue_at': 'int',
        'data_category': 'list[str]'
    }

    attribute_map = {
        'obs': 'obs',
        'result_json_overdue_at': 'result_json_overdue_at',
        'data_category': 'data_category'
    }

    def __init__(self, obs=None, result_json_overdue_at=None, data_category=None):
        """TaskOutputHostingForDisplay

        The model defined in huaweicloud sdk

        :param obs: 作业所有结果文件所在的OBS桶和路径
        :type obs: list[:class:`huaweicloudsdkvas.v2.TaskOutputHostingForDisplayObs`]
        :param result_json_overdue_at: 作业结果文件的过期时间
        :type result_json_overdue_at: int
        :param data_category: 作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要
        :type data_category: list[str]
        """
        
        

        self._obs = None
        self._result_json_overdue_at = None
        self._data_category = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if result_json_overdue_at is not None:
            self.result_json_overdue_at = result_json_overdue_at
        if data_category is not None:
            self.data_category = data_category

    @property
    def obs(self):
        """Gets the obs of this TaskOutputHostingForDisplay.

        作业所有结果文件所在的OBS桶和路径

        :return: The obs of this TaskOutputHostingForDisplay.
        :rtype: list[:class:`huaweicloudsdkvas.v2.TaskOutputHostingForDisplayObs`]
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this TaskOutputHostingForDisplay.

        作业所有结果文件所在的OBS桶和路径

        :param obs: The obs of this TaskOutputHostingForDisplay.
        :type obs: list[:class:`huaweicloudsdkvas.v2.TaskOutputHostingForDisplayObs`]
        """
        self._obs = obs

    @property
    def result_json_overdue_at(self):
        """Gets the result_json_overdue_at of this TaskOutputHostingForDisplay.

        作业结果文件的过期时间

        :return: The result_json_overdue_at of this TaskOutputHostingForDisplay.
        :rtype: int
        """
        return self._result_json_overdue_at

    @result_json_overdue_at.setter
    def result_json_overdue_at(self, result_json_overdue_at):
        """Sets the result_json_overdue_at of this TaskOutputHostingForDisplay.

        作业结果文件的过期时间

        :param result_json_overdue_at: The result_json_overdue_at of this TaskOutputHostingForDisplay.
        :type result_json_overdue_at: int
        """
        self._result_json_overdue_at = result_json_overdue_at

    @property
    def data_category(self):
        """Gets the data_category of this TaskOutputHostingForDisplay.

        作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要

        :return: The data_category of this TaskOutputHostingForDisplay.
        :rtype: list[str]
        """
        return self._data_category

    @data_category.setter
    def data_category(self, data_category):
        """Sets the data_category of this TaskOutputHostingForDisplay.

        作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要

        :param data_category: The data_category of this TaskOutputHostingForDisplay.
        :type data_category: list[str]
        """
        self._data_category = data_category

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
        if not isinstance(other, TaskOutputHostingForDisplay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
