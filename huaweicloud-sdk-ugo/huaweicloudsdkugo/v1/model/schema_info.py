# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchemaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_select_all_schemas': 'bool',
        'schemas_list': 'list[str]'
    }

    attribute_map = {
        'is_select_all_schemas': 'is_select_all_schemas',
        'schemas_list': 'schemas_list'
    }

    def __init__(self, is_select_all_schemas=None, schemas_list=None):
        """SchemaInfo

        The model defined in huaweicloud sdk

        :param is_select_all_schemas: 是否选择全部schema。
        :type is_select_all_schemas: bool
        :param schemas_list: 需要评估的源库schema列表。is_select_all_schemas为false时，必填。
        :type schemas_list: list[str]
        """
        
        

        self._is_select_all_schemas = None
        self._schemas_list = None
        self.discriminator = None

        self.is_select_all_schemas = is_select_all_schemas
        if schemas_list is not None:
            self.schemas_list = schemas_list

    @property
    def is_select_all_schemas(self):
        """Gets the is_select_all_schemas of this SchemaInfo.

        是否选择全部schema。

        :return: The is_select_all_schemas of this SchemaInfo.
        :rtype: bool
        """
        return self._is_select_all_schemas

    @is_select_all_schemas.setter
    def is_select_all_schemas(self, is_select_all_schemas):
        """Sets the is_select_all_schemas of this SchemaInfo.

        是否选择全部schema。

        :param is_select_all_schemas: The is_select_all_schemas of this SchemaInfo.
        :type is_select_all_schemas: bool
        """
        self._is_select_all_schemas = is_select_all_schemas

    @property
    def schemas_list(self):
        """Gets the schemas_list of this SchemaInfo.

        需要评估的源库schema列表。is_select_all_schemas为false时，必填。

        :return: The schemas_list of this SchemaInfo.
        :rtype: list[str]
        """
        return self._schemas_list

    @schemas_list.setter
    def schemas_list(self, schemas_list):
        """Sets the schemas_list of this SchemaInfo.

        需要评估的源库schema列表。is_select_all_schemas为false时，必填。

        :param schemas_list: The schemas_list of this SchemaInfo.
        :type schemas_list: list[str]
        """
        self._schemas_list = schemas_list

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
        if not isinstance(other, SchemaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
