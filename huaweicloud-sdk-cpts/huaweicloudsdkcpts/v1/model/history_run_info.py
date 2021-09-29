# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryRunInfo:


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
        'run_id': 'int',
        'run_type': 'int',
        'start_time': 'str',
        'continue_time': 'int',
        'temp_names': 'list[TempName]'
    }

    attribute_map = {
        'name': 'name',
        'run_id': 'run_id',
        'run_type': 'run_type',
        'start_time': 'start_time',
        'continue_time': 'continue_time',
        'temp_names': 'temp_names'
    }

    def __init__(self, name=None, run_id=None, run_type=None, start_time=None, continue_time=None, temp_names=None):
        """HistoryRunInfo - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._run_id = None
        self._run_type = None
        self._start_time = None
        self._continue_time = None
        self._temp_names = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if run_id is not None:
            self.run_id = run_id
        if run_type is not None:
            self.run_type = run_type
        if start_time is not None:
            self.start_time = start_time
        if continue_time is not None:
            self.continue_time = continue_time
        if temp_names is not None:
            self.temp_names = temp_names

    @property
    def name(self):
        """Gets the name of this HistoryRunInfo.

        name

        :return: The name of this HistoryRunInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HistoryRunInfo.

        name

        :param name: The name of this HistoryRunInfo.
        :type: str
        """
        self._name = name

    @property
    def run_id(self):
        """Gets the run_id of this HistoryRunInfo.

        run_id

        :return: The run_id of this HistoryRunInfo.
        :rtype: int
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this HistoryRunInfo.

        run_id

        :param run_id: The run_id of this HistoryRunInfo.
        :type: int
        """
        self._run_id = run_id

    @property
    def run_type(self):
        """Gets the run_type of this HistoryRunInfo.

        run_type

        :return: The run_type of this HistoryRunInfo.
        :rtype: int
        """
        return self._run_type

    @run_type.setter
    def run_type(self, run_type):
        """Sets the run_type of this HistoryRunInfo.

        run_type

        :param run_type: The run_type of this HistoryRunInfo.
        :type: int
        """
        self._run_type = run_type

    @property
    def start_time(self):
        """Gets the start_time of this HistoryRunInfo.

        start_time

        :return: The start_time of this HistoryRunInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this HistoryRunInfo.

        start_time

        :param start_time: The start_time of this HistoryRunInfo.
        :type: str
        """
        self._start_time = start_time

    @property
    def continue_time(self):
        """Gets the continue_time of this HistoryRunInfo.

        continue_time

        :return: The continue_time of this HistoryRunInfo.
        :rtype: int
        """
        return self._continue_time

    @continue_time.setter
    def continue_time(self, continue_time):
        """Sets the continue_time of this HistoryRunInfo.

        continue_time

        :param continue_time: The continue_time of this HistoryRunInfo.
        :type: int
        """
        self._continue_time = continue_time

    @property
    def temp_names(self):
        """Gets the temp_names of this HistoryRunInfo.

        temp_names

        :return: The temp_names of this HistoryRunInfo.
        :rtype: list[TempName]
        """
        return self._temp_names

    @temp_names.setter
    def temp_names(self, temp_names):
        """Sets the temp_names of this HistoryRunInfo.

        temp_names

        :param temp_names: The temp_names of this HistoryRunInfo.
        :type: list[TempName]
        """
        self._temp_names = temp_names

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
        if not isinstance(other, HistoryRunInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
