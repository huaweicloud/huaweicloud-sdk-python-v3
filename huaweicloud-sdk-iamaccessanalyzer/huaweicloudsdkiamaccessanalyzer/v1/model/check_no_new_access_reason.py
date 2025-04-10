# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckNoNewAccessReason:

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
        'statement_id': 'str',
        'statement_index': 'int'
    }

    attribute_map = {
        'description': 'description',
        'statement_id': 'statement_id',
        'statement_index': 'statement_index'
    }

    def __init__(self, description=None, statement_id=None, statement_index=None):
        r"""CheckNoNewAccessReason

        The model defined in huaweicloud sdk

        :param description: 对访问权限检查结果的推理的描述。
        :type description: str
        :param statement_id: 新增权限statement的sid标识符。
        :type statement_id: str
        :param statement_index: 新增权限statement的index，从0开始。
        :type statement_index: int
        """
        
        

        self._description = None
        self._statement_id = None
        self._statement_index = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if statement_id is not None:
            self.statement_id = statement_id
        if statement_index is not None:
            self.statement_index = statement_index

    @property
    def description(self):
        r"""Gets the description of this CheckNoNewAccessReason.

        对访问权限检查结果的推理的描述。

        :return: The description of this CheckNoNewAccessReason.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CheckNoNewAccessReason.

        对访问权限检查结果的推理的描述。

        :param description: The description of this CheckNoNewAccessReason.
        :type description: str
        """
        self._description = description

    @property
    def statement_id(self):
        r"""Gets the statement_id of this CheckNoNewAccessReason.

        新增权限statement的sid标识符。

        :return: The statement_id of this CheckNoNewAccessReason.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this CheckNoNewAccessReason.

        新增权限statement的sid标识符。

        :param statement_id: The statement_id of this CheckNoNewAccessReason.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def statement_index(self):
        r"""Gets the statement_index of this CheckNoNewAccessReason.

        新增权限statement的index，从0开始。

        :return: The statement_index of this CheckNoNewAccessReason.
        :rtype: int
        """
        return self._statement_index

    @statement_index.setter
    def statement_index(self, statement_index):
        r"""Sets the statement_index of this CheckNoNewAccessReason.

        新增权限statement的index，从0开始。

        :param statement_index: The statement_index of this CheckNoNewAccessReason.
        :type statement_index: int
        """
        self._statement_index = statement_index

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
        if not isinstance(other, CheckNoNewAccessReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
