# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContactV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'contact_way': 'int',
        'contact_value': 'str',
        'area_code': 'str',
        'verified_id': 'str'
    }

    attribute_map = {
        'contact_way': 'contact_way',
        'contact_value': 'contact_value',
        'area_code': 'area_code',
        'verified_id': 'verified_id'
    }

    def __init__(self, contact_way=None, contact_value=None, area_code=None, verified_id=None):
        """ContactV2

        The model defined in huaweicloud sdk

        :param contact_way: 联系方式类型
        :type contact_way: int
        :param contact_value: 联系方式值
        :type contact_value: str
        :param area_code: 国家码
        :type area_code: str
        :param verified_id: 验证序列号
        :type verified_id: str
        """
        
        

        self._contact_way = None
        self._contact_value = None
        self._area_code = None
        self._verified_id = None
        self.discriminator = None

        if contact_way is not None:
            self.contact_way = contact_way
        if contact_value is not None:
            self.contact_value = contact_value
        if area_code is not None:
            self.area_code = area_code
        if verified_id is not None:
            self.verified_id = verified_id

    @property
    def contact_way(self):
        """Gets the contact_way of this ContactV2.

        联系方式类型

        :return: The contact_way of this ContactV2.
        :rtype: int
        """
        return self._contact_way

    @contact_way.setter
    def contact_way(self, contact_way):
        """Sets the contact_way of this ContactV2.

        联系方式类型

        :param contact_way: The contact_way of this ContactV2.
        :type contact_way: int
        """
        self._contact_way = contact_way

    @property
    def contact_value(self):
        """Gets the contact_value of this ContactV2.

        联系方式值

        :return: The contact_value of this ContactV2.
        :rtype: str
        """
        return self._contact_value

    @contact_value.setter
    def contact_value(self, contact_value):
        """Sets the contact_value of this ContactV2.

        联系方式值

        :param contact_value: The contact_value of this ContactV2.
        :type contact_value: str
        """
        self._contact_value = contact_value

    @property
    def area_code(self):
        """Gets the area_code of this ContactV2.

        国家码

        :return: The area_code of this ContactV2.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this ContactV2.

        国家码

        :param area_code: The area_code of this ContactV2.
        :type area_code: str
        """
        self._area_code = area_code

    @property
    def verified_id(self):
        """Gets the verified_id of this ContactV2.

        验证序列号

        :return: The verified_id of this ContactV2.
        :rtype: str
        """
        return self._verified_id

    @verified_id.setter
    def verified_id(self, verified_id):
        """Sets the verified_id of this ContactV2.

        验证序列号

        :param verified_id: The verified_id of this ContactV2.
        :type verified_id: str
        """
        self._verified_id = verified_id

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
        if not isinstance(other, ContactV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
