# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateSimpleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'title': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description'
    }

    def __init__(self, id=None, title=None, description=None):
        r"""TemplateSimpleInfo

        The model defined in huaweicloud sdk

        :param id: 模板id。
        :type id: str
        :param title: 模板名。
        :type title: str
        :param description: 模板描述。
        :type description: str
        """
        
        

        self._id = None
        self._title = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this TemplateSimpleInfo.

        模板id。

        :return: The id of this TemplateSimpleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TemplateSimpleInfo.

        模板id。

        :param id: The id of this TemplateSimpleInfo.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this TemplateSimpleInfo.

        模板名。

        :return: The title of this TemplateSimpleInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this TemplateSimpleInfo.

        模板名。

        :param title: The title of this TemplateSimpleInfo.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this TemplateSimpleInfo.

        模板描述。

        :return: The description of this TemplateSimpleInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateSimpleInfo.

        模板描述。

        :param description: The description of this TemplateSimpleInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, TemplateSimpleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
