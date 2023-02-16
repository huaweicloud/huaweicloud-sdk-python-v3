# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QaFeedbackReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'question': 'str',
        'feedback_id': 'str',
        'qa_pair_source': 'str',
        'feedback_option_id': 'str',
        'feedback_description': 'str',
        'qa_pair_id': 'str',
        'request_id': 'str',
        'feedback_source': 'str',
        'flow_node_id': 'str'
    }

    attribute_map = {
        'question': 'question',
        'feedback_id': 'feedback_id',
        'qa_pair_source': 'qa_pair_source',
        'feedback_option_id': 'feedback_option_id',
        'feedback_description': 'feedback_description',
        'qa_pair_id': 'qa_pair_id',
        'request_id': 'request_id',
        'feedback_source': 'feedback_source',
        'flow_node_id': 'flow_node_id'
    }

    def __init__(self, question=None, feedback_id=None, qa_pair_source=None, feedback_option_id=None, feedback_description=None, qa_pair_id=None, request_id=None, feedback_source=None, flow_node_id=None):
        """QaFeedbackReq

        The model defined in huaweicloud sdk

        :param question: 用户问题
        :type question: str
        :param feedback_id: 反馈记录Id
        :type feedback_id: str
        :param qa_pair_source: - IROBOT_QA:  - RECOMMEND_WORD_QA:  
        :type qa_pair_source: str
        :param feedback_option_id: 反馈选项id
        :type feedback_option_id: str
        :param feedback_description: 反馈描述
        :type feedback_description: str
        :param qa_pair_id: 语料id
        :type qa_pair_id: str
        :param request_id: 请求id
        :type request_id: str
        :param feedback_source: - FAQ:  - FLOW:  
        :type feedback_source: str
        :param flow_node_id: 流程节点Id
        :type flow_node_id: str
        """
        
        

        self._question = None
        self._feedback_id = None
        self._qa_pair_source = None
        self._feedback_option_id = None
        self._feedback_description = None
        self._qa_pair_id = None
        self._request_id = None
        self._feedback_source = None
        self._flow_node_id = None
        self.discriminator = None

        self.question = question
        if feedback_id is not None:
            self.feedback_id = feedback_id
        if qa_pair_source is not None:
            self.qa_pair_source = qa_pair_source
        if feedback_option_id is not None:
            self.feedback_option_id = feedback_option_id
        if feedback_description is not None:
            self.feedback_description = feedback_description
        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id
        if request_id is not None:
            self.request_id = request_id
        self.feedback_source = feedback_source
        if flow_node_id is not None:
            self.flow_node_id = flow_node_id

    @property
    def question(self):
        """Gets the question of this QaFeedbackReq.

        用户问题

        :return: The question of this QaFeedbackReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this QaFeedbackReq.

        用户问题

        :param question: The question of this QaFeedbackReq.
        :type question: str
        """
        self._question = question

    @property
    def feedback_id(self):
        """Gets the feedback_id of this QaFeedbackReq.

        反馈记录Id

        :return: The feedback_id of this QaFeedbackReq.
        :rtype: str
        """
        return self._feedback_id

    @feedback_id.setter
    def feedback_id(self, feedback_id):
        """Sets the feedback_id of this QaFeedbackReq.

        反馈记录Id

        :param feedback_id: The feedback_id of this QaFeedbackReq.
        :type feedback_id: str
        """
        self._feedback_id = feedback_id

    @property
    def qa_pair_source(self):
        """Gets the qa_pair_source of this QaFeedbackReq.

        - IROBOT_QA:  - RECOMMEND_WORD_QA:  

        :return: The qa_pair_source of this QaFeedbackReq.
        :rtype: str
        """
        return self._qa_pair_source

    @qa_pair_source.setter
    def qa_pair_source(self, qa_pair_source):
        """Sets the qa_pair_source of this QaFeedbackReq.

        - IROBOT_QA:  - RECOMMEND_WORD_QA:  

        :param qa_pair_source: The qa_pair_source of this QaFeedbackReq.
        :type qa_pair_source: str
        """
        self._qa_pair_source = qa_pair_source

    @property
    def feedback_option_id(self):
        """Gets the feedback_option_id of this QaFeedbackReq.

        反馈选项id

        :return: The feedback_option_id of this QaFeedbackReq.
        :rtype: str
        """
        return self._feedback_option_id

    @feedback_option_id.setter
    def feedback_option_id(self, feedback_option_id):
        """Sets the feedback_option_id of this QaFeedbackReq.

        反馈选项id

        :param feedback_option_id: The feedback_option_id of this QaFeedbackReq.
        :type feedback_option_id: str
        """
        self._feedback_option_id = feedback_option_id

    @property
    def feedback_description(self):
        """Gets the feedback_description of this QaFeedbackReq.

        反馈描述

        :return: The feedback_description of this QaFeedbackReq.
        :rtype: str
        """
        return self._feedback_description

    @feedback_description.setter
    def feedback_description(self, feedback_description):
        """Sets the feedback_description of this QaFeedbackReq.

        反馈描述

        :param feedback_description: The feedback_description of this QaFeedbackReq.
        :type feedback_description: str
        """
        self._feedback_description = feedback_description

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this QaFeedbackReq.

        语料id

        :return: The qa_pair_id of this QaFeedbackReq.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this QaFeedbackReq.

        语料id

        :param qa_pair_id: The qa_pair_id of this QaFeedbackReq.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

    @property
    def request_id(self):
        """Gets the request_id of this QaFeedbackReq.

        请求id

        :return: The request_id of this QaFeedbackReq.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this QaFeedbackReq.

        请求id

        :param request_id: The request_id of this QaFeedbackReq.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def feedback_source(self):
        """Gets the feedback_source of this QaFeedbackReq.

        - FAQ:  - FLOW:  

        :return: The feedback_source of this QaFeedbackReq.
        :rtype: str
        """
        return self._feedback_source

    @feedback_source.setter
    def feedback_source(self, feedback_source):
        """Sets the feedback_source of this QaFeedbackReq.

        - FAQ:  - FLOW:  

        :param feedback_source: The feedback_source of this QaFeedbackReq.
        :type feedback_source: str
        """
        self._feedback_source = feedback_source

    @property
    def flow_node_id(self):
        """Gets the flow_node_id of this QaFeedbackReq.

        流程节点Id

        :return: The flow_node_id of this QaFeedbackReq.
        :rtype: str
        """
        return self._flow_node_id

    @flow_node_id.setter
    def flow_node_id(self, flow_node_id):
        """Sets the flow_node_id of this QaFeedbackReq.

        流程节点Id

        :param flow_node_id: The flow_node_id of this QaFeedbackReq.
        :type flow_node_id: str
        """
        self._flow_node_id = flow_node_id

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
        if not isinstance(other, QaFeedbackReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
