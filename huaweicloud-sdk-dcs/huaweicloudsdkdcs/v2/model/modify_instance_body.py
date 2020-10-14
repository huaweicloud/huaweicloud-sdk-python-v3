# coding: utf-8

import pprint
import re

import six





class ModifyInstanceBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'security_group_id': 'str',
        'instance_backup_policy': 'BackupPolicy'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'security_group_id': 'security_group_id',
        'instance_backup_policy': 'instance_backup_policy'
    }

    def __init__(self, name=None, description=None, maintain_begin=None, maintain_end=None, security_group_id=None, instance_backup_policy=None):
        """ModifyInstanceBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._maintain_begin = None
        self._maintain_end = None
        self._security_group_id = None
        self._instance_backup_policy = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if instance_backup_policy is not None:
            self.instance_backup_policy = instance_backup_policy

    @property
    def name(self):
        """Gets the name of this ModifyInstanceBody.

        实例名称  由英文字符开头，只能由英文字母、数字、中划线和下划线组成。  创建单个实例时，名称长度为4到64位的字符串。批量创建实例时，名称长度为4到56位的字符串，且实例名称格式为“自定义名称-n”，其中n从000开始，依次递增。例如，批量创建两个实例，自定义名称为dcs_demo，则两个实例的名称为dcs_demo-000和dcs_demo-001。 

        :return: The name of this ModifyInstanceBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyInstanceBody.

        实例名称  由英文字符开头，只能由英文字母、数字、中划线和下划线组成。  创建单个实例时，名称长度为4到64位的字符串。批量创建实例时，名称长度为4到56位的字符串，且实例名称格式为“自定义名称-n”，其中n从000开始，依次递增。例如，批量创建两个实例，自定义名称为dcs_demo，则两个实例的名称为dcs_demo-000和dcs_demo-001。 

        :param name: The name of this ModifyInstanceBody.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ModifyInstanceBody.

        实例的描述信息 长度不超过1024的字符串。 > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。 

        :return: The description of this ModifyInstanceBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyInstanceBody.

        实例的描述信息 长度不超过1024的字符串。 > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。 

        :param description: The description of this ModifyInstanceBody.
        :type: str
        """
        self._description = description

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this ModifyInstanceBody.

        '维护时间窗开始时间，格式为HH:mm:ss。' - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 开始时间必须为22:00:00、02:00:00、06:00:00、10:00:00、14:00:00和18:00:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。 

        :return: The maintain_begin of this ModifyInstanceBody.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this ModifyInstanceBody.

        '维护时间窗开始时间，格式为HH:mm:ss。' - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 开始时间必须为22:00:00、02:00:00、06:00:00、10:00:00、14:00:00和18:00:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。 

        :param maintain_begin: The maintain_begin of this ModifyInstanceBody.
        :type: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this ModifyInstanceBody.

        '维护时间窗开始时间，格式为HH:mm:ss。' - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00:00时，结束时间为02:00:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空。 

        :return: The maintain_end of this ModifyInstanceBody.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this ModifyInstanceBody.

        '维护时间窗开始时间，格式为HH:mm:ss。' - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00:00时，结束时间为02:00:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空。 

        :param maintain_end: The maintain_end of this ModifyInstanceBody.
        :type: str
        """
        self._maintain_end = maintain_end

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ModifyInstanceBody.

        安全组ID  可从虚拟私有云服务的控制台界面或者API接口查询得到。  约束：只有Redis 3.0支持 

        :return: The security_group_id of this ModifyInstanceBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ModifyInstanceBody.

        安全组ID  可从虚拟私有云服务的控制台界面或者API接口查询得到。  约束：只有Redis 3.0支持 

        :param security_group_id: The security_group_id of this ModifyInstanceBody.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def instance_backup_policy(self):
        """Gets the instance_backup_policy of this ModifyInstanceBody.


        :return: The instance_backup_policy of this ModifyInstanceBody.
        :rtype: BackupPolicy
        """
        return self._instance_backup_policy

    @instance_backup_policy.setter
    def instance_backup_policy(self, instance_backup_policy):
        """Sets the instance_backup_policy of this ModifyInstanceBody.


        :param instance_backup_policy: The instance_backup_policy of this ModifyInstanceBody.
        :type: BackupPolicy
        """
        self._instance_backup_policy = instance_backup_policy

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
