# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemParametersResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'parameter_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parameter_name': 'parameter_name',
        'description': 'description'
    }

    def __init__(self, id=None, parameter_name=None, description=None):
        r"""SystemParametersResult

        The model defined in huaweicloud sdk

        :param id: 编号
        :type id: int
        :param parameter_name: 参数名称
        :type parameter_name: str
        :param description: 参数描述
        :type description: str
        """
        
        

        self._id = None
        self._parameter_name = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parameter_name is not None:
            self.parameter_name = parameter_name
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this SystemParametersResult.

        编号

        :return: The id of this SystemParametersResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SystemParametersResult.

        编号

        :param id: The id of this SystemParametersResult.
        :type id: int
        """
        self._id = id

    @property
    def parameter_name(self):
        r"""Gets the parameter_name of this SystemParametersResult.

        参数名称

        :return: The parameter_name of this SystemParametersResult.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        r"""Sets the parameter_name of this SystemParametersResult.

        参数名称

        :param parameter_name: The parameter_name of this SystemParametersResult.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def description(self):
        r"""Gets the description of this SystemParametersResult.

        参数描述

        :return: The description of this SystemParametersResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SystemParametersResult.

        参数描述

        :param description: The description of this SystemParametersResult.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, SystemParametersResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
