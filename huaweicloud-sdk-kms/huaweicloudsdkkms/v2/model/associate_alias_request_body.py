# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateAliasRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'target_key_id': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'target_key_id': 'target_key_id'
    }

    def __init__(self, alias=None, target_key_id=None):
        r"""AssociateAliasRequestBody

        The model defined in huaweicloud sdk

        :param alias: 待关联别名
        :type alias: str
        :param target_key_id: 待关联的密钥ID
        :type target_key_id: str
        """
        
        

        self._alias = None
        self._target_key_id = None
        self.discriminator = None

        self.alias = alias
        self.target_key_id = target_key_id

    @property
    def alias(self):
        r"""Gets the alias of this AssociateAliasRequestBody.

        待关联别名

        :return: The alias of this AssociateAliasRequestBody.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AssociateAliasRequestBody.

        待关联别名

        :param alias: The alias of this AssociateAliasRequestBody.
        :type alias: str
        """
        self._alias = alias

    @property
    def target_key_id(self):
        r"""Gets the target_key_id of this AssociateAliasRequestBody.

        待关联的密钥ID

        :return: The target_key_id of this AssociateAliasRequestBody.
        :rtype: str
        """
        return self._target_key_id

    @target_key_id.setter
    def target_key_id(self, target_key_id):
        r"""Sets the target_key_id of this AssociateAliasRequestBody.

        待关联的密钥ID

        :param target_key_id: The target_key_id of this AssociateAliasRequestBody.
        :type target_key_id: str
        """
        self._target_key_id = target_key_id

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
        if not isinstance(other, AssociateAliasRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
