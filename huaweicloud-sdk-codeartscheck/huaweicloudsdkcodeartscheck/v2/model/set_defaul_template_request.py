# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetDefaulTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'ruleset_id': 'str',
        'language': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'ruleset_id': 'ruleset_id',
        'language': 'language'
    }

    def __init__(self, project_id=None, ruleset_id=None, language=None):
        r"""SetDefaulTemplateRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param ruleset_id: 规则集ID
        :type ruleset_id: str
        :param language: 规则集语言
        :type language: str
        """
        
        

        self._project_id = None
        self._ruleset_id = None
        self._language = None
        self.discriminator = None

        self.project_id = project_id
        self.ruleset_id = ruleset_id
        self.language = language

    @property
    def project_id(self):
        r"""Gets the project_id of this SetDefaulTemplateRequest.

        项目ID

        :return: The project_id of this SetDefaulTemplateRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SetDefaulTemplateRequest.

        项目ID

        :param project_id: The project_id of this SetDefaulTemplateRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ruleset_id(self):
        r"""Gets the ruleset_id of this SetDefaulTemplateRequest.

        规则集ID

        :return: The ruleset_id of this SetDefaulTemplateRequest.
        :rtype: str
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        r"""Sets the ruleset_id of this SetDefaulTemplateRequest.

        规则集ID

        :param ruleset_id: The ruleset_id of this SetDefaulTemplateRequest.
        :type ruleset_id: str
        """
        self._ruleset_id = ruleset_id

    @property
    def language(self):
        r"""Gets the language of this SetDefaulTemplateRequest.

        规则集语言

        :return: The language of this SetDefaulTemplateRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this SetDefaulTemplateRequest.

        规则集语言

        :param language: The language of this SetDefaulTemplateRequest.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, SetDefaulTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
