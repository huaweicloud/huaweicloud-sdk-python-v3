# coding: utf-8

import pprint
import re

import six





class UpdateMember:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'vault_id': 'vault_id'
    }

    def __init__(self, status=None, vault_id=None):
        """UpdateMember - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._vault_id = None
        self.discriminator = None

        self.status = status
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def status(self):
        """Gets the status of this UpdateMember.

        备份共享状态

        :return: The status of this UpdateMember.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateMember.

        备份共享状态

        :param status: The status of this UpdateMember.
        :type: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this UpdateMember.

        共享的备份将存入的存储库，仅支持uuid 更新member状态的时候，如果是接受，必须传入vault_id，如果是拒绝，则无需

        :return: The vault_id of this UpdateMember.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this UpdateMember.

        共享的备份将存入的存储库，仅支持uuid 更新member状态的时候，如果是接受，必须传入vault_id，如果是拒绝，则无需

        :param vault_id: The vault_id of this UpdateMember.
        :type: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, UpdateMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
