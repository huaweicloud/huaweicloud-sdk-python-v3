# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InPlaceRollingUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_defined_step': 'int'
    }

    attribute_map = {
        'user_defined_step': 'userDefinedStep'
    }

    def __init__(self, user_defined_step=None):
        """InPlaceRollingUpdate

        The model defined in huaweicloud sdk

        :param user_defined_step: 节点升级步长，取值范围为[1, 40]，建议取值20
        :type user_defined_step: int
        """
        
        

        self._user_defined_step = None
        self.discriminator = None

        if user_defined_step is not None:
            self.user_defined_step = user_defined_step

    @property
    def user_defined_step(self):
        """Gets the user_defined_step of this InPlaceRollingUpdate.

        节点升级步长，取值范围为[1, 40]，建议取值20

        :return: The user_defined_step of this InPlaceRollingUpdate.
        :rtype: int
        """
        return self._user_defined_step

    @user_defined_step.setter
    def user_defined_step(self, user_defined_step):
        """Sets the user_defined_step of this InPlaceRollingUpdate.

        节点升级步长，取值范围为[1, 40]，建议取值20

        :param user_defined_step: The user_defined_step of this InPlaceRollingUpdate.
        :type user_defined_step: int
        """
        self._user_defined_step = user_defined_step

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
        if not isinstance(other, InPlaceRollingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
