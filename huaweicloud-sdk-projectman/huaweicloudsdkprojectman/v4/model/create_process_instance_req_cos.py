# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProcessInstanceReqCos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'issue_id': 'str',
        'issue_category': 'str',
        'change_type': 'str',
        'before_change': 'str',
        'after_change': 'str'
    }

    attribute_map = {
        'number': 'number',
        'issue_id': 'issue_id',
        'issue_category': 'issue_category',
        'change_type': 'change_type',
        'before_change': 'before_change',
        'after_change': 'after_change'
    }

    def __init__(self, number=None, issue_id=None, issue_category=None, change_type=None, before_change=None, after_change=None):
        r"""CreateProcessInstanceReqCos

        The model defined in huaweicloud sdk

        :param number: 工作项编号
        :type number: str
        :param issue_id: 工作项ID
        :type issue_id: str
        :param issue_category: 工作项类型
        :type issue_category: str
        :param change_type: 变更类型
        :type change_type: str
        :param before_change: 变更前
        :type before_change: str
        :param after_change: 变更后
        :type after_change: str
        """
        
        

        self._number = None
        self._issue_id = None
        self._issue_category = None
        self._change_type = None
        self._before_change = None
        self._after_change = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if issue_id is not None:
            self.issue_id = issue_id
        if issue_category is not None:
            self.issue_category = issue_category
        if change_type is not None:
            self.change_type = change_type
        if before_change is not None:
            self.before_change = before_change
        if after_change is not None:
            self.after_change = after_change

    @property
    def number(self):
        r"""Gets the number of this CreateProcessInstanceReqCos.

        工作项编号

        :return: The number of this CreateProcessInstanceReqCos.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this CreateProcessInstanceReqCos.

        工作项编号

        :param number: The number of this CreateProcessInstanceReqCos.
        :type number: str
        """
        self._number = number

    @property
    def issue_id(self):
        r"""Gets the issue_id of this CreateProcessInstanceReqCos.

        工作项ID

        :return: The issue_id of this CreateProcessInstanceReqCos.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this CreateProcessInstanceReqCos.

        工作项ID

        :param issue_id: The issue_id of this CreateProcessInstanceReqCos.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def issue_category(self):
        r"""Gets the issue_category of this CreateProcessInstanceReqCos.

        工作项类型

        :return: The issue_category of this CreateProcessInstanceReqCos.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this CreateProcessInstanceReqCos.

        工作项类型

        :param issue_category: The issue_category of this CreateProcessInstanceReqCos.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def change_type(self):
        r"""Gets the change_type of this CreateProcessInstanceReqCos.

        变更类型

        :return: The change_type of this CreateProcessInstanceReqCos.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this CreateProcessInstanceReqCos.

        变更类型

        :param change_type: The change_type of this CreateProcessInstanceReqCos.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def before_change(self):
        r"""Gets the before_change of this CreateProcessInstanceReqCos.

        变更前

        :return: The before_change of this CreateProcessInstanceReqCos.
        :rtype: str
        """
        return self._before_change

    @before_change.setter
    def before_change(self, before_change):
        r"""Sets the before_change of this CreateProcessInstanceReqCos.

        变更前

        :param before_change: The before_change of this CreateProcessInstanceReqCos.
        :type before_change: str
        """
        self._before_change = before_change

    @property
    def after_change(self):
        r"""Gets the after_change of this CreateProcessInstanceReqCos.

        变更后

        :return: The after_change of this CreateProcessInstanceReqCos.
        :rtype: str
        """
        return self._after_change

    @after_change.setter
    def after_change(self, after_change):
        r"""Sets the after_change of this CreateProcessInstanceReqCos.

        变更后

        :param after_change: The after_change of this CreateProcessInstanceReqCos.
        :type after_change: str
        """
        self._after_change = after_change

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateProcessInstanceReqCos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
