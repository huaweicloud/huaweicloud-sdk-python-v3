# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareTaskParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_task_id': 'str',
        'type': 'str',
        'start_time': 'str',
        'option': 'dict(str, str)',
        'db_object': 'dict(str, DatabaseObject)',
        'data_process_info': 'list[DataProcessInfo]'
    }

    attribute_map = {
        'compare_task_id': 'compare_task_id',
        'type': 'type',
        'start_time': 'start_time',
        'option': 'option',
        'db_object': 'db_object',
        'data_process_info': 'data_process_info'
    }

    def __init__(self, compare_task_id=None, type=None, start_time=None, option=None, db_object=None, data_process_info=None):
        r"""CompareTaskParams

        The model defined in huaweicloud sdk

        :param compare_task_id: 取消对比任务必填。
        :type compare_task_id: str
        :param type: 对比任务模式。取值： - object：对象对比。 - lines：行数对比。 - contents：内容对比。
        :type type: str
        :param start_time: 定时启动时间，时间戳格式。
        :type start_time: str
        :param option: 对比策略。
        :type option: dict(str, str)
        :param db_object: 对比选择对象。
        :type db_object: dict(str, DatabaseObject)
        :param data_process_info: 更新数据加工规则请求体
        :type data_process_info: list[:class:`huaweicloudsdkdrs.v5.DataProcessInfo`]
        """
        
        

        self._compare_task_id = None
        self._type = None
        self._start_time = None
        self._option = None
        self._db_object = None
        self._data_process_info = None
        self.discriminator = None

        if compare_task_id is not None:
            self.compare_task_id = compare_task_id
        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if option is not None:
            self.option = option
        if db_object is not None:
            self.db_object = db_object
        if data_process_info is not None:
            self.data_process_info = data_process_info

    @property
    def compare_task_id(self):
        r"""Gets the compare_task_id of this CompareTaskParams.

        取消对比任务必填。

        :return: The compare_task_id of this CompareTaskParams.
        :rtype: str
        """
        return self._compare_task_id

    @compare_task_id.setter
    def compare_task_id(self, compare_task_id):
        r"""Sets the compare_task_id of this CompareTaskParams.

        取消对比任务必填。

        :param compare_task_id: The compare_task_id of this CompareTaskParams.
        :type compare_task_id: str
        """
        self._compare_task_id = compare_task_id

    @property
    def type(self):
        r"""Gets the type of this CompareTaskParams.

        对比任务模式。取值： - object：对象对比。 - lines：行数对比。 - contents：内容对比。

        :return: The type of this CompareTaskParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CompareTaskParams.

        对比任务模式。取值： - object：对象对比。 - lines：行数对比。 - contents：内容对比。

        :param type: The type of this CompareTaskParams.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this CompareTaskParams.

        定时启动时间，时间戳格式。

        :return: The start_time of this CompareTaskParams.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CompareTaskParams.

        定时启动时间，时间戳格式。

        :param start_time: The start_time of this CompareTaskParams.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def option(self):
        r"""Gets the option of this CompareTaskParams.

        对比策略。

        :return: The option of this CompareTaskParams.
        :rtype: dict(str, str)
        """
        return self._option

    @option.setter
    def option(self, option):
        r"""Sets the option of this CompareTaskParams.

        对比策略。

        :param option: The option of this CompareTaskParams.
        :type option: dict(str, str)
        """
        self._option = option

    @property
    def db_object(self):
        r"""Gets the db_object of this CompareTaskParams.

        对比选择对象。

        :return: The db_object of this CompareTaskParams.
        :rtype: dict(str, DatabaseObject)
        """
        return self._db_object

    @db_object.setter
    def db_object(self, db_object):
        r"""Sets the db_object of this CompareTaskParams.

        对比选择对象。

        :param db_object: The db_object of this CompareTaskParams.
        :type db_object: dict(str, DatabaseObject)
        """
        self._db_object = db_object

    @property
    def data_process_info(self):
        r"""Gets the data_process_info of this CompareTaskParams.

        更新数据加工规则请求体

        :return: The data_process_info of this CompareTaskParams.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DataProcessInfo`]
        """
        return self._data_process_info

    @data_process_info.setter
    def data_process_info(self, data_process_info):
        r"""Sets the data_process_info of this CompareTaskParams.

        更新数据加工规则请求体

        :param data_process_info: The data_process_info of this CompareTaskParams.
        :type data_process_info: list[:class:`huaweicloudsdkdrs.v5.DataProcessInfo`]
        """
        self._data_process_info = data_process_info

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
        if not isinstance(other, CompareTaskParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
