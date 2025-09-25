# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatRsp:

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
        'alias': 'str',
        'creator': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'top_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'alias': 'alias',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'top_time': 'top_time'
    }

    def __init__(self, id=None, title=None, alias=None, creator=None, create_time=None, update_time=None, top_time=None):
        r"""ChatRsp

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param title: **参数解释**： 对话名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type title: str
        :param alias: **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type alias: str
        :param creator: **参数解释**： 对话创建者。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type creator: str
        :param create_time: **参数解释**： 创建对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        :param update_time: **参数解释**： 更新对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type update_time: str
        :param top_time: **参数解释**： 置顶对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type top_time: str
        """
        
        

        self._id = None
        self._title = None
        self._alias = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._top_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if alias is not None:
            self.alias = alias
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if top_time is not None:
            self.top_time = top_time

    @property
    def id(self):
        r"""Gets the id of this ChatRsp.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this ChatRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChatRsp.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this ChatRsp.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this ChatRsp.

        **参数解释**： 对话名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The title of this ChatRsp.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ChatRsp.

        **参数解释**： 对话名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param title: The title of this ChatRsp.
        :type title: str
        """
        self._title = title

    @property
    def alias(self):
        r"""Gets the alias of this ChatRsp.

        **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The alias of this ChatRsp.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this ChatRsp.

        **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param alias: The alias of this ChatRsp.
        :type alias: str
        """
        self._alias = alias

    @property
    def creator(self):
        r"""Gets the creator of this ChatRsp.

        **参数解释**： 对话创建者。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The creator of this ChatRsp.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ChatRsp.

        **参数解释**： 对话创建者。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param creator: The creator of this ChatRsp.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ChatRsp.

        **参数解释**： 创建对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this ChatRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ChatRsp.

        **参数解释**： 创建对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this ChatRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ChatRsp.

        **参数解释**： 更新对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The update_time of this ChatRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ChatRsp.

        **参数解释**： 更新对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param update_time: The update_time of this ChatRsp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def top_time(self):
        r"""Gets the top_time of this ChatRsp.

        **参数解释**： 置顶对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The top_time of this ChatRsp.
        :rtype: str
        """
        return self._top_time

    @top_time.setter
    def top_time(self, top_time):
        r"""Sets the top_time of this ChatRsp.

        **参数解释**： 置顶对话时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param top_time: The top_time of this ChatRsp.
        :type top_time: str
        """
        self._top_time = top_time

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
        if not isinstance(other, ChatRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
