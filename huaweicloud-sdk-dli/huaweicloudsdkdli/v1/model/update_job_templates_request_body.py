# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateJobTemplatesRequestBody:

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
        'body': 'str',
        'group': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'body': 'body',
        'group': 'group',
        'description': 'description'
    }

    def __init__(self, name=None, body=None, group=None, description=None):
        """UpdateJobTemplatesRequestBody

        The model defined in huaweicloud sdk

        :param name: 名字
        :type name: str
        :param body: 模板内容
        :type body: str
        :param group: 分组
        :type group: str
        :param description: 描述信息
        :type description: str
        """
        
        

        self._name = None
        self._body = None
        self._group = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.body = body
        if group is not None:
            self.group = group
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this UpdateJobTemplatesRequestBody.

        名字

        :return: The name of this UpdateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateJobTemplatesRequestBody.

        名字

        :param name: The name of this UpdateJobTemplatesRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def body(self):
        """Gets the body of this UpdateJobTemplatesRequestBody.

        模板内容

        :return: The body of this UpdateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateJobTemplatesRequestBody.

        模板内容

        :param body: The body of this UpdateJobTemplatesRequestBody.
        :type body: str
        """
        self._body = body

    @property
    def group(self):
        """Gets the group of this UpdateJobTemplatesRequestBody.

        分组

        :return: The group of this UpdateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UpdateJobTemplatesRequestBody.

        分组

        :param group: The group of this UpdateJobTemplatesRequestBody.
        :type group: str
        """
        self._group = group

    @property
    def description(self):
        """Gets the description of this UpdateJobTemplatesRequestBody.

        描述信息

        :return: The description of this UpdateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateJobTemplatesRequestBody.

        描述信息

        :param description: The description of this UpdateJobTemplatesRequestBody.
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
        if not isinstance(other, UpdateJobTemplatesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
