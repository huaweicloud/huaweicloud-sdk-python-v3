# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelVersionInput:

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
        'config': 'ModelConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'config': 'config'
    }

    def __init__(self, name=None, description=None, config=None):
        r"""ModelVersionInput

        The model defined in huaweicloud sdk

        :param name: 模型版本名称, 只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param config: 
        :type config: :class:`huaweicloudsdkdataartsfabric.v1.ModelConfig`
        """
        
        

        self._name = None
        self._description = None
        self._config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if config is not None:
            self.config = config

    @property
    def name(self):
        r"""Gets the name of this ModelVersionInput.

        模型版本名称, 只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this ModelVersionInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelVersionInput.

        模型版本名称, 只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this ModelVersionInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModelVersionInput.

        描述信息

        :return: The description of this ModelVersionInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelVersionInput.

        描述信息

        :param description: The description of this ModelVersionInput.
        :type description: str
        """
        self._description = description

    @property
    def config(self):
        r"""Gets the config of this ModelVersionInput.

        :return: The config of this ModelVersionInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ModelConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this ModelVersionInput.

        :param config: The config of this ModelVersionInput.
        :type config: :class:`huaweicloudsdkdataartsfabric.v1.ModelConfig`
        """
        self._config = config

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
        if not isinstance(other, ModelVersionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
