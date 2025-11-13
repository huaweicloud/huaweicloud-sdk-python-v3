# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReplicationProfilesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'profile_id': 'str',
        'profile_name': 'str',
        'agent_type': 'str',
        'description': 'str',
        'is_def_profile': 'bool'
    }

    attribute_map = {
        'profile_id': 'profile_id',
        'profile_name': 'profile_name',
        'agent_type': 'agent_type',
        'description': 'description',
        'is_def_profile': 'is_def_profile'
    }

    def __init__(self, profile_id=None, profile_name=None, agent_type=None, description=None, is_def_profile=None):
        r"""ListReplicationProfilesResult

        The model defined in huaweicloud sdk

        :param profile_id: 配置文件id。
        :type profile_id: str
        :param profile_name: 配置文件名。
        :type profile_name: str
        :param agent_type: 代理类型。  snapshot：快照代理 log_reader：日志读取器代理 distribution：分发代理 merge:合并代理 queue_reader：队列读取器代理。
        :type agent_type: str
        :param description: 配置文件说明。
        :type description: str
        :param is_def_profile: 是否为默认配置。  true：是默认配置。 false：不是默认配置。
        :type is_def_profile: bool
        """
        
        

        self._profile_id = None
        self._profile_name = None
        self._agent_type = None
        self._description = None
        self._is_def_profile = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        if profile_name is not None:
            self.profile_name = profile_name
        if agent_type is not None:
            self.agent_type = agent_type
        if description is not None:
            self.description = description
        if is_def_profile is not None:
            self.is_def_profile = is_def_profile

    @property
    def profile_id(self):
        r"""Gets the profile_id of this ListReplicationProfilesResult.

        配置文件id。

        :return: The profile_id of this ListReplicationProfilesResult.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        r"""Sets the profile_id of this ListReplicationProfilesResult.

        配置文件id。

        :param profile_id: The profile_id of this ListReplicationProfilesResult.
        :type profile_id: str
        """
        self._profile_id = profile_id

    @property
    def profile_name(self):
        r"""Gets the profile_name of this ListReplicationProfilesResult.

        配置文件名。

        :return: The profile_name of this ListReplicationProfilesResult.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        r"""Sets the profile_name of this ListReplicationProfilesResult.

        配置文件名。

        :param profile_name: The profile_name of this ListReplicationProfilesResult.
        :type profile_name: str
        """
        self._profile_name = profile_name

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ListReplicationProfilesResult.

        代理类型。  snapshot：快照代理 log_reader：日志读取器代理 distribution：分发代理 merge:合并代理 queue_reader：队列读取器代理。

        :return: The agent_type of this ListReplicationProfilesResult.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ListReplicationProfilesResult.

        代理类型。  snapshot：快照代理 log_reader：日志读取器代理 distribution：分发代理 merge:合并代理 queue_reader：队列读取器代理。

        :param agent_type: The agent_type of this ListReplicationProfilesResult.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def description(self):
        r"""Gets the description of this ListReplicationProfilesResult.

        配置文件说明。

        :return: The description of this ListReplicationProfilesResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListReplicationProfilesResult.

        配置文件说明。

        :param description: The description of this ListReplicationProfilesResult.
        :type description: str
        """
        self._description = description

    @property
    def is_def_profile(self):
        r"""Gets the is_def_profile of this ListReplicationProfilesResult.

        是否为默认配置。  true：是默认配置。 false：不是默认配置。

        :return: The is_def_profile of this ListReplicationProfilesResult.
        :rtype: bool
        """
        return self._is_def_profile

    @is_def_profile.setter
    def is_def_profile(self, is_def_profile):
        r"""Sets the is_def_profile of this ListReplicationProfilesResult.

        是否为默认配置。  true：是默认配置。 false：不是默认配置。

        :param is_def_profile: The is_def_profile of this ListReplicationProfilesResult.
        :type is_def_profile: bool
        """
        self._is_def_profile = is_def_profile

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
        if not isinstance(other, ListReplicationProfilesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
