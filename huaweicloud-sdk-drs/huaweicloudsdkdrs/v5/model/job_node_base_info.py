# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobNodeBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_type': 'str',
        'arch': 'str',
        'availability_zone': 'str',
        'status': 'str',
        'role': 'str'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'arch': 'arch',
        'availability_zone': 'availability_zone',
        'status': 'status',
        'role': 'role'
    }

    def __init__(self, instance_type=None, arch=None, availability_zone=None, status=None, role=None):
        """JobNodeBaseInfo

        The model defined in huaweicloud sdk

        :param instance_type: 实例类型。取值： - single：单机。 - ha：主备。
        :type instance_type: str
        :param arch: CPU架构。取值： - x86 - arm
        :type arch: str
        :param availability_zone: 可用区ID。 约束：对于任务实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用“,”英文逗号隔开。示例： - 实例类型为single：\&quot;cn-north-4a\&quot; - 实例类型为ha：\&quot;cn-north-4a,cn-north-4b\&quot;
        :type availability_zone: str
        :param status: 状态。
        :type status: str
        :param role: 任务主备角色。
        :type role: str
        """
        
        

        self._instance_type = None
        self._arch = None
        self._availability_zone = None
        self._status = None
        self._role = None
        self.discriminator = None

        self.instance_type = instance_type
        self.arch = arch
        self.availability_zone = availability_zone
        if status is not None:
            self.status = status
        if role is not None:
            self.role = role

    @property
    def instance_type(self):
        """Gets the instance_type of this JobNodeBaseInfo.

        实例类型。取值： - single：单机。 - ha：主备。

        :return: The instance_type of this JobNodeBaseInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this JobNodeBaseInfo.

        实例类型。取值： - single：单机。 - ha：主备。

        :param instance_type: The instance_type of this JobNodeBaseInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def arch(self):
        """Gets the arch of this JobNodeBaseInfo.

        CPU架构。取值： - x86 - arm

        :return: The arch of this JobNodeBaseInfo.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this JobNodeBaseInfo.

        CPU架构。取值： - x86 - arm

        :param arch: The arch of this JobNodeBaseInfo.
        :type arch: str
        """
        self._arch = arch

    @property
    def availability_zone(self):
        """Gets the availability_zone of this JobNodeBaseInfo.

        可用区ID。 约束：对于任务实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用“,”英文逗号隔开。示例： - 实例类型为single：\"cn-north-4a\" - 实例类型为ha：\"cn-north-4a,cn-north-4b\"

        :return: The availability_zone of this JobNodeBaseInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this JobNodeBaseInfo.

        可用区ID。 约束：对于任务实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用“,”英文逗号隔开。示例： - 实例类型为single：\"cn-north-4a\" - 实例类型为ha：\"cn-north-4a,cn-north-4b\"

        :param availability_zone: The availability_zone of this JobNodeBaseInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def status(self):
        """Gets the status of this JobNodeBaseInfo.

        状态。

        :return: The status of this JobNodeBaseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobNodeBaseInfo.

        状态。

        :param status: The status of this JobNodeBaseInfo.
        :type status: str
        """
        self._status = status

    @property
    def role(self):
        """Gets the role of this JobNodeBaseInfo.

        任务主备角色。

        :return: The role of this JobNodeBaseInfo.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this JobNodeBaseInfo.

        任务主备角色。

        :param role: The role of this JobNodeBaseInfo.
        :type role: str
        """
        self._role = role

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
        if not isinstance(other, JobNodeBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
