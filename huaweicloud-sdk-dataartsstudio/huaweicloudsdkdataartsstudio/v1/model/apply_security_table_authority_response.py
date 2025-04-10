# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplySecurityTableAuthorityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'describe': 'str',
        'permission_center_url': 'str',
        'workspace_id': 'str',
        'application_id': 'str'
    }

    attribute_map = {
        'describe': 'describe',
        'permission_center_url': 'permission_center_url',
        'workspace_id': 'workspace_id',
        'application_id': 'application_id'
    }

    def __init__(self, describe=None, permission_center_url=None, workspace_id=None, application_id=None):
        r"""ApplySecurityTableAuthorityResponse

        The model defined in huaweicloud sdk

        :param describe: 描述
        :type describe: str
        :param permission_center_url: 审批页面地址
        :type permission_center_url: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param application_id: 工单id
        :type application_id: str
        """
        
        super(ApplySecurityTableAuthorityResponse, self).__init__()

        self._describe = None
        self._permission_center_url = None
        self._workspace_id = None
        self._application_id = None
        self.discriminator = None

        if describe is not None:
            self.describe = describe
        if permission_center_url is not None:
            self.permission_center_url = permission_center_url
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if application_id is not None:
            self.application_id = application_id

    @property
    def describe(self):
        r"""Gets the describe of this ApplySecurityTableAuthorityResponse.

        描述

        :return: The describe of this ApplySecurityTableAuthorityResponse.
        :rtype: str
        """
        return self._describe

    @describe.setter
    def describe(self, describe):
        r"""Sets the describe of this ApplySecurityTableAuthorityResponse.

        描述

        :param describe: The describe of this ApplySecurityTableAuthorityResponse.
        :type describe: str
        """
        self._describe = describe

    @property
    def permission_center_url(self):
        r"""Gets the permission_center_url of this ApplySecurityTableAuthorityResponse.

        审批页面地址

        :return: The permission_center_url of this ApplySecurityTableAuthorityResponse.
        :rtype: str
        """
        return self._permission_center_url

    @permission_center_url.setter
    def permission_center_url(self, permission_center_url):
        r"""Sets the permission_center_url of this ApplySecurityTableAuthorityResponse.

        审批页面地址

        :param permission_center_url: The permission_center_url of this ApplySecurityTableAuthorityResponse.
        :type permission_center_url: str
        """
        self._permission_center_url = permission_center_url

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ApplySecurityTableAuthorityResponse.

        工作空间id

        :return: The workspace_id of this ApplySecurityTableAuthorityResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ApplySecurityTableAuthorityResponse.

        工作空间id

        :param workspace_id: The workspace_id of this ApplySecurityTableAuthorityResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def application_id(self):
        r"""Gets the application_id of this ApplySecurityTableAuthorityResponse.

        工单id

        :return: The application_id of this ApplySecurityTableAuthorityResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ApplySecurityTableAuthorityResponse.

        工单id

        :param application_id: The application_id of this ApplySecurityTableAuthorityResponse.
        :type application_id: str
        """
        self._application_id = application_id

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
        if not isinstance(other, ApplySecurityTableAuthorityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
