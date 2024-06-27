# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBasicAwReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'dft_check_point_list': 'list[CheckPoint]',
        'dft_custom_header': 'list[AwParam]',
        'dft_retry_interval': 'str',
        'dft_retry_times': 'str',
        'dft_variable_list': 'list[AwVariable]',
        'name': 'str',
        'param_type_and_dft_value': 'list[AwParam]'
    }

    attribute_map = {
        'description': 'description',
        'dft_check_point_list': 'dft_check_point_list',
        'dft_custom_header': 'dft_custom_header',
        'dft_retry_interval': 'dft_retry_interval',
        'dft_retry_times': 'dft_retry_times',
        'dft_variable_list': 'dft_variable_list',
        'name': 'name',
        'param_type_and_dft_value': 'param_type_and_dft_value'
    }

    def __init__(self, description=None, dft_check_point_list=None, dft_custom_header=None, dft_retry_interval=None, dft_retry_times=None, dft_variable_list=None, name=None, param_type_and_dft_value=None):
        """UpdateBasicAwReq

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param dft_check_point_list: 默认检查点List
        :type dft_check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        :param dft_custom_header: AW参数类list
        :type dft_custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        :param dft_retry_interval: 重试间隔时间 (ms) 为空表示不等待(目前内部使用)
        :type dft_retry_interval: str
        :param dft_retry_times: 重试次数(目前内部使用)
        :type dft_retry_times: str
        :param dft_variable_list: 定义的变量信息
        :type dft_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        :param name: 名称
        :type name: str
        :param param_type_and_dft_value: 参数类型和参数默认值对应List
        :type param_type_and_dft_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        
        

        self._description = None
        self._dft_check_point_list = None
        self._dft_custom_header = None
        self._dft_retry_interval = None
        self._dft_retry_times = None
        self._dft_variable_list = None
        self._name = None
        self._param_type_and_dft_value = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if dft_check_point_list is not None:
            self.dft_check_point_list = dft_check_point_list
        if dft_custom_header is not None:
            self.dft_custom_header = dft_custom_header
        if dft_retry_interval is not None:
            self.dft_retry_interval = dft_retry_interval
        if dft_retry_times is not None:
            self.dft_retry_times = dft_retry_times
        if dft_variable_list is not None:
            self.dft_variable_list = dft_variable_list
        if name is not None:
            self.name = name
        if param_type_and_dft_value is not None:
            self.param_type_and_dft_value = param_type_and_dft_value

    @property
    def description(self):
        """Gets the description of this UpdateBasicAwReq.

        描述

        :return: The description of this UpdateBasicAwReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateBasicAwReq.

        描述

        :param description: The description of this UpdateBasicAwReq.
        :type description: str
        """
        self._description = description

    @property
    def dft_check_point_list(self):
        """Gets the dft_check_point_list of this UpdateBasicAwReq.

        默认检查点List

        :return: The dft_check_point_list of this UpdateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        return self._dft_check_point_list

    @dft_check_point_list.setter
    def dft_check_point_list(self, dft_check_point_list):
        """Sets the dft_check_point_list of this UpdateBasicAwReq.

        默认检查点List

        :param dft_check_point_list: The dft_check_point_list of this UpdateBasicAwReq.
        :type dft_check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        self._dft_check_point_list = dft_check_point_list

    @property
    def dft_custom_header(self):
        """Gets the dft_custom_header of this UpdateBasicAwReq.

        AW参数类list

        :return: The dft_custom_header of this UpdateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._dft_custom_header

    @dft_custom_header.setter
    def dft_custom_header(self, dft_custom_header):
        """Sets the dft_custom_header of this UpdateBasicAwReq.

        AW参数类list

        :param dft_custom_header: The dft_custom_header of this UpdateBasicAwReq.
        :type dft_custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._dft_custom_header = dft_custom_header

    @property
    def dft_retry_interval(self):
        """Gets the dft_retry_interval of this UpdateBasicAwReq.

        重试间隔时间 (ms) 为空表示不等待(目前内部使用)

        :return: The dft_retry_interval of this UpdateBasicAwReq.
        :rtype: str
        """
        return self._dft_retry_interval

    @dft_retry_interval.setter
    def dft_retry_interval(self, dft_retry_interval):
        """Sets the dft_retry_interval of this UpdateBasicAwReq.

        重试间隔时间 (ms) 为空表示不等待(目前内部使用)

        :param dft_retry_interval: The dft_retry_interval of this UpdateBasicAwReq.
        :type dft_retry_interval: str
        """
        self._dft_retry_interval = dft_retry_interval

    @property
    def dft_retry_times(self):
        """Gets the dft_retry_times of this UpdateBasicAwReq.

        重试次数(目前内部使用)

        :return: The dft_retry_times of this UpdateBasicAwReq.
        :rtype: str
        """
        return self._dft_retry_times

    @dft_retry_times.setter
    def dft_retry_times(self, dft_retry_times):
        """Sets the dft_retry_times of this UpdateBasicAwReq.

        重试次数(目前内部使用)

        :param dft_retry_times: The dft_retry_times of this UpdateBasicAwReq.
        :type dft_retry_times: str
        """
        self._dft_retry_times = dft_retry_times

    @property
    def dft_variable_list(self):
        """Gets the dft_variable_list of this UpdateBasicAwReq.

        定义的变量信息

        :return: The dft_variable_list of this UpdateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._dft_variable_list

    @dft_variable_list.setter
    def dft_variable_list(self, dft_variable_list):
        """Sets the dft_variable_list of this UpdateBasicAwReq.

        定义的变量信息

        :param dft_variable_list: The dft_variable_list of this UpdateBasicAwReq.
        :type dft_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._dft_variable_list = dft_variable_list

    @property
    def name(self):
        """Gets the name of this UpdateBasicAwReq.

        名称

        :return: The name of this UpdateBasicAwReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateBasicAwReq.

        名称

        :param name: The name of this UpdateBasicAwReq.
        :type name: str
        """
        self._name = name

    @property
    def param_type_and_dft_value(self):
        """Gets the param_type_and_dft_value of this UpdateBasicAwReq.

        参数类型和参数默认值对应List

        :return: The param_type_and_dft_value of this UpdateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._param_type_and_dft_value

    @param_type_and_dft_value.setter
    def param_type_and_dft_value(self, param_type_and_dft_value):
        """Sets the param_type_and_dft_value of this UpdateBasicAwReq.

        参数类型和参数默认值对应List

        :param param_type_and_dft_value: The param_type_and_dft_value of this UpdateBasicAwReq.
        :type param_type_and_dft_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._param_type_and_dft_value = param_type_and_dft_value

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
        if not isinstance(other, UpdateBasicAwReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
