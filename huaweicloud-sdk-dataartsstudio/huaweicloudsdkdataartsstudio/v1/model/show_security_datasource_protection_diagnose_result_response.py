# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityDatasourceProtectionDiagnoseResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'scanning': 'bool',
        'check_time': 'int',
        'kerberos': 'SecurityCertification',
        'public_network_access': 'PublicNetworkAccess',
        'security_group': 'SecurityGroupResult'
    }

    attribute_map = {
        'task_id': 'task_id',
        'scanning': 'scanning',
        'check_time': 'check_time',
        'kerberos': 'kerberos',
        'public_network_access': 'public_network_access',
        'security_group': 'security_group'
    }

    def __init__(self, task_id=None, scanning=None, check_time=None, kerberos=None, public_network_access=None, security_group=None):
        r"""ShowSecurityDatasourceProtectionDiagnoseResultResponse

        The model defined in huaweicloud sdk

        :param task_id: 诊断任务id
        :type task_id: str
        :param scanning: 是否正在扫描
        :type scanning: bool
        :param check_time: 最新检测时间。
        :type check_time: int
        :param kerberos: 
        :type kerberos: :class:`huaweicloudsdkdataartsstudio.v1.SecurityCertification`
        :param public_network_access: 
        :type public_network_access: :class:`huaweicloudsdkdataartsstudio.v1.PublicNetworkAccess`
        :param security_group: 
        :type security_group: :class:`huaweicloudsdkdataartsstudio.v1.SecurityGroupResult`
        """
        
        super(ShowSecurityDatasourceProtectionDiagnoseResultResponse, self).__init__()

        self._task_id = None
        self._scanning = None
        self._check_time = None
        self._kerberos = None
        self._public_network_access = None
        self._security_group = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if scanning is not None:
            self.scanning = scanning
        if check_time is not None:
            self.check_time = check_time
        if kerberos is not None:
            self.kerberos = kerberos
        if public_network_access is not None:
            self.public_network_access = public_network_access
        if security_group is not None:
            self.security_group = security_group

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        诊断任务id

        :return: The task_id of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        诊断任务id

        :param task_id: The task_id of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def scanning(self):
        r"""Gets the scanning of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        是否正在扫描

        :return: The scanning of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :rtype: bool
        """
        return self._scanning

    @scanning.setter
    def scanning(self, scanning):
        r"""Sets the scanning of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        是否正在扫描

        :param scanning: The scanning of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :type scanning: bool
        """
        self._scanning = scanning

    @property
    def check_time(self):
        r"""Gets the check_time of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        最新检测时间。

        :return: The check_time of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :rtype: int
        """
        return self._check_time

    @check_time.setter
    def check_time(self, check_time):
        r"""Sets the check_time of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        最新检测时间。

        :param check_time: The check_time of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :type check_time: int
        """
        self._check_time = check_time

    @property
    def kerberos(self):
        r"""Gets the kerberos of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        :return: The kerberos of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SecurityCertification`
        """
        return self._kerberos

    @kerberos.setter
    def kerberos(self, kerberos):
        r"""Sets the kerberos of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        :param kerberos: The kerberos of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :type kerberos: :class:`huaweicloudsdkdataartsstudio.v1.SecurityCertification`
        """
        self._kerberos = kerberos

    @property
    def public_network_access(self):
        r"""Gets the public_network_access of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        :return: The public_network_access of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PublicNetworkAccess`
        """
        return self._public_network_access

    @public_network_access.setter
    def public_network_access(self, public_network_access):
        r"""Sets the public_network_access of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        :param public_network_access: The public_network_access of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :type public_network_access: :class:`huaweicloudsdkdataartsstudio.v1.PublicNetworkAccess`
        """
        self._public_network_access = public_network_access

    @property
    def security_group(self):
        r"""Gets the security_group of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        :return: The security_group of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SecurityGroupResult`
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.

        :param security_group: The security_group of this ShowSecurityDatasourceProtectionDiagnoseResultResponse.
        :type security_group: :class:`huaweicloudsdkdataartsstudio.v1.SecurityGroupResult`
        """
        self._security_group = security_group

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
        if not isinstance(other, ShowSecurityDatasourceProtectionDiagnoseResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
