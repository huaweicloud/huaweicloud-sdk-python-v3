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
        'inputs': 'list[Input]',
        'name': 'str',
        'id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'inputs': 'inputs',
        'name': 'name',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, inputs=None, name=None, id=None, type=None):
        """Configs

        The model defined in huaweicloud sdk

        :param inputs: 输入参数列表，列表中的每个参数为“name,value”结构，请参考inputs数据结构参数说明。在“from-config-values”数据结构中，不同的源连接类型有不同的“inputs”参数列表，请参见源端作业参数说明下的章节。在“to-cofig-values”数据结构中，不同的目的连接类型有不同的“inputs”参数列表，请参见目的端作业参数说明下面的子章节。在“driver-config-values”数据结构中，“inputs”具体参数请参见作业任务参数说明。
        :type inputs: list[:class:`huaweicloudsdkcdm.v1.Input`]
        :param name: 配置名称：源端作业的配置名称为“fromJobConfig”。目的端作业的配置名称为“toJobConfig”,连接的配置名称固定为“linkConfig”。
        :type name: str
        :param id: 配置ID
        :type id: int
        :param type: 配置类型
        :type type: str
        """
        
        

        self._inputs = None
        self._name = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.inputs = inputs
        self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def inputs(self):
        """Gets the inputs of this Configs.

        输入参数列表，列表中的每个参数为“name,value”结构，请参考inputs数据结构参数说明。在“from-config-values”数据结构中，不同的源连接类型有不同的“inputs”参数列表，请参见源端作业参数说明下的章节。在“to-cofig-values”数据结构中，不同的目的连接类型有不同的“inputs”参数列表，请参见目的端作业参数说明下面的子章节。在“driver-config-values”数据结构中，“inputs”具体参数请参见作业任务参数说明。

        :return: The inputs of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Input`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Configs.

        输入参数列表，列表中的每个参数为“name,value”结构，请参考inputs数据结构参数说明。在“from-config-values”数据结构中，不同的源连接类型有不同的“inputs”参数列表，请参见源端作业参数说明下的章节。在“to-cofig-values”数据结构中，不同的目的连接类型有不同的“inputs”参数列表，请参见目的端作业参数说明下面的子章节。在“driver-config-values”数据结构中，“inputs”具体参数请参见作业任务参数说明。

        :param inputs: The inputs of this Configs.
        :type inputs: list[:class:`huaweicloudsdkcdm.v1.Input`]
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
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this Configs.

        配置ID

        :return: The id of this Configs.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Configs.

        配置ID

        :param id: The id of this Configs.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Configs.

        配置类型

        :return: The type of this Configs.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Configs.

        配置类型

        :param type: The type of this Configs.
        :type type: str
        """
        self._type = type

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
