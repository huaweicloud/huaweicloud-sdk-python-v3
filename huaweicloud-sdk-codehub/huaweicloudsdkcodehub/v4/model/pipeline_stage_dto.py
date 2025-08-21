# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineStageDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'repository_id': 'int',
        'pipeline_id': 'int',
        'name': 'str',
        'sort_id': 'int',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'pipeline_id': 'pipeline_id',
        'name': 'name',
        'sort_id': 'sort_id',
        'status': 'status'
    }

    def __init__(self, id=None, repository_id=None, pipeline_id=None, name=None, sort_id=None, status=None):
        r"""PipelineStageDto

        The model defined in huaweicloud sdk

        :param id: 阶段ID
        :type id: int
        :param repository_id: 仓库ID
        :type repository_id: int
        :param pipeline_id: 流水线ID
        :type pipeline_id: int
        :param name: 阶段名称
        :type name: str
        :param sort_id: 阶段顺序id
        :type sort_id: int
        :param status: 阶段状态, pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时
        :type status: str
        """
        
        

        self._id = None
        self._repository_id = None
        self._pipeline_id = None
        self._name = None
        self._sort_id = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if name is not None:
            self.name = name
        if sort_id is not None:
            self.sort_id = sort_id
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this PipelineStageDto.

        阶段ID

        :return: The id of this PipelineStageDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PipelineStageDto.

        阶段ID

        :param id: The id of this PipelineStageDto.
        :type id: int
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this PipelineStageDto.

        仓库ID

        :return: The repository_id of this PipelineStageDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this PipelineStageDto.

        仓库ID

        :param repository_id: The repository_id of this PipelineStageDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this PipelineStageDto.

        流水线ID

        :return: The pipeline_id of this PipelineStageDto.
        :rtype: int
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this PipelineStageDto.

        流水线ID

        :param pipeline_id: The pipeline_id of this PipelineStageDto.
        :type pipeline_id: int
        """
        self._pipeline_id = pipeline_id

    @property
    def name(self):
        r"""Gets the name of this PipelineStageDto.

        阶段名称

        :return: The name of this PipelineStageDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PipelineStageDto.

        阶段名称

        :param name: The name of this PipelineStageDto.
        :type name: str
        """
        self._name = name

    @property
    def sort_id(self):
        r"""Gets the sort_id of this PipelineStageDto.

        阶段顺序id

        :return: The sort_id of this PipelineStageDto.
        :rtype: int
        """
        return self._sort_id

    @sort_id.setter
    def sort_id(self, sort_id):
        r"""Sets the sort_id of this PipelineStageDto.

        阶段顺序id

        :param sort_id: The sort_id of this PipelineStageDto.
        :type sort_id: int
        """
        self._sort_id = sort_id

    @property
    def status(self):
        r"""Gets the status of this PipelineStageDto.

        阶段状态, pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :return: The status of this PipelineStageDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PipelineStageDto.

        阶段状态, pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :param status: The status of this PipelineStageDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PipelineStageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
