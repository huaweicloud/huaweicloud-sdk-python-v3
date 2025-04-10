# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLineGroupsRequestBody:

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
        'description': 'str',
        'lines': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'lines': 'lines'
    }

    def __init__(self, name=None, description=None, lines=None):
        r"""UpdateLineGroupsRequestBody

        The model defined in huaweicloud sdk

        :param name: 线路分组名称。 不能与自定义线路名称、预制线路名称重复。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。
        :type name: str
        :param description: 线路分组的描述信息。长度不超过255个字符。默认值为空。
        :type description: str
        :param lines: 线路列表。
        :type lines: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._lines = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.lines = lines

    @property
    def name(self):
        r"""Gets the name of this UpdateLineGroupsRequestBody.

        线路分组名称。 不能与自定义线路名称、预制线路名称重复。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :return: The name of this UpdateLineGroupsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateLineGroupsRequestBody.

        线路分组名称。 不能与自定义线路名称、预制线路名称重复。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :param name: The name of this UpdateLineGroupsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateLineGroupsRequestBody.

        线路分组的描述信息。长度不超过255个字符。默认值为空。

        :return: The description of this UpdateLineGroupsRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateLineGroupsRequestBody.

        线路分组的描述信息。长度不超过255个字符。默认值为空。

        :param description: The description of this UpdateLineGroupsRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def lines(self):
        r"""Gets the lines of this UpdateLineGroupsRequestBody.

        线路列表。

        :return: The lines of this UpdateLineGroupsRequestBody.
        :rtype: list[str]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this UpdateLineGroupsRequestBody.

        线路列表。

        :param lines: The lines of this UpdateLineGroupsRequestBody.
        :type lines: list[str]
        """
        self._lines = lines

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
        if not isinstance(other, UpdateLineGroupsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
