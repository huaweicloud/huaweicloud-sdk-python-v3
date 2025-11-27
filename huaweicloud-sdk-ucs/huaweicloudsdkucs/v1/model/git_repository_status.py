# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GitRepositoryStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'observed_generation': 'int',
        'conditions': 'list[object]',
        'artifact': 'Artifact'
    }

    attribute_map = {
        'observed_generation': 'observedGeneration',
        'conditions': 'conditions',
        'artifact': 'artifact'
    }

    def __init__(self, observed_generation=None, conditions=None, artifact=None):
        r"""GitRepositoryStatus

        The model defined in huaweicloud sdk

        :param observed_generation: 控制器上次处理的GitRepository版本号
        :type observed_generation: int
        :param conditions: GitRepository当前的条件集合，用于表示对象的不同状态
        :type conditions: list[object]
        :param artifact: 
        :type artifact: :class:`huaweicloudsdkucs.v1.Artifact`
        """
        
        

        self._observed_generation = None
        self._conditions = None
        self._artifact = None
        self.discriminator = None

        if observed_generation is not None:
            self.observed_generation = observed_generation
        if conditions is not None:
            self.conditions = conditions
        if artifact is not None:
            self.artifact = artifact

    @property
    def observed_generation(self):
        r"""Gets the observed_generation of this GitRepositoryStatus.

        控制器上次处理的GitRepository版本号

        :return: The observed_generation of this GitRepositoryStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        r"""Sets the observed_generation of this GitRepositoryStatus.

        控制器上次处理的GitRepository版本号

        :param observed_generation: The observed_generation of this GitRepositoryStatus.
        :type observed_generation: int
        """
        self._observed_generation = observed_generation

    @property
    def conditions(self):
        r"""Gets the conditions of this GitRepositoryStatus.

        GitRepository当前的条件集合，用于表示对象的不同状态

        :return: The conditions of this GitRepositoryStatus.
        :rtype: list[object]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this GitRepositoryStatus.

        GitRepository当前的条件集合，用于表示对象的不同状态

        :param conditions: The conditions of this GitRepositoryStatus.
        :type conditions: list[object]
        """
        self._conditions = conditions

    @property
    def artifact(self):
        r"""Gets the artifact of this GitRepositoryStatus.

        :return: The artifact of this GitRepositoryStatus.
        :rtype: :class:`huaweicloudsdkucs.v1.Artifact`
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        r"""Sets the artifact of this GitRepositoryStatus.

        :param artifact: The artifact of this GitRepositoryStatus.
        :type artifact: :class:`huaweicloudsdkucs.v1.Artifact`
        """
        self._artifact = artifact

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
        if not isinstance(other, GitRepositoryStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
