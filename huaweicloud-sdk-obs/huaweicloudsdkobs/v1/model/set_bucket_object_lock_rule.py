# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketObjectLockRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Rule"

    sensitive_list = []

    openapi_types = {
        'default_retention': 'SetBucketObjectLockDefaultRetention'
    }

    attribute_map = {
        'default_retention': 'DefaultRetention'
    }

    def __init__(self, default_retention=None):
        r"""SetBucketObjectLockRule

        The model defined in huaweicloud sdk

        :param default_retention: 
        :type default_retention: :class:`huaweicloudsdkobs.v1.SetBucketObjectLockDefaultRetention`
        """
        
        

        self._default_retention = None
        self.discriminator = None

        if default_retention is not None:
            self.default_retention = default_retention

    @property
    def default_retention(self):
        r"""Gets the default_retention of this SetBucketObjectLockRule.

        :return: The default_retention of this SetBucketObjectLockRule.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketObjectLockDefaultRetention`
        """
        return self._default_retention

    @default_retention.setter
    def default_retention(self, default_retention):
        r"""Sets the default_retention of this SetBucketObjectLockRule.

        :param default_retention: The default_retention of this SetBucketObjectLockRule.
        :type default_retention: :class:`huaweicloudsdkobs.v1.SetBucketObjectLockDefaultRetention`
        """
        self._default_retention = default_retention

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
        if not isinstance(other, SetBucketObjectLockRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
