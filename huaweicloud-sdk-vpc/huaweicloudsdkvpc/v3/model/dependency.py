# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dependency:

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
        'instance_id': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name'
    }

    def __init__(self, type=None, instance_id=None, instance_name=None):
        r"""Dependency

        The model defined in huaweicloud sdk

        :param type: **参数解释**： IP地址组关联的资源类型。 **取值范围**： - sg：IP地址组关联的安全组。 - acl：IP地址组关联的网络ACL。
        :type type: str
        :param instance_id: **参数解释**： IP地址组关联资源的ID。 **取值范围**： 带“-”的标准UUID格式。
        :type instance_id: str
        :param instance_name: **参数解释**： IP地址组关联资源的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。
        :type instance_name: str
        """
        
        

        self._type = None
        self._instance_id = None
        self._instance_name = None
        self.discriminator = None

        self.type = type
        self.instance_id = instance_id
        self.instance_name = instance_name

    @property
    def type(self):
        r"""Gets the type of this Dependency.

        **参数解释**： IP地址组关联的资源类型。 **取值范围**： - sg：IP地址组关联的安全组。 - acl：IP地址组关联的网络ACL。

        :return: The type of this Dependency.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Dependency.

        **参数解释**： IP地址组关联的资源类型。 **取值范围**： - sg：IP地址组关联的安全组。 - acl：IP地址组关联的网络ACL。

        :param type: The type of this Dependency.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Dependency.

        **参数解释**： IP地址组关联资源的ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The instance_id of this Dependency.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Dependency.

        **参数解释**： IP地址组关联资源的ID。 **取值范围**： 带“-”的标准UUID格式。

        :param instance_id: The instance_id of this Dependency.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this Dependency.

        **参数解释**： IP地址组关联资源的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。

        :return: The instance_name of this Dependency.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this Dependency.

        **参数解释**： IP地址组关联资源的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。

        :param instance_name: The instance_name of this Dependency.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, Dependency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
