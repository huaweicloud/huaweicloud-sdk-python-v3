# coding: utf-8

import re
import six





class CreateCcRuleRequestBody:


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
        'limit_num': 'int',
        'limit_period': 'int',
        'url': 'str',
        'mode': 'int',
        'action': 'CreateCcRuleRequestBodyAction',
        'tag_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'limit_num': 'limit_num',
        'limit_period': 'limit_period',
        'url': 'url',
        'mode': 'mode',
        'action': 'action',
        'tag_type': 'tag_type'
    }

    def __init__(self, description=None, limit_num=None, limit_period=None, url=None, mode=None, action=None, tag_type=None):
        """CreateCcRuleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._limit_num = None
        self._limit_period = None
        self._url = None
        self._mode = None
        self._action = None
        self._tag_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if limit_num is not None:
            self.limit_num = limit_num
        if limit_period is not None:
            self.limit_period = limit_period
        if url is not None:
            self.url = url
        if mode is not None:
            self.mode = mode
        if action is not None:
            self.action = action
        if tag_type is not None:
            self.tag_type = tag_type

    @property
    def description(self):
        """Gets the description of this CreateCcRuleRequestBody.

        规则描述

        :return: The description of this CreateCcRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCcRuleRequestBody.

        规则描述

        :param description: The description of this CreateCcRuleRequestBody.
        :type: str
        """
        self._description = description

    @property
    def limit_num(self):
        """Gets the limit_num of this CreateCcRuleRequestBody.

        限制频率次数

        :return: The limit_num of this CreateCcRuleRequestBody.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        """Sets the limit_num of this CreateCcRuleRequestBody.

        限制频率次数

        :param limit_num: The limit_num of this CreateCcRuleRequestBody.
        :type: int
        """
        self._limit_num = limit_num

    @property
    def limit_period(self):
        """Gets the limit_period of this CreateCcRuleRequestBody.

        限制频率单位时间

        :return: The limit_period of this CreateCcRuleRequestBody.
        :rtype: int
        """
        return self._limit_period

    @limit_period.setter
    def limit_period(self, limit_period):
        """Sets the limit_period of this CreateCcRuleRequestBody.

        限制频率单位时间

        :param limit_period: The limit_period of this CreateCcRuleRequestBody.
        :type: int
        """
        self._limit_period = limit_period

    @property
    def url(self):
        """Gets the url of this CreateCcRuleRequestBody.

        url

        :return: The url of this CreateCcRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateCcRuleRequestBody.

        url

        :param url: The url of this CreateCcRuleRequestBody.
        :type: str
        """
        self._url = url

    @property
    def mode(self):
        """Gets the mode of this CreateCcRuleRequestBody.

        工作模式：（0标准，1高级），高级模式参数无法在同一个接口同一份文档中用描述，参考console页面构建参数

        :return: The mode of this CreateCcRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateCcRuleRequestBody.

        工作模式：（0标准，1高级），高级模式参数无法在同一个接口同一份文档中用描述，参考console页面构建参数

        :param mode: The mode of this CreateCcRuleRequestBody.
        :type: int
        """
        self._mode = mode

    @property
    def action(self):
        """Gets the action of this CreateCcRuleRequestBody.


        :return: The action of this CreateCcRuleRequestBody.
        :rtype: CreateCcRuleRequestBodyAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateCcRuleRequestBody.


        :param action: The action of this CreateCcRuleRequestBody.
        :type: CreateCcRuleRequestBodyAction
        """
        self._action = action

    @property
    def tag_type(self):
        """Gets the tag_type of this CreateCcRuleRequestBody.

        限制频率次数

        :return: The tag_type of this CreateCcRuleRequestBody.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this CreateCcRuleRequestBody.

        限制频率次数

        :param tag_type: The tag_type of this CreateCcRuleRequestBody.
        :type: str
        """
        self._tag_type = tag_type

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateCcRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
