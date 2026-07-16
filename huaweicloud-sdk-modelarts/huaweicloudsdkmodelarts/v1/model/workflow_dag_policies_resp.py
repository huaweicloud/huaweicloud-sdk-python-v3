# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowDagPoliciesResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'use_cache': 'bool'
    }

    attribute_map = {
        'use_cache': 'use_cache'
    }

    def __init__(self, use_cache=None):
        r"""WorkflowDagPoliciesResp

        The model defined in huaweicloud sdk

        :param use_cache: **参数解释**：是否使用缓存。 **取值范围**： - true：使用缓存 - false：不使用缓存
        :type use_cache: bool
        """
        
        

        self._use_cache = None
        self.discriminator = None

        if use_cache is not None:
            self.use_cache = use_cache

    @property
    def use_cache(self):
        r"""Gets the use_cache of this WorkflowDagPoliciesResp.

        **参数解释**：是否使用缓存。 **取值范围**： - true：使用缓存 - false：不使用缓存

        :return: The use_cache of this WorkflowDagPoliciesResp.
        :rtype: bool
        """
        return self._use_cache

    @use_cache.setter
    def use_cache(self, use_cache):
        r"""Sets the use_cache of this WorkflowDagPoliciesResp.

        **参数解释**：是否使用缓存。 **取值范围**： - true：使用缓存 - false：不使用缓存

        :param use_cache: The use_cache of this WorkflowDagPoliciesResp.
        :type use_cache: bool
        """
        self._use_cache = use_cache

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
        if not isinstance(other, WorkflowDagPoliciesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
