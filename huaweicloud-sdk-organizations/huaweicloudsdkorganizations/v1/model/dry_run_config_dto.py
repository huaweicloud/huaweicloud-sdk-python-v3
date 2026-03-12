# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DryRunConfigDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'root_id': 'str',
        'status': 'str',
        'bucket_name': 'str',
        'region_id': 'str',
        'bucket_prefix': 'str',
        'agency_name': 'str',
        'policy_type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'root_id': 'root_id',
        'status': 'status',
        'bucket_name': 'bucket_name',
        'region_id': 'region_id',
        'bucket_prefix': 'bucket_prefix',
        'agency_name': 'agency_name',
        'policy_type': 'policy_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, root_id=None, status=None, bucket_name=None, region_id=None, bucket_prefix=None, agency_name=None, policy_type=None, created_at=None, updated_at=None):
        r"""DryRunConfigDto

        The model defined in huaweicloud sdk

        :param root_id: 根的唯一标识符（ID）。
        :type root_id: str
        :param status: 策略试运行的开启状态。enabled：启用；pending_enable：启用中；disabled：禁用；pending_disable：禁用中。
        :type status: str
        :param bucket_name: 用户桶名称。
        :type bucket_name: str
        :param region_id: 用户桶所在的region。
        :type region_id: str
        :param bucket_prefix: 用户桶的前缀。
        :type bucket_prefix: str
        :param agency_name: 委托名称。Organizations服务通过此委托将试运行日志写入用户obs桶
        :type agency_name: str
        :param policy_type: 试运行策略的类型名称，service_control_policy服务控制策略。
        :type policy_type: str
        :param created_at: 策略试运行配置的开启时间。
        :type created_at: datetime
        :param updated_at: 策略试运行配置的更新时间。
        :type updated_at: datetime
        """
        
        

        self._root_id = None
        self._status = None
        self._bucket_name = None
        self._region_id = None
        self._bucket_prefix = None
        self._agency_name = None
        self._policy_type = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.root_id = root_id
        self.status = status
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if region_id is not None:
            self.region_id = region_id
        if bucket_prefix is not None:
            self.bucket_prefix = bucket_prefix
        if agency_name is not None:
            self.agency_name = agency_name
        self.policy_type = policy_type
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def root_id(self):
        r"""Gets the root_id of this DryRunConfigDto.

        根的唯一标识符（ID）。

        :return: The root_id of this DryRunConfigDto.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this DryRunConfigDto.

        根的唯一标识符（ID）。

        :param root_id: The root_id of this DryRunConfigDto.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def status(self):
        r"""Gets the status of this DryRunConfigDto.

        策略试运行的开启状态。enabled：启用；pending_enable：启用中；disabled：禁用；pending_disable：禁用中。

        :return: The status of this DryRunConfigDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DryRunConfigDto.

        策略试运行的开启状态。enabled：启用；pending_enable：启用中；disabled：禁用；pending_disable：禁用中。

        :param status: The status of this DryRunConfigDto.
        :type status: str
        """
        self._status = status

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this DryRunConfigDto.

        用户桶名称。

        :return: The bucket_name of this DryRunConfigDto.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this DryRunConfigDto.

        用户桶名称。

        :param bucket_name: The bucket_name of this DryRunConfigDto.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def region_id(self):
        r"""Gets the region_id of this DryRunConfigDto.

        用户桶所在的region。

        :return: The region_id of this DryRunConfigDto.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this DryRunConfigDto.

        用户桶所在的region。

        :param region_id: The region_id of this DryRunConfigDto.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def bucket_prefix(self):
        r"""Gets the bucket_prefix of this DryRunConfigDto.

        用户桶的前缀。

        :return: The bucket_prefix of this DryRunConfigDto.
        :rtype: str
        """
        return self._bucket_prefix

    @bucket_prefix.setter
    def bucket_prefix(self, bucket_prefix):
        r"""Sets the bucket_prefix of this DryRunConfigDto.

        用户桶的前缀。

        :param bucket_prefix: The bucket_prefix of this DryRunConfigDto.
        :type bucket_prefix: str
        """
        self._bucket_prefix = bucket_prefix

    @property
    def agency_name(self):
        r"""Gets the agency_name of this DryRunConfigDto.

        委托名称。Organizations服务通过此委托将试运行日志写入用户obs桶

        :return: The agency_name of this DryRunConfigDto.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this DryRunConfigDto.

        委托名称。Organizations服务通过此委托将试运行日志写入用户obs桶

        :param agency_name: The agency_name of this DryRunConfigDto.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def policy_type(self):
        r"""Gets the policy_type of this DryRunConfigDto.

        试运行策略的类型名称，service_control_policy服务控制策略。

        :return: The policy_type of this DryRunConfigDto.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this DryRunConfigDto.

        试运行策略的类型名称，service_control_policy服务控制策略。

        :param policy_type: The policy_type of this DryRunConfigDto.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def created_at(self):
        r"""Gets the created_at of this DryRunConfigDto.

        策略试运行配置的开启时间。

        :return: The created_at of this DryRunConfigDto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DryRunConfigDto.

        策略试运行配置的开启时间。

        :param created_at: The created_at of this DryRunConfigDto.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DryRunConfigDto.

        策略试运行配置的更新时间。

        :return: The updated_at of this DryRunConfigDto.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DryRunConfigDto.

        策略试运行配置的更新时间。

        :param updated_at: The updated_at of this DryRunConfigDto.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, DryRunConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
