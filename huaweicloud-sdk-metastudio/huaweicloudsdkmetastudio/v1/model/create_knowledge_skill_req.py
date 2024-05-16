# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKnowledgeSkillReq:

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
        'identify': 'str'
    }

    attribute_map = {
        'name': 'name',
        'identify': 'identify'
    }

    def __init__(self, name=None, identify=None):
        """CreateKnowledgeSkillReq

        The model defined in huaweicloud sdk

        :param name: 技能名称。
        :type name: str
        :param identify: 技能标识。
        :type identify: str
        """
        
        

        self._name = None
        self._identify = None
        self.discriminator = None

        self.name = name
        self.identify = identify

    @property
    def name(self):
        """Gets the name of this CreateKnowledgeSkillReq.

        技能名称。

        :return: The name of this CreateKnowledgeSkillReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateKnowledgeSkillReq.

        技能名称。

        :param name: The name of this CreateKnowledgeSkillReq.
        :type name: str
        """
        self._name = name

    @property
    def identify(self):
        """Gets the identify of this CreateKnowledgeSkillReq.

        技能标识。

        :return: The identify of this CreateKnowledgeSkillReq.
        :rtype: str
        """
        return self._identify

    @identify.setter
    def identify(self, identify):
        """Sets the identify of this CreateKnowledgeSkillReq.

        技能标识。

        :param identify: The identify of this CreateKnowledgeSkillReq.
        :type identify: str
        """
        self._identify = identify

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
        if not isinstance(other, CreateKnowledgeSkillReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
