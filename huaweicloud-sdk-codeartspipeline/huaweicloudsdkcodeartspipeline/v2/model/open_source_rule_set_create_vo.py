# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenSourceRuleSetCreateVO:

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
        'parent_id': 'str',
        'content': 'OpenSourceRuleContent'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'content': 'content'
    }

    def __init__(self, name=None, parent_id=None, content=None):
        """OpenSourceRuleSetCreateVO

        The model defined in huaweicloud sdk

        :param name: 开源治理策略名称
        :type name: str
        :param parent_id: 开源治理策略父策略ID
        :type parent_id: str
        :param content: 
        :type content: :class:`huaweicloudsdkcodeartspipeline.v2.OpenSourceRuleContent`
        """
        
        

        self._name = None
        self._parent_id = None
        self._content = None
        self.discriminator = None

        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        self.content = content

    @property
    def name(self):
        """Gets the name of this OpenSourceRuleSetCreateVO.

        开源治理策略名称

        :return: The name of this OpenSourceRuleSetCreateVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenSourceRuleSetCreateVO.

        开源治理策略名称

        :param name: The name of this OpenSourceRuleSetCreateVO.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this OpenSourceRuleSetCreateVO.

        开源治理策略父策略ID

        :return: The parent_id of this OpenSourceRuleSetCreateVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this OpenSourceRuleSetCreateVO.

        开源治理策略父策略ID

        :param parent_id: The parent_id of this OpenSourceRuleSetCreateVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def content(self):
        """Gets the content of this OpenSourceRuleSetCreateVO.

        :return: The content of this OpenSourceRuleSetCreateVO.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.OpenSourceRuleContent`
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this OpenSourceRuleSetCreateVO.

        :param content: The content of this OpenSourceRuleSetCreateVO.
        :type content: :class:`huaweicloudsdkcodeartspipeline.v2.OpenSourceRuleContent`
        """
        self._content = content

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
        if not isinstance(other, OpenSourceRuleSetCreateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
