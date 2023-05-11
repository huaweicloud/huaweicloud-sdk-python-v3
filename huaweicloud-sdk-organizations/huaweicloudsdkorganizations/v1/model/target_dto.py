# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetDto:

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
        'entity': 'str'
    }

    attribute_map = {
        'type': 'type',
        'entity': 'entity'
    }

    def __init__(self, type=None, entity=None):
        """TargetDto

        The model defined in huaweicloud sdk

        :param type: 目标类型，account：账户，email：邮箱。
        :type type: str
        :param entity: 如果指定 &#39;type:account&#39;，则必须提供帐号ID作为实体。如果指定&#39;type:email&#39;，则必须指定与帐号关联的电子邮件地址。
        :type entity: str
        """
        
        

        self._type = None
        self._entity = None
        self.discriminator = None

        self.type = type
        self.entity = entity

    @property
    def type(self):
        """Gets the type of this TargetDto.

        目标类型，account：账户，email：邮箱。

        :return: The type of this TargetDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TargetDto.

        目标类型，account：账户，email：邮箱。

        :param type: The type of this TargetDto.
        :type type: str
        """
        self._type = type

    @property
    def entity(self):
        """Gets the entity of this TargetDto.

        如果指定 'type:account'，则必须提供帐号ID作为实体。如果指定'type:email'，则必须指定与帐号关联的电子邮件地址。

        :return: The entity of this TargetDto.
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this TargetDto.

        如果指定 'type:account'，则必须提供帐号ID作为实体。如果指定'type:email'，则必须指定与帐号关联的电子邮件地址。

        :param entity: The entity of this TargetDto.
        :type entity: str
        """
        self._entity = entity

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
        if not isinstance(other, TargetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
