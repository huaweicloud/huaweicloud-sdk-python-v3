# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityPermissionManagementDiagnoseResultResponse(SdkResponse):

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
        'check_time': 'int',
        'scanning': 'bool',
        'high_permission': 'HighPermission',
        'unreasonable_permission': 'UnreasonablePermission'
    }

    attribute_map = {
        'task_id': 'task_id',
        'check_time': 'check_time',
        'scanning': 'scanning',
        'high_permission': 'high_permission',
        'unreasonable_permission': 'unreasonable_permission'
    }

    def __init__(self, task_id=None, check_time=None, scanning=None, high_permission=None, unreasonable_permission=None):
        r"""ShowSecurityPermissionManagementDiagnoseResultResponse

        The model defined in huaweicloud sdk

        :param task_id: 诊断任务id。
        :type task_id: str
        :param check_time: 最新检测时间。
        :type check_time: int
        :param scanning: 是否正在诊断。
        :type scanning: bool
        :param high_permission: 
        :type high_permission: :class:`huaweicloudsdkdataartsstudio.v1.HighPermission`
        :param unreasonable_permission: 
        :type unreasonable_permission: :class:`huaweicloudsdkdataartsstudio.v1.UnreasonablePermission`
        """
        
        super(ShowSecurityPermissionManagementDiagnoseResultResponse, self).__init__()

        self._task_id = None
        self._check_time = None
        self._scanning = None
        self._high_permission = None
        self._unreasonable_permission = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if check_time is not None:
            self.check_time = check_time
        if scanning is not None:
            self.scanning = scanning
        if high_permission is not None:
            self.high_permission = high_permission
        if unreasonable_permission is not None:
            self.unreasonable_permission = unreasonable_permission

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        诊断任务id。

        :return: The task_id of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        诊断任务id。

        :param task_id: The task_id of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def check_time(self):
        r"""Gets the check_time of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        最新检测时间。

        :return: The check_time of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :rtype: int
        """
        return self._check_time

    @check_time.setter
    def check_time(self, check_time):
        r"""Sets the check_time of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        最新检测时间。

        :param check_time: The check_time of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :type check_time: int
        """
        self._check_time = check_time

    @property
    def scanning(self):
        r"""Gets the scanning of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        是否正在诊断。

        :return: The scanning of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :rtype: bool
        """
        return self._scanning

    @scanning.setter
    def scanning(self, scanning):
        r"""Sets the scanning of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        是否正在诊断。

        :param scanning: The scanning of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :type scanning: bool
        """
        self._scanning = scanning

    @property
    def high_permission(self):
        r"""Gets the high_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        :return: The high_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.HighPermission`
        """
        return self._high_permission

    @high_permission.setter
    def high_permission(self, high_permission):
        r"""Sets the high_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        :param high_permission: The high_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :type high_permission: :class:`huaweicloudsdkdataartsstudio.v1.HighPermission`
        """
        self._high_permission = high_permission

    @property
    def unreasonable_permission(self):
        r"""Gets the unreasonable_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        :return: The unreasonable_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UnreasonablePermission`
        """
        return self._unreasonable_permission

    @unreasonable_permission.setter
    def unreasonable_permission(self, unreasonable_permission):
        r"""Sets the unreasonable_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.

        :param unreasonable_permission: The unreasonable_permission of this ShowSecurityPermissionManagementDiagnoseResultResponse.
        :type unreasonable_permission: :class:`huaweicloudsdkdataartsstudio.v1.UnreasonablePermission`
        """
        self._unreasonable_permission = unreasonable_permission

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
        if not isinstance(other, ShowSecurityPermissionManagementDiagnoseResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
