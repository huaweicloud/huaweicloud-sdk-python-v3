# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyObjects:

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
        'object_id': 'str',
        'object_name': 'str'
    }

    attribute_map = {
        'object_type': 'object_type',
        'object_id': 'object_id',
        'object_name': 'object_name'
    }

    def __init__(self, object_type=None, object_id=None, object_name=None):
        r"""ApplyObjects

        The model defined in huaweicloud sdk

        :param object_type: 绑定对象类型枚举。 - USER：用户 - USER_GROUP：用户组 - ALL: 全部用户
        :type object_type: str
        :param object_id: 用户/用户组id。
        :type object_id: str
        :param object_name: 用户/用户组名称。
        :type object_name: str
        """
        
        

        self._object_type = None
        self._object_id = None
        self._object_name = None
        self.discriminator = None

        self.object_type = object_type
        self.object_id = object_id
        self.object_name = object_name

    @property
    def object_type(self):
        r"""Gets the object_type of this ApplyObjects.

        绑定对象类型枚举。 - USER：用户 - USER_GROUP：用户组 - ALL: 全部用户

        :return: The object_type of this ApplyObjects.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ApplyObjects.

        绑定对象类型枚举。 - USER：用户 - USER_GROUP：用户组 - ALL: 全部用户

        :param object_type: The object_type of this ApplyObjects.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_id(self):
        r"""Gets the object_id of this ApplyObjects.

        用户/用户组id。

        :return: The object_id of this ApplyObjects.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ApplyObjects.

        用户/用户组id。

        :param object_id: The object_id of this ApplyObjects.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_name(self):
        r"""Gets the object_name of this ApplyObjects.

        用户/用户组名称。

        :return: The object_name of this ApplyObjects.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ApplyObjects.

        用户/用户组名称。

        :param object_name: The object_name of this ApplyObjects.
        :type object_name: str
        """
        self._object_name = object_name

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
        if not isinstance(other, ApplyObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
