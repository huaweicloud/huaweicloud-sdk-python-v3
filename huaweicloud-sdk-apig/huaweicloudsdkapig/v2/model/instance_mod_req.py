# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceModReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'instance_name': 'str',
        'security_group_id': 'str',
        'vpcep_service_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'instance_name': 'instance_name',
        'security_group_id': 'security_group_id',
        'vpcep_service_name': 'vpcep_service_name'
    }

    def __init__(self, description=None, maintain_begin=None, maintain_end=None, instance_name=None, security_group_id=None, vpcep_service_name=None):
        """InstanceModReq

        The model defined in huaweicloud sdk

        :param description: 实例描述
        :type description: str
        :param maintain_begin: 维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。
        :type maintain_end: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param security_group_id: 指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 
        :type security_group_id: str
        :param vpcep_service_name: 终端节点服务的名称。  长度不超过16个字符，允许输入大小写字母、数字、下划线、中划线。  如果您不填写该参数，系统生成的终端节点服务的名称为{region}.apig.{service_id}。 如果您填写该参数，系统生成的终端节点服务的名称为{region}.{vpcep_service_name}.{service_id}。 
        :type vpcep_service_name: str
        """
        
        

        self._description = None
        self._maintain_begin = None
        self._maintain_end = None
        self._instance_name = None
        self._security_group_id = None
        self._vpcep_service_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if instance_name is not None:
            self.instance_name = instance_name
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if vpcep_service_name is not None:
            self.vpcep_service_name = vpcep_service_name

    @property
    def description(self):
        """Gets the description of this InstanceModReq.

        实例描述

        :return: The description of this InstanceModReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceModReq.

        实例描述

        :param description: The description of this InstanceModReq.
        :type description: str
        """
        self._description = description

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this InstanceModReq.

        维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :return: The maintain_begin of this InstanceModReq.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this InstanceModReq.

        维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :param maintain_begin: The maintain_begin of this InstanceModReq.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this InstanceModReq.

        维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :return: The maintain_end of this InstanceModReq.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this InstanceModReq.

        维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :param maintain_end: The maintain_end of this InstanceModReq.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceModReq.

        实例名称

        :return: The instance_name of this InstanceModReq.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceModReq.

        实例名称

        :param instance_name: The instance_name of this InstanceModReq.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceModReq.

        指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 

        :return: The security_group_id of this InstanceModReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceModReq.

        指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 

        :param security_group_id: The security_group_id of this InstanceModReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def vpcep_service_name(self):
        """Gets the vpcep_service_name of this InstanceModReq.

        终端节点服务的名称。  长度不超过16个字符，允许输入大小写字母、数字、下划线、中划线。  如果您不填写该参数，系统生成的终端节点服务的名称为{region}.apig.{service_id}。 如果您填写该参数，系统生成的终端节点服务的名称为{region}.{vpcep_service_name}.{service_id}。 

        :return: The vpcep_service_name of this InstanceModReq.
        :rtype: str
        """
        return self._vpcep_service_name

    @vpcep_service_name.setter
    def vpcep_service_name(self, vpcep_service_name):
        """Sets the vpcep_service_name of this InstanceModReq.

        终端节点服务的名称。  长度不超过16个字符，允许输入大小写字母、数字、下划线、中划线。  如果您不填写该参数，系统生成的终端节点服务的名称为{region}.apig.{service_id}。 如果您填写该参数，系统生成的终端节点服务的名称为{region}.{vpcep_service_name}.{service_id}。 

        :param vpcep_service_name: The vpcep_service_name of this InstanceModReq.
        :type vpcep_service_name: str
        """
        self._vpcep_service_name = vpcep_service_name

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
        if not isinstance(other, InstanceModReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
