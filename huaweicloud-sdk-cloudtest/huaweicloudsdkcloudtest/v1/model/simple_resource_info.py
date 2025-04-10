# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleResourceInfo:

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
        'owner': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'owner': 'owner',
        'resource_id': 'resource_id'
    }

    def __init__(self, type=None, owner=None, resource_id=None):
        r"""SimpleResourceInfo

        The model defined in huaweicloud sdk

        :param type: 资源类型
        :type type: str
        :param owner: 资源责任人
        :type owner: str
        :param resource_id: 资源id
        :type resource_id: str
        """
        
        

        self._type = None
        self._owner = None
        self._resource_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if owner is not None:
            self.owner = owner
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def type(self):
        r"""Gets the type of this SimpleResourceInfo.

        资源类型

        :return: The type of this SimpleResourceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SimpleResourceInfo.

        资源类型

        :param type: The type of this SimpleResourceInfo.
        :type type: str
        """
        self._type = type

    @property
    def owner(self):
        r"""Gets the owner of this SimpleResourceInfo.

        资源责任人

        :return: The owner of this SimpleResourceInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this SimpleResourceInfo.

        资源责任人

        :param owner: The owner of this SimpleResourceInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SimpleResourceInfo.

        资源id

        :return: The resource_id of this SimpleResourceInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SimpleResourceInfo.

        资源id

        :param resource_id: The resource_id of this SimpleResourceInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, SimpleResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
