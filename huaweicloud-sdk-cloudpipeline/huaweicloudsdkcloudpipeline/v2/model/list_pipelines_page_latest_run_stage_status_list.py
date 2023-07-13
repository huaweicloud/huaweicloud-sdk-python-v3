# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelinesPageLatestRunStageStatusList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sequence': 'int',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'sequence': 'sequence',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, name=None, sequence=None, status=None, start_time=None, end_time=None):
        """ListPipelinesPageLatestRunStageStatusList

        The model defined in huaweicloud sdk

        :param name: 阶段名
        :type name: str
        :param sequence: 序列号
        :type sequence: int
        :param status: 状态
        :type status: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        """
        
        

        self._name = None
        self._sequence = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if sequence is not None:
            self.sequence = sequence
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def name(self):
        """Gets the name of this ListPipelinesPageLatestRunStageStatusList.

        阶段名

        :return: The name of this ListPipelinesPageLatestRunStageStatusList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPipelinesPageLatestRunStageStatusList.

        阶段名

        :param name: The name of this ListPipelinesPageLatestRunStageStatusList.
        :type name: str
        """
        self._name = name

    @property
    def sequence(self):
        """Gets the sequence of this ListPipelinesPageLatestRunStageStatusList.

        序列号

        :return: The sequence of this ListPipelinesPageLatestRunStageStatusList.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ListPipelinesPageLatestRunStageStatusList.

        序列号

        :param sequence: The sequence of this ListPipelinesPageLatestRunStageStatusList.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def status(self):
        """Gets the status of this ListPipelinesPageLatestRunStageStatusList.

        状态

        :return: The status of this ListPipelinesPageLatestRunStageStatusList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPipelinesPageLatestRunStageStatusList.

        状态

        :param status: The status of this ListPipelinesPageLatestRunStageStatusList.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ListPipelinesPageLatestRunStageStatusList.

        开始时间

        :return: The start_time of this ListPipelinesPageLatestRunStageStatusList.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListPipelinesPageLatestRunStageStatusList.

        开始时间

        :param start_time: The start_time of this ListPipelinesPageLatestRunStageStatusList.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListPipelinesPageLatestRunStageStatusList.

        结束时间

        :return: The end_time of this ListPipelinesPageLatestRunStageStatusList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListPipelinesPageLatestRunStageStatusList.

        结束时间

        :param end_time: The end_time of this ListPipelinesPageLatestRunStageStatusList.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListPipelinesPageLatestRunStageStatusList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
