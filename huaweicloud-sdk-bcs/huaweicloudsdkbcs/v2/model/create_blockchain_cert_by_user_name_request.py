# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBlockchainCertByUserNameRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'org_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'org_name': 'org_name',
        'user_name': 'user_name'
    }

    def __init__(self, blockchain_id=None, org_name=None, user_name=None):
        """CreateBlockchainCertByUserNameRequest - a model defined in huaweicloud sdk"""
        
        

        self._blockchain_id = None
        self._org_name = None
        self._user_name = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        self.org_name = org_name
        self.user_name = user_name

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this CreateBlockchainCertByUserNameRequest.

        blockchainID

        :return: The blockchain_id of this CreateBlockchainCertByUserNameRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this CreateBlockchainCertByUserNameRequest.

        blockchainID

        :param blockchain_id: The blockchain_id of this CreateBlockchainCertByUserNameRequest.
        :type: str
        """
        self._blockchain_id = blockchain_id

    @property
    def org_name(self):
        """Gets the org_name of this CreateBlockchainCertByUserNameRequest.

        peer组织名称

        :return: The org_name of this CreateBlockchainCertByUserNameRequest.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this CreateBlockchainCertByUserNameRequest.

        peer组织名称

        :param org_name: The org_name of this CreateBlockchainCertByUserNameRequest.
        :type: str
        """
        self._org_name = org_name

    @property
    def user_name(self):
        """Gets the user_name of this CreateBlockchainCertByUserNameRequest.

        用户名称，字符串长度4-24，必须包含a-z，0-9，以小写字母开头，以小写字母或者数字结尾

        :return: The user_name of this CreateBlockchainCertByUserNameRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateBlockchainCertByUserNameRequest.

        用户名称，字符串长度4-24，必须包含a-z，0-9，以小写字母开头，以小写字母或者数字结尾

        :param user_name: The user_name of this CreateBlockchainCertByUserNameRequest.
        :type: str
        """
        self._user_name = user_name

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
        if not isinstance(other, CreateBlockchainCertByUserNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
