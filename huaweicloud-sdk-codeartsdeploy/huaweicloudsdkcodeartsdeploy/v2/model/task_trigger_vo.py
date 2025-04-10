# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskTriggerVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_source': 'str',
        'artifact_source_system': 'str',
        'artifact_type': 'str'
    }

    attribute_map = {
        'trigger_source': 'trigger_source',
        'artifact_source_system': 'artifact_source_system',
        'artifact_type': 'artifact_type'
    }

    def __init__(self, trigger_source=None, artifact_source_system=None, artifact_type=None):
        r"""TaskTriggerVO

        The model defined in huaweicloud sdk

        :param trigger_source: 部署任务允许执行的场景。其中0：所有执行请求均可，1：只允许流水线触发
        :type trigger_source: str
        :param artifact_source_system: 当任务只允许流水线触发执行时，流水线传递的来源信息，当前只有CloudArtifact
        :type artifact_source_system: str
        :param artifact_type: 当任务只允许流水线触发执行时，对应流水线源的制品仓库类型（generic、docker）
        :type artifact_type: str
        """
        
        

        self._trigger_source = None
        self._artifact_source_system = None
        self._artifact_type = None
        self.discriminator = None

        if trigger_source is not None:
            self.trigger_source = trigger_source
        if artifact_source_system is not None:
            self.artifact_source_system = artifact_source_system
        if artifact_type is not None:
            self.artifact_type = artifact_type

    @property
    def trigger_source(self):
        r"""Gets the trigger_source of this TaskTriggerVO.

        部署任务允许执行的场景。其中0：所有执行请求均可，1：只允许流水线触发

        :return: The trigger_source of this TaskTriggerVO.
        :rtype: str
        """
        return self._trigger_source

    @trigger_source.setter
    def trigger_source(self, trigger_source):
        r"""Sets the trigger_source of this TaskTriggerVO.

        部署任务允许执行的场景。其中0：所有执行请求均可，1：只允许流水线触发

        :param trigger_source: The trigger_source of this TaskTriggerVO.
        :type trigger_source: str
        """
        self._trigger_source = trigger_source

    @property
    def artifact_source_system(self):
        r"""Gets the artifact_source_system of this TaskTriggerVO.

        当任务只允许流水线触发执行时，流水线传递的来源信息，当前只有CloudArtifact

        :return: The artifact_source_system of this TaskTriggerVO.
        :rtype: str
        """
        return self._artifact_source_system

    @artifact_source_system.setter
    def artifact_source_system(self, artifact_source_system):
        r"""Sets the artifact_source_system of this TaskTriggerVO.

        当任务只允许流水线触发执行时，流水线传递的来源信息，当前只有CloudArtifact

        :param artifact_source_system: The artifact_source_system of this TaskTriggerVO.
        :type artifact_source_system: str
        """
        self._artifact_source_system = artifact_source_system

    @property
    def artifact_type(self):
        r"""Gets the artifact_type of this TaskTriggerVO.

        当任务只允许流水线触发执行时，对应流水线源的制品仓库类型（generic、docker）

        :return: The artifact_type of this TaskTriggerVO.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        r"""Sets the artifact_type of this TaskTriggerVO.

        当任务只允许流水线触发执行时，对应流水线源的制品仓库类型（generic、docker）

        :param artifact_type: The artifact_type of this TaskTriggerVO.
        :type artifact_type: str
        """
        self._artifact_type = artifact_type

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
        if not isinstance(other, TaskTriggerVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
