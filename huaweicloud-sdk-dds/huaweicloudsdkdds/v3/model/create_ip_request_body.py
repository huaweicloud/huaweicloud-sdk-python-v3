# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpRequestBody:

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
        'target_id': 'str',
        'password': 'str'
    }

    attribute_map = {
        'type': 'type',
        'target_id': 'target_id',
        'password': 'password'
    }

    def __init__(self, type=None, target_id=None, password=None):
        """CreateIpRequestBody

        The model defined in huaweicloud sdk

        :param type: 待打开IP开关的对象类型。 - 扩容shard组时，取值为“shard”。 - 扩容config组时，取值为“config”。
        :type type: str
        :param target_id: Shard组ID 注意：   1. 第一次添加Shard/Config IP时，该参数不传。   2. 对于已经添加过Shard IP的实例，需要传入该参数为新扩容的Shard组添加IP。
        :type target_id: str
        :param password: 打开集群开关设置的密码。 注意：该密码暂不支持修改，请谨慎操作。
        :type password: str
        """
        
        

        self._type = None
        self._target_id = None
        self._password = None
        self.discriminator = None

        self.type = type
        if target_id is not None:
            self.target_id = target_id
        self.password = password

    @property
    def type(self):
        """Gets the type of this CreateIpRequestBody.

        待打开IP开关的对象类型。 - 扩容shard组时，取值为“shard”。 - 扩容config组时，取值为“config”。

        :return: The type of this CreateIpRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateIpRequestBody.

        待打开IP开关的对象类型。 - 扩容shard组时，取值为“shard”。 - 扩容config组时，取值为“config”。

        :param type: The type of this CreateIpRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def target_id(self):
        """Gets the target_id of this CreateIpRequestBody.

        Shard组ID 注意：   1. 第一次添加Shard/Config IP时，该参数不传。   2. 对于已经添加过Shard IP的实例，需要传入该参数为新扩容的Shard组添加IP。

        :return: The target_id of this CreateIpRequestBody.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this CreateIpRequestBody.

        Shard组ID 注意：   1. 第一次添加Shard/Config IP时，该参数不传。   2. 对于已经添加过Shard IP的实例，需要传入该参数为新扩容的Shard组添加IP。

        :param target_id: The target_id of this CreateIpRequestBody.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def password(self):
        """Gets the password of this CreateIpRequestBody.

        打开集群开关设置的密码。 注意：该密码暂不支持修改，请谨慎操作。

        :return: The password of this CreateIpRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateIpRequestBody.

        打开集群开关设置的密码。 注意：该密码暂不支持修改，请谨慎操作。

        :param password: The password of this CreateIpRequestBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, CreateIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
