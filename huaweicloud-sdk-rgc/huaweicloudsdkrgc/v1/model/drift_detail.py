# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DriftDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manage_account_id': 'str',
        'drift_type': 'str',
        'drift_target_id': 'str',
        'drift_target_type': 'str',
        'drift_message': 'str',
        'parent_organization_unit_id': 'str'
    }

    attribute_map = {
        'manage_account_id': 'manage_account_id',
        'drift_type': 'drift_type',
        'drift_target_id': 'drift_target_id',
        'drift_target_type': 'drift_target_type',
        'drift_message': 'drift_message',
        'parent_organization_unit_id': 'parent_organization_unit_id'
    }

    def __init__(self, manage_account_id=None, drift_type=None, drift_target_id=None, drift_target_type=None, drift_message=None, parent_organization_unit_id=None):
        """DriftDetail

        The model defined in huaweicloud sdk

        :param manage_account_id: 管理纳管账号ID。
        :type manage_account_id: str
        :param drift_type: 漂移类型。
        :type drift_type: str
        :param drift_target_id: 漂移发生的纳管账号ID或注册OU ID。
        :type drift_target_id: str
        :param drift_target_type: 漂移目标类型，类型有accountId和policyId。
        :type drift_target_type: str
        :param drift_message: 漂移信息。
        :type drift_message: str
        :param parent_organization_unit_id: 父注册OU ID。
        :type parent_organization_unit_id: str
        """
        
        

        self._manage_account_id = None
        self._drift_type = None
        self._drift_target_id = None
        self._drift_target_type = None
        self._drift_message = None
        self._parent_organization_unit_id = None
        self.discriminator = None

        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if drift_type is not None:
            self.drift_type = drift_type
        if drift_target_id is not None:
            self.drift_target_id = drift_target_id
        if drift_target_type is not None:
            self.drift_target_type = drift_target_type
        if drift_message is not None:
            self.drift_message = drift_message
        if parent_organization_unit_id is not None:
            self.parent_organization_unit_id = parent_organization_unit_id

    @property
    def manage_account_id(self):
        """Gets the manage_account_id of this DriftDetail.

        管理纳管账号ID。

        :return: The manage_account_id of this DriftDetail.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        """Sets the manage_account_id of this DriftDetail.

        管理纳管账号ID。

        :param manage_account_id: The manage_account_id of this DriftDetail.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def drift_type(self):
        """Gets the drift_type of this DriftDetail.

        漂移类型。

        :return: The drift_type of this DriftDetail.
        :rtype: str
        """
        return self._drift_type

    @drift_type.setter
    def drift_type(self, drift_type):
        """Sets the drift_type of this DriftDetail.

        漂移类型。

        :param drift_type: The drift_type of this DriftDetail.
        :type drift_type: str
        """
        self._drift_type = drift_type

    @property
    def drift_target_id(self):
        """Gets the drift_target_id of this DriftDetail.

        漂移发生的纳管账号ID或注册OU ID。

        :return: The drift_target_id of this DriftDetail.
        :rtype: str
        """
        return self._drift_target_id

    @drift_target_id.setter
    def drift_target_id(self, drift_target_id):
        """Sets the drift_target_id of this DriftDetail.

        漂移发生的纳管账号ID或注册OU ID。

        :param drift_target_id: The drift_target_id of this DriftDetail.
        :type drift_target_id: str
        """
        self._drift_target_id = drift_target_id

    @property
    def drift_target_type(self):
        """Gets the drift_target_type of this DriftDetail.

        漂移目标类型，类型有accountId和policyId。

        :return: The drift_target_type of this DriftDetail.
        :rtype: str
        """
        return self._drift_target_type

    @drift_target_type.setter
    def drift_target_type(self, drift_target_type):
        """Sets the drift_target_type of this DriftDetail.

        漂移目标类型，类型有accountId和policyId。

        :param drift_target_type: The drift_target_type of this DriftDetail.
        :type drift_target_type: str
        """
        self._drift_target_type = drift_target_type

    @property
    def drift_message(self):
        """Gets the drift_message of this DriftDetail.

        漂移信息。

        :return: The drift_message of this DriftDetail.
        :rtype: str
        """
        return self._drift_message

    @drift_message.setter
    def drift_message(self, drift_message):
        """Sets the drift_message of this DriftDetail.

        漂移信息。

        :param drift_message: The drift_message of this DriftDetail.
        :type drift_message: str
        """
        self._drift_message = drift_message

    @property
    def parent_organization_unit_id(self):
        """Gets the parent_organization_unit_id of this DriftDetail.

        父注册OU ID。

        :return: The parent_organization_unit_id of this DriftDetail.
        :rtype: str
        """
        return self._parent_organization_unit_id

    @parent_organization_unit_id.setter
    def parent_organization_unit_id(self, parent_organization_unit_id):
        """Sets the parent_organization_unit_id of this DriftDetail.

        父注册OU ID。

        :param parent_organization_unit_id: The parent_organization_unit_id of this DriftDetail.
        :type parent_organization_unit_id: str
        """
        self._parent_organization_unit_id = parent_organization_unit_id

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
        if not isinstance(other, DriftDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
