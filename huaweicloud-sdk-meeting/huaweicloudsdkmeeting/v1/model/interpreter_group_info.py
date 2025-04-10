# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterpreterGroupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'group_type': 'str',
        'first_language': 'str',
        'second_language': 'str',
        'interpreters': 'list[InterpreterInfo]'
    }

    attribute_map = {
        'group_id': 'groupID',
        'group_name': 'groupName',
        'group_type': 'groupType',
        'first_language': 'firstLanguage',
        'second_language': 'secondLanguage',
        'interpreters': 'interpreters'
    }

    def __init__(self, group_id=None, group_name=None, group_type=None, first_language=None, second_language=None, interpreters=None):
        r"""InterpreterGroupInfo

        The model defined in huaweicloud sdk

        :param group_id: 传译组序号。
        :type group_id: str
        :param group_name: 传译组名称。
        :type group_name: str
        :param group_type: 传译组类型，MANUAL：人工传译，AI：AI传译。默认MANUAL。
        :type group_type: str
        :param first_language: 传译组支持的第一种语言。
        :type first_language: str
        :param second_language: 传译组支持的第二种语言。
        :type second_language: str
        :param interpreters: 传译员列表。
        :type interpreters: list[:class:`huaweicloudsdkmeeting.v1.InterpreterInfo`]
        """
        
        

        self._group_id = None
        self._group_name = None
        self._group_type = None
        self._first_language = None
        self._second_language = None
        self._interpreters = None
        self.discriminator = None

        self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if group_type is not None:
            self.group_type = group_type
        self.first_language = first_language
        self.second_language = second_language
        if interpreters is not None:
            self.interpreters = interpreters

    @property
    def group_id(self):
        r"""Gets the group_id of this InterpreterGroupInfo.

        传译组序号。

        :return: The group_id of this InterpreterGroupInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this InterpreterGroupInfo.

        传译组序号。

        :param group_id: The group_id of this InterpreterGroupInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this InterpreterGroupInfo.

        传译组名称。

        :return: The group_name of this InterpreterGroupInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this InterpreterGroupInfo.

        传译组名称。

        :param group_name: The group_name of this InterpreterGroupInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_type(self):
        r"""Gets the group_type of this InterpreterGroupInfo.

        传译组类型，MANUAL：人工传译，AI：AI传译。默认MANUAL。

        :return: The group_type of this InterpreterGroupInfo.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this InterpreterGroupInfo.

        传译组类型，MANUAL：人工传译，AI：AI传译。默认MANUAL。

        :param group_type: The group_type of this InterpreterGroupInfo.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def first_language(self):
        r"""Gets the first_language of this InterpreterGroupInfo.

        传译组支持的第一种语言。

        :return: The first_language of this InterpreterGroupInfo.
        :rtype: str
        """
        return self._first_language

    @first_language.setter
    def first_language(self, first_language):
        r"""Sets the first_language of this InterpreterGroupInfo.

        传译组支持的第一种语言。

        :param first_language: The first_language of this InterpreterGroupInfo.
        :type first_language: str
        """
        self._first_language = first_language

    @property
    def second_language(self):
        r"""Gets the second_language of this InterpreterGroupInfo.

        传译组支持的第二种语言。

        :return: The second_language of this InterpreterGroupInfo.
        :rtype: str
        """
        return self._second_language

    @second_language.setter
    def second_language(self, second_language):
        r"""Sets the second_language of this InterpreterGroupInfo.

        传译组支持的第二种语言。

        :param second_language: The second_language of this InterpreterGroupInfo.
        :type second_language: str
        """
        self._second_language = second_language

    @property
    def interpreters(self):
        r"""Gets the interpreters of this InterpreterGroupInfo.

        传译员列表。

        :return: The interpreters of this InterpreterGroupInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.InterpreterInfo`]
        """
        return self._interpreters

    @interpreters.setter
    def interpreters(self, interpreters):
        r"""Sets the interpreters of this InterpreterGroupInfo.

        传译员列表。

        :param interpreters: The interpreters of this InterpreterGroupInfo.
        :type interpreters: list[:class:`huaweicloudsdkmeeting.v1.InterpreterInfo`]
        """
        self._interpreters = interpreters

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
        if not isinstance(other, InterpreterGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
