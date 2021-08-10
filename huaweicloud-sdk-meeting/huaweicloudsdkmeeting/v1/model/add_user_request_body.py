# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddUserRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'contact': 'str',
        'country': 'str',
        'dept_code': 'str',
        'title': 'str',
        'sort_level': 'int',
        'desc': 'str'
    }

    attribute_map = {
        'name': 'name',
        'contact': 'contact',
        'country': 'country',
        'dept_code': 'deptCode',
        'title': 'title',
        'sort_level': 'sortLevel',
        'desc': 'desc'
    }

    def __init__(self, name=None, contact=None, country=None, dept_code=None, title=None, sort_level=None, desc=None):
        """AddUserRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._contact = None
        self._country = None
        self._dept_code = None
        self._title = None
        self._sort_level = None
        self._desc = None
        self.discriminator = None

        self.name = name
        self.contact = contact
        if country is not None:
            self.country = country
        if dept_code is not None:
            self.dept_code = dept_code
        if title is not None:
            self.title = title
        if sort_level is not None:
            self.sort_level = sort_level
        if desc is not None:
            self.desc = desc

    @property
    def name(self):
        """Gets the name of this AddUserRequestBody.

        用户名称

        :return: The name of this AddUserRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddUserRequestBody.

        用户名称

        :param name: The name of this AddUserRequestBody.
        :type: str
        """
        self._name = name

    @property
    def contact(self):
        """Gets the contact of this AddUserRequestBody.

        后台自动识别是手机还是邮箱,若为手机号，则要求和国家码匹配

        :return: The contact of this AddUserRequestBody.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this AddUserRequestBody.

        后台自动识别是手机还是邮箱,若为手机号，则要求和国家码匹配

        :param contact: The contact of this AddUserRequestBody.
        :type: str
        """
        self._contact = contact

    @property
    def country(self):
        """Gets the country of this AddUserRequestBody.

        国家码。 国家和国家码的对应关系请参考:https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :return: The country of this AddUserRequestBody.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddUserRequestBody.

        国家码。 国家和国家码的对应关系请参考:https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :param country: The country of this AddUserRequestBody.
        :type: str
        """
        self._country = country

    @property
    def dept_code(self):
        """Gets the dept_code of this AddUserRequestBody.

        部门编号，若不携带则默认根部门

        :return: The dept_code of this AddUserRequestBody.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this AddUserRequestBody.

        部门编号，若不携带则默认根部门

        :param dept_code: The dept_code of this AddUserRequestBody.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def title(self):
        """Gets the title of this AddUserRequestBody.

        职位

        :return: The title of this AddUserRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AddUserRequestBody.

        职位

        :param title: The title of this AddUserRequestBody.
        :type: str
        """
        self._title = title

    @property
    def sort_level(self):
        """Gets the sort_level of this AddUserRequestBody.

        通讯录排序等级，序号越低优先级越高

        :return: The sort_level of this AddUserRequestBody.
        :rtype: int
        """
        return self._sort_level

    @sort_level.setter
    def sort_level(self, sort_level):
        """Sets the sort_level of this AddUserRequestBody.

        通讯录排序等级，序号越低优先级越高

        :param sort_level: The sort_level of this AddUserRequestBody.
        :type: int
        """
        self._sort_level = sort_level

    @property
    def desc(self):
        """Gets the desc of this AddUserRequestBody.

        备注

        :return: The desc of this AddUserRequestBody.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this AddUserRequestBody.

        备注

        :param desc: The desc of this AddUserRequestBody.
        :type: str
        """
        self._desc = desc

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
        if not isinstance(other, AddUserRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
