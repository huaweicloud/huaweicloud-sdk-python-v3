# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualificationCategory:

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
        'initial_issue_date': 'str',
        'issue_date': 'str',
        'expiry_date': 'str'
    }

    attribute_map = {
        'category': 'category',
        'initial_issue_date': 'initial_issue_date',
        'issue_date': 'issue_date',
        'expiry_date': 'expiry_date'
    }

    def __init__(self, category=None, initial_issue_date=None, issue_date=None, expiry_date=None):
        """QualificationCategory

        The model defined in huaweicloud sdk

        :param category: 诚信考核信息（非必有，依赖对应从业资格证板式）。 
        :type category: str
        :param initial_issue_date: 初次领证日期（非必有，依赖对应从业资格证板式） 
        :type initial_issue_date: str
        :param issue_date: 有效起始日期（非必有，依赖对应从业资格证板式） 
        :type issue_date: str
        :param expiry_date: 有效期至 
        :type expiry_date: str
        """
        
        

        self._category = None
        self._initial_issue_date = None
        self._issue_date = None
        self._expiry_date = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if initial_issue_date is not None:
            self.initial_issue_date = initial_issue_date
        if issue_date is not None:
            self.issue_date = issue_date
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def category(self):
        """Gets the category of this QualificationCategory.

        诚信考核信息（非必有，依赖对应从业资格证板式）。 

        :return: The category of this QualificationCategory.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this QualificationCategory.

        诚信考核信息（非必有，依赖对应从业资格证板式）。 

        :param category: The category of this QualificationCategory.
        :type category: str
        """
        self._category = category

    @property
    def initial_issue_date(self):
        """Gets the initial_issue_date of this QualificationCategory.

        初次领证日期（非必有，依赖对应从业资格证板式） 

        :return: The initial_issue_date of this QualificationCategory.
        :rtype: str
        """
        return self._initial_issue_date

    @initial_issue_date.setter
    def initial_issue_date(self, initial_issue_date):
        """Sets the initial_issue_date of this QualificationCategory.

        初次领证日期（非必有，依赖对应从业资格证板式） 

        :param initial_issue_date: The initial_issue_date of this QualificationCategory.
        :type initial_issue_date: str
        """
        self._initial_issue_date = initial_issue_date

    @property
    def issue_date(self):
        """Gets the issue_date of this QualificationCategory.

        有效起始日期（非必有，依赖对应从业资格证板式） 

        :return: The issue_date of this QualificationCategory.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this QualificationCategory.

        有效起始日期（非必有，依赖对应从业资格证板式） 

        :param issue_date: The issue_date of this QualificationCategory.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this QualificationCategory.

        有效期至 

        :return: The expiry_date of this QualificationCategory.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this QualificationCategory.

        有效期至 

        :param expiry_date: The expiry_date of this QualificationCategory.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

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
        if not isinstance(other, QualificationCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
