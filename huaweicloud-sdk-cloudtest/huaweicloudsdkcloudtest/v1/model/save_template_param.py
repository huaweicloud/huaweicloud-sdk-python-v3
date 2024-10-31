# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveTemplateParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'mindmap_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'mindmap_id': 'mindmap_id',
        'name': 'name'
    }

    def __init__(self, description=None, mindmap_id=None, name=None):
        """SaveTemplateParam

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param mindmap_id: 脑图ID
        :type mindmap_id: str
        :param name: 脑图名称
        :type name: str
        """
        
        

        self._description = None
        self._mindmap_id = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this SaveTemplateParam.

        描述

        :return: The description of this SaveTemplateParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SaveTemplateParam.

        描述

        :param description: The description of this SaveTemplateParam.
        :type description: str
        """
        self._description = description

    @property
    def mindmap_id(self):
        """Gets the mindmap_id of this SaveTemplateParam.

        脑图ID

        :return: The mindmap_id of this SaveTemplateParam.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        """Sets the mindmap_id of this SaveTemplateParam.

        脑图ID

        :param mindmap_id: The mindmap_id of this SaveTemplateParam.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def name(self):
        """Gets the name of this SaveTemplateParam.

        脑图名称

        :return: The name of this SaveTemplateParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTemplateParam.

        脑图名称

        :param name: The name of this SaveTemplateParam.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, SaveTemplateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
