# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivacyComplianceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'subtype_list': 'list[PrivacyComplianceSubtype]'
    }

    attribute_map = {
        'category': 'category',
        'subtype_list': 'subtype_list'
    }

    def __init__(self, category=None, subtype_list=None):
        """PrivacyComplianceInfo

        The model defined in huaweicloud sdk

        :param category: 隐私合规类型
        :type category: str
        :param subtype_list: 隐私合规子类型列表
        :type subtype_list: list[:class:`huaweicloudsdkdevsecurity.v1.PrivacyComplianceSubtype`]
        """
        
        

        self._category = None
        self._subtype_list = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if subtype_list is not None:
            self.subtype_list = subtype_list

    @property
    def category(self):
        """Gets the category of this PrivacyComplianceInfo.

        隐私合规类型

        :return: The category of this PrivacyComplianceInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PrivacyComplianceInfo.

        隐私合规类型

        :param category: The category of this PrivacyComplianceInfo.
        :type category: str
        """
        self._category = category

    @property
    def subtype_list(self):
        """Gets the subtype_list of this PrivacyComplianceInfo.

        隐私合规子类型列表

        :return: The subtype_list of this PrivacyComplianceInfo.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.PrivacyComplianceSubtype`]
        """
        return self._subtype_list

    @subtype_list.setter
    def subtype_list(self, subtype_list):
        """Sets the subtype_list of this PrivacyComplianceInfo.

        隐私合规子类型列表

        :param subtype_list: The subtype_list of this PrivacyComplianceInfo.
        :type subtype_list: list[:class:`huaweicloudsdkdevsecurity.v1.PrivacyComplianceSubtype`]
        """
        self._subtype_list = subtype_list

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
        if not isinstance(other, PrivacyComplianceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
