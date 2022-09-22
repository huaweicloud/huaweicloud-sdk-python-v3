# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEventSchemaVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'schema_id': 'str',
        'version': 'int'
    }

    attribute_map = {
        'schema_id': 'schema_id',
        'version': 'version'
    }

    def __init__(self, schema_id=None, version=None):
        """DeleteEventSchemaVersionRequest

        The model defined in huaweicloud sdk

        :param schema_id: 指定查询的事件模型ID
        :type schema_id: str
        :param version: 指定查询的事件模型版本号
        :type version: int
        """
        
        

        self._schema_id = None
        self._version = None
        self.discriminator = None

        self.schema_id = schema_id
        self.version = version

    @property
    def schema_id(self):
        """Gets the schema_id of this DeleteEventSchemaVersionRequest.

        指定查询的事件模型ID

        :return: The schema_id of this DeleteEventSchemaVersionRequest.
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this DeleteEventSchemaVersionRequest.

        指定查询的事件模型ID

        :param schema_id: The schema_id of this DeleteEventSchemaVersionRequest.
        :type schema_id: str
        """
        self._schema_id = schema_id

    @property
    def version(self):
        """Gets the version of this DeleteEventSchemaVersionRequest.

        指定查询的事件模型版本号

        :return: The version of this DeleteEventSchemaVersionRequest.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeleteEventSchemaVersionRequest.

        指定查询的事件模型版本号

        :param version: The version of this DeleteEventSchemaVersionRequest.
        :type version: int
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
        if not isinstance(other, DeleteEventSchemaVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
