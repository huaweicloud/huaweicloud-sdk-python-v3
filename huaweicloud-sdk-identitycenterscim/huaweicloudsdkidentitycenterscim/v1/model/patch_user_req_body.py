# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchUserReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schemas': 'list[str]',
        'operations': 'list[OperationItemDto]'
    }

    attribute_map = {
        'schemas': 'schemas',
        'operations': 'Operations'
    }

    def __init__(self, schemas=None, operations=None):
        """PatchUserReqBody

        The model defined in huaweicloud sdk

        :param schemas: 概要
        :type schemas: list[str]
        :param operations: 要执行的修改操作列表
        :type operations: list[:class:`huaweicloudsdkidentitycenterscim.v1.OperationItemDto`]
        """
        
        

        self._schemas = None
        self._operations = None
        self.discriminator = None

        self.schemas = schemas
        self.operations = operations

    @property
    def schemas(self):
        """Gets the schemas of this PatchUserReqBody.

        概要

        :return: The schemas of this PatchUserReqBody.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this PatchUserReqBody.

        概要

        :param schemas: The schemas of this PatchUserReqBody.
        :type schemas: list[str]
        """
        self._schemas = schemas

    @property
    def operations(self):
        """Gets the operations of this PatchUserReqBody.

        要执行的修改操作列表

        :return: The operations of this PatchUserReqBody.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.OperationItemDto`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this PatchUserReqBody.

        要执行的修改操作列表

        :param operations: The operations of this PatchUserReqBody.
        :type operations: list[:class:`huaweicloudsdkidentitycenterscim.v1.OperationItemDto`]
        """
        self._operations = operations

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
        if not isinstance(other, PatchUserReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
