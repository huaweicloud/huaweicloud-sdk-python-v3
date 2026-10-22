# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomAnswersItem:

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
        'name': 'str',
        'description': 'str',
        'answers': 'list[str]',
        'referenced_rules': 'list[ReferencedRule]',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'answers': 'answers',
        'referenced_rules': 'referenced_rules',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, answers=None, referenced_rules=None, create_time=None, update_time=None):
        r"""CustomAnswersItem

        The model defined in huaweicloud sdk

        :param id: 代答库ID
        :type id: str
        :param name: 代答库名称
        :type name: str
        :param description: 代答库描述
        :type description: str
        :param answers: 答案列表（按seq排序）
        :type answers: list[str]
        :param referenced_rules: 引用的策略列表
        :type referenced_rules: list[:class:`huaweicloudsdkwaf.v1.ReferencedRule`]
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._answers = None
        self._referenced_rules = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if answers is not None:
            self.answers = answers
        if referenced_rules is not None:
            self.referenced_rules = referenced_rules
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this CustomAnswersItem.

        代答库ID

        :return: The id of this CustomAnswersItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomAnswersItem.

        代答库ID

        :param id: The id of this CustomAnswersItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CustomAnswersItem.

        代答库名称

        :return: The name of this CustomAnswersItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomAnswersItem.

        代答库名称

        :param name: The name of this CustomAnswersItem.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CustomAnswersItem.

        代答库描述

        :return: The description of this CustomAnswersItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CustomAnswersItem.

        代答库描述

        :param description: The description of this CustomAnswersItem.
        :type description: str
        """
        self._description = description

    @property
    def answers(self):
        r"""Gets the answers of this CustomAnswersItem.

        答案列表（按seq排序）

        :return: The answers of this CustomAnswersItem.
        :rtype: list[str]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        r"""Sets the answers of this CustomAnswersItem.

        答案列表（按seq排序）

        :param answers: The answers of this CustomAnswersItem.
        :type answers: list[str]
        """
        self._answers = answers

    @property
    def referenced_rules(self):
        r"""Gets the referenced_rules of this CustomAnswersItem.

        引用的策略列表

        :return: The referenced_rules of this CustomAnswersItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ReferencedRule`]
        """
        return self._referenced_rules

    @referenced_rules.setter
    def referenced_rules(self, referenced_rules):
        r"""Sets the referenced_rules of this CustomAnswersItem.

        引用的策略列表

        :param referenced_rules: The referenced_rules of this CustomAnswersItem.
        :type referenced_rules: list[:class:`huaweicloudsdkwaf.v1.ReferencedRule`]
        """
        self._referenced_rules = referenced_rules

    @property
    def create_time(self):
        r"""Gets the create_time of this CustomAnswersItem.

        创建时间

        :return: The create_time of this CustomAnswersItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CustomAnswersItem.

        创建时间

        :param create_time: The create_time of this CustomAnswersItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CustomAnswersItem.

        更新时间

        :return: The update_time of this CustomAnswersItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CustomAnswersItem.

        更新时间

        :param update_time: The update_time of this CustomAnswersItem.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, CustomAnswersItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
