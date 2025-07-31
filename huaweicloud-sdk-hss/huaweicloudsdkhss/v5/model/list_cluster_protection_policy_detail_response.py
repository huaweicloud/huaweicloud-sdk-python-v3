# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterProtectionPolicyDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'x_auth_token': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'region': 'str',
        'general_policy_num': 'int',
        'malicious_image_policy_num': 'int',
        'security_policy_num': 'int',
        'data_list': 'list[ClusterPolicyResponseInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'x_auth_token': 'x_auth_token',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'region': 'region',
        'general_policy_num': 'general_policy_num',
        'malicious_image_policy_num': 'malicious_image_policy_num',
        'security_policy_num': 'security_policy_num',
        'data_list': 'data_list'
    }

    def __init__(self, total_num=None, x_auth_token=None, project_id=None, enterprise_project_id=None, region=None, general_policy_num=None, malicious_image_policy_num=None, security_policy_num=None, data_list=None):
        r"""ListClusterProtectionPolicyDetailResponse

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param x_auth_token: 用户Token。
        :type x_auth_token: str
        :param project_id: 项目ID
        :type project_id: str
        :param enterprise_project_id: 企业ID
        :type enterprise_project_id: str
        :param region: Region
        :type region: str
        :param general_policy_num: general策略数
        :type general_policy_num: int
        :param malicious_image_policy_num: malicious_image策略数
        :type malicious_image_policy_num: int
        :param security_policy_num: security_policy策略数
        :type security_policy_num: int
        :param data_list: 集群防护策略列表
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ClusterPolicyResponseInfo`]
        """
        
        super(ListClusterProtectionPolicyDetailResponse, self).__init__()

        self._total_num = None
        self._x_auth_token = None
        self._project_id = None
        self._enterprise_project_id = None
        self._region = None
        self._general_policy_num = None
        self._malicious_image_policy_num = None
        self._security_policy_num = None
        self._data_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if x_auth_token is not None:
            self.x_auth_token = x_auth_token
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if region is not None:
            self.region = region
        if general_policy_num is not None:
            self.general_policy_num = general_policy_num
        if malicious_image_policy_num is not None:
            self.malicious_image_policy_num = malicious_image_policy_num
        if security_policy_num is not None:
            self.security_policy_num = security_policy_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListClusterProtectionPolicyDetailResponse.

        总数

        :return: The total_num of this ListClusterProtectionPolicyDetailResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListClusterProtectionPolicyDetailResponse.

        总数

        :param total_num: The total_num of this ListClusterProtectionPolicyDetailResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def x_auth_token(self):
        r"""Gets the x_auth_token of this ListClusterProtectionPolicyDetailResponse.

        用户Token。

        :return: The x_auth_token of this ListClusterProtectionPolicyDetailResponse.
        :rtype: str
        """
        return self._x_auth_token

    @x_auth_token.setter
    def x_auth_token(self, x_auth_token):
        r"""Sets the x_auth_token of this ListClusterProtectionPolicyDetailResponse.

        用户Token。

        :param x_auth_token: The x_auth_token of this ListClusterProtectionPolicyDetailResponse.
        :type x_auth_token: str
        """
        self._x_auth_token = x_auth_token

    @property
    def project_id(self):
        r"""Gets the project_id of this ListClusterProtectionPolicyDetailResponse.

        项目ID

        :return: The project_id of this ListClusterProtectionPolicyDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListClusterProtectionPolicyDetailResponse.

        项目ID

        :param project_id: The project_id of this ListClusterProtectionPolicyDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListClusterProtectionPolicyDetailResponse.

        企业ID

        :return: The enterprise_project_id of this ListClusterProtectionPolicyDetailResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListClusterProtectionPolicyDetailResponse.

        企业ID

        :param enterprise_project_id: The enterprise_project_id of this ListClusterProtectionPolicyDetailResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region(self):
        r"""Gets the region of this ListClusterProtectionPolicyDetailResponse.

        Region

        :return: The region of this ListClusterProtectionPolicyDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListClusterProtectionPolicyDetailResponse.

        Region

        :param region: The region of this ListClusterProtectionPolicyDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def general_policy_num(self):
        r"""Gets the general_policy_num of this ListClusterProtectionPolicyDetailResponse.

        general策略数

        :return: The general_policy_num of this ListClusterProtectionPolicyDetailResponse.
        :rtype: int
        """
        return self._general_policy_num

    @general_policy_num.setter
    def general_policy_num(self, general_policy_num):
        r"""Sets the general_policy_num of this ListClusterProtectionPolicyDetailResponse.

        general策略数

        :param general_policy_num: The general_policy_num of this ListClusterProtectionPolicyDetailResponse.
        :type general_policy_num: int
        """
        self._general_policy_num = general_policy_num

    @property
    def malicious_image_policy_num(self):
        r"""Gets the malicious_image_policy_num of this ListClusterProtectionPolicyDetailResponse.

        malicious_image策略数

        :return: The malicious_image_policy_num of this ListClusterProtectionPolicyDetailResponse.
        :rtype: int
        """
        return self._malicious_image_policy_num

    @malicious_image_policy_num.setter
    def malicious_image_policy_num(self, malicious_image_policy_num):
        r"""Sets the malicious_image_policy_num of this ListClusterProtectionPolicyDetailResponse.

        malicious_image策略数

        :param malicious_image_policy_num: The malicious_image_policy_num of this ListClusterProtectionPolicyDetailResponse.
        :type malicious_image_policy_num: int
        """
        self._malicious_image_policy_num = malicious_image_policy_num

    @property
    def security_policy_num(self):
        r"""Gets the security_policy_num of this ListClusterProtectionPolicyDetailResponse.

        security_policy策略数

        :return: The security_policy_num of this ListClusterProtectionPolicyDetailResponse.
        :rtype: int
        """
        return self._security_policy_num

    @security_policy_num.setter
    def security_policy_num(self, security_policy_num):
        r"""Sets the security_policy_num of this ListClusterProtectionPolicyDetailResponse.

        security_policy策略数

        :param security_policy_num: The security_policy_num of this ListClusterProtectionPolicyDetailResponse.
        :type security_policy_num: int
        """
        self._security_policy_num = security_policy_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListClusterProtectionPolicyDetailResponse.

        集群防护策略列表

        :return: The data_list of this ListClusterProtectionPolicyDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterPolicyResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListClusterProtectionPolicyDetailResponse.

        集群防护策略列表

        :param data_list: The data_list of this ListClusterProtectionPolicyDetailResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ClusterPolicyResponseInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListClusterProtectionPolicyDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
