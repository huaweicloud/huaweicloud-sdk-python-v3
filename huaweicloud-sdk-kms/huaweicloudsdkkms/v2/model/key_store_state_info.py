# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyStoreStateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keystore_id': 'str',
        'keystore_state': 'str'
    }

    attribute_map = {
        'keystore_id': 'keystore_id',
        'keystore_state': 'keystore_state'
    }

    def __init__(self, keystore_id=None, keystore_state=None):
        """KeyStoreStateInfo

        The model defined in huaweicloud sdk

        :param keystore_id: 密钥库ID
        :type keystore_id: str
        :param keystore_state: 密钥库状态
        :type keystore_state: str
        """
        
        

        self._keystore_id = None
        self._keystore_state = None
        self.discriminator = None

        if keystore_id is not None:
            self.keystore_id = keystore_id
        if keystore_state is not None:
            self.keystore_state = keystore_state

    @property
    def keystore_id(self):
        """Gets the keystore_id of this KeyStoreStateInfo.

        密钥库ID

        :return: The keystore_id of this KeyStoreStateInfo.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        """Sets the keystore_id of this KeyStoreStateInfo.

        密钥库ID

        :param keystore_id: The keystore_id of this KeyStoreStateInfo.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def keystore_state(self):
        """Gets the keystore_state of this KeyStoreStateInfo.

        密钥库状态

        :return: The keystore_state of this KeyStoreStateInfo.
        :rtype: str
        """
        return self._keystore_state

    @keystore_state.setter
    def keystore_state(self, keystore_state):
        """Sets the keystore_state of this KeyStoreStateInfo.

        密钥库状态

        :param keystore_state: The keystore_state of this KeyStoreStateInfo.
        :type keystore_state: str
        """
        self._keystore_state = keystore_state

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
        if not isinstance(other, KeyStoreStateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
