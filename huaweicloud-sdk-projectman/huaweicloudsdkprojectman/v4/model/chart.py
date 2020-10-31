# coding: utf-8

import pprint
import re

import six





class Chart:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'finished_num': 'int',
        'iteration_id': 'int',
        'project_num_id': 'int',
        'remaining_num': 'int',
        'total': 'int'
    }

    attribute_map = {
        'date': 'date',
        'finished_num': 'finished_num',
        'iteration_id': 'iteration_id',
        'project_num_id': 'project_num_id',
        'remaining_num': 'remaining_num',
        'total': 'total'
    }

    def __init__(self, date=None, finished_num=None, iteration_id=None, project_num_id=None, remaining_num=None, total=None):
        """Chart - a model defined in huaweicloud sdk"""
        
        

        self._date = None
        self._finished_num = None
        self._iteration_id = None
        self._project_num_id = None
        self._remaining_num = None
        self._total = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if finished_num is not None:
            self.finished_num = finished_num
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if project_num_id is not None:
            self.project_num_id = project_num_id
        if remaining_num is not None:
            self.remaining_num = remaining_num
        if total is not None:
            self.total = total

    @property
    def date(self):
        """Gets the date of this Chart.

        统计时间

        :return: The date of this Chart.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Chart.

        统计时间

        :param date: The date of this Chart.
        :type: str
        """
        self._date = date

    @property
    def finished_num(self):
        """Gets the finished_num of this Chart.

        完成story工单

        :return: The finished_num of this Chart.
        :rtype: int
        """
        return self._finished_num

    @finished_num.setter
    def finished_num(self, finished_num):
        """Sets the finished_num of this Chart.

        完成story工单

        :param finished_num: The finished_num of this Chart.
        :type: int
        """
        self._finished_num = finished_num

    @property
    def iteration_id(self):
        """Gets the iteration_id of this Chart.

        迭代id

        :return: The iteration_id of this Chart.
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this Chart.

        迭代id

        :param iteration_id: The iteration_id of this Chart.
        :type: int
        """
        self._iteration_id = iteration_id

    @property
    def project_num_id(self):
        """Gets the project_num_id of this Chart.

        项目id

        :return: The project_num_id of this Chart.
        :rtype: int
        """
        return self._project_num_id

    @project_num_id.setter
    def project_num_id(self, project_num_id):
        """Sets the project_num_id of this Chart.

        项目id

        :param project_num_id: The project_num_id of this Chart.
        :type: int
        """
        self._project_num_id = project_num_id

    @property
    def remaining_num(self):
        """Gets the remaining_num of this Chart.

        未完成story数

        :return: The remaining_num of this Chart.
        :rtype: int
        """
        return self._remaining_num

    @remaining_num.setter
    def remaining_num(self, remaining_num):
        """Sets the remaining_num of this Chart.

        未完成story数

        :param remaining_num: The remaining_num of this Chart.
        :type: int
        """
        self._remaining_num = remaining_num

    @property
    def total(self):
        """Gets the total of this Chart.

        总story数

        :return: The total of this Chart.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Chart.

        总story数

        :param total: The total of this Chart.
        :type: int
        """
        self._total = total

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Chart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
