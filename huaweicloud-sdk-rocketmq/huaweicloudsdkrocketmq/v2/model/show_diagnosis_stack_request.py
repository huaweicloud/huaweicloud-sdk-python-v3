# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiagnosisStackRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'stack_id': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'stack_id': 'stack_id'
    }

    def __init__(self, engine=None, stack_id=None):
        r"""ShowDiagnosisStackRequest

        The model defined in huaweicloud sdk

        :param engine: **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type engine: str
        :param stack_id: **参数解释**： 堆ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type stack_id: str
        """
        
        

        self._engine = None
        self._stack_id = None
        self.discriminator = None

        self.engine = engine
        self.stack_id = stack_id

    @property
    def engine(self):
        r"""Gets the engine of this ShowDiagnosisStackRequest.

        **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The engine of this ShowDiagnosisStackRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ShowDiagnosisStackRequest.

        **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param engine: The engine of this ShowDiagnosisStackRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def stack_id(self):
        r"""Gets the stack_id of this ShowDiagnosisStackRequest.

        **参数解释**： 堆ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The stack_id of this ShowDiagnosisStackRequest.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        r"""Sets the stack_id of this ShowDiagnosisStackRequest.

        **参数解释**： 堆ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param stack_id: The stack_id of this ShowDiagnosisStackRequest.
        :type stack_id: str
        """
        self._stack_id = stack_id

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
        if not isinstance(other, ShowDiagnosisStackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
