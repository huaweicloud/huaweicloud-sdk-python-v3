# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateAZRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_available_zones': 'list[str]',
        'execute_immediately': 'bool'
    }

    attribute_map = {
        'new_available_zones': 'new_available_zones',
        'execute_immediately': 'execute_immediately'
    }

    def __init__(self, new_available_zones=None, execute_immediately=None):
        r"""MigrateAZRequestBody

        The model defined in huaweicloud sdk

        :param new_available_zones: **参数解释**： 新可用区。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type new_available_zones: list[str]
        :param execute_immediately: **参数解释**： 是否立即执行变更。 **约束限制**： 不涉及。 **取值范围**： true：立即执行变更。 false：暂不执行变更。 **默认取值**： true 
        :type execute_immediately: bool
        """
        
        

        self._new_available_zones = None
        self._execute_immediately = None
        self.discriminator = None

        if new_available_zones is not None:
            self.new_available_zones = new_available_zones
        if execute_immediately is not None:
            self.execute_immediately = execute_immediately

    @property
    def new_available_zones(self):
        r"""Gets the new_available_zones of this MigrateAZRequestBody.

        **参数解释**： 新可用区。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The new_available_zones of this MigrateAZRequestBody.
        :rtype: list[str]
        """
        return self._new_available_zones

    @new_available_zones.setter
    def new_available_zones(self, new_available_zones):
        r"""Sets the new_available_zones of this MigrateAZRequestBody.

        **参数解释**： 新可用区。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param new_available_zones: The new_available_zones of this MigrateAZRequestBody.
        :type new_available_zones: list[str]
        """
        self._new_available_zones = new_available_zones

    @property
    def execute_immediately(self):
        r"""Gets the execute_immediately of this MigrateAZRequestBody.

        **参数解释**： 是否立即执行变更。 **约束限制**： 不涉及。 **取值范围**： true：立即执行变更。 false：暂不执行变更。 **默认取值**： true 

        :return: The execute_immediately of this MigrateAZRequestBody.
        :rtype: bool
        """
        return self._execute_immediately

    @execute_immediately.setter
    def execute_immediately(self, execute_immediately):
        r"""Sets the execute_immediately of this MigrateAZRequestBody.

        **参数解释**： 是否立即执行变更。 **约束限制**： 不涉及。 **取值范围**： true：立即执行变更。 false：暂不执行变更。 **默认取值**： true 

        :param execute_immediately: The execute_immediately of this MigrateAZRequestBody.
        :type execute_immediately: bool
        """
        self._execute_immediately = execute_immediately

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
        if not isinstance(other, MigrateAZRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
