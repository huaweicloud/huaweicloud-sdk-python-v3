# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTachReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity_id': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id'
    }

    def __init__(self, entity_id=None):
        r"""PolicyTachReqBody

        The model defined in huaweicloud sdk

        :param entity_id: 根、组织单元或账号的唯一标识符（ID）。
        :type entity_id: str
        """
        
        

        self._entity_id = None
        self.discriminator = None

        self.entity_id = entity_id

    @property
    def entity_id(self):
        r"""Gets the entity_id of this PolicyTachReqBody.

        根、组织单元或账号的唯一标识符（ID）。

        :return: The entity_id of this PolicyTachReqBody.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this PolicyTachReqBody.

        根、组织单元或账号的唯一标识符（ID）。

        :param entity_id: The entity_id of this PolicyTachReqBody.
        :type entity_id: str
        """
        self._entity_id = entity_id

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
        if not isinstance(other, PolicyTachReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
