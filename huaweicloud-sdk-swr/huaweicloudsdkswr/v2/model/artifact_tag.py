# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArtifactTag:

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
        'artifact_id': 'int',
        'name': 'str',
        'push_time': 'datetime',
        'pull_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'artifact_id': 'artifact_id',
        'name': 'name',
        'push_time': 'push_time',
        'pull_time': 'pull_time'
    }

    def __init__(self, id=None, repository_id=None, artifact_id=None, name=None, push_time=None, pull_time=None):
        r"""ArtifactTag

        The model defined in huaweicloud sdk

        :param id: Tag ID
        :type id: int
        :param repository_id: 制品仓库ID
        :type repository_id: int
        :param artifact_id: 制品版本ID
        :type artifact_id: int
        :param name: tag名称
        :type name: str
        :param push_time: tag的上传时间
        :type push_time: datetime
        :param pull_time: tag的下载时间
        :type pull_time: datetime
        """
        
        

        self._id = None
        self._repository_id = None
        self._artifact_id = None
        self._name = None
        self._push_time = None
        self._pull_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if artifact_id is not None:
            self.artifact_id = artifact_id
        if name is not None:
            self.name = name
        if push_time is not None:
            self.push_time = push_time
        if pull_time is not None:
            self.pull_time = pull_time

    @property
    def id(self):
        r"""Gets the id of this ArtifactTag.

        Tag ID

        :return: The id of this ArtifactTag.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ArtifactTag.

        Tag ID

        :param id: The id of this ArtifactTag.
        :type id: int
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ArtifactTag.

        制品仓库ID

        :return: The repository_id of this ArtifactTag.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ArtifactTag.

        制品仓库ID

        :param repository_id: The repository_id of this ArtifactTag.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def artifact_id(self):
        r"""Gets the artifact_id of this ArtifactTag.

        制品版本ID

        :return: The artifact_id of this ArtifactTag.
        :rtype: int
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        r"""Sets the artifact_id of this ArtifactTag.

        制品版本ID

        :param artifact_id: The artifact_id of this ArtifactTag.
        :type artifact_id: int
        """
        self._artifact_id = artifact_id

    @property
    def name(self):
        r"""Gets the name of this ArtifactTag.

        tag名称

        :return: The name of this ArtifactTag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ArtifactTag.

        tag名称

        :param name: The name of this ArtifactTag.
        :type name: str
        """
        self._name = name

    @property
    def push_time(self):
        r"""Gets the push_time of this ArtifactTag.

        tag的上传时间

        :return: The push_time of this ArtifactTag.
        :rtype: datetime
        """
        return self._push_time

    @push_time.setter
    def push_time(self, push_time):
        r"""Sets the push_time of this ArtifactTag.

        tag的上传时间

        :param push_time: The push_time of this ArtifactTag.
        :type push_time: datetime
        """
        self._push_time = push_time

    @property
    def pull_time(self):
        r"""Gets the pull_time of this ArtifactTag.

        tag的下载时间

        :return: The pull_time of this ArtifactTag.
        :rtype: datetime
        """
        return self._pull_time

    @pull_time.setter
    def pull_time(self, pull_time):
        r"""Sets the pull_time of this ArtifactTag.

        tag的下载时间

        :param pull_time: The pull_time of this ArtifactTag.
        :type pull_time: datetime
        """
        self._pull_time = pull_time

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
        if not isinstance(other, ArtifactTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
