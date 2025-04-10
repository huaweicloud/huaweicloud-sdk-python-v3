# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_json': 'object',
        'input_url': 'str',
        'output_url': 'str'
    }

    attribute_map = {
        'input_json': 'input_json',
        'input_url': 'input_url',
        'output_url': 'output_url'
    }

    def __init__(self, input_json=None, input_url=None, output_url=None):
        r"""TaskDto

        The model defined in huaweicloud sdk

        :param input_json: 任务输入信息，json格式；每个子服务该对象结构不同，框架层不解析具体key，运行态直接透传给子服务REST API处理（参数合法性校验 只能子服务镜像内进行；当前算法镜像提供单独校验接口和处理接口，后续待统一交互机制）
        :type input_json: object
        :param input_url: 任务输入信息为文件格式，传入值为租户OBS对应的文件绝对路径；在请求信息大于12MB情形使用该参数，需用户在Console进行OBS委托授权方可使用（和input_json二选一），暂不开放该功能
        :type input_url: str
        :param output_url: 任务输出信息为文件格式，传入值为租户OBS对应的待存储路径前缀（和input_url成对使用），文件名服务端固定用task_id命名；在响应信息大于12MB情形使用该参数，需用户在Console进行OBS委托授权方可使用，暂不开放该功能
        :type output_url: str
        """
        
        

        self._input_json = None
        self._input_url = None
        self._output_url = None
        self.discriminator = None

        self.input_json = input_json
        if input_url is not None:
            self.input_url = input_url
        if output_url is not None:
            self.output_url = output_url

    @property
    def input_json(self):
        r"""Gets the input_json of this TaskDto.

        任务输入信息，json格式；每个子服务该对象结构不同，框架层不解析具体key，运行态直接透传给子服务REST API处理（参数合法性校验 只能子服务镜像内进行；当前算法镜像提供单独校验接口和处理接口，后续待统一交互机制）

        :return: The input_json of this TaskDto.
        :rtype: object
        """
        return self._input_json

    @input_json.setter
    def input_json(self, input_json):
        r"""Sets the input_json of this TaskDto.

        任务输入信息，json格式；每个子服务该对象结构不同，框架层不解析具体key，运行态直接透传给子服务REST API处理（参数合法性校验 只能子服务镜像内进行；当前算法镜像提供单独校验接口和处理接口，后续待统一交互机制）

        :param input_json: The input_json of this TaskDto.
        :type input_json: object
        """
        self._input_json = input_json

    @property
    def input_url(self):
        r"""Gets the input_url of this TaskDto.

        任务输入信息为文件格式，传入值为租户OBS对应的文件绝对路径；在请求信息大于12MB情形使用该参数，需用户在Console进行OBS委托授权方可使用（和input_json二选一），暂不开放该功能

        :return: The input_url of this TaskDto.
        :rtype: str
        """
        return self._input_url

    @input_url.setter
    def input_url(self, input_url):
        r"""Sets the input_url of this TaskDto.

        任务输入信息为文件格式，传入值为租户OBS对应的文件绝对路径；在请求信息大于12MB情形使用该参数，需用户在Console进行OBS委托授权方可使用（和input_json二选一），暂不开放该功能

        :param input_url: The input_url of this TaskDto.
        :type input_url: str
        """
        self._input_url = input_url

    @property
    def output_url(self):
        r"""Gets the output_url of this TaskDto.

        任务输出信息为文件格式，传入值为租户OBS对应的待存储路径前缀（和input_url成对使用），文件名服务端固定用task_id命名；在响应信息大于12MB情形使用该参数，需用户在Console进行OBS委托授权方可使用，暂不开放该功能

        :return: The output_url of this TaskDto.
        :rtype: str
        """
        return self._output_url

    @output_url.setter
    def output_url(self, output_url):
        r"""Sets the output_url of this TaskDto.

        任务输出信息为文件格式，传入值为租户OBS对应的待存储路径前缀（和input_url成对使用），文件名服务端固定用task_id命名；在响应信息大于12MB情形使用该参数，需用户在Console进行OBS委托授权方可使用，暂不开放该功能

        :param output_url: The output_url of this TaskDto.
        :type output_url: str
        """
        self._output_url = output_url

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
        if not isinstance(other, TaskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
