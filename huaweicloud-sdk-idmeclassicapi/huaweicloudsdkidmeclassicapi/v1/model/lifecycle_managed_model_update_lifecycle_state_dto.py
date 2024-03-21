# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LifecycleManagedModelUpdateLifecycleStateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'lifecycle_state': 'ObjectReferenceParamDTO',
        'modifier': 'str'
    }

    attribute_map = {
        'id': 'id',
        'lifecycle_state': 'lifecycleState',
        'modifier': 'modifier'
    }

    def __init__(self, id=None, lifecycle_state=None, modifier=None):
        """LifecycleManagedModelUpdateLifecycleStateDTO

        The model defined in huaweicloud sdk

        :param id: 唯一标识。
        :type id: str
        :param lifecycle_state: 
        :type lifecycle_state: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param modifier: 更新人
        :type modifier: str
        """
        
        

        self._id = None
        self._lifecycle_state = None
        self._modifier = None
        self.discriminator = None

        self.id = id
        self.lifecycle_state = lifecycle_state
        if modifier is not None:
            self.modifier = modifier

    @property
    def id(self):
        """Gets the id of this LifecycleManagedModelUpdateLifecycleStateDTO.

        唯一标识。

        :return: The id of this LifecycleManagedModelUpdateLifecycleStateDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LifecycleManagedModelUpdateLifecycleStateDTO.

        唯一标识。

        :param id: The id of this LifecycleManagedModelUpdateLifecycleStateDTO.
        :type id: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this LifecycleManagedModelUpdateLifecycleStateDTO.

        :return: The lifecycle_state of this LifecycleManagedModelUpdateLifecycleStateDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this LifecycleManagedModelUpdateLifecycleStateDTO.

        :param lifecycle_state: The lifecycle_state of this LifecycleManagedModelUpdateLifecycleStateDTO.
        :type lifecycle_state: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._lifecycle_state = lifecycle_state

    @property
    def modifier(self):
        """Gets the modifier of this LifecycleManagedModelUpdateLifecycleStateDTO.

        更新人

        :return: The modifier of this LifecycleManagedModelUpdateLifecycleStateDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this LifecycleManagedModelUpdateLifecycleStateDTO.

        更新人

        :param modifier: The modifier of this LifecycleManagedModelUpdateLifecycleStateDTO.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, LifecycleManagedModelUpdateLifecycleStateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
