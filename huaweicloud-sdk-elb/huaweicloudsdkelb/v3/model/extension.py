# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Extension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ep_id': 'str',
        'ep_service_id': 'str'
    }

    attribute_map = {
        'ep_id': 'ep_id',
        'ep_service_id': 'ep_service_id'
    }

    def __init__(self, ep_id=None, ep_service_id=None):
        r"""Extension

        The model defined in huaweicloud sdk

        :param ep_id: **参数解释**：EP ID.  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type ep_id: str
        :param ep_service_id: **参数解释**：EP Service ID.  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type ep_service_id: str
        """
        
        

        self._ep_id = None
        self._ep_service_id = None
        self.discriminator = None

        if ep_id is not None:
            self.ep_id = ep_id
        if ep_service_id is not None:
            self.ep_service_id = ep_service_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this Extension.

        **参数解释**：EP ID.  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ep_id of this Extension.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this Extension.

        **参数解释**：EP ID.  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param ep_id: The ep_id of this Extension.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_service_id(self):
        r"""Gets the ep_service_id of this Extension.

        **参数解释**：EP Service ID.  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ep_service_id of this Extension.
        :rtype: str
        """
        return self._ep_service_id

    @ep_service_id.setter
    def ep_service_id(self, ep_service_id):
        r"""Sets the ep_service_id of this Extension.

        **参数解释**：EP Service ID.  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param ep_service_id: The ep_service_id of this Extension.
        :type ep_service_id: str
        """
        self._ep_service_id = ep_service_id

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
        if not isinstance(other, Extension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
