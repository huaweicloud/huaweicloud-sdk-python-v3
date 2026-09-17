# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRiskInfoEngineRiskDesc:

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
        r"""ShowRiskInfoEngineRiskDesc

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param engine_name: 当前引擎
        :type engine_name: str
        :param engine_version: 当前引擎小版本
        :type engine_version: str
        :param level: 风险等级，默认1
        :type level: int
        :param suggest: 建议升级原因,无风险为空
        :type suggest: str
        :param influence: 升级影响，无风险为空
        :type influence: str
        :param guidance: 指导链接，无风险为空
        :type guidance: str
        :param service_impact_duration: 业务影响时长，无风险为空
        :type service_impact_duration: str
        :param upgrade_duration: 升级时长，无风险为空
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

        if instance_id is not None:
            self.instance_id = instance_id
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
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
        r"""Gets the instance_id of this ShowRiskInfoEngineRiskDesc.

        实例id

        :return: The instance_id of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowRiskInfoEngineRiskDesc.

        实例id

        :param instance_id: The instance_id of this ShowRiskInfoEngineRiskDesc.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_name(self):
        r"""Gets the engine_name of this ShowRiskInfoEngineRiskDesc.

        当前引擎

        :return: The engine_name of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this ShowRiskInfoEngineRiskDesc.

        当前引擎

        :param engine_name: The engine_name of this ShowRiskInfoEngineRiskDesc.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowRiskInfoEngineRiskDesc.

        当前引擎小版本

        :return: The engine_version of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowRiskInfoEngineRiskDesc.

        当前引擎小版本

        :param engine_version: The engine_version of this ShowRiskInfoEngineRiskDesc.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def level(self):
        r"""Gets the level of this ShowRiskInfoEngineRiskDesc.

        风险等级，默认1

        :return: The level of this ShowRiskInfoEngineRiskDesc.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowRiskInfoEngineRiskDesc.

        风险等级，默认1

        :param level: The level of this ShowRiskInfoEngineRiskDesc.
        :type level: int
        """
        self._level = level

    @property
    def suggest(self):
        r"""Gets the suggest of this ShowRiskInfoEngineRiskDesc.

        建议升级原因,无风险为空

        :return: The suggest of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._suggest

    @suggest.setter
    def suggest(self, suggest):
        r"""Sets the suggest of this ShowRiskInfoEngineRiskDesc.

        建议升级原因,无风险为空

        :param suggest: The suggest of this ShowRiskInfoEngineRiskDesc.
        :type suggest: str
        """
        self._suggest = suggest

    @property
    def influence(self):
        r"""Gets the influence of this ShowRiskInfoEngineRiskDesc.

        升级影响，无风险为空

        :return: The influence of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._influence

    @influence.setter
    def influence(self, influence):
        r"""Sets the influence of this ShowRiskInfoEngineRiskDesc.

        升级影响，无风险为空

        :param influence: The influence of this ShowRiskInfoEngineRiskDesc.
        :type influence: str
        """
        self._influence = influence

    @property
    def guidance(self):
        r"""Gets the guidance of this ShowRiskInfoEngineRiskDesc.

        指导链接，无风险为空

        :return: The guidance of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._guidance

    @guidance.setter
    def guidance(self, guidance):
        r"""Sets the guidance of this ShowRiskInfoEngineRiskDesc.

        指导链接，无风险为空

        :param guidance: The guidance of this ShowRiskInfoEngineRiskDesc.
        :type guidance: str
        """
        self._guidance = guidance

    @property
    def service_impact_duration(self):
        r"""Gets the service_impact_duration of this ShowRiskInfoEngineRiskDesc.

        业务影响时长，无风险为空

        :return: The service_impact_duration of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._service_impact_duration

    @service_impact_duration.setter
    def service_impact_duration(self, service_impact_duration):
        r"""Sets the service_impact_duration of this ShowRiskInfoEngineRiskDesc.

        业务影响时长，无风险为空

        :param service_impact_duration: The service_impact_duration of this ShowRiskInfoEngineRiskDesc.
        :type service_impact_duration: str
        """
        self._service_impact_duration = service_impact_duration

    @property
    def upgrade_duration(self):
        r"""Gets the upgrade_duration of this ShowRiskInfoEngineRiskDesc.

        升级时长，无风险为空

        :return: The upgrade_duration of this ShowRiskInfoEngineRiskDesc.
        :rtype: str
        """
        return self._upgrade_duration

    @upgrade_duration.setter
    def upgrade_duration(self, upgrade_duration):
        r"""Sets the upgrade_duration of this ShowRiskInfoEngineRiskDesc.

        升级时长，无风险为空

        :param upgrade_duration: The upgrade_duration of this ShowRiskInfoEngineRiskDesc.
        :type upgrade_duration: str
        """
        self._upgrade_duration = upgrade_duration

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
        if not isinstance(other, ShowRiskInfoEngineRiskDesc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
