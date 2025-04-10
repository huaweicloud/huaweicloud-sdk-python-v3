# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Risks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'level': 'int',
        'suggest': 'str',
        'influence': 'str',
        'guidance': 'str',
        'service_impact_duration': 'str',
        'upgrade_duration': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'level': 'level',
        'suggest': 'suggest',
        'influence': 'influence',
        'guidance': 'guidance',
        'service_impact_duration': 'service_impact_duration',
        'upgrade_duration': 'upgrade_duration'
    }

    def __init__(self, instance_id=None, engine_name=None, engine_version=None, level=None, suggest=None, influence=None, guidance=None, service_impact_duration=None, upgrade_duration=None):
        r"""Risks

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param engine_name: 引擎名称。
        :type engine_name: str
        :param engine_version: 当前引擎版本。
        :type engine_version: str
        :param level: 风险等级。
        :type level: int
        :param suggest: 建议升级原因。
        :type suggest: str
        :param influence: 升级影响。
        :type influence: str
        :param guidance: 指导连接。
        :type guidance: str
        :param service_impact_duration: 业务影响时长。
        :type service_impact_duration: str
        :param upgrade_duration: 升级时长。
        :type upgrade_duration: str
        """
        
        

        self._instance_id = None
        self._engine_name = None
        self._engine_version = None
        self._level = None
        self._suggest = None
        self._influence = None
        self._guidance = None
        self._service_impact_duration = None
        self._upgrade_duration = None
        self.discriminator = None

        self.instance_id = instance_id
        self.engine_name = engine_name
        self.engine_version = engine_version
        if level is not None:
            self.level = level
        if suggest is not None:
            self.suggest = suggest
        if influence is not None:
            self.influence = influence
        if guidance is not None:
            self.guidance = guidance
        if service_impact_duration is not None:
            self.service_impact_duration = service_impact_duration
        if upgrade_duration is not None:
            self.upgrade_duration = upgrade_duration

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Risks.

        实例ID。

        :return: The instance_id of this Risks.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Risks.

        实例ID。

        :param instance_id: The instance_id of this Risks.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_name(self):
        r"""Gets the engine_name of this Risks.

        引擎名称。

        :return: The engine_name of this Risks.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this Risks.

        引擎名称。

        :param engine_name: The engine_name of this Risks.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this Risks.

        当前引擎版本。

        :return: The engine_version of this Risks.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this Risks.

        当前引擎版本。

        :param engine_version: The engine_version of this Risks.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def level(self):
        r"""Gets the level of this Risks.

        风险等级。

        :return: The level of this Risks.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this Risks.

        风险等级。

        :param level: The level of this Risks.
        :type level: int
        """
        self._level = level

    @property
    def suggest(self):
        r"""Gets the suggest of this Risks.

        建议升级原因。

        :return: The suggest of this Risks.
        :rtype: str
        """
        return self._suggest

    @suggest.setter
    def suggest(self, suggest):
        r"""Sets the suggest of this Risks.

        建议升级原因。

        :param suggest: The suggest of this Risks.
        :type suggest: str
        """
        self._suggest = suggest

    @property
    def influence(self):
        r"""Gets the influence of this Risks.

        升级影响。

        :return: The influence of this Risks.
        :rtype: str
        """
        return self._influence

    @influence.setter
    def influence(self, influence):
        r"""Sets the influence of this Risks.

        升级影响。

        :param influence: The influence of this Risks.
        :type influence: str
        """
        self._influence = influence

    @property
    def guidance(self):
        r"""Gets the guidance of this Risks.

        指导连接。

        :return: The guidance of this Risks.
        :rtype: str
        """
        return self._guidance

    @guidance.setter
    def guidance(self, guidance):
        r"""Sets the guidance of this Risks.

        指导连接。

        :param guidance: The guidance of this Risks.
        :type guidance: str
        """
        self._guidance = guidance

    @property
    def service_impact_duration(self):
        r"""Gets the service_impact_duration of this Risks.

        业务影响时长。

        :return: The service_impact_duration of this Risks.
        :rtype: str
        """
        return self._service_impact_duration

    @service_impact_duration.setter
    def service_impact_duration(self, service_impact_duration):
        r"""Sets the service_impact_duration of this Risks.

        业务影响时长。

        :param service_impact_duration: The service_impact_duration of this Risks.
        :type service_impact_duration: str
        """
        self._service_impact_duration = service_impact_duration

    @property
    def upgrade_duration(self):
        r"""Gets the upgrade_duration of this Risks.

        升级时长。

        :return: The upgrade_duration of this Risks.
        :rtype: str
        """
        return self._upgrade_duration

    @upgrade_duration.setter
    def upgrade_duration(self, upgrade_duration):
        r"""Sets the upgrade_duration of this Risks.

        升级时长。

        :param upgrade_duration: The upgrade_duration of this Risks.
        :type upgrade_duration: str
        """
        self._upgrade_duration = upgrade_duration

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
        if not isinstance(other, Risks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
