# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssistAuthConfigApplyObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'object_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'object_type': 'object_type',
        'object_name': 'object_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, object_type=None, object_name=None, offset=None, limit=None):
        r"""ShowAssistAuthConfigApplyObjectsRequest

        The model defined in huaweicloud sdk

        :param object_type: 绑定对象类型枚举。 - USER：用户 - USER_GROUP：用户组 - ALL: 全部用户
        :type object_type: str
        :param object_name: 对象名称。
        :type object_name: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回查询应用对象限制。取值范围1-1000，默认值是100。
        :type limit: int
        """
        
        

        self._object_type = None
        self._object_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if object_type is not None:
            self.object_type = object_type
        if object_name is not None:
            self.object_name = object_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def object_type(self):
        r"""Gets the object_type of this ShowAssistAuthConfigApplyObjectsRequest.

        绑定对象类型枚举。 - USER：用户 - USER_GROUP：用户组 - ALL: 全部用户

        :return: The object_type of this ShowAssistAuthConfigApplyObjectsRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ShowAssistAuthConfigApplyObjectsRequest.

        绑定对象类型枚举。 - USER：用户 - USER_GROUP：用户组 - ALL: 全部用户

        :param object_type: The object_type of this ShowAssistAuthConfigApplyObjectsRequest.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        r"""Gets the object_name of this ShowAssistAuthConfigApplyObjectsRequest.

        对象名称。

        :return: The object_name of this ShowAssistAuthConfigApplyObjectsRequest.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ShowAssistAuthConfigApplyObjectsRequest.

        对象名称。

        :param object_name: The object_name of this ShowAssistAuthConfigApplyObjectsRequest.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def offset(self):
        r"""Gets the offset of this ShowAssistAuthConfigApplyObjectsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ShowAssistAuthConfigApplyObjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAssistAuthConfigApplyObjectsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ShowAssistAuthConfigApplyObjectsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowAssistAuthConfigApplyObjectsRequest.

        用于分页查询，返回查询应用对象限制。取值范围1-1000，默认值是100。

        :return: The limit of this ShowAssistAuthConfigApplyObjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAssistAuthConfigApplyObjectsRequest.

        用于分页查询，返回查询应用对象限制。取值范围1-1000，默认值是100。

        :param limit: The limit of this ShowAssistAuthConfigApplyObjectsRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAssistAuthConfigApplyObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
