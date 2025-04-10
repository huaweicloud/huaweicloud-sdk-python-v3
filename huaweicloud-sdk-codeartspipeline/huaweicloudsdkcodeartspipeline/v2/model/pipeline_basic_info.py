# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineBasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'project_name': 'str',
        'pipeline_id': 'str',
        'pipeline_name': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'executor_id': 'str',
        'executor_name': 'str',
        'start_time': 'str',
        'create_time': 'str',
        'watched': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'pipeline_id': 'pipeline_id',
        'pipeline_name': 'pipeline_name',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'executor_id': 'executor_id',
        'executor_name': 'executor_name',
        'start_time': 'start_time',
        'create_time': 'create_time',
        'watched': 'watched'
    }

    def __init__(self, project_id=None, project_name=None, pipeline_id=None, pipeline_name=None, creator_id=None, creator_name=None, executor_id=None, executor_name=None, start_time=None, create_time=None, watched=None):
        r"""PipelineBasicInfo

        The model defined in huaweicloud sdk

        :param project_id: CodeArts项目id
        :type project_id: str
        :param project_name: CodeArts项目名字
        :type project_name: str
        :param pipeline_id: 流水线id
        :type pipeline_id: str
        :param pipeline_name: 流水线名字
        :type pipeline_name: str
        :param creator_id: 流水线创建人id
        :type creator_id: str
        :param creator_name: 流水线创建人名字
        :type creator_name: str
        :param executor_id: 流水线创建人id
        :type executor_id: str
        :param executor_name: 流水线执行人名字
        :type executor_name: str
        :param start_time: 启动时间
        :type start_time: str
        :param create_time: 创建时间
        :type create_time: str
        :param watched: 用户是否关注流水线：true（关注），false（未关注）
        :type watched: str
        """
        
        

        self._project_id = None
        self._project_name = None
        self._pipeline_id = None
        self._pipeline_name = None
        self._creator_id = None
        self._creator_name = None
        self._executor_id = None
        self._executor_name = None
        self._start_time = None
        self._create_time = None
        self._watched = None
        self.discriminator = None

        self.project_id = project_id
        self.project_name = project_name
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.executor_id = executor_id
        self.executor_name = executor_name
        self.start_time = start_time
        self.create_time = create_time
        self.watched = watched

    @property
    def project_id(self):
        r"""Gets the project_id of this PipelineBasicInfo.

        CodeArts项目id

        :return: The project_id of this PipelineBasicInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PipelineBasicInfo.

        CodeArts项目id

        :param project_id: The project_id of this PipelineBasicInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this PipelineBasicInfo.

        CodeArts项目名字

        :return: The project_name of this PipelineBasicInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this PipelineBasicInfo.

        CodeArts项目名字

        :param project_name: The project_name of this PipelineBasicInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this PipelineBasicInfo.

        流水线id

        :return: The pipeline_id of this PipelineBasicInfo.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this PipelineBasicInfo.

        流水线id

        :param pipeline_id: The pipeline_id of this PipelineBasicInfo.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_name(self):
        r"""Gets the pipeline_name of this PipelineBasicInfo.

        流水线名字

        :return: The pipeline_name of this PipelineBasicInfo.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        r"""Sets the pipeline_name of this PipelineBasicInfo.

        流水线名字

        :param pipeline_name: The pipeline_name of this PipelineBasicInfo.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def creator_id(self):
        r"""Gets the creator_id of this PipelineBasicInfo.

        流水线创建人id

        :return: The creator_id of this PipelineBasicInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this PipelineBasicInfo.

        流水线创建人id

        :param creator_id: The creator_id of this PipelineBasicInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this PipelineBasicInfo.

        流水线创建人名字

        :return: The creator_name of this PipelineBasicInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this PipelineBasicInfo.

        流水线创建人名字

        :param creator_name: The creator_name of this PipelineBasicInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def executor_id(self):
        r"""Gets the executor_id of this PipelineBasicInfo.

        流水线创建人id

        :return: The executor_id of this PipelineBasicInfo.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        r"""Sets the executor_id of this PipelineBasicInfo.

        流水线创建人id

        :param executor_id: The executor_id of this PipelineBasicInfo.
        :type executor_id: str
        """
        self._executor_id = executor_id

    @property
    def executor_name(self):
        r"""Gets the executor_name of this PipelineBasicInfo.

        流水线执行人名字

        :return: The executor_name of this PipelineBasicInfo.
        :rtype: str
        """
        return self._executor_name

    @executor_name.setter
    def executor_name(self, executor_name):
        r"""Sets the executor_name of this PipelineBasicInfo.

        流水线执行人名字

        :param executor_name: The executor_name of this PipelineBasicInfo.
        :type executor_name: str
        """
        self._executor_name = executor_name

    @property
    def start_time(self):
        r"""Gets the start_time of this PipelineBasicInfo.

        启动时间

        :return: The start_time of this PipelineBasicInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this PipelineBasicInfo.

        启动时间

        :param start_time: The start_time of this PipelineBasicInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def create_time(self):
        r"""Gets the create_time of this PipelineBasicInfo.

        创建时间

        :return: The create_time of this PipelineBasicInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PipelineBasicInfo.

        创建时间

        :param create_time: The create_time of this PipelineBasicInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def watched(self):
        r"""Gets the watched of this PipelineBasicInfo.

        用户是否关注流水线：true（关注），false（未关注）

        :return: The watched of this PipelineBasicInfo.
        :rtype: str
        """
        return self._watched

    @watched.setter
    def watched(self, watched):
        r"""Sets the watched of this PipelineBasicInfo.

        用户是否关注流水线：true（关注），false（未关注）

        :param watched: The watched of this PipelineBasicInfo.
        :type watched: str
        """
        self._watched = watched

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
        if not isinstance(other, PipelineBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
