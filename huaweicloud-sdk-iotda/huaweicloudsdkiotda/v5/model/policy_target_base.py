# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTargetBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_type': 'str',
        'target_id': 'str'
    }

    attribute_map = {
        'target_type': 'target_type',
        'target_id': 'target_id'
    }

    def __init__(self, target_type=None, target_id=None):
        r"""PolicyTargetBase

        The model defined in huaweicloud sdk

        :param target_type: **参数说明**：策略绑定的目标类型。 **取值范围**：device|product|app，device表示设备，product表示产品，app表示整个资源空间。
        :type target_type: str
        :param target_id: 策略绑定的目标ID
        :type target_id: str
        """
        
        

        self._target_type = None
        self._target_id = None
        self.discriminator = None

        self.target_type = target_type
        self.target_id = target_id

    @property
    def target_type(self):
        r"""Gets the target_type of this PolicyTargetBase.

        **参数说明**：策略绑定的目标类型。 **取值范围**：device|product|app，device表示设备，product表示产品，app表示整个资源空间。

        :return: The target_type of this PolicyTargetBase.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this PolicyTargetBase.

        **参数说明**：策略绑定的目标类型。 **取值范围**：device|product|app，device表示设备，product表示产品，app表示整个资源空间。

        :param target_type: The target_type of this PolicyTargetBase.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_id(self):
        r"""Gets the target_id of this PolicyTargetBase.

        策略绑定的目标ID

        :return: The target_id of this PolicyTargetBase.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this PolicyTargetBase.

        策略绑定的目标ID

        :param target_id: The target_id of this PolicyTargetBase.
        :type target_id: str
        """
        self._target_id = target_id

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
        if not isinstance(other, PolicyTargetBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
