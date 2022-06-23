# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSessionReqGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'resources': 'list[CreateSessionReqResource]'
    }

    attribute_map = {
        'name': 'name',
        'resources': 'resources'
    }

    def __init__(self, name=None, resources=None):
        """CreateSessionReqGroup

        The model defined in huaweicloud sdk

        :param name: 用户组名称。
        :type name: str
        :param resources: 用户组资源。
        :type resources: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqResource`]
        """
        
        

        self._name = None
        self._resources = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if resources is not None:
            self.resources = resources

    @property
    def name(self):
        """Gets the name of this CreateSessionReqGroup.

        用户组名称。

        :return: The name of this CreateSessionReqGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSessionReqGroup.

        用户组名称。

        :param name: The name of this CreateSessionReqGroup.
        :type name: str
        """
        self._name = name

    @property
    def resources(self):
        """Gets the resources of this CreateSessionReqGroup.

        用户组资源。

        :return: The resources of this CreateSessionReqGroup.
        :rtype: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CreateSessionReqGroup.

        用户组资源。

        :param resources: The resources of this CreateSessionReqGroup.
        :type resources: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqResource`]
        """
        self._resources = resources

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
        if not isinstance(other, CreateSessionReqGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
