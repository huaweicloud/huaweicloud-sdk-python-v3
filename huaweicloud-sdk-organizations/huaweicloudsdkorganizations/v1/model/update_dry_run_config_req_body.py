# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDryRunConfigReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_type': 'str',
        'root_id': 'str',
        'status': 'str',
        'bucket_name': 'str',
        'region_id': 'str',
        'bucket_prefix': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'policy_type': 'policy_type',
        'root_id': 'root_id',
        'status': 'status',
        'bucket_name': 'bucket_name',
        'region_id': 'region_id',
        'bucket_prefix': 'bucket_prefix',
        'agency_name': 'agency_name'
    }

    def __init__(self, policy_type=None, root_id=None, status=None, bucket_name=None, region_id=None, bucket_prefix=None, agency_name=None):
        r"""UpdateDryRunConfigReqBody

        The model defined in huaweicloud sdk

        :param policy_type: 试运行策略的类型名称，service_control_policy服务控制策略。
        :type policy_type: str
        :param root_id: 根的唯一标识符（ID）。
        :type root_id: str
        :param status: 策略试运行的开启状态。enabled：启用；disabled 禁用。
        :type status: str
        :param bucket_name: 用户桶名称。
        :type bucket_name: str
        :param region_id: 用户桶所在的region。
        :type region_id: str
        :param bucket_prefix: 用户桶的前缀。
        :type bucket_prefix: str
        :param agency_name: 委托名称。Organizations服务通过此委托将试运行日志写入用户obs桶
        :type agency_name: str
        """
        
        

        self._policy_type = None
        self._root_id = None
        self._status = None
        self._bucket_name = None
        self._region_id = None
        self._bucket_prefix = None
        self._agency_name = None
        self.discriminator = None

        self.policy_type = policy_type
        self.root_id = root_id
        if status is not None:
            self.status = status
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if region_id is not None:
            self.region_id = region_id
        if bucket_prefix is not None:
            self.bucket_prefix = bucket_prefix
        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def policy_type(self):
        r"""Gets the policy_type of this UpdateDryRunConfigReqBody.

        试运行策略的类型名称，service_control_policy服务控制策略。

        :return: The policy_type of this UpdateDryRunConfigReqBody.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this UpdateDryRunConfigReqBody.

        试运行策略的类型名称，service_control_policy服务控制策略。

        :param policy_type: The policy_type of this UpdateDryRunConfigReqBody.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def root_id(self):
        r"""Gets the root_id of this UpdateDryRunConfigReqBody.

        根的唯一标识符（ID）。

        :return: The root_id of this UpdateDryRunConfigReqBody.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this UpdateDryRunConfigReqBody.

        根的唯一标识符（ID）。

        :param root_id: The root_id of this UpdateDryRunConfigReqBody.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def status(self):
        r"""Gets the status of this UpdateDryRunConfigReqBody.

        策略试运行的开启状态。enabled：启用；disabled 禁用。

        :return: The status of this UpdateDryRunConfigReqBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateDryRunConfigReqBody.

        策略试运行的开启状态。enabled：启用；disabled 禁用。

        :param status: The status of this UpdateDryRunConfigReqBody.
        :type status: str
        """
        self._status = status

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this UpdateDryRunConfigReqBody.

        用户桶名称。

        :return: The bucket_name of this UpdateDryRunConfigReqBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this UpdateDryRunConfigReqBody.

        用户桶名称。

        :param bucket_name: The bucket_name of this UpdateDryRunConfigReqBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def region_id(self):
        r"""Gets the region_id of this UpdateDryRunConfigReqBody.

        用户桶所在的region。

        :return: The region_id of this UpdateDryRunConfigReqBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this UpdateDryRunConfigReqBody.

        用户桶所在的region。

        :param region_id: The region_id of this UpdateDryRunConfigReqBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def bucket_prefix(self):
        r"""Gets the bucket_prefix of this UpdateDryRunConfigReqBody.

        用户桶的前缀。

        :return: The bucket_prefix of this UpdateDryRunConfigReqBody.
        :rtype: str
        """
        return self._bucket_prefix

    @bucket_prefix.setter
    def bucket_prefix(self, bucket_prefix):
        r"""Sets the bucket_prefix of this UpdateDryRunConfigReqBody.

        用户桶的前缀。

        :param bucket_prefix: The bucket_prefix of this UpdateDryRunConfigReqBody.
        :type bucket_prefix: str
        """
        self._bucket_prefix = bucket_prefix

    @property
    def agency_name(self):
        r"""Gets the agency_name of this UpdateDryRunConfigReqBody.

        委托名称。Organizations服务通过此委托将试运行日志写入用户obs桶

        :return: The agency_name of this UpdateDryRunConfigReqBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this UpdateDryRunConfigReqBody.

        委托名称。Organizations服务通过此委托将试运行日志写入用户obs桶

        :param agency_name: The agency_name of this UpdateDryRunConfigReqBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, UpdateDryRunConfigReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
