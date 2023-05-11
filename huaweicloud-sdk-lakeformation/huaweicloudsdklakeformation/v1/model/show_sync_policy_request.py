# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSyncPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'last_known_version': 'int',
        'supports_policy_deltas': 'bool',
        'is_return_policy_data': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'last_known_version': 'last_known_version',
        'supports_policy_deltas': 'supports_policy_deltas',
        'is_return_policy_data': 'is_return_policy_data'
    }

    def __init__(self, instance_id=None, last_known_version=None, supports_policy_deltas=None, is_return_policy_data=None):
        """ShowSyncPolicyRequest

        The model defined in huaweicloud sdk

        :param instance_id: instance id
        :type instance_id: str
        :param last_known_version: lastKnownVersion
        :type last_known_version: int
        :param supports_policy_deltas: supportsPolicyDeltas
        :type supports_policy_deltas: bool
        :param is_return_policy_data: isReturnPolicyData
        :type is_return_policy_data: bool
        """
        
        

        self._instance_id = None
        self._last_known_version = None
        self._supports_policy_deltas = None
        self._is_return_policy_data = None
        self.discriminator = None

        self.instance_id = instance_id
        if last_known_version is not None:
            self.last_known_version = last_known_version
        if supports_policy_deltas is not None:
            self.supports_policy_deltas = supports_policy_deltas
        if is_return_policy_data is not None:
            self.is_return_policy_data = is_return_policy_data

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowSyncPolicyRequest.

        instance id

        :return: The instance_id of this ShowSyncPolicyRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowSyncPolicyRequest.

        instance id

        :param instance_id: The instance_id of this ShowSyncPolicyRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def last_known_version(self):
        """Gets the last_known_version of this ShowSyncPolicyRequest.

        lastKnownVersion

        :return: The last_known_version of this ShowSyncPolicyRequest.
        :rtype: int
        """
        return self._last_known_version

    @last_known_version.setter
    def last_known_version(self, last_known_version):
        """Sets the last_known_version of this ShowSyncPolicyRequest.

        lastKnownVersion

        :param last_known_version: The last_known_version of this ShowSyncPolicyRequest.
        :type last_known_version: int
        """
        self._last_known_version = last_known_version

    @property
    def supports_policy_deltas(self):
        """Gets the supports_policy_deltas of this ShowSyncPolicyRequest.

        supportsPolicyDeltas

        :return: The supports_policy_deltas of this ShowSyncPolicyRequest.
        :rtype: bool
        """
        return self._supports_policy_deltas

    @supports_policy_deltas.setter
    def supports_policy_deltas(self, supports_policy_deltas):
        """Sets the supports_policy_deltas of this ShowSyncPolicyRequest.

        supportsPolicyDeltas

        :param supports_policy_deltas: The supports_policy_deltas of this ShowSyncPolicyRequest.
        :type supports_policy_deltas: bool
        """
        self._supports_policy_deltas = supports_policy_deltas

    @property
    def is_return_policy_data(self):
        """Gets the is_return_policy_data of this ShowSyncPolicyRequest.

        isReturnPolicyData

        :return: The is_return_policy_data of this ShowSyncPolicyRequest.
        :rtype: bool
        """
        return self._is_return_policy_data

    @is_return_policy_data.setter
    def is_return_policy_data(self, is_return_policy_data):
        """Sets the is_return_policy_data of this ShowSyncPolicyRequest.

        isReturnPolicyData

        :param is_return_policy_data: The is_return_policy_data of this ShowSyncPolicyRequest.
        :type is_return_policy_data: bool
        """
        self._is_return_policy_data = is_return_policy_data

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
        if not isinstance(other, ShowSyncPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
