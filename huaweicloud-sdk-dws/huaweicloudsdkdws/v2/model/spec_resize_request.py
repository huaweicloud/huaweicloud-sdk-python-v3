# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecResizeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_flavor_id': 'str',
        'force_backup': 'bool'
    }

    attribute_map = {
        'target_flavor_id': 'target_flavor_id',
        'force_backup': 'force_backup'
    }

    def __init__(self, target_flavor_id=None, force_backup=None):
        r"""SpecResizeRequest

        The model defined in huaweicloud sdk

        :param target_flavor_id: **参数解释**： 目标规格ID。 **取值范围**： 不涉及。
        :type target_flavor_id: str
        :param force_backup: **参数解释**： 强制备份。字段已废弃，不再生效。 **取值范围**： 不涉及。
        :type force_backup: bool
        """
        
        

        self._target_flavor_id = None
        self._force_backup = None
        self.discriminator = None

        self.target_flavor_id = target_flavor_id
        if force_backup is not None:
            self.force_backup = force_backup

    @property
    def target_flavor_id(self):
        r"""Gets the target_flavor_id of this SpecResizeRequest.

        **参数解释**： 目标规格ID。 **取值范围**： 不涉及。

        :return: The target_flavor_id of this SpecResizeRequest.
        :rtype: str
        """
        return self._target_flavor_id

    @target_flavor_id.setter
    def target_flavor_id(self, target_flavor_id):
        r"""Sets the target_flavor_id of this SpecResizeRequest.

        **参数解释**： 目标规格ID。 **取值范围**： 不涉及。

        :param target_flavor_id: The target_flavor_id of this SpecResizeRequest.
        :type target_flavor_id: str
        """
        self._target_flavor_id = target_flavor_id

    @property
    def force_backup(self):
        r"""Gets the force_backup of this SpecResizeRequest.

        **参数解释**： 强制备份。字段已废弃，不再生效。 **取值范围**： 不涉及。

        :return: The force_backup of this SpecResizeRequest.
        :rtype: bool
        """
        return self._force_backup

    @force_backup.setter
    def force_backup(self, force_backup):
        r"""Sets the force_backup of this SpecResizeRequest.

        **参数解释**： 强制备份。字段已废弃，不再生效。 **取值范围**： 不涉及。

        :param force_backup: The force_backup of this SpecResizeRequest.
        :type force_backup: bool
        """
        self._force_backup = force_backup

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
        if not isinstance(other, SpecResizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
