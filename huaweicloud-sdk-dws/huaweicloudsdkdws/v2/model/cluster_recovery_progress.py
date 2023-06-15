# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterRecoveryProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'action_type': 'str',
        'unrestore_keys': 'str',
        'action_start_time': 'str',
        'action_end_time': 'str'
    }

    attribute_map = {
        'key': 'key',
        'action_type': 'action_type',
        'unrestore_keys': 'unrestore_keys',
        'action_start_time': 'action_start_time',
        'action_end_time': 'action_end_time'
    }

    def __init__(self, key=None, action_type=None, unrestore_keys=None, action_start_time=None, action_end_time=None):
        """ClusterRecoveryProgress

        The model defined in huaweicloud sdk

        :param key: key
        :type key: str
        :param action_type: action_type
        :type action_type: str
        :param unrestore_keys: unrestore_keys
        :type unrestore_keys: str
        :param action_start_time: action_start_time
        :type action_start_time: str
        :param action_end_time: action_end_time
        :type action_end_time: str
        """
        
        

        self._key = None
        self._action_type = None
        self._unrestore_keys = None
        self._action_start_time = None
        self._action_end_time = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if action_type is not None:
            self.action_type = action_type
        if unrestore_keys is not None:
            self.unrestore_keys = unrestore_keys
        if action_start_time is not None:
            self.action_start_time = action_start_time
        if action_end_time is not None:
            self.action_end_time = action_end_time

    @property
    def key(self):
        """Gets the key of this ClusterRecoveryProgress.

        key

        :return: The key of this ClusterRecoveryProgress.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ClusterRecoveryProgress.

        key

        :param key: The key of this ClusterRecoveryProgress.
        :type key: str
        """
        self._key = key

    @property
    def action_type(self):
        """Gets the action_type of this ClusterRecoveryProgress.

        action_type

        :return: The action_type of this ClusterRecoveryProgress.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ClusterRecoveryProgress.

        action_type

        :param action_type: The action_type of this ClusterRecoveryProgress.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def unrestore_keys(self):
        """Gets the unrestore_keys of this ClusterRecoveryProgress.

        unrestore_keys

        :return: The unrestore_keys of this ClusterRecoveryProgress.
        :rtype: str
        """
        return self._unrestore_keys

    @unrestore_keys.setter
    def unrestore_keys(self, unrestore_keys):
        """Sets the unrestore_keys of this ClusterRecoveryProgress.

        unrestore_keys

        :param unrestore_keys: The unrestore_keys of this ClusterRecoveryProgress.
        :type unrestore_keys: str
        """
        self._unrestore_keys = unrestore_keys

    @property
    def action_start_time(self):
        """Gets the action_start_time of this ClusterRecoveryProgress.

        action_start_time

        :return: The action_start_time of this ClusterRecoveryProgress.
        :rtype: str
        """
        return self._action_start_time

    @action_start_time.setter
    def action_start_time(self, action_start_time):
        """Sets the action_start_time of this ClusterRecoveryProgress.

        action_start_time

        :param action_start_time: The action_start_time of this ClusterRecoveryProgress.
        :type action_start_time: str
        """
        self._action_start_time = action_start_time

    @property
    def action_end_time(self):
        """Gets the action_end_time of this ClusterRecoveryProgress.

        action_end_time

        :return: The action_end_time of this ClusterRecoveryProgress.
        :rtype: str
        """
        return self._action_end_time

    @action_end_time.setter
    def action_end_time(self, action_end_time):
        """Sets the action_end_time of this ClusterRecoveryProgress.

        action_end_time

        :param action_end_time: The action_end_time of this ClusterRecoveryProgress.
        :type action_end_time: str
        """
        self._action_end_time = action_end_time

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
        if not isinstance(other, ClusterRecoveryProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
