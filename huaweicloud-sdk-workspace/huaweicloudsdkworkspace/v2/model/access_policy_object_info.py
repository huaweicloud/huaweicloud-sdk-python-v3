# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicyObjectInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'object_name': 'str',
        'object_type': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'object_name': 'object_name',
        'object_type': 'object_type'
    }

    def __init__(self, object_id=None, object_name=None, object_type=None):
        """AccessPolicyObjectInfo

        The model defined in huaweicloud sdk

        :param object_id: 黑名单中的对象id，目前仅用户对象。
        :type object_id: str
        :param object_name: 对象名。
        :type object_name: str
        :param object_type: 对象类型，当前只支持用户类型。 * USER： 用户
        :type object_type: str
        """
        
        

        self._object_id = None
        self._object_name = None
        self._object_type = None
        self.discriminator = None

        self.object_id = object_id
        if object_name is not None:
            self.object_name = object_name
        self.object_type = object_type

    @property
    def object_id(self):
        """Gets the object_id of this AccessPolicyObjectInfo.

        黑名单中的对象id，目前仅用户对象。

        :return: The object_id of this AccessPolicyObjectInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AccessPolicyObjectInfo.

        黑名单中的对象id，目前仅用户对象。

        :param object_id: The object_id of this AccessPolicyObjectInfo.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_name(self):
        """Gets the object_name of this AccessPolicyObjectInfo.

        对象名。

        :return: The object_name of this AccessPolicyObjectInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this AccessPolicyObjectInfo.

        对象名。

        :param object_name: The object_name of this AccessPolicyObjectInfo.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_type(self):
        """Gets the object_type of this AccessPolicyObjectInfo.

        对象类型，当前只支持用户类型。 * USER： 用户

        :return: The object_type of this AccessPolicyObjectInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this AccessPolicyObjectInfo.

        对象类型，当前只支持用户类型。 * USER： 用户

        :param object_type: The object_type of this AccessPolicyObjectInfo.
        :type object_type: str
        """
        self._object_type = object_type

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
        if not isinstance(other, AccessPolicyObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
