# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KustomizationStatus:

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
        'last_attempted_revision': 'str'
    }

    attribute_map = {
        'observed_generation': 'observedGeneration',
        'conditions': 'conditions',
        'last_attempted_revision': 'lastAttemptedRevision'
    }

    def __init__(self, observed_generation=None, conditions=None, last_attempted_revision=None):
        r"""KustomizationStatus

        The model defined in huaweicloud sdk

        :param observed_generation: 最近一次成功协调的资源版本号，用于标识控制器已处理的对象代
        :type observed_generation: int
        :param conditions: 当前对象的状态条件列表
        :type conditions: list[object]
        :param last_attempted_revision: 最近一次成功应用的版本号
        :type last_attempted_revision: str
        """
        
        

        self._observed_generation = None
        self._conditions = None
        self._last_attempted_revision = None
        self.discriminator = None

        if observed_generation is not None:
            self.observed_generation = observed_generation
        if conditions is not None:
            self.conditions = conditions
        if last_attempted_revision is not None:
            self.last_attempted_revision = last_attempted_revision

    @property
    def observed_generation(self):
        r"""Gets the observed_generation of this KustomizationStatus.

        最近一次成功协调的资源版本号，用于标识控制器已处理的对象代

        :return: The observed_generation of this KustomizationStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        r"""Sets the observed_generation of this KustomizationStatus.

        最近一次成功协调的资源版本号，用于标识控制器已处理的对象代

        :param observed_generation: The observed_generation of this KustomizationStatus.
        :type observed_generation: int
        """
        self._observed_generation = observed_generation

    @property
    def conditions(self):
        r"""Gets the conditions of this KustomizationStatus.

        当前对象的状态条件列表

        :return: The conditions of this KustomizationStatus.
        :rtype: list[object]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this KustomizationStatus.

        当前对象的状态条件列表

        :param conditions: The conditions of this KustomizationStatus.
        :type conditions: list[object]
        """
        self._conditions = conditions

    @property
    def last_attempted_revision(self):
        r"""Gets the last_attempted_revision of this KustomizationStatus.

        最近一次成功应用的版本号

        :return: The last_attempted_revision of this KustomizationStatus.
        :rtype: str
        """
        return self._last_attempted_revision

    @last_attempted_revision.setter
    def last_attempted_revision(self, last_attempted_revision):
        r"""Sets the last_attempted_revision of this KustomizationStatus.

        最近一次成功应用的版本号

        :param last_attempted_revision: The last_attempted_revision of this KustomizationStatus.
        :type last_attempted_revision: str
        """
        self._last_attempted_revision = last_attempted_revision

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
        if not isinstance(other, KustomizationStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
