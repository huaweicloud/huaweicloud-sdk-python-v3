# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDockerRepositoryDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'display_name': 'str',
        'description': 'str',
        'type': 'str'
    }

    attribute_map = {
        'format': 'format',
        'display_name': 'display_name',
        'description': 'description',
        'type': 'type'
    }

    def __init__(self, format=None, display_name=None, description=None, type=None):
        r"""CreateDockerRepositoryDO

        The model defined in huaweicloud sdk

        :param format: 仓库格式
        :type format: str
        :param display_name: 仓库展示名称
        :type display_name: str
        :param description: 仓库描述
        :type description: str
        :param type: 仓库类型
        :type type: str
        """
        
        

        self._format = None
        self._display_name = None
        self._description = None
        self._type = None
        self.discriminator = None

        self.format = format
        self.display_name = display_name
        if description is not None:
            self.description = description
        self.type = type

    @property
    def format(self):
        r"""Gets the format of this CreateDockerRepositoryDO.

        仓库格式

        :return: The format of this CreateDockerRepositoryDO.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this CreateDockerRepositoryDO.

        仓库格式

        :param format: The format of this CreateDockerRepositoryDO.
        :type format: str
        """
        self._format = format

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateDockerRepositoryDO.

        仓库展示名称

        :return: The display_name of this CreateDockerRepositoryDO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateDockerRepositoryDO.

        仓库展示名称

        :param display_name: The display_name of this CreateDockerRepositoryDO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this CreateDockerRepositoryDO.

        仓库描述

        :return: The description of this CreateDockerRepositoryDO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDockerRepositoryDO.

        仓库描述

        :param description: The description of this CreateDockerRepositoryDO.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateDockerRepositoryDO.

        仓库类型

        :return: The type of this CreateDockerRepositoryDO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateDockerRepositoryDO.

        仓库类型

        :param type: The type of this CreateDockerRepositoryDO.
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
        if not isinstance(other, CreateDockerRepositoryDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
