# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Answer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'id': 'str',
        'tags': 'list[str]',
        'answer_type': 'str',
        'qa_flow_entry': 'CbsFlowEntry'
    }

    attribute_map = {
        'content': 'content',
        'id': 'id',
        'tags': 'tags',
        'answer_type': 'answer_type',
        'qa_flow_entry': 'qa_flow_entry'
    }

    def __init__(self, content=None, id=None, tags=None, answer_type=None, qa_flow_entry=None):
        """Answer

        The model defined in huaweicloud sdk

        :param content: 答案内容
        :type content: str
        :param id: 答案Id
        :type id: str
        :param tags: 标签列表
        :type tags: list[str]
        :param answer_type: - TEXT:  - RICH_TEXT:  - FLOW:  - QA_PAIR:  
        :type answer_type: str
        :param qa_flow_entry: 
        :type qa_flow_entry: :class:`huaweicloudsdkosm.v2.CbsFlowEntry`
        """
        
        

        self._content = None
        self._id = None
        self._tags = None
        self._answer_type = None
        self._qa_flow_entry = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if id is not None:
            self.id = id
        if tags is not None:
            self.tags = tags
        if answer_type is not None:
            self.answer_type = answer_type
        if qa_flow_entry is not None:
            self.qa_flow_entry = qa_flow_entry

    @property
    def content(self):
        """Gets the content of this Answer.

        答案内容

        :return: The content of this Answer.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Answer.

        答案内容

        :param content: The content of this Answer.
        :type content: str
        """
        self._content = content

    @property
    def id(self):
        """Gets the id of this Answer.

        答案Id

        :return: The id of this Answer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Answer.

        答案Id

        :param id: The id of this Answer.
        :type id: str
        """
        self._id = id

    @property
    def tags(self):
        """Gets the tags of this Answer.

        标签列表

        :return: The tags of this Answer.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Answer.

        标签列表

        :param tags: The tags of this Answer.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def answer_type(self):
        """Gets the answer_type of this Answer.

        - TEXT:  - RICH_TEXT:  - FLOW:  - QA_PAIR:  

        :return: The answer_type of this Answer.
        :rtype: str
        """
        return self._answer_type

    @answer_type.setter
    def answer_type(self, answer_type):
        """Sets the answer_type of this Answer.

        - TEXT:  - RICH_TEXT:  - FLOW:  - QA_PAIR:  

        :param answer_type: The answer_type of this Answer.
        :type answer_type: str
        """
        self._answer_type = answer_type

    @property
    def qa_flow_entry(self):
        """Gets the qa_flow_entry of this Answer.

        :return: The qa_flow_entry of this Answer.
        :rtype: :class:`huaweicloudsdkosm.v2.CbsFlowEntry`
        """
        return self._qa_flow_entry

    @qa_flow_entry.setter
    def qa_flow_entry(self, qa_flow_entry):
        """Sets the qa_flow_entry of this Answer.

        :param qa_flow_entry: The qa_flow_entry of this Answer.
        :type qa_flow_entry: :class:`huaweicloudsdkosm.v2.CbsFlowEntry`
        """
        self._qa_flow_entry = qa_flow_entry

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
        if not isinstance(other, Answer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
