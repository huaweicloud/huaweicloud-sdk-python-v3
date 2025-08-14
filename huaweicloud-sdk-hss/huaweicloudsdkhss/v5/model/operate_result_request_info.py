# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateResultRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'result_id': 'str',
        'event_type': 'int',
        'occur_time': 'int',
        'file_hash': 'str',
        'file_path': 'str',
        'file_attr': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'result_id': 'result_id',
        'event_type': 'event_type',
        'occur_time': 'occur_time',
        'file_hash': 'file_hash',
        'file_path': 'file_path',
        'file_attr': 'file_attr'
    }

    def __init__(self, agent_id=None, result_id=None, event_type=None, occur_time=None, file_hash=None, file_path=None, file_attr=None):
        r"""OperateResultRequestInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param result_id: 病毒查杀结果ID
        :type result_id: str
        :param event_type: 事件类型
        :type event_type: int
        :param occur_time: **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 
        :type occur_time: int
        :param file_hash: **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 
        :type file_hash: str
        :param file_path: **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 
        :type file_path: str
        :param file_attr: **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 
        :type file_attr: str
        """
        
        

        self._agent_id = None
        self._result_id = None
        self._event_type = None
        self._occur_time = None
        self._file_hash = None
        self._file_path = None
        self._file_attr = None
        self.discriminator = None

        self.agent_id = agent_id
        self.result_id = result_id
        self.event_type = event_type
        if occur_time is not None:
            self.occur_time = occur_time
        self.file_hash = file_hash
        self.file_path = file_path
        self.file_attr = file_attr

    @property
    def agent_id(self):
        r"""Gets the agent_id of this OperateResultRequestInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this OperateResultRequestInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this OperateResultRequestInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this OperateResultRequestInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def result_id(self):
        r"""Gets the result_id of this OperateResultRequestInfo.

        病毒查杀结果ID

        :return: The result_id of this OperateResultRequestInfo.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        r"""Sets the result_id of this OperateResultRequestInfo.

        病毒查杀结果ID

        :param result_id: The result_id of this OperateResultRequestInfo.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def event_type(self):
        r"""Gets the event_type of this OperateResultRequestInfo.

        事件类型

        :return: The event_type of this OperateResultRequestInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this OperateResultRequestInfo.

        事件类型

        :param event_type: The event_type of this OperateResultRequestInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def occur_time(self):
        r"""Gets the occur_time of this OperateResultRequestInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The occur_time of this OperateResultRequestInfo.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this OperateResultRequestInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :param occur_time: The occur_time of this OperateResultRequestInfo.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def file_hash(self):
        r"""Gets the file_hash of this OperateResultRequestInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :return: The file_hash of this OperateResultRequestInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this OperateResultRequestInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :param file_hash: The file_hash of this OperateResultRequestInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_path(self):
        r"""Gets the file_path of this OperateResultRequestInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_path of this OperateResultRequestInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this OperateResultRequestInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :param file_path: The file_path of this OperateResultRequestInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_attr(self):
        r"""Gets the file_attr of this OperateResultRequestInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :return: The file_attr of this OperateResultRequestInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        r"""Sets the file_attr of this OperateResultRequestInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :param file_attr: The file_attr of this OperateResultRequestInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

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
        if not isinstance(other, OperateResultRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
