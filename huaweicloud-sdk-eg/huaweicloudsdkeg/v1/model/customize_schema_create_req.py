# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeSchemaCreateReq:

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
        'compatibility': 'str',
        'format': 'str',
        'data_sample': 'str',
        'definition': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'compatibility': 'compatibility',
        'format': 'format',
        'data_sample': 'data_sample',
        'definition': 'definition'
    }

    def __init__(self, name=None, description=None, compatibility=None, format=None, data_sample=None, definition=None):
        """CustomizeSchemaCreateReq

        The model defined in huaweicloud sdk

        :param name: 事件模型名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头
        :type name: str
        :param description: 事件模型描述
        :type description: str
        :param compatibility: 事件模型兼容性
        :type compatibility: str
        :param format: schema内容格式
        :type format: str
        :param data_sample: 事件示例
        :type data_sample: str
        :param definition: 事件模型内容定义
        :type definition: str
        """
        
        

        self._name = None
        self._description = None
        self._compatibility = None
        self._format = None
        self._data_sample = None
        self._definition = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.compatibility = compatibility
        if format is not None:
            self.format = format
        if data_sample is not None:
            self.data_sample = data_sample
        self.definition = definition

    @property
    def name(self):
        """Gets the name of this CustomizeSchemaCreateReq.

        事件模型名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :return: The name of this CustomizeSchemaCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomizeSchemaCreateReq.

        事件模型名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :param name: The name of this CustomizeSchemaCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CustomizeSchemaCreateReq.

        事件模型描述

        :return: The description of this CustomizeSchemaCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomizeSchemaCreateReq.

        事件模型描述

        :param description: The description of this CustomizeSchemaCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def compatibility(self):
        """Gets the compatibility of this CustomizeSchemaCreateReq.

        事件模型兼容性

        :return: The compatibility of this CustomizeSchemaCreateReq.
        :rtype: str
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        """Sets the compatibility of this CustomizeSchemaCreateReq.

        事件模型兼容性

        :param compatibility: The compatibility of this CustomizeSchemaCreateReq.
        :type compatibility: str
        """
        self._compatibility = compatibility

    @property
    def format(self):
        """Gets the format of this CustomizeSchemaCreateReq.

        schema内容格式

        :return: The format of this CustomizeSchemaCreateReq.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CustomizeSchemaCreateReq.

        schema内容格式

        :param format: The format of this CustomizeSchemaCreateReq.
        :type format: str
        """
        self._format = format

    @property
    def data_sample(self):
        """Gets the data_sample of this CustomizeSchemaCreateReq.

        事件示例

        :return: The data_sample of this CustomizeSchemaCreateReq.
        :rtype: str
        """
        return self._data_sample

    @data_sample.setter
    def data_sample(self, data_sample):
        """Sets the data_sample of this CustomizeSchemaCreateReq.

        事件示例

        :param data_sample: The data_sample of this CustomizeSchemaCreateReq.
        :type data_sample: str
        """
        self._data_sample = data_sample

    @property
    def definition(self):
        """Gets the definition of this CustomizeSchemaCreateReq.

        事件模型内容定义

        :return: The definition of this CustomizeSchemaCreateReq.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this CustomizeSchemaCreateReq.

        事件模型内容定义

        :param definition: The definition of this CustomizeSchemaCreateReq.
        :type definition: str
        """
        self._definition = definition

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
        if not isinstance(other, CustomizeSchemaCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
