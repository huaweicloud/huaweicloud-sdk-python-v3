# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterGroupStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conditions': 'list[ClusterGroupCondition]'
    }

    attribute_map = {
        'conditions': 'conditions'
    }

    def __init__(self, conditions=None):
        r"""ClusterGroupStatus

        The model defined in huaweicloud sdk

        :param conditions: 
        :type conditions: list[:class:`huaweicloudsdkucs.v1.ClusterGroupCondition`]
        """
        
        

        self._conditions = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions

    @property
    def conditions(self):
        r"""Gets the conditions of this ClusterGroupStatus.

        :return: The conditions of this ClusterGroupStatus.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ClusterGroupCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ClusterGroupStatus.

        :param conditions: The conditions of this ClusterGroupStatus.
        :type conditions: list[:class:`huaweicloudsdkucs.v1.ClusterGroupCondition`]
        """
        self._conditions = conditions

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
        if not isinstance(other, ClusterGroupStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
