# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Privilege:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object': 'str',
        'privileges': 'list[str]'
    }

    attribute_map = {
        'object': 'object',
        'privileges': 'privileges'
    }

    def __init__(self, object=None, privileges=None):
        """Privilege

        The model defined in huaweicloud sdk

        :param object: 赋权的DLI资源，具体可参考https://support.huaweicloud.com/usermanual-dli/dli_01_0417.html
        :type object: str
        :param privileges: 待赋权，回收或更新的权限列表。 说明： 若“action”为“update”，更新列表为空，则表示回收用户在DLI的所有资源权限。
        :type privileges: list[str]
        """
        
        

        self._object = None
        self._privileges = None
        self.discriminator = None

        self.object = object
        self.privileges = privileges

    @property
    def object(self):
        """Gets the object of this Privilege.

        赋权的DLI资源，具体可参考https://support.huaweicloud.com/usermanual-dli/dli_01_0417.html

        :return: The object of this Privilege.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Privilege.

        赋权的DLI资源，具体可参考https://support.huaweicloud.com/usermanual-dli/dli_01_0417.html

        :param object: The object of this Privilege.
        :type object: str
        """
        self._object = object

    @property
    def privileges(self):
        """Gets the privileges of this Privilege.

        待赋权，回收或更新的权限列表。 说明： 若“action”为“update”，更新列表为空，则表示回收用户在DLI的所有资源权限。

        :return: The privileges of this Privilege.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this Privilege.

        待赋权，回收或更新的权限列表。 说明： 若“action”为“update”，更新列表为空，则表示回收用户在DLI的所有资源权限。

        :param privileges: The privileges of this Privilege.
        :type privileges: list[str]
        """
        self._privileges = privileges

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
        if not isinstance(other, Privilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
