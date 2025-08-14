# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeApplicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_urn': 'str',
        'application_provider_urn': 'str',
        'assignment_config': 'AssignmentConfigDto',
        'created_date': 'int',
        'description': 'str',
        'instance_urn': 'str',
        'name': 'str',
        'portal_options': 'PortalOptionsDto',
        'status': 'str',
        'application_account': 'str'
    }

    attribute_map = {
        'application_urn': 'application_urn',
        'application_provider_urn': 'application_provider_urn',
        'assignment_config': 'assignment_config',
        'created_date': 'created_date',
        'description': 'description',
        'instance_urn': 'instance_urn',
        'name': 'name',
        'portal_options': 'portal_options',
        'status': 'status',
        'application_account': 'application_account'
    }

    def __init__(self, application_urn=None, application_provider_urn=None, assignment_config=None, created_date=None, description=None, instance_urn=None, name=None, portal_options=None, status=None, application_account=None):
        r"""DescribeApplicationResponse

        The model defined in huaweicloud sdk

        :param application_urn: 应用程序URN
        :type application_urn: str
        :param application_provider_urn: 应用程序提供商URN
        :type application_provider_urn: str
        :param assignment_config: 
        :type assignment_config: :class:`huaweicloudsdkidentitycenter.v1.AssignmentConfigDto`
        :param created_date: 创建时间
        :type created_date: int
        :param description: 应用程序描述
        :type description: str
        :param instance_urn: IAM身份中心实例URN
        :type instance_urn: str
        :param name: 应用程序显示名
        :type name: str
        :param portal_options: 
        :type portal_options: :class:`huaweicloudsdkidentitycenter.v1.PortalOptionsDto`
        :param status: 状态
        :type status: str
        :param application_account: 华为云账号
        :type application_account: str
        """
        
        super(DescribeApplicationResponse, self).__init__()

        self._application_urn = None
        self._application_provider_urn = None
        self._assignment_config = None
        self._created_date = None
        self._description = None
        self._instance_urn = None
        self._name = None
        self._portal_options = None
        self._status = None
        self._application_account = None
        self.discriminator = None

        if application_urn is not None:
            self.application_urn = application_urn
        if application_provider_urn is not None:
            self.application_provider_urn = application_provider_urn
        if assignment_config is not None:
            self.assignment_config = assignment_config
        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if instance_urn is not None:
            self.instance_urn = instance_urn
        if name is not None:
            self.name = name
        if portal_options is not None:
            self.portal_options = portal_options
        if status is not None:
            self.status = status
        if application_account is not None:
            self.application_account = application_account

    @property
    def application_urn(self):
        r"""Gets the application_urn of this DescribeApplicationResponse.

        应用程序URN

        :return: The application_urn of this DescribeApplicationResponse.
        :rtype: str
        """
        return self._application_urn

    @application_urn.setter
    def application_urn(self, application_urn):
        r"""Sets the application_urn of this DescribeApplicationResponse.

        应用程序URN

        :param application_urn: The application_urn of this DescribeApplicationResponse.
        :type application_urn: str
        """
        self._application_urn = application_urn

    @property
    def application_provider_urn(self):
        r"""Gets the application_provider_urn of this DescribeApplicationResponse.

        应用程序提供商URN

        :return: The application_provider_urn of this DescribeApplicationResponse.
        :rtype: str
        """
        return self._application_provider_urn

    @application_provider_urn.setter
    def application_provider_urn(self, application_provider_urn):
        r"""Sets the application_provider_urn of this DescribeApplicationResponse.

        应用程序提供商URN

        :param application_provider_urn: The application_provider_urn of this DescribeApplicationResponse.
        :type application_provider_urn: str
        """
        self._application_provider_urn = application_provider_urn

    @property
    def assignment_config(self):
        r"""Gets the assignment_config of this DescribeApplicationResponse.

        :return: The assignment_config of this DescribeApplicationResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.AssignmentConfigDto`
        """
        return self._assignment_config

    @assignment_config.setter
    def assignment_config(self, assignment_config):
        r"""Sets the assignment_config of this DescribeApplicationResponse.

        :param assignment_config: The assignment_config of this DescribeApplicationResponse.
        :type assignment_config: :class:`huaweicloudsdkidentitycenter.v1.AssignmentConfigDto`
        """
        self._assignment_config = assignment_config

    @property
    def created_date(self):
        r"""Gets the created_date of this DescribeApplicationResponse.

        创建时间

        :return: The created_date of this DescribeApplicationResponse.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this DescribeApplicationResponse.

        创建时间

        :param created_date: The created_date of this DescribeApplicationResponse.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def description(self):
        r"""Gets the description of this DescribeApplicationResponse.

        应用程序描述

        :return: The description of this DescribeApplicationResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DescribeApplicationResponse.

        应用程序描述

        :param description: The description of this DescribeApplicationResponse.
        :type description: str
        """
        self._description = description

    @property
    def instance_urn(self):
        r"""Gets the instance_urn of this DescribeApplicationResponse.

        IAM身份中心实例URN

        :return: The instance_urn of this DescribeApplicationResponse.
        :rtype: str
        """
        return self._instance_urn

    @instance_urn.setter
    def instance_urn(self, instance_urn):
        r"""Sets the instance_urn of this DescribeApplicationResponse.

        IAM身份中心实例URN

        :param instance_urn: The instance_urn of this DescribeApplicationResponse.
        :type instance_urn: str
        """
        self._instance_urn = instance_urn

    @property
    def name(self):
        r"""Gets the name of this DescribeApplicationResponse.

        应用程序显示名

        :return: The name of this DescribeApplicationResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DescribeApplicationResponse.

        应用程序显示名

        :param name: The name of this DescribeApplicationResponse.
        :type name: str
        """
        self._name = name

    @property
    def portal_options(self):
        r"""Gets the portal_options of this DescribeApplicationResponse.

        :return: The portal_options of this DescribeApplicationResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PortalOptionsDto`
        """
        return self._portal_options

    @portal_options.setter
    def portal_options(self, portal_options):
        r"""Sets the portal_options of this DescribeApplicationResponse.

        :param portal_options: The portal_options of this DescribeApplicationResponse.
        :type portal_options: :class:`huaweicloudsdkidentitycenter.v1.PortalOptionsDto`
        """
        self._portal_options = portal_options

    @property
    def status(self):
        r"""Gets the status of this DescribeApplicationResponse.

        状态

        :return: The status of this DescribeApplicationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DescribeApplicationResponse.

        状态

        :param status: The status of this DescribeApplicationResponse.
        :type status: str
        """
        self._status = status

    @property
    def application_account(self):
        r"""Gets the application_account of this DescribeApplicationResponse.

        华为云账号

        :return: The application_account of this DescribeApplicationResponse.
        :rtype: str
        """
        return self._application_account

    @application_account.setter
    def application_account(self, application_account):
        r"""Sets the application_account of this DescribeApplicationResponse.

        华为云账号

        :param application_account: The application_account of this DescribeApplicationResponse.
        :type application_account: str
        """
        self._application_account = application_account

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
        if not isinstance(other, DescribeApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
