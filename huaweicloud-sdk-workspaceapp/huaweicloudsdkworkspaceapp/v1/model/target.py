# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Target:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'target_name': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'target_id': 'target_id',
        'target_name': 'target_name',
        'target_type': 'target_type'
    }

    def __init__(self, target_id=None, target_name=None, target_type=None):
        """Target

        The model defined in huaweicloud sdk

        :param target_id: 对象ID。
        :type target_id: str
        :param target_name: 对象名称。
        :type target_name: str
        :param target_type: 对象类型。 - USER：表示用户。   target_id：为用户ID。   target_name：为用户name。 - USERGROUP：表示用户组。   target_id：为用户组ID。   target_name：为用户组name。 - APPGROUP：应用组。   target_id：应用组id。   target_name：应用组名称。 - OU：组织单元。   target_id：OUID。   target_name：OU名称。 - ALL：表示所有。   target_id：default-apply-all-targets。   target_name：All-Targets。
        :type target_type: str
        """
        
        

        self._target_id = None
        self._target_name = None
        self._target_type = None
        self.discriminator = None

        self.target_id = target_id
        self.target_name = target_name
        self.target_type = target_type

    @property
    def target_id(self):
        """Gets the target_id of this Target.

        对象ID。

        :return: The target_id of this Target.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this Target.

        对象ID。

        :param target_id: The target_id of this Target.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_name(self):
        """Gets the target_name of this Target.

        对象名称。

        :return: The target_name of this Target.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this Target.

        对象名称。

        :param target_name: The target_name of this Target.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def target_type(self):
        """Gets the target_type of this Target.

        对象类型。 - USER：表示用户。   target_id：为用户ID。   target_name：为用户name。 - USERGROUP：表示用户组。   target_id：为用户组ID。   target_name：为用户组name。 - APPGROUP：应用组。   target_id：应用组id。   target_name：应用组名称。 - OU：组织单元。   target_id：OUID。   target_name：OU名称。 - ALL：表示所有。   target_id：default-apply-all-targets。   target_name：All-Targets。

        :return: The target_type of this Target.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this Target.

        对象类型。 - USER：表示用户。   target_id：为用户ID。   target_name：为用户name。 - USERGROUP：表示用户组。   target_id：为用户组ID。   target_name：为用户组name。 - APPGROUP：应用组。   target_id：应用组id。   target_name：应用组名称。 - OU：组织单元。   target_id：OUID。   target_name：OU名称。 - ALL：表示所有。   target_id：default-apply-all-targets。   target_name：All-Targets。

        :param target_type: The target_type of this Target.
        :type target_type: str
        """
        self._target_type = target_type

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
        if not isinstance(other, Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
