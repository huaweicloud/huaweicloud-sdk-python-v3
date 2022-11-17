# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskParameterDto:

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
        'source': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'source': 'source',
        'values': 'values'
    }

    def __init__(self, name=None, source=None, values=None):
        """TaskParameterDto

        The model defined in huaweicloud sdk

        :param name: 子任务的参数名称，长度为[1,32]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。需要和已有应用的参数名称一致。
        :type name: str
        :param source: 子任务的参数类型，不填默认为MANUAL
        :type source: str
        :param values: 子任务的参数数值，根据参数类型进行合法性校验
        :type values: list[str]
        """
        
        

        self._name = None
        self._source = None
        self._values = None
        self.discriminator = None

        self.name = name
        if source is not None:
            self.source = source
        if values is not None:
            self.values = values

    @property
    def name(self):
        """Gets the name of this TaskParameterDto.

        子任务的参数名称，长度为[1,32]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。需要和已有应用的参数名称一致。

        :return: The name of this TaskParameterDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskParameterDto.

        子任务的参数名称，长度为[1,32]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。需要和已有应用的参数名称一致。

        :param name: The name of this TaskParameterDto.
        :type name: str
        """
        self._name = name

    @property
    def source(self):
        """Gets the source of this TaskParameterDto.

        子任务的参数类型，不填默认为MANUAL

        :return: The source of this TaskParameterDto.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TaskParameterDto.

        子任务的参数类型，不填默认为MANUAL

        :param source: The source of this TaskParameterDto.
        :type source: str
        """
        self._source = source

    @property
    def values(self):
        """Gets the values of this TaskParameterDto.

        子任务的参数数值，根据参数类型进行合法性校验

        :return: The values of this TaskParameterDto.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TaskParameterDto.

        子任务的参数数值，根据参数类型进行合法性校验

        :param values: The values of this TaskParameterDto.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, TaskParameterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
