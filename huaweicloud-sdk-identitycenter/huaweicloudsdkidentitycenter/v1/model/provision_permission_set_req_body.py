# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProvisionPermissionSetReqBody:

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
        'target_type': 'str'
    }

    attribute_map = {
        'target_id': 'target_id',
        'target_type': 'target_type'
    }

    def __init__(self, target_id=None, target_type=None):
        r"""ProvisionPermissionSetReqBody

        The model defined in huaweicloud sdk

        :param target_id: 账号ID
        :type target_id: str
        :param target_type: 创建绑定的实体类型
        :type target_type: str
        """
        
        

        self._target_id = None
        self._target_type = None
        self.discriminator = None

        if target_id is not None:
            self.target_id = target_id
        self.target_type = target_type

    @property
    def target_id(self):
        r"""Gets the target_id of this ProvisionPermissionSetReqBody.

        账号ID

        :return: The target_id of this ProvisionPermissionSetReqBody.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this ProvisionPermissionSetReqBody.

        账号ID

        :param target_id: The target_id of this ProvisionPermissionSetReqBody.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_type(self):
        r"""Gets the target_type of this ProvisionPermissionSetReqBody.

        创建绑定的实体类型

        :return: The target_type of this ProvisionPermissionSetReqBody.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this ProvisionPermissionSetReqBody.

        创建绑定的实体类型

        :param target_type: The target_type of this ProvisionPermissionSetReqBody.
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
        if not isinstance(other, ProvisionPermissionSetReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
