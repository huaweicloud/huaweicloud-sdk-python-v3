# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMigrateStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'project_status': 'list[DomainMigrateProjectStatus]'
    }

    attribute_map = {
        'status': 'status',
        'project_status': 'project_status'
    }

    def __init__(self, status=None, project_status=None):
        r"""ShowMigrateStatusResponse

        The model defined in huaweicloud sdk

        :param status: 租户迁移状态
        :type status: str
        :param project_status: 项目迁移状态
        :type project_status: list[:class:`huaweicloudsdkcbr.v1.DomainMigrateProjectStatus`]
        """
        
        super(ShowMigrateStatusResponse, self).__init__()

        self._status = None
        self._project_status = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if project_status is not None:
            self.project_status = project_status

    @property
    def status(self):
        r"""Gets the status of this ShowMigrateStatusResponse.

        租户迁移状态

        :return: The status of this ShowMigrateStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowMigrateStatusResponse.

        租户迁移状态

        :param status: The status of this ShowMigrateStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def project_status(self):
        r"""Gets the project_status of this ShowMigrateStatusResponse.

        项目迁移状态

        :return: The project_status of this ShowMigrateStatusResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.DomainMigrateProjectStatus`]
        """
        return self._project_status

    @project_status.setter
    def project_status(self, project_status):
        r"""Sets the project_status of this ShowMigrateStatusResponse.

        项目迁移状态

        :param project_status: The project_status of this ShowMigrateStatusResponse.
        :type project_status: list[:class:`huaweicloudsdkcbr.v1.DomainMigrateProjectStatus`]
        """
        self._project_status = project_status

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
        if not isinstance(other, ShowMigrateStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
