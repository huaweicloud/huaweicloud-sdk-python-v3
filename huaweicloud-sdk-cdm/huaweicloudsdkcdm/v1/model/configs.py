# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Configs:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'inputs': 'list[object]',
        'name': 'str'
    }

    attribute_map = {
        'inputs': 'inputs',
        'name': 'name'
    }

    def __init__(self, inputs=None, name=None):
        """Configs - a model defined in huaweicloud sdk"""
        
        

        self._inputs = None
        self._name = None
        self.discriminator = None

        self.inputs = inputs
        self.name = name

    @property
    def inputs(self):
        """Gets the inputs of this Configs.


        :return: The inputs of this Configs.
        :rtype: list[object]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Configs.


        :param inputs: The inputs of this Configs.
        :type: list[object]
        """
        self._inputs = inputs

    @property
    def name(self):
        """Gets the name of this Configs.

        配置名称：源端作业的配置名称为“fromJobConfig”。目的端作业的配置名称为“toJobConfig”,连接的配置名称固定为“linkConfig”。

        :return: The name of this Configs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Configs.

        配置名称：源端作业的配置名称为“fromJobConfig”。目的端作业的配置名称为“toJobConfig”,连接的配置名称固定为“linkConfig”。

        :param name: The name of this Configs.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, Configs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other