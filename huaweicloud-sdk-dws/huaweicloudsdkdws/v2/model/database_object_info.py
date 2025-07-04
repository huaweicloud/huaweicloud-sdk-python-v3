# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseObjectInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obj_name': 'str'
    }

    attribute_map = {
        'obj_name': 'obj_name'
    }

    def __init__(self, obj_name=None):
        r"""DatabaseObjectInfo

        The model defined in huaweicloud sdk

        :param obj_name: **参数解释**： 对象名称。 **取值范围**： 不涉及。
        :type obj_name: str
        """
        
        

        self._obj_name = None
        self.discriminator = None

        if obj_name is not None:
            self.obj_name = obj_name

    @property
    def obj_name(self):
        r"""Gets the obj_name of this DatabaseObjectInfo.

        **参数解释**： 对象名称。 **取值范围**： 不涉及。

        :return: The obj_name of this DatabaseObjectInfo.
        :rtype: str
        """
        return self._obj_name

    @obj_name.setter
    def obj_name(self, obj_name):
        r"""Sets the obj_name of this DatabaseObjectInfo.

        **参数解释**： 对象名称。 **取值范围**： 不涉及。

        :param obj_name: The obj_name of this DatabaseObjectInfo.
        :type obj_name: str
        """
        self._obj_name = obj_name

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
        if not isinstance(other, DatabaseObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
