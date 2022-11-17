# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModCorpBasicInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'auto_user_create': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'auto_user_create': 'autoUserCreate'
    }

    def __init__(self, address=None, auto_user_create=None):
        """ModCorpBasicInfoDTO

        The model defined in huaweicloud sdk

        :param address: 企业所在地，最大长度为255个字符。 
        :type address: str
        :param auto_user_create: 企业自动开户开关。
        :type auto_user_create: bool
        """
        
        

        self._address = None
        self._auto_user_create = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if auto_user_create is not None:
            self.auto_user_create = auto_user_create

    @property
    def address(self):
        """Gets the address of this ModCorpBasicInfoDTO.

        企业所在地，最大长度为255个字符。 

        :return: The address of this ModCorpBasicInfoDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ModCorpBasicInfoDTO.

        企业所在地，最大长度为255个字符。 

        :param address: The address of this ModCorpBasicInfoDTO.
        :type address: str
        """
        self._address = address

    @property
    def auto_user_create(self):
        """Gets the auto_user_create of this ModCorpBasicInfoDTO.

        企业自动开户开关。

        :return: The auto_user_create of this ModCorpBasicInfoDTO.
        :rtype: bool
        """
        return self._auto_user_create

    @auto_user_create.setter
    def auto_user_create(self, auto_user_create):
        """Sets the auto_user_create of this ModCorpBasicInfoDTO.

        企业自动开户开关。

        :param auto_user_create: The auto_user_create of this ModCorpBasicInfoDTO.
        :type auto_user_create: bool
        """
        self._auto_user_create = auto_user_create

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
        if not isinstance(other, ModCorpBasicInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
