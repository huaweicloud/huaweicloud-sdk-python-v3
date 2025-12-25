# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDisasterRecovery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'dr_type': 'str',
        'primary_cluster_id': 'str',
        'standby_cluster_id': 'str',
        'dr_sync_period': 'str',
        'primary_obs_bucket': 'str',
        'standby_obs_bucket': 'str',
        'discovery_recovery_id': 'str',
        'primary_cluster_region': 'str',
        'standby_cluster_region': 'str',
        'primary_cluster_project_id': 'str',
        'standby_cluster_project_id': 'str',
        'cluster_role': 'str',
        'primary_cluster_info': 'CreateDrClusterDto'
    }

    attribute_map = {
        'name': 'name',
        'dr_type': 'dr_type',
        'primary_cluster_id': 'primary_cluster_id',
        'standby_cluster_id': 'standby_cluster_id',
        'dr_sync_period': 'dr_sync_period',
        'primary_obs_bucket': 'primary_obs_bucket',
        'standby_obs_bucket': 'standby_obs_bucket',
        'discovery_recovery_id': 'discovery_recovery_id',
        'primary_cluster_region': 'primary_cluster_region',
        'standby_cluster_region': 'standby_cluster_region',
        'primary_cluster_project_id': 'primary_cluster_project_id',
        'standby_cluster_project_id': 'standby_cluster_project_id',
        'cluster_role': 'cluster_role',
        'primary_cluster_info': 'primary_cluster_info'
    }

    def __init__(self, name=None, dr_type=None, primary_cluster_id=None, standby_cluster_id=None, dr_sync_period=None, primary_obs_bucket=None, standby_obs_bucket=None, discovery_recovery_id=None, primary_cluster_region=None, standby_cluster_region=None, primary_cluster_project_id=None, standby_cluster_project_id=None, cluster_role=None, primary_cluster_info=None):
        r"""CreateDisasterRecovery

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 名称。 **取值范围**： 不涉及。
        :type name: str
        :param dr_type: **参数解释**： 容灾类型。 **取值范围**： - az，跨az容灾。 - region，跨region容灾。
        :type dr_type: str
        :param primary_cluster_id: **参数解释**： 主集群ID。 **取值范围**： 不涉及。
        :type primary_cluster_id: str
        :param standby_cluster_id: **参数解释**： 备集群ID。 **取值范围**： 不涉及。
        :type standby_cluster_id: str
        :param dr_sync_period: **参数解释**： 同步周期。 **取值范围**： 不涉及。
        :type dr_sync_period: str
        :param primary_obs_bucket: **参数解释**： 主集群OBS桶。 **取值范围**： 不涉及。
        :type primary_obs_bucket: str
        :param standby_obs_bucket: **参数解释**： 备集群obs桶。 **取值范围**： 不涉及。
        :type standby_obs_bucket: str
        :param discovery_recovery_id: **参数解释**： 容灾ID。 **取值范围**： 不涉及。
        :type discovery_recovery_id: str
        :param primary_cluster_region: **参数解释**： 容灾主Region。 **取值范围**： 不涉及。
        :type primary_cluster_region: str
        :param standby_cluster_region: **参数解释**： 容灾备Region。 **取值范围**： 不涉及。
        :type standby_cluster_region: str
        :param primary_cluster_project_id: **参数解释**： 容灾主集群项目ID。 **取值范围**： 不涉及。
        :type primary_cluster_project_id: str
        :param standby_cluster_project_id: **参数解释**： 容灾备集群项目ID。 **取值范围**： 不涉及。
        :type standby_cluster_project_id: str
        :param cluster_role: **参数解释**： 集群角色。 **取值范围**： 不涉及。
        :type cluster_role: str
        :param primary_cluster_info: 
        :type primary_cluster_info: :class:`huaweicloudsdkdws.v2.CreateDrClusterDto`
        """
        
        

        self._name = None
        self._dr_type = None
        self._primary_cluster_id = None
        self._standby_cluster_id = None
        self._dr_sync_period = None
        self._primary_obs_bucket = None
        self._standby_obs_bucket = None
        self._discovery_recovery_id = None
        self._primary_cluster_region = None
        self._standby_cluster_region = None
        self._primary_cluster_project_id = None
        self._standby_cluster_project_id = None
        self._cluster_role = None
        self._primary_cluster_info = None
        self.discriminator = None

        self.name = name
        self.dr_type = dr_type
        self.primary_cluster_id = primary_cluster_id
        self.standby_cluster_id = standby_cluster_id
        self.dr_sync_period = dr_sync_period
        if primary_obs_bucket is not None:
            self.primary_obs_bucket = primary_obs_bucket
        if standby_obs_bucket is not None:
            self.standby_obs_bucket = standby_obs_bucket
        if discovery_recovery_id is not None:
            self.discovery_recovery_id = discovery_recovery_id
        if primary_cluster_region is not None:
            self.primary_cluster_region = primary_cluster_region
        if standby_cluster_region is not None:
            self.standby_cluster_region = standby_cluster_region
        if primary_cluster_project_id is not None:
            self.primary_cluster_project_id = primary_cluster_project_id
        if standby_cluster_project_id is not None:
            self.standby_cluster_project_id = standby_cluster_project_id
        if cluster_role is not None:
            self.cluster_role = cluster_role
        if primary_cluster_info is not None:
            self.primary_cluster_info = primary_cluster_info

    @property
    def name(self):
        r"""Gets the name of this CreateDisasterRecovery.

        **参数解释**： 名称。 **取值范围**： 不涉及。

        :return: The name of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDisasterRecovery.

        **参数解释**： 名称。 **取值范围**： 不涉及。

        :param name: The name of this CreateDisasterRecovery.
        :type name: str
        """
        self._name = name

    @property
    def dr_type(self):
        r"""Gets the dr_type of this CreateDisasterRecovery.

        **参数解释**： 容灾类型。 **取值范围**： - az，跨az容灾。 - region，跨region容灾。

        :return: The dr_type of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        r"""Sets the dr_type of this CreateDisasterRecovery.

        **参数解释**： 容灾类型。 **取值范围**： - az，跨az容灾。 - region，跨region容灾。

        :param dr_type: The dr_type of this CreateDisasterRecovery.
        :type dr_type: str
        """
        self._dr_type = dr_type

    @property
    def primary_cluster_id(self):
        r"""Gets the primary_cluster_id of this CreateDisasterRecovery.

        **参数解释**： 主集群ID。 **取值范围**： 不涉及。

        :return: The primary_cluster_id of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_id

    @primary_cluster_id.setter
    def primary_cluster_id(self, primary_cluster_id):
        r"""Sets the primary_cluster_id of this CreateDisasterRecovery.

        **参数解释**： 主集群ID。 **取值范围**： 不涉及。

        :param primary_cluster_id: The primary_cluster_id of this CreateDisasterRecovery.
        :type primary_cluster_id: str
        """
        self._primary_cluster_id = primary_cluster_id

    @property
    def standby_cluster_id(self):
        r"""Gets the standby_cluster_id of this CreateDisasterRecovery.

        **参数解释**： 备集群ID。 **取值范围**： 不涉及。

        :return: The standby_cluster_id of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_id

    @standby_cluster_id.setter
    def standby_cluster_id(self, standby_cluster_id):
        r"""Sets the standby_cluster_id of this CreateDisasterRecovery.

        **参数解释**： 备集群ID。 **取值范围**： 不涉及。

        :param standby_cluster_id: The standby_cluster_id of this CreateDisasterRecovery.
        :type standby_cluster_id: str
        """
        self._standby_cluster_id = standby_cluster_id

    @property
    def dr_sync_period(self):
        r"""Gets the dr_sync_period of this CreateDisasterRecovery.

        **参数解释**： 同步周期。 **取值范围**： 不涉及。

        :return: The dr_sync_period of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._dr_sync_period

    @dr_sync_period.setter
    def dr_sync_period(self, dr_sync_period):
        r"""Sets the dr_sync_period of this CreateDisasterRecovery.

        **参数解释**： 同步周期。 **取值范围**： 不涉及。

        :param dr_sync_period: The dr_sync_period of this CreateDisasterRecovery.
        :type dr_sync_period: str
        """
        self._dr_sync_period = dr_sync_period

    @property
    def primary_obs_bucket(self):
        r"""Gets the primary_obs_bucket of this CreateDisasterRecovery.

        **参数解释**： 主集群OBS桶。 **取值范围**： 不涉及。

        :return: The primary_obs_bucket of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._primary_obs_bucket

    @primary_obs_bucket.setter
    def primary_obs_bucket(self, primary_obs_bucket):
        r"""Sets the primary_obs_bucket of this CreateDisasterRecovery.

        **参数解释**： 主集群OBS桶。 **取值范围**： 不涉及。

        :param primary_obs_bucket: The primary_obs_bucket of this CreateDisasterRecovery.
        :type primary_obs_bucket: str
        """
        self._primary_obs_bucket = primary_obs_bucket

    @property
    def standby_obs_bucket(self):
        r"""Gets the standby_obs_bucket of this CreateDisasterRecovery.

        **参数解释**： 备集群obs桶。 **取值范围**： 不涉及。

        :return: The standby_obs_bucket of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._standby_obs_bucket

    @standby_obs_bucket.setter
    def standby_obs_bucket(self, standby_obs_bucket):
        r"""Sets the standby_obs_bucket of this CreateDisasterRecovery.

        **参数解释**： 备集群obs桶。 **取值范围**： 不涉及。

        :param standby_obs_bucket: The standby_obs_bucket of this CreateDisasterRecovery.
        :type standby_obs_bucket: str
        """
        self._standby_obs_bucket = standby_obs_bucket

    @property
    def discovery_recovery_id(self):
        r"""Gets the discovery_recovery_id of this CreateDisasterRecovery.

        **参数解释**： 容灾ID。 **取值范围**： 不涉及。

        :return: The discovery_recovery_id of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._discovery_recovery_id

    @discovery_recovery_id.setter
    def discovery_recovery_id(self, discovery_recovery_id):
        r"""Sets the discovery_recovery_id of this CreateDisasterRecovery.

        **参数解释**： 容灾ID。 **取值范围**： 不涉及。

        :param discovery_recovery_id: The discovery_recovery_id of this CreateDisasterRecovery.
        :type discovery_recovery_id: str
        """
        self._discovery_recovery_id = discovery_recovery_id

    @property
    def primary_cluster_region(self):
        r"""Gets the primary_cluster_region of this CreateDisasterRecovery.

        **参数解释**： 容灾主Region。 **取值范围**： 不涉及。

        :return: The primary_cluster_region of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_region

    @primary_cluster_region.setter
    def primary_cluster_region(self, primary_cluster_region):
        r"""Sets the primary_cluster_region of this CreateDisasterRecovery.

        **参数解释**： 容灾主Region。 **取值范围**： 不涉及。

        :param primary_cluster_region: The primary_cluster_region of this CreateDisasterRecovery.
        :type primary_cluster_region: str
        """
        self._primary_cluster_region = primary_cluster_region

    @property
    def standby_cluster_region(self):
        r"""Gets the standby_cluster_region of this CreateDisasterRecovery.

        **参数解释**： 容灾备Region。 **取值范围**： 不涉及。

        :return: The standby_cluster_region of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_region

    @standby_cluster_region.setter
    def standby_cluster_region(self, standby_cluster_region):
        r"""Sets the standby_cluster_region of this CreateDisasterRecovery.

        **参数解释**： 容灾备Region。 **取值范围**： 不涉及。

        :param standby_cluster_region: The standby_cluster_region of this CreateDisasterRecovery.
        :type standby_cluster_region: str
        """
        self._standby_cluster_region = standby_cluster_region

    @property
    def primary_cluster_project_id(self):
        r"""Gets the primary_cluster_project_id of this CreateDisasterRecovery.

        **参数解释**： 容灾主集群项目ID。 **取值范围**： 不涉及。

        :return: The primary_cluster_project_id of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_project_id

    @primary_cluster_project_id.setter
    def primary_cluster_project_id(self, primary_cluster_project_id):
        r"""Sets the primary_cluster_project_id of this CreateDisasterRecovery.

        **参数解释**： 容灾主集群项目ID。 **取值范围**： 不涉及。

        :param primary_cluster_project_id: The primary_cluster_project_id of this CreateDisasterRecovery.
        :type primary_cluster_project_id: str
        """
        self._primary_cluster_project_id = primary_cluster_project_id

    @property
    def standby_cluster_project_id(self):
        r"""Gets the standby_cluster_project_id of this CreateDisasterRecovery.

        **参数解释**： 容灾备集群项目ID。 **取值范围**： 不涉及。

        :return: The standby_cluster_project_id of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_project_id

    @standby_cluster_project_id.setter
    def standby_cluster_project_id(self, standby_cluster_project_id):
        r"""Sets the standby_cluster_project_id of this CreateDisasterRecovery.

        **参数解释**： 容灾备集群项目ID。 **取值范围**： 不涉及。

        :param standby_cluster_project_id: The standby_cluster_project_id of this CreateDisasterRecovery.
        :type standby_cluster_project_id: str
        """
        self._standby_cluster_project_id = standby_cluster_project_id

    @property
    def cluster_role(self):
        r"""Gets the cluster_role of this CreateDisasterRecovery.

        **参数解释**： 集群角色。 **取值范围**： 不涉及。

        :return: The cluster_role of this CreateDisasterRecovery.
        :rtype: str
        """
        return self._cluster_role

    @cluster_role.setter
    def cluster_role(self, cluster_role):
        r"""Sets the cluster_role of this CreateDisasterRecovery.

        **参数解释**： 集群角色。 **取值范围**： 不涉及。

        :param cluster_role: The cluster_role of this CreateDisasterRecovery.
        :type cluster_role: str
        """
        self._cluster_role = cluster_role

    @property
    def primary_cluster_info(self):
        r"""Gets the primary_cluster_info of this CreateDisasterRecovery.

        :return: The primary_cluster_info of this CreateDisasterRecovery.
        :rtype: :class:`huaweicloudsdkdws.v2.CreateDrClusterDto`
        """
        return self._primary_cluster_info

    @primary_cluster_info.setter
    def primary_cluster_info(self, primary_cluster_info):
        r"""Sets the primary_cluster_info of this CreateDisasterRecovery.

        :param primary_cluster_info: The primary_cluster_info of this CreateDisasterRecovery.
        :type primary_cluster_info: :class:`huaweicloudsdkdws.v2.CreateDrClusterDto`
        """
        self._primary_cluster_info = primary_cluster_info

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
        if not isinstance(other, CreateDisasterRecovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
