# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskRequestBody:

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
        'description': 'str',
        'timing': 'TaskTiming',
        'input': 'TaskInput',
        'output': 'TaskOutput',
        'service_config': 'TaskServiceConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'timing': 'timing',
        'input': 'input',
        'output': 'output',
        'service_config': 'service_config'
    }

    def __init__(self, name=None, description=None, timing=None, input=None, output=None, service_config=None):
        """UpdateTaskRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业的名称，必填。仅能包含汉字、字母、数字、中划线和下划线，长度介于1~100之间。
        :type name: str
        :param description: 作业的描述，选填。长度不超过500。
        :type description: str
        :param timing: 
        :type timing: :class:`huaweicloudsdkvas.v2.TaskTiming`
        :param input: 
        :type input: :class:`huaweicloudsdkvas.v2.TaskInput`
        :param output: 
        :type output: :class:`huaweicloudsdkvas.v2.TaskOutput`
        :param service_config: 
        :type service_config: :class:`huaweicloudsdkvas.v2.TaskServiceConfig`
        """
        
        

        self._name = None
        self._description = None
        self._timing = None
        self._input = None
        self._output = None
        self._service_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if timing is not None:
            self.timing = timing
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if service_config is not None:
            self.service_config = service_config

    @property
    def name(self):
        """Gets the name of this UpdateTaskRequestBody.

        作业的名称，必填。仅能包含汉字、字母、数字、中划线和下划线，长度介于1~100之间。

        :return: The name of this UpdateTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTaskRequestBody.

        作业的名称，必填。仅能包含汉字、字母、数字、中划线和下划线，长度介于1~100之间。

        :param name: The name of this UpdateTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateTaskRequestBody.

        作业的描述，选填。长度不超过500。

        :return: The description of this UpdateTaskRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTaskRequestBody.

        作业的描述，选填。长度不超过500。

        :param description: The description of this UpdateTaskRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def timing(self):
        """Gets the timing of this UpdateTaskRequestBody.

        :return: The timing of this UpdateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskTiming`
        """
        return self._timing

    @timing.setter
    def timing(self, timing):
        """Sets the timing of this UpdateTaskRequestBody.

        :param timing: The timing of this UpdateTaskRequestBody.
        :type timing: :class:`huaweicloudsdkvas.v2.TaskTiming`
        """
        self._timing = timing

    @property
    def input(self):
        """Gets the input of this UpdateTaskRequestBody.

        :return: The input of this UpdateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskInput`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this UpdateTaskRequestBody.

        :param input: The input of this UpdateTaskRequestBody.
        :type input: :class:`huaweicloudsdkvas.v2.TaskInput`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this UpdateTaskRequestBody.

        :return: The output of this UpdateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskOutput`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this UpdateTaskRequestBody.

        :param output: The output of this UpdateTaskRequestBody.
        :type output: :class:`huaweicloudsdkvas.v2.TaskOutput`
        """
        self._output = output

    @property
    def service_config(self):
        """Gets the service_config of this UpdateTaskRequestBody.

        :return: The service_config of this UpdateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskServiceConfig`
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        """Sets the service_config of this UpdateTaskRequestBody.

        :param service_config: The service_config of this UpdateTaskRequestBody.
        :type service_config: :class:`huaweicloudsdkvas.v2.TaskServiceConfig`
        """
        self._service_config = service_config

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
        if not isinstance(other, UpdateTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
