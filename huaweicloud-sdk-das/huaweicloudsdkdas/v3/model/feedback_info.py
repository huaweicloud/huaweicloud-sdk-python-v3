# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeedbackInfo:

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
        'project_id': 'str',
        'message_id': 'str',
        'feedback_grade': 'str',
        'feedback_content': 'str',
        'gmt_created': 'int',
        'gmt_modified': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'message_id': 'message_id',
        'feedback_grade': 'feedback_grade',
        'feedback_content': 'feedback_content',
        'gmt_created': 'gmt_created',
        'gmt_modified': 'gmt_modified'
    }

    def __init__(self, id=None, project_id=None, message_id=None, feedback_grade=None, feedback_content=None, gmt_created=None, gmt_modified=None):
        r"""FeedbackInfo

        The model defined in huaweicloud sdk

        :param id: 编号
        :type id: str
        :param project_id: 项目Id
        :type project_id: str
        :param message_id: 任务消息唯一Id
        :type message_id: str
        :param feedback_grade: 反馈等级
        :type feedback_grade: str
        :param feedback_content: 反馈内容
        :type feedback_content: str
        :param gmt_created: 创建时间
        :type gmt_created: int
        :param gmt_modified: 修改时间
        :type gmt_modified: int
        """
        
        

        self._id = None
        self._project_id = None
        self._message_id = None
        self._feedback_grade = None
        self._feedback_content = None
        self._gmt_created = None
        self._gmt_modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if message_id is not None:
            self.message_id = message_id
        if feedback_grade is not None:
            self.feedback_grade = feedback_grade
        if feedback_content is not None:
            self.feedback_content = feedback_content
        if gmt_created is not None:
            self.gmt_created = gmt_created
        if gmt_modified is not None:
            self.gmt_modified = gmt_modified

    @property
    def id(self):
        r"""Gets the id of this FeedbackInfo.

        编号

        :return: The id of this FeedbackInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FeedbackInfo.

        编号

        :param id: The id of this FeedbackInfo.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this FeedbackInfo.

        项目Id

        :return: The project_id of this FeedbackInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this FeedbackInfo.

        项目Id

        :param project_id: The project_id of this FeedbackInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def message_id(self):
        r"""Gets the message_id of this FeedbackInfo.

        任务消息唯一Id

        :return: The message_id of this FeedbackInfo.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        r"""Sets the message_id of this FeedbackInfo.

        任务消息唯一Id

        :param message_id: The message_id of this FeedbackInfo.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def feedback_grade(self):
        r"""Gets the feedback_grade of this FeedbackInfo.

        反馈等级

        :return: The feedback_grade of this FeedbackInfo.
        :rtype: str
        """
        return self._feedback_grade

    @feedback_grade.setter
    def feedback_grade(self, feedback_grade):
        r"""Sets the feedback_grade of this FeedbackInfo.

        反馈等级

        :param feedback_grade: The feedback_grade of this FeedbackInfo.
        :type feedback_grade: str
        """
        self._feedback_grade = feedback_grade

    @property
    def feedback_content(self):
        r"""Gets the feedback_content of this FeedbackInfo.

        反馈内容

        :return: The feedback_content of this FeedbackInfo.
        :rtype: str
        """
        return self._feedback_content

    @feedback_content.setter
    def feedback_content(self, feedback_content):
        r"""Sets the feedback_content of this FeedbackInfo.

        反馈内容

        :param feedback_content: The feedback_content of this FeedbackInfo.
        :type feedback_content: str
        """
        self._feedback_content = feedback_content

    @property
    def gmt_created(self):
        r"""Gets the gmt_created of this FeedbackInfo.

        创建时间

        :return: The gmt_created of this FeedbackInfo.
        :rtype: int
        """
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, gmt_created):
        r"""Sets the gmt_created of this FeedbackInfo.

        创建时间

        :param gmt_created: The gmt_created of this FeedbackInfo.
        :type gmt_created: int
        """
        self._gmt_created = gmt_created

    @property
    def gmt_modified(self):
        r"""Gets the gmt_modified of this FeedbackInfo.

        修改时间

        :return: The gmt_modified of this FeedbackInfo.
        :rtype: int
        """
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, gmt_modified):
        r"""Sets the gmt_modified of this FeedbackInfo.

        修改时间

        :param gmt_modified: The gmt_modified of this FeedbackInfo.
        :type gmt_modified: int
        """
        self._gmt_modified = gmt_modified

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
        if not isinstance(other, FeedbackInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
