# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateRepositoryList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'projects': 'list[TemplateRepository]',
        'total': 'int'
    }

    attribute_map = {
        'projects': 'projects',
        'total': 'total'
    }

    def __init__(self, projects=None, total=None):
        r"""TemplateRepositoryList

        The model defined in huaweicloud sdk

        :param projects: 模板列表
        :type projects: list[:class:`huaweicloudsdkcodehub.v3.TemplateRepository`]
        :param total: 模板总数
        :type total: int
        """
        
        

        self._projects = None
        self._total = None
        self.discriminator = None

        if projects is not None:
            self.projects = projects
        if total is not None:
            self.total = total

    @property
    def projects(self):
        r"""Gets the projects of this TemplateRepositoryList.

        模板列表

        :return: The projects of this TemplateRepositoryList.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.TemplateRepository`]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        r"""Sets the projects of this TemplateRepositoryList.

        模板列表

        :param projects: The projects of this TemplateRepositoryList.
        :type projects: list[:class:`huaweicloudsdkcodehub.v3.TemplateRepository`]
        """
        self._projects = projects

    @property
    def total(self):
        r"""Gets the total of this TemplateRepositoryList.

        模板总数

        :return: The total of this TemplateRepositoryList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this TemplateRepositoryList.

        模板总数

        :param total: The total of this TemplateRepositoryList.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, TemplateRepositoryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
