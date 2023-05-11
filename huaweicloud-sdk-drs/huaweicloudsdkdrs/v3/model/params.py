# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Params:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_result': 'str',
        'data_type': 'str',
        'group': 'str',
        'key': 'str',
        'need_restart': 'str',
        'source_value': 'str',
        'target_value': 'str',
        'value_range': 'str',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'compare_result': 'compare_result',
        'data_type': 'data_type',
        'group': 'group',
        'key': 'key',
        'need_restart': 'need_restart',
        'source_value': 'source_value',
        'target_value': 'target_value',
        'value_range': 'value_range',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, compare_result=None, data_type=None, group=None, key=None, need_restart=None, source_value=None, target_value=None, value_range=None, error_code=None, error_message=None):
        """Params

        The model defined in huaweicloud sdk

        :param compare_result: 参数对比结果
        :type compare_result: str
        :param data_type: 参数类型
        :type data_type: str
        :param group: 分组。 - common-常规参数 - performance-性能参数
        :type group: str
        :param key: 参数名
        :type key: str
        :param need_restart: 是否需要重启
        :type need_restart: str
        :param source_value: 源数据库参数值
        :type source_value: str
        :param target_value: 目标数据库参数值
        :type target_value: str
        :param value_range: 参数范围
        :type value_range: str
        :param error_code: 错误码
        :type error_code: str
        :param error_message: 错误信息
        :type error_message: str
        """
        
        

        self._compare_result = None
        self._data_type = None
        self._group = None
        self._key = None
        self._need_restart = None
        self._source_value = None
        self._target_value = None
        self._value_range = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if compare_result is not None:
            self.compare_result = compare_result
        if data_type is not None:
            self.data_type = data_type
        if group is not None:
            self.group = group
        if key is not None:
            self.key = key
        if need_restart is not None:
            self.need_restart = need_restart
        if source_value is not None:
            self.source_value = source_value
        if target_value is not None:
            self.target_value = target_value
        if value_range is not None:
            self.value_range = value_range
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def compare_result(self):
        """Gets the compare_result of this Params.

        参数对比结果

        :return: The compare_result of this Params.
        :rtype: str
        """
        return self._compare_result

    @compare_result.setter
    def compare_result(self, compare_result):
        """Sets the compare_result of this Params.

        参数对比结果

        :param compare_result: The compare_result of this Params.
        :type compare_result: str
        """
        self._compare_result = compare_result

    @property
    def data_type(self):
        """Gets the data_type of this Params.

        参数类型

        :return: The data_type of this Params.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Params.

        参数类型

        :param data_type: The data_type of this Params.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def group(self):
        """Gets the group of this Params.

        分组。 - common-常规参数 - performance-性能参数

        :return: The group of this Params.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Params.

        分组。 - common-常规参数 - performance-性能参数

        :param group: The group of this Params.
        :type group: str
        """
        self._group = group

    @property
    def key(self):
        """Gets the key of this Params.

        参数名

        :return: The key of this Params.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Params.

        参数名

        :param key: The key of this Params.
        :type key: str
        """
        self._key = key

    @property
    def need_restart(self):
        """Gets the need_restart of this Params.

        是否需要重启

        :return: The need_restart of this Params.
        :rtype: str
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        """Sets the need_restart of this Params.

        是否需要重启

        :param need_restart: The need_restart of this Params.
        :type need_restart: str
        """
        self._need_restart = need_restart

    @property
    def source_value(self):
        """Gets the source_value of this Params.

        源数据库参数值

        :return: The source_value of this Params.
        :rtype: str
        """
        return self._source_value

    @source_value.setter
    def source_value(self, source_value):
        """Sets the source_value of this Params.

        源数据库参数值

        :param source_value: The source_value of this Params.
        :type source_value: str
        """
        self._source_value = source_value

    @property
    def target_value(self):
        """Gets the target_value of this Params.

        目标数据库参数值

        :return: The target_value of this Params.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this Params.

        目标数据库参数值

        :param target_value: The target_value of this Params.
        :type target_value: str
        """
        self._target_value = target_value

    @property
    def value_range(self):
        """Gets the value_range of this Params.

        参数范围

        :return: The value_range of this Params.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this Params.

        参数范围

        :param value_range: The value_range of this Params.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def error_code(self):
        """Gets the error_code of this Params.

        错误码

        :return: The error_code of this Params.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Params.

        错误码

        :param error_code: The error_code of this Params.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this Params.

        错误信息

        :return: The error_message of this Params.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this Params.

        错误信息

        :param error_message: The error_message of this Params.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
