# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Step:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'params': 'dict(str, str)',
        'enable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'params': 'params',
        'enable': 'enable'
    }

    def __init__(self, id=None, name=None, params=None, enable=None):
        """Step

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param name: 名称
        :type name: str
        :param params: 参数
        :type params: dict(str, str)
        :param enable: 是否开启
        :type enable: bool
        """
        
        

        self._id = None
        self._name = None
        self._params = None
        self._enable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if params is not None:
            self.params = params
        if enable is not None:
            self.enable = enable

    @property
    def id(self):
        """Gets the id of this Step.

        id

        :return: The id of this Step.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Step.

        id

        :param id: The id of this Step.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Step.

        名称

        :return: The name of this Step.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Step.

        名称

        :param name: The name of this Step.
        :type name: str
        """
        self._name = name

    @property
    def params(self):
        """Gets the params of this Step.

        参数

        :return: The params of this Step.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Step.

        参数

        :param params: The params of this Step.
        :type params: dict(str, str)
        """
        self._params = params

    @property
    def enable(self):
        """Gets the enable of this Step.

        是否开启

        :return: The enable of this Step.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this Step.

        是否开启

        :param enable: The enable of this Step.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, Step):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
