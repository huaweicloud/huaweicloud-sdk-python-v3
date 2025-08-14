# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseSchemaSubjectDetailsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_id_format': 'str',
        'include': 'str'
    }

    attribute_map = {
        'name_id_format': 'name_id_format',
        'include': 'include'
    }

    def __init__(self, name_id_format=None, include=None):
        r"""ResponseSchemaSubjectDetailsDto

        The model defined in huaweicloud sdk

        :param name_id_format: NameID的格式
        :type name_id_format: str
        :param include: 是否包含NameID
        :type include: str
        """
        
        

        self._name_id_format = None
        self._include = None
        self.discriminator = None

        self.name_id_format = name_id_format
        self.include = include

    @property
    def name_id_format(self):
        r"""Gets the name_id_format of this ResponseSchemaSubjectDetailsDto.

        NameID的格式

        :return: The name_id_format of this ResponseSchemaSubjectDetailsDto.
        :rtype: str
        """
        return self._name_id_format

    @name_id_format.setter
    def name_id_format(self, name_id_format):
        r"""Sets the name_id_format of this ResponseSchemaSubjectDetailsDto.

        NameID的格式

        :param name_id_format: The name_id_format of this ResponseSchemaSubjectDetailsDto.
        :type name_id_format: str
        """
        self._name_id_format = name_id_format

    @property
    def include(self):
        r"""Gets the include of this ResponseSchemaSubjectDetailsDto.

        是否包含NameID

        :return: The include of this ResponseSchemaSubjectDetailsDto.
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        r"""Sets the include of this ResponseSchemaSubjectDetailsDto.

        是否包含NameID

        :param include: The include of this ResponseSchemaSubjectDetailsDto.
        :type include: str
        """
        self._include = include

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
        if not isinstance(other, ResponseSchemaSubjectDetailsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
