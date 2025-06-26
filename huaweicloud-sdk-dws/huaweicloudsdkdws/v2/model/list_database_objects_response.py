# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'object_list': 'list[DatabaseObjectInfo]',
        'count': 'str'
    }

    attribute_map = {
        'type': 'type',
        'object_list': 'object_list',
        'count': 'count'
    }

    def __init__(self, type=None, object_list=None, count=None):
        r"""ListDatabaseObjectsResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 类型。 **取值范围**： DATABASE、SCHEMA、TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE、NODEGROUP
        :type type: str
        :param object_list: **参数解释**： 对象列表。 **取值范围**： 不涉及。
        :type object_list: list[:class:`huaweicloudsdkdws.v2.DatabaseObjectInfo`]
        :param count: **参数解释**： 对象总条数。 **取值范围**： 不涉及。
        :type count: str
        """
        
        super(ListDatabaseObjectsResponse, self).__init__()

        self._type = None
        self._object_list = None
        self._count = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if object_list is not None:
            self.object_list = object_list
        if count is not None:
            self.count = count

    @property
    def type(self):
        r"""Gets the type of this ListDatabaseObjectsResponse.

        **参数解释**： 类型。 **取值范围**： DATABASE、SCHEMA、TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE、NODEGROUP

        :return: The type of this ListDatabaseObjectsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDatabaseObjectsResponse.

        **参数解释**： 类型。 **取值范围**： DATABASE、SCHEMA、TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE、NODEGROUP

        :param type: The type of this ListDatabaseObjectsResponse.
        :type type: str
        """
        self._type = type

    @property
    def object_list(self):
        r"""Gets the object_list of this ListDatabaseObjectsResponse.

        **参数解释**： 对象列表。 **取值范围**： 不涉及。

        :return: The object_list of this ListDatabaseObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.DatabaseObjectInfo`]
        """
        return self._object_list

    @object_list.setter
    def object_list(self, object_list):
        r"""Sets the object_list of this ListDatabaseObjectsResponse.

        **参数解释**： 对象列表。 **取值范围**： 不涉及。

        :param object_list: The object_list of this ListDatabaseObjectsResponse.
        :type object_list: list[:class:`huaweicloudsdkdws.v2.DatabaseObjectInfo`]
        """
        self._object_list = object_list

    @property
    def count(self):
        r"""Gets the count of this ListDatabaseObjectsResponse.

        **参数解释**： 对象总条数。 **取值范围**： 不涉及。

        :return: The count of this ListDatabaseObjectsResponse.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDatabaseObjectsResponse.

        **参数解释**： 对象总条数。 **取值范围**： 不涉及。

        :param count: The count of this ListDatabaseObjectsResponse.
        :type count: str
        """
        self._count = count

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
        if not isinstance(other, ListDatabaseObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
