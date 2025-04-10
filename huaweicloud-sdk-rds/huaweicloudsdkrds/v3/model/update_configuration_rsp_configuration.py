# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConfigurationRspConfiguration:

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
        'ignored_params': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ignored_params': 'ignored_params'
    }

    def __init__(self, id=None, name=None, ignored_params=None):
        r"""UpdateConfigurationRspConfiguration

        The model defined in huaweicloud sdk

        :param id: 参数模板ID。
        :type id: str
        :param name: 参数模板名称。
        :type name: str
        :param ignored_params: 请求参数“values”中被忽略掉，没有生效的参数名称列表。 当参数不存在时，参数修改不会下发，并通过此参数返回所有被忽略的参数名称。
        :type ignored_params: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._ignored_params = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ignored_params is not None:
            self.ignored_params = ignored_params

    @property
    def id(self):
        r"""Gets the id of this UpdateConfigurationRspConfiguration.

        参数模板ID。

        :return: The id of this UpdateConfigurationRspConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateConfigurationRspConfiguration.

        参数模板ID。

        :param id: The id of this UpdateConfigurationRspConfiguration.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateConfigurationRspConfiguration.

        参数模板名称。

        :return: The name of this UpdateConfigurationRspConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateConfigurationRspConfiguration.

        参数模板名称。

        :param name: The name of this UpdateConfigurationRspConfiguration.
        :type name: str
        """
        self._name = name

    @property
    def ignored_params(self):
        r"""Gets the ignored_params of this UpdateConfigurationRspConfiguration.

        请求参数“values”中被忽略掉，没有生效的参数名称列表。 当参数不存在时，参数修改不会下发，并通过此参数返回所有被忽略的参数名称。

        :return: The ignored_params of this UpdateConfigurationRspConfiguration.
        :rtype: list[str]
        """
        return self._ignored_params

    @ignored_params.setter
    def ignored_params(self, ignored_params):
        r"""Sets the ignored_params of this UpdateConfigurationRspConfiguration.

        请求参数“values”中被忽略掉，没有生效的参数名称列表。 当参数不存在时，参数修改不会下发，并通过此参数返回所有被忽略的参数名称。

        :param ignored_params: The ignored_params of this UpdateConfigurationRspConfiguration.
        :type ignored_params: list[str]
        """
        self._ignored_params = ignored_params

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
        if not isinstance(other, UpdateConfigurationRspConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
