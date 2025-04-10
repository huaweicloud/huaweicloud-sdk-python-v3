# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchemasList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'schema_name': 'schema_name',
        'description': 'description'
    }

    def __init__(self, schema_name=None, description=None):
        r"""SchemasList

        The model defined in huaweicloud sdk

        :param schema_name: schema名称
        :type schema_name: str
        :param description: schema描述
        :type description: str
        """
        
        

        self._schema_name = None
        self._description = None
        self.discriminator = None

        if schema_name is not None:
            self.schema_name = schema_name
        if description is not None:
            self.description = description

    @property
    def schema_name(self):
        r"""Gets the schema_name of this SchemasList.

        schema名称

        :return: The schema_name of this SchemasList.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this SchemasList.

        schema名称

        :param schema_name: The schema_name of this SchemasList.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def description(self):
        r"""Gets the description of this SchemasList.

        schema描述

        :return: The description of this SchemasList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SchemasList.

        schema描述

        :param description: The description of this SchemasList.
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
        if not isinstance(other, SchemasList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
