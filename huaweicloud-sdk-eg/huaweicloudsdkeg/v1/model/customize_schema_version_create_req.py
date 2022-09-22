# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeSchemaVersionCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data_sample': 'str',
        'definition': 'str'
    }

    attribute_map = {
        'data_sample': 'data_sample',
        'definition': 'definition'
    }

    def __init__(self, data_sample=None, definition=None):
        """CustomizeSchemaVersionCreateReq

        The model defined in huaweicloud sdk

        :param data_sample: 事件示例
        :type data_sample: str
        :param definition: 事件模型内容定义
        :type definition: str
        """
        
        

        self._data_sample = None
        self._definition = None
        self.discriminator = None

        if data_sample is not None:
            self.data_sample = data_sample
        if definition is not None:
            self.definition = definition

    @property
    def data_sample(self):
        """Gets the data_sample of this CustomizeSchemaVersionCreateReq.

        事件示例

        :return: The data_sample of this CustomizeSchemaVersionCreateReq.
        :rtype: str
        """
        return self._data_sample

    @data_sample.setter
    def data_sample(self, data_sample):
        """Sets the data_sample of this CustomizeSchemaVersionCreateReq.

        事件示例

        :param data_sample: The data_sample of this CustomizeSchemaVersionCreateReq.
        :type data_sample: str
        """
        self._data_sample = data_sample

    @property
    def definition(self):
        """Gets the definition of this CustomizeSchemaVersionCreateReq.

        事件模型内容定义

        :return: The definition of this CustomizeSchemaVersionCreateReq.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this CustomizeSchemaVersionCreateReq.

        事件模型内容定义

        :param definition: The definition of this CustomizeSchemaVersionCreateReq.
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
        if not isinstance(other, CustomizeSchemaVersionCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
