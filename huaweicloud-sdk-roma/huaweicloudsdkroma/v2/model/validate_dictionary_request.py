# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateDictionaryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'name': 'str',
        'code': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'code': 'code'
    }

    def __init__(self, instance_id=None, name=None, code=None):
        """ValidateDictionaryRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param name: 待校验是否重复的字典名称，精确匹配
        :type name: str
        :param code: 待校验是否重复的字典编码，精确匹配
        :type code: str
        """
        
        

        self._instance_id = None
        self._name = None
        self._code = None
        self.discriminator = None

        self.instance_id = instance_id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code

    @property
    def instance_id(self):
        """Gets the instance_id of this ValidateDictionaryRequest.

        实例ID

        :return: The instance_id of this ValidateDictionaryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ValidateDictionaryRequest.

        实例ID

        :param instance_id: The instance_id of this ValidateDictionaryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this ValidateDictionaryRequest.

        待校验是否重复的字典名称，精确匹配

        :return: The name of this ValidateDictionaryRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ValidateDictionaryRequest.

        待校验是否重复的字典名称，精确匹配

        :param name: The name of this ValidateDictionaryRequest.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        """Gets the code of this ValidateDictionaryRequest.

        待校验是否重复的字典编码，精确匹配

        :return: The code of this ValidateDictionaryRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ValidateDictionaryRequest.

        待校验是否重复的字典编码，精确匹配

        :param code: The code of this ValidateDictionaryRequest.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, ValidateDictionaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
