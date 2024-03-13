# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddEcnWithVpcRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'subnet_id': 'str',
        'local_subnet_list': 'list[str]',
        'region_project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'local_subnet_list': 'local_subnet_list',
        'region_project_id': 'region_project_id',
        'region_id': 'region_id'
    }

    def __init__(self, vpc_id=None, subnet_id=None, local_subnet_list=None, region_project_id=None, region_id=None):
        """AddEcnWithVpcRequestBody

        The model defined in huaweicloud sdk

        :param vpc_id: 虚拟私有云ID
        :type vpc_id: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param local_subnet_list: 本端子网列表
        :type local_subnet_list: list[str]
        :param region_project_id: 虚拟私有云区域项目ID
        :type region_project_id: str
        :param region_id: 区域ID
        :type region_id: str
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._local_subnet_list = None
        self._region_project_id = None
        self._region_id = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.local_subnet_list = local_subnet_list
        self.region_project_id = region_project_id
        self.region_id = region_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AddEcnWithVpcRequestBody.

        虚拟私有云ID

        :return: The vpc_id of this AddEcnWithVpcRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AddEcnWithVpcRequestBody.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this AddEcnWithVpcRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AddEcnWithVpcRequestBody.

        子网ID

        :return: The subnet_id of this AddEcnWithVpcRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AddEcnWithVpcRequestBody.

        子网ID

        :param subnet_id: The subnet_id of this AddEcnWithVpcRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def local_subnet_list(self):
        """Gets the local_subnet_list of this AddEcnWithVpcRequestBody.

        本端子网列表

        :return: The local_subnet_list of this AddEcnWithVpcRequestBody.
        :rtype: list[str]
        """
        return self._local_subnet_list

    @local_subnet_list.setter
    def local_subnet_list(self, local_subnet_list):
        """Sets the local_subnet_list of this AddEcnWithVpcRequestBody.

        本端子网列表

        :param local_subnet_list: The local_subnet_list of this AddEcnWithVpcRequestBody.
        :type local_subnet_list: list[str]
        """
        self._local_subnet_list = local_subnet_list

    @property
    def region_project_id(self):
        """Gets the region_project_id of this AddEcnWithVpcRequestBody.

        虚拟私有云区域项目ID

        :return: The region_project_id of this AddEcnWithVpcRequestBody.
        :rtype: str
        """
        return self._region_project_id

    @region_project_id.setter
    def region_project_id(self, region_project_id):
        """Sets the region_project_id of this AddEcnWithVpcRequestBody.

        虚拟私有云区域项目ID

        :param region_project_id: The region_project_id of this AddEcnWithVpcRequestBody.
        :type region_project_id: str
        """
        self._region_project_id = region_project_id

    @property
    def region_id(self):
        """Gets the region_id of this AddEcnWithVpcRequestBody.

        区域ID

        :return: The region_id of this AddEcnWithVpcRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AddEcnWithVpcRequestBody.

        区域ID

        :param region_id: The region_id of this AddEcnWithVpcRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, AddEcnWithVpcRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
