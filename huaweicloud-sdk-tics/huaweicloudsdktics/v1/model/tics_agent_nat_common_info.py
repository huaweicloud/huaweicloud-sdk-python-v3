# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsAgentNatCommonInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_id': 'str',
        'project_id': 'str',
        'subnet_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'nat_id': 'nat_id',
        'project_id': 'project_id',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, nat_id=None, project_id=None, subnet_id=None, vpc_id=None):
        """TicsAgentNatCommonInfo

        The model defined in huaweicloud sdk

        :param nat_id: 可信节点绑定的网关id
        :type nat_id: str
        :param project_id: 项目id
        :type project_id: str
        :param subnet_id: 可信节点绑定的CCE集群所在子网id
        :type subnet_id: str
        :param vpc_id: 可信节点绑定的CCE集群所在虚拟私有云id
        :type vpc_id: str
        """
        
        

        self._nat_id = None
        self._project_id = None
        self._subnet_id = None
        self._vpc_id = None
        self.discriminator = None

        if nat_id is not None:
            self.nat_id = nat_id
        if project_id is not None:
            self.project_id = project_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def nat_id(self):
        """Gets the nat_id of this TicsAgentNatCommonInfo.

        可信节点绑定的网关id

        :return: The nat_id of this TicsAgentNatCommonInfo.
        :rtype: str
        """
        return self._nat_id

    @nat_id.setter
    def nat_id(self, nat_id):
        """Sets the nat_id of this TicsAgentNatCommonInfo.

        可信节点绑定的网关id

        :param nat_id: The nat_id of this TicsAgentNatCommonInfo.
        :type nat_id: str
        """
        self._nat_id = nat_id

    @property
    def project_id(self):
        """Gets the project_id of this TicsAgentNatCommonInfo.

        项目id

        :return: The project_id of this TicsAgentNatCommonInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TicsAgentNatCommonInfo.

        项目id

        :param project_id: The project_id of this TicsAgentNatCommonInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this TicsAgentNatCommonInfo.

        可信节点绑定的CCE集群所在子网id

        :return: The subnet_id of this TicsAgentNatCommonInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this TicsAgentNatCommonInfo.

        可信节点绑定的CCE集群所在子网id

        :param subnet_id: The subnet_id of this TicsAgentNatCommonInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this TicsAgentNatCommonInfo.

        可信节点绑定的CCE集群所在虚拟私有云id

        :return: The vpc_id of this TicsAgentNatCommonInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this TicsAgentNatCommonInfo.

        可信节点绑定的CCE集群所在虚拟私有云id

        :param vpc_id: The vpc_id of this TicsAgentNatCommonInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, TicsAgentNatCommonInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
