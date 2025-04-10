# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelInput:

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
        'type': 'ModelType',
        'version': 'ModelVersionInput'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, name=None, description=None, type=None, version=None):
        r"""CreateModelInput

        The model defined in huaweicloud sdk

        :param name: 一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.ModelType`
        :param version: 
        :type version: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInput`
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._version = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.version = version

    @property
    def name(self):
        r"""Gets the name of this CreateModelInput.

        一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this CreateModelInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelInput.

        一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this CreateModelInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateModelInput.

        描述信息

        :return: The description of this CreateModelInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelInput.

        描述信息

        :param description: The description of this CreateModelInput.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateModelInput.

        :return: The type of this CreateModelInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ModelType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateModelInput.

        :param type: The type of this CreateModelInput.
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.ModelType`
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this CreateModelInput.

        :return: The version of this CreateModelInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInput`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateModelInput.

        :param version: The version of this CreateModelInput.
        :type version: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInput`
        """
        self._version = version

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
        if not isinstance(other, CreateModelInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
