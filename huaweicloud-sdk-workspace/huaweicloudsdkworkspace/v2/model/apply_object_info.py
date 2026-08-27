# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyObjectInfo:

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
        'object_id': 'str'
    }

    attribute_map = {
        'object_type': 'object_type',
        'object_id': 'object_id'
    }

    def __init__(self, object_type=None, object_id=None):
        r"""ApplyObjectInfo

        The model defined in huaweicloud sdk

        :param object_type: 应用对象类型，包括DESKTOP（单桌面）、ALL_DESKTOPS（全部桌面）、DESKTOP_POOL（桌面池）、DESKTOP_TAG（桌面标签）、ALL_USERS（全部用户）、USER（单个用户）、USER_GROUP（用户组）
        :type object_type: str
        :param object_id: 对象ID（object_type为ALL_DESKTOPS或ALL_USERS时可为null）
        :type object_id: str
        """
        
        

        self._object_type = None
        self._object_id = None
        self.discriminator = None

        if object_type is not None:
            self.object_type = object_type
        if object_id is not None:
            self.object_id = object_id

    @property
    def object_type(self):
        r"""Gets the object_type of this ApplyObjectInfo.

        应用对象类型，包括DESKTOP（单桌面）、ALL_DESKTOPS（全部桌面）、DESKTOP_POOL（桌面池）、DESKTOP_TAG（桌面标签）、ALL_USERS（全部用户）、USER（单个用户）、USER_GROUP（用户组）

        :return: The object_type of this ApplyObjectInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ApplyObjectInfo.

        应用对象类型，包括DESKTOP（单桌面）、ALL_DESKTOPS（全部桌面）、DESKTOP_POOL（桌面池）、DESKTOP_TAG（桌面标签）、ALL_USERS（全部用户）、USER（单个用户）、USER_GROUP（用户组）

        :param object_type: The object_type of this ApplyObjectInfo.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_id(self):
        r"""Gets the object_id of this ApplyObjectInfo.

        对象ID（object_type为ALL_DESKTOPS或ALL_USERS时可为null）

        :return: The object_id of this ApplyObjectInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ApplyObjectInfo.

        对象ID（object_type为ALL_DESKTOPS或ALL_USERS时可为null）

        :param object_id: The object_id of this ApplyObjectInfo.
        :type object_id: str
        """
        self._object_id = object_id

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
        if not isinstance(other, ApplyObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
