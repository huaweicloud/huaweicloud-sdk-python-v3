# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComplianceStatusForAccountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_account_id': 'str',
        'control_id': 'str'
    }

    attribute_map = {
        'managed_account_id': 'managed_account_id',
        'control_id': 'control_id'
    }

    def __init__(self, managed_account_id=None, control_id=None):
        """ShowComplianceStatusForAccountRequest

        The model defined in huaweicloud sdk

        :param managed_account_id: 纳管账号ID。
        :type managed_account_id: str
        :param control_id: 启用的控制策略信息。
        :type control_id: str
        """
        
        

        self._managed_account_id = None
        self._control_id = None
        self.discriminator = None

        self.managed_account_id = managed_account_id
        if control_id is not None:
            self.control_id = control_id

    @property
    def managed_account_id(self):
        """Gets the managed_account_id of this ShowComplianceStatusForAccountRequest.

        纳管账号ID。

        :return: The managed_account_id of this ShowComplianceStatusForAccountRequest.
        :rtype: str
        """
        return self._managed_account_id

    @managed_account_id.setter
    def managed_account_id(self, managed_account_id):
        """Sets the managed_account_id of this ShowComplianceStatusForAccountRequest.

        纳管账号ID。

        :param managed_account_id: The managed_account_id of this ShowComplianceStatusForAccountRequest.
        :type managed_account_id: str
        """
        self._managed_account_id = managed_account_id

    @property
    def control_id(self):
        """Gets the control_id of this ShowComplianceStatusForAccountRequest.

        启用的控制策略信息。

        :return: The control_id of this ShowComplianceStatusForAccountRequest.
        :rtype: str
        """
        return self._control_id

    @control_id.setter
    def control_id(self, control_id):
        """Sets the control_id of this ShowComplianceStatusForAccountRequest.

        启用的控制策略信息。

        :param control_id: The control_id of this ShowComplianceStatusForAccountRequest.
        :type control_id: str
        """
        self._control_id = control_id

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
        if not isinstance(other, ShowComplianceStatusForAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
