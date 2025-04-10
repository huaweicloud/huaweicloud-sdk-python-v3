# coding: utf-8

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
        'run_id': 'float',
        'run_type': 'float',
        'start_time': 'str',
        'end_time': 'str',
        'continue_time': 'float',
        'temp_names': 'list[TempName]',
        'parallel': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'run_id': 'run_id',
        'run_type': 'run_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'continue_time': 'continue_time',
        'temp_names': 'temp_names',
        'parallel': 'parallel'
    }

    def __init__(self, name=None, run_id=None, run_type=None, start_time=None, end_time=None, continue_time=None, temp_names=None, parallel=None):
        r"""HistoryRunInfo

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param run_id: 报告id
        :type run_id: float
        :param run_type: 任务类型（0：旧版本任务；1：融合版本任务）
        :type run_type: float
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param continue_time: 继续时间
        :type continue_time: float
        :param temp_names: 用例或者事务名称
        :type temp_names: list[:class:`huaweicloudsdkcpts.v1.TempName`]
        :param parallel: 任务间用例是否并行执行
        :type parallel: bool
        """
        
        

        self._name = None
        self._run_id = None
        self._run_type = None
        self._start_time = None
        self._end_time = None
        self._continue_time = None
        self._temp_names = None
        self._parallel = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if run_id is not None:
            self.run_id = run_id
        if run_type is not None:
            self.run_type = run_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if continue_time is not None:
            self.continue_time = continue_time
        if temp_names is not None:
            self.temp_names = temp_names
        if parallel is not None:
            self.parallel = parallel

    @property
    def name(self):
        r"""Gets the name of this HistoryRunInfo.

        名称

        :return: The name of this HistoryRunInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HistoryRunInfo.

        名称

        :param name: The name of this HistoryRunInfo.
        :type name: str
        """
        self._name = name

    @property
    def run_id(self):
        r"""Gets the run_id of this HistoryRunInfo.

        报告id

        :return: The run_id of this HistoryRunInfo.
        :rtype: float
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        r"""Sets the run_id of this HistoryRunInfo.

        报告id

        :param run_id: The run_id of this HistoryRunInfo.
        :type run_id: float
        """
        self._run_id = run_id

    @property
    def run_type(self):
        r"""Gets the run_type of this HistoryRunInfo.

        任务类型（0：旧版本任务；1：融合版本任务）

        :return: The run_type of this HistoryRunInfo.
        :rtype: float
        """
        return self._run_type

    @run_type.setter
    def run_type(self, run_type):
        r"""Sets the run_type of this HistoryRunInfo.

        任务类型（0：旧版本任务；1：融合版本任务）

        :param run_type: The run_type of this HistoryRunInfo.
        :type run_type: float
        """
        self._run_type = run_type

    @property
    def start_time(self):
        r"""Gets the start_time of this HistoryRunInfo.

        开始时间

        :return: The start_time of this HistoryRunInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this HistoryRunInfo.

        开始时间

        :param start_time: The start_time of this HistoryRunInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this HistoryRunInfo.

        结束时间

        :return: The end_time of this HistoryRunInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this HistoryRunInfo.

        结束时间

        :param end_time: The end_time of this HistoryRunInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def continue_time(self):
        r"""Gets the continue_time of this HistoryRunInfo.

        继续时间

        :return: The continue_time of this HistoryRunInfo.
        :rtype: float
        """
        return self._continue_time

    @continue_time.setter
    def continue_time(self, continue_time):
        r"""Sets the continue_time of this HistoryRunInfo.

        继续时间

        :param continue_time: The continue_time of this HistoryRunInfo.
        :type continue_time: float
        """
        self._continue_time = continue_time

    @property
    def temp_names(self):
        r"""Gets the temp_names of this HistoryRunInfo.

        用例或者事务名称

        :return: The temp_names of this HistoryRunInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.TempName`]
        """
        return self._temp_names

    @temp_names.setter
    def temp_names(self, temp_names):
        r"""Sets the temp_names of this HistoryRunInfo.

        用例或者事务名称

        :param temp_names: The temp_names of this HistoryRunInfo.
        :type temp_names: list[:class:`huaweicloudsdkcpts.v1.TempName`]
        """
        self._temp_names = temp_names

    @property
    def parallel(self):
        r"""Gets the parallel of this HistoryRunInfo.

        任务间用例是否并行执行

        :return: The parallel of this HistoryRunInfo.
        :rtype: bool
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        r"""Sets the parallel of this HistoryRunInfo.

        任务间用例是否并行执行

        :param parallel: The parallel of this HistoryRunInfo.
        :type parallel: bool
        """
        self._parallel = parallel

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
