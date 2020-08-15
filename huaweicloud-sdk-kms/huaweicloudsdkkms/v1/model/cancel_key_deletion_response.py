# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CancelKeyDeletionResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'key_state': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_state': 'key_state'
    }

    def __init__(self, key_id=None, key_state=None):
        """CancelKeyDeletionResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._key_id = None
        self._key_state = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if key_state is not None:
            self.key_state = key_state

    @property
    def key_id(self):
        """Gets the key_id of this CancelKeyDeletionResponse.

        密钥ID

        :return: The key_id of this CancelKeyDeletionResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this CancelKeyDeletionResponse.

        密钥ID

        :param key_id: The key_id of this CancelKeyDeletionResponse.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_state(self):
        """Gets the key_state of this CancelKeyDeletionResponse.

        密钥状态： - 2为启用状态 - 3为禁用状态 - 4为计划删除状态 - 5为等待导入状态 - 7为冻结状态

        :return: The key_state of this CancelKeyDeletionResponse.
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        """Sets the key_state of this CancelKeyDeletionResponse.

        密钥状态： - 2为启用状态 - 3为禁用状态 - 4为计划删除状态 - 5为等待导入状态 - 7为冻结状态

        :param key_state: The key_state of this CancelKeyDeletionResponse.
        :type: str
        """
        self._key_state = key_state

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CancelKeyDeletionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
