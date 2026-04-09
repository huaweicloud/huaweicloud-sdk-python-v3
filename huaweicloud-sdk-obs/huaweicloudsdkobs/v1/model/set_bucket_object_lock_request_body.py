# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketObjectLockRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "ObjectLockConfiguration"

    sensitive_list = []

    openapi_types = {
        'object_lock_enabled': 'str',
        'rule': 'SetBucketObjectLockRule'
    }

    attribute_map = {
        'object_lock_enabled': 'ObjectLockEnabled',
        'rule': 'Rule'
    }

    def __init__(self, object_lock_enabled=None, rule=None):
        r"""SetBucketObjectLockRequestBody

        The model defined in huaweicloud sdk

        :param object_lock_enabled: Definition:  Bucket-level WORM status. Constraints:  None Range: Enabled:  Bucket-level WORM is enabled. Default value:  None 
        :type object_lock_enabled: str
        :param rule: 
        :type rule: :class:`huaweicloudsdkobs.v1.SetBucketObjectLockRule`
        """
        
        

        self._object_lock_enabled = None
        self._rule = None
        self.discriminator = None

        if object_lock_enabled is not None:
            self.object_lock_enabled = object_lock_enabled
        if rule is not None:
            self.rule = rule

    @property
    def object_lock_enabled(self):
        r"""Gets the object_lock_enabled of this SetBucketObjectLockRequestBody.

        Definition:  Bucket-level WORM status. Constraints:  None Range: Enabled:  Bucket-level WORM is enabled. Default value:  None 

        :return: The object_lock_enabled of this SetBucketObjectLockRequestBody.
        :rtype: str
        """
        return self._object_lock_enabled

    @object_lock_enabled.setter
    def object_lock_enabled(self, object_lock_enabled):
        r"""Sets the object_lock_enabled of this SetBucketObjectLockRequestBody.

        Definition:  Bucket-level WORM status. Constraints:  None Range: Enabled:  Bucket-level WORM is enabled. Default value:  None 

        :param object_lock_enabled: The object_lock_enabled of this SetBucketObjectLockRequestBody.
        :type object_lock_enabled: str
        """
        self._object_lock_enabled = object_lock_enabled

    @property
    def rule(self):
        r"""Gets the rule of this SetBucketObjectLockRequestBody.

        :return: The rule of this SetBucketObjectLockRequestBody.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketObjectLockRule`
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this SetBucketObjectLockRequestBody.

        :param rule: The rule of this SetBucketObjectLockRequestBody.
        :type rule: :class:`huaweicloudsdkobs.v1.SetBucketObjectLockRule`
        """
        self._rule = rule

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
        if not isinstance(other, SetBucketObjectLockRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
