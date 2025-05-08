# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRunbookRequestBody:

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
        'content': 'str',
        'description': 'str',
        'risk_level': 'str'
    }

    attribute_map = {
        'name': 'name',
        'content': 'content',
        'description': 'description',
        'risk_level': 'risk_level'
    }

    def __init__(self, name=None, content=None, description=None, risk_level=None):
        r"""UpdateRunbookRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业名称
        :type name: str
        :param content: 作业内容，DSL语句，最大长度64KB
        :type content: str
        :param description: 描述
        :type description: str
        :param risk_level: 风险等级
        :type risk_level: str
        """
        
        

        self._name = None
        self._content = None
        self._description = None
        self._risk_level = None
        self.discriminator = None

        self.name = name
        self.content = content
        if description is not None:
            self.description = description
        if risk_level is not None:
            self.risk_level = risk_level

    @property
    def name(self):
        r"""Gets the name of this UpdateRunbookRequestBody.

        作业名称

        :return: The name of this UpdateRunbookRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateRunbookRequestBody.

        作业名称

        :param name: The name of this UpdateRunbookRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        r"""Gets the content of this UpdateRunbookRequestBody.

        作业内容，DSL语句，最大长度64KB

        :return: The content of this UpdateRunbookRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this UpdateRunbookRequestBody.

        作业内容，DSL语句，最大长度64KB

        :param content: The content of this UpdateRunbookRequestBody.
        :type content: str
        """
        self._content = content

    @property
    def description(self):
        r"""Gets the description of this UpdateRunbookRequestBody.

        描述

        :return: The description of this UpdateRunbookRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateRunbookRequestBody.

        描述

        :param description: The description of this UpdateRunbookRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def risk_level(self):
        r"""Gets the risk_level of this UpdateRunbookRequestBody.

        风险等级

        :return: The risk_level of this UpdateRunbookRequestBody.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this UpdateRunbookRequestBody.

        风险等级

        :param risk_level: The risk_level of this UpdateRunbookRequestBody.
        :type risk_level: str
        """
        self._risk_level = risk_level

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
        if not isinstance(other, UpdateRunbookRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
