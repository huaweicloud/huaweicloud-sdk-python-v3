# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EwProtectResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protected_resource_type': 'int',
        'protected_resource_name': 'str',
        'protected_resource_id': 'str',
        'protected_resource_nat_name': 'str',
        'protected_resource_nat_id': 'str',
        'protected_resource_project_id': 'str',
        'protected_resource_mode': 'str'
    }

    attribute_map = {
        'protected_resource_type': 'protected_resource_type',
        'protected_resource_name': 'protected_resource_name',
        'protected_resource_id': 'protected_resource_id',
        'protected_resource_nat_name': 'protected_resource_nat_name',
        'protected_resource_nat_id': 'protected_resource_nat_id',
        'protected_resource_project_id': 'protected_resource_project_id',
        'protected_resource_mode': 'protected_resource_mode'
    }

    def __init__(self, protected_resource_type=None, protected_resource_name=None, protected_resource_id=None, protected_resource_nat_name=None, protected_resource_nat_id=None, protected_resource_project_id=None, protected_resource_mode=None):
        """EwProtectResourceInfo

        The model defined in huaweicloud sdk

        :param protected_resource_type: 防护资源类型：0 VPC，1 VGW
        :type protected_resource_type: int
        :param protected_resource_name: 防护资源名称
        :type protected_resource_name: str
        :param protected_resource_id: 防护资源id
        :type protected_resource_id: str
        :param protected_resource_nat_name: 防护资源nat网关名称
        :type protected_resource_nat_name: str
        :param protected_resource_nat_id: 防护资源nat网关id
        :type protected_resource_nat_id: str
        :param protected_resource_project_id: 防护资源租户id
        :type protected_resource_project_id: str
        :param protected_resource_mode: 防护资源模式
        :type protected_resource_mode: str
        """
        
        

        self._protected_resource_type = None
        self._protected_resource_name = None
        self._protected_resource_id = None
        self._protected_resource_nat_name = None
        self._protected_resource_nat_id = None
        self._protected_resource_project_id = None
        self._protected_resource_mode = None
        self.discriminator = None

        self.protected_resource_type = protected_resource_type
        self.protected_resource_name = protected_resource_name
        self.protected_resource_id = protected_resource_id
        if protected_resource_nat_name is not None:
            self.protected_resource_nat_name = protected_resource_nat_name
        if protected_resource_nat_id is not None:
            self.protected_resource_nat_id = protected_resource_nat_id
        if protected_resource_project_id is not None:
            self.protected_resource_project_id = protected_resource_project_id
        if protected_resource_mode is not None:
            self.protected_resource_mode = protected_resource_mode

    @property
    def protected_resource_type(self):
        """Gets the protected_resource_type of this EwProtectResourceInfo.

        防护资源类型：0 VPC，1 VGW

        :return: The protected_resource_type of this EwProtectResourceInfo.
        :rtype: int
        """
        return self._protected_resource_type

    @protected_resource_type.setter
    def protected_resource_type(self, protected_resource_type):
        """Sets the protected_resource_type of this EwProtectResourceInfo.

        防护资源类型：0 VPC，1 VGW

        :param protected_resource_type: The protected_resource_type of this EwProtectResourceInfo.
        :type protected_resource_type: int
        """
        self._protected_resource_type = protected_resource_type

    @property
    def protected_resource_name(self):
        """Gets the protected_resource_name of this EwProtectResourceInfo.

        防护资源名称

        :return: The protected_resource_name of this EwProtectResourceInfo.
        :rtype: str
        """
        return self._protected_resource_name

    @protected_resource_name.setter
    def protected_resource_name(self, protected_resource_name):
        """Sets the protected_resource_name of this EwProtectResourceInfo.

        防护资源名称

        :param protected_resource_name: The protected_resource_name of this EwProtectResourceInfo.
        :type protected_resource_name: str
        """
        self._protected_resource_name = protected_resource_name

    @property
    def protected_resource_id(self):
        """Gets the protected_resource_id of this EwProtectResourceInfo.

        防护资源id

        :return: The protected_resource_id of this EwProtectResourceInfo.
        :rtype: str
        """
        return self._protected_resource_id

    @protected_resource_id.setter
    def protected_resource_id(self, protected_resource_id):
        """Sets the protected_resource_id of this EwProtectResourceInfo.

        防护资源id

        :param protected_resource_id: The protected_resource_id of this EwProtectResourceInfo.
        :type protected_resource_id: str
        """
        self._protected_resource_id = protected_resource_id

    @property
    def protected_resource_nat_name(self):
        """Gets the protected_resource_nat_name of this EwProtectResourceInfo.

        防护资源nat网关名称

        :return: The protected_resource_nat_name of this EwProtectResourceInfo.
        :rtype: str
        """
        return self._protected_resource_nat_name

    @protected_resource_nat_name.setter
    def protected_resource_nat_name(self, protected_resource_nat_name):
        """Sets the protected_resource_nat_name of this EwProtectResourceInfo.

        防护资源nat网关名称

        :param protected_resource_nat_name: The protected_resource_nat_name of this EwProtectResourceInfo.
        :type protected_resource_nat_name: str
        """
        self._protected_resource_nat_name = protected_resource_nat_name

    @property
    def protected_resource_nat_id(self):
        """Gets the protected_resource_nat_id of this EwProtectResourceInfo.

        防护资源nat网关id

        :return: The protected_resource_nat_id of this EwProtectResourceInfo.
        :rtype: str
        """
        return self._protected_resource_nat_id

    @protected_resource_nat_id.setter
    def protected_resource_nat_id(self, protected_resource_nat_id):
        """Sets the protected_resource_nat_id of this EwProtectResourceInfo.

        防护资源nat网关id

        :param protected_resource_nat_id: The protected_resource_nat_id of this EwProtectResourceInfo.
        :type protected_resource_nat_id: str
        """
        self._protected_resource_nat_id = protected_resource_nat_id

    @property
    def protected_resource_project_id(self):
        """Gets the protected_resource_project_id of this EwProtectResourceInfo.

        防护资源租户id

        :return: The protected_resource_project_id of this EwProtectResourceInfo.
        :rtype: str
        """
        return self._protected_resource_project_id

    @protected_resource_project_id.setter
    def protected_resource_project_id(self, protected_resource_project_id):
        """Sets the protected_resource_project_id of this EwProtectResourceInfo.

        防护资源租户id

        :param protected_resource_project_id: The protected_resource_project_id of this EwProtectResourceInfo.
        :type protected_resource_project_id: str
        """
        self._protected_resource_project_id = protected_resource_project_id

    @property
    def protected_resource_mode(self):
        """Gets the protected_resource_mode of this EwProtectResourceInfo.

        防护资源模式

        :return: The protected_resource_mode of this EwProtectResourceInfo.
        :rtype: str
        """
        return self._protected_resource_mode

    @protected_resource_mode.setter
    def protected_resource_mode(self, protected_resource_mode):
        """Sets the protected_resource_mode of this EwProtectResourceInfo.

        防护资源模式

        :param protected_resource_mode: The protected_resource_mode of this EwProtectResourceInfo.
        :type protected_resource_mode: str
        """
        self._protected_resource_mode = protected_resource_mode

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
        if not isinstance(other, EwProtectResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
