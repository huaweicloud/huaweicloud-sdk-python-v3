# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntellectualPropertyV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_type': 'str',
        'ip_area': 'str',
        'ip_number': 'str',
        'ip_content': 'str'
    }

    attribute_map = {
        'ip_type': 'ip_type',
        'ip_area': 'ip_area',
        'ip_number': 'ip_number',
        'ip_content': 'ip_content'
    }

    def __init__(self, ip_type=None, ip_area=None, ip_number=None, ip_content=None):
        r"""IntellectualPropertyV2

        The model defined in huaweicloud sdk

        :param ip_type: 知识产权类型,分：著作权-copyright、商标权-trademark、专利权-patent
        :type ip_type: str
        :param ip_area: 知识产权注册国家/地区
        :type ip_area: str
        :param ip_number: 商标注册号/专利申请号
        :type ip_number: str
        :param ip_content: 知识产权情况简述
        :type ip_content: str
        """
        
        

        self._ip_type = None
        self._ip_area = None
        self._ip_number = None
        self._ip_content = None
        self.discriminator = None

        if ip_type is not None:
            self.ip_type = ip_type
        if ip_area is not None:
            self.ip_area = ip_area
        if ip_number is not None:
            self.ip_number = ip_number
        if ip_content is not None:
            self.ip_content = ip_content

    @property
    def ip_type(self):
        r"""Gets the ip_type of this IntellectualPropertyV2.

        知识产权类型,分：著作权-copyright、商标权-trademark、专利权-patent

        :return: The ip_type of this IntellectualPropertyV2.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this IntellectualPropertyV2.

        知识产权类型,分：著作权-copyright、商标权-trademark、专利权-patent

        :param ip_type: The ip_type of this IntellectualPropertyV2.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip_area(self):
        r"""Gets the ip_area of this IntellectualPropertyV2.

        知识产权注册国家/地区

        :return: The ip_area of this IntellectualPropertyV2.
        :rtype: str
        """
        return self._ip_area

    @ip_area.setter
    def ip_area(self, ip_area):
        r"""Sets the ip_area of this IntellectualPropertyV2.

        知识产权注册国家/地区

        :param ip_area: The ip_area of this IntellectualPropertyV2.
        :type ip_area: str
        """
        self._ip_area = ip_area

    @property
    def ip_number(self):
        r"""Gets the ip_number of this IntellectualPropertyV2.

        商标注册号/专利申请号

        :return: The ip_number of this IntellectualPropertyV2.
        :rtype: str
        """
        return self._ip_number

    @ip_number.setter
    def ip_number(self, ip_number):
        r"""Sets the ip_number of this IntellectualPropertyV2.

        商标注册号/专利申请号

        :param ip_number: The ip_number of this IntellectualPropertyV2.
        :type ip_number: str
        """
        self._ip_number = ip_number

    @property
    def ip_content(self):
        r"""Gets the ip_content of this IntellectualPropertyV2.

        知识产权情况简述

        :return: The ip_content of this IntellectualPropertyV2.
        :rtype: str
        """
        return self._ip_content

    @ip_content.setter
    def ip_content(self, ip_content):
        r"""Sets the ip_content of this IntellectualPropertyV2.

        知识产权情况简述

        :param ip_content: The ip_content of this IntellectualPropertyV2.
        :type ip_content: str
        """
        self._ip_content = ip_content

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
        if not isinstance(other, IntellectualPropertyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
