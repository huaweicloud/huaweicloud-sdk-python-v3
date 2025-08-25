# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_name': 'str',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'domain_id': 'str',
        'description': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'domain_id': 'domain_id',
        'description': 'description',
        'create_time': 'create_time'
    }

    def __init__(self, app_id=None, app_name=None, vpc_id=None, vpc_name=None, subnet_id=None, subnet_name=None, domain_id=None, description=None, create_time=None):
        r"""AppInfo

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param vpc_id: 应用所属的VPC的ID
        :type vpc_id: str
        :param vpc_name: 应用所属的VPC的名称
        :type vpc_name: str
        :param subnet_id: 应用所属的VPC的子网iID
        :type subnet_id: str
        :param subnet_name: 应用所属的VPC的子网
        :type subnet_name: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param description: 应用描述
        :type description: str
        :param create_time: 应用的创建时间，UNIX时间戳，单位毫秒
        :type create_time: int
        """
        
        

        self._app_id = None
        self._app_name = None
        self._vpc_id = None
        self._vpc_name = None
        self._subnet_id = None
        self._subnet_name = None
        self._domain_id = None
        self._description = None
        self._create_time = None
        self.discriminator = None

        self.app_id = app_id
        self.app_name = app_name
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.subnet_id = subnet_id
        self.subnet_name = subnet_name
        self.domain_id = domain_id
        self.description = description
        self.create_time = create_time

    @property
    def app_id(self):
        r"""Gets the app_id of this AppInfo.

        应用ID

        :return: The app_id of this AppInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AppInfo.

        应用ID

        :param app_id: The app_id of this AppInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this AppInfo.

        应用名称

        :return: The app_name of this AppInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AppInfo.

        应用名称

        :param app_name: The app_name of this AppInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this AppInfo.

        应用所属的VPC的ID

        :return: The vpc_id of this AppInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this AppInfo.

        应用所属的VPC的ID

        :param vpc_id: The vpc_id of this AppInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this AppInfo.

        应用所属的VPC的名称

        :return: The vpc_name of this AppInfo.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this AppInfo.

        应用所属的VPC的名称

        :param vpc_name: The vpc_name of this AppInfo.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this AppInfo.

        应用所属的VPC的子网iID

        :return: The subnet_id of this AppInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this AppInfo.

        应用所属的VPC的子网iID

        :param subnet_id: The subnet_id of this AppInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this AppInfo.

        应用所属的VPC的子网

        :return: The subnet_name of this AppInfo.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this AppInfo.

        应用所属的VPC的子网

        :param subnet_name: The subnet_name of this AppInfo.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AppInfo.

        账号ID

        :return: The domain_id of this AppInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AppInfo.

        账号ID

        :param domain_id: The domain_id of this AppInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def description(self):
        r"""Gets the description of this AppInfo.

        应用描述

        :return: The description of this AppInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AppInfo.

        应用描述

        :param description: The description of this AppInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this AppInfo.

        应用的创建时间，UNIX时间戳，单位毫秒

        :return: The create_time of this AppInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AppInfo.

        应用的创建时间，UNIX时间戳，单位毫秒

        :param create_time: The create_time of this AppInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, AppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
