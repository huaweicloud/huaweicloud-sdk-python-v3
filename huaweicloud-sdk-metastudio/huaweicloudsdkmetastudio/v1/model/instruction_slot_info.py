# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstructionSlotInfo:

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
        'knowledge_library_list': 'list[SlotKnowledgeLibraryInfo]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'knowledge_library_list': 'knowledge_library_list'
    }

    def __init__(self, name=None, description=None, knowledge_library_list=None):
        r"""InstructionSlotInfo

        The model defined in huaweicloud sdk

        :param name: 槽位名称。
        :type name: str
        :param description: 槽位描述。
        :type description: str
        :param knowledge_library_list: 知识库列表
        :type knowledge_library_list: list[:class:`huaweicloudsdkmetastudio.v1.SlotKnowledgeLibraryInfo`]
        """
        
        

        self._name = None
        self._description = None
        self._knowledge_library_list = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if knowledge_library_list is not None:
            self.knowledge_library_list = knowledge_library_list

    @property
    def name(self):
        r"""Gets the name of this InstructionSlotInfo.

        槽位名称。

        :return: The name of this InstructionSlotInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstructionSlotInfo.

        槽位名称。

        :param name: The name of this InstructionSlotInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this InstructionSlotInfo.

        槽位描述。

        :return: The description of this InstructionSlotInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstructionSlotInfo.

        槽位描述。

        :param description: The description of this InstructionSlotInfo.
        :type description: str
        """
        self._description = description

    @property
    def knowledge_library_list(self):
        r"""Gets the knowledge_library_list of this InstructionSlotInfo.

        知识库列表

        :return: The knowledge_library_list of this InstructionSlotInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SlotKnowledgeLibraryInfo`]
        """
        return self._knowledge_library_list

    @knowledge_library_list.setter
    def knowledge_library_list(self, knowledge_library_list):
        r"""Sets the knowledge_library_list of this InstructionSlotInfo.

        知识库列表

        :param knowledge_library_list: The knowledge_library_list of this InstructionSlotInfo.
        :type knowledge_library_list: list[:class:`huaweicloudsdkmetastudio.v1.SlotKnowledgeLibraryInfo`]
        """
        self._knowledge_library_list = knowledge_library_list

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
        if not isinstance(other, InstructionSlotInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
