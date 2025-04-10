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
        'input_json': 'object'
    }

    attribute_map = {
        'input_json': 'input_json'
    }

    def __init__(self, input_json=None):
        r"""TaskDto

        The model defined in huaweicloud sdk

        :param input_json: 任务输入信息，json格式；每个子服务该对象结构不同，框架层不解析具体key，运行态直接透传给子服务REST API处理（参数合法性校验 只能子服务镜像内进行；当前算法镜像提供单独校验接口和处理接口，后续待统一交互机制）
        :type input_json: object
        """
        
        

        self._input_json = None
        self.discriminator = None

        self.input_json = input_json

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
