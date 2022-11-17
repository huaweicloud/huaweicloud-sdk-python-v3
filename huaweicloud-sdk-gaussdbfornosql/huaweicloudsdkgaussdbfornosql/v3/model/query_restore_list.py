# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRestoreList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_mode': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'vpc_id': 'str',
        'subnet_ids': 'list[str]',
        'security_group_ids': 'list[str]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_mode': 'instance_mode',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'vpc_id': 'vpc_id',
        'subnet_ids': 'subnet_ids',
        'security_group_ids': 'security_group_ids'
    }

    def __init__(self, instance_id=None, instance_mode=None, engine_name=None, engine_version=None, vpc_id=None, subnet_ids=None, security_group_ids=None):
        """QueryRestoreList

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_mode: 实例模式
        :type instance_mode: str
        :param engine_name: 引擎名称
        :type engine_name: str
        :param engine_version: 引擎版本
        :type engine_version: str
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param subnet_ids: 子网ID列表
        :type subnet_ids: list[str]
        :param security_group_ids: 安全组ID列表
        :type security_group_ids: list[str]
        """
        
        

        self._instance_id = None
        self._instance_mode = None
        self._engine_name = None
        self._engine_version = None
        self._vpc_id = None
        self._subnet_ids = None
        self._security_group_ids = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_mode = instance_mode
        self.engine_name = engine_name
        self.engine_version = engine_version
        self.vpc_id = vpc_id
        self.subnet_ids = subnet_ids
        self.security_group_ids = security_group_ids

    @property
    def instance_id(self):
        """Gets the instance_id of this QueryRestoreList.

        实例ID

        :return: The instance_id of this QueryRestoreList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this QueryRestoreList.

        实例ID

        :param instance_id: The instance_id of this QueryRestoreList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_mode(self):
        """Gets the instance_mode of this QueryRestoreList.

        实例模式

        :return: The instance_mode of this QueryRestoreList.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        """Sets the instance_mode of this QueryRestoreList.

        实例模式

        :param instance_mode: The instance_mode of this QueryRestoreList.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def engine_name(self):
        """Gets the engine_name of this QueryRestoreList.

        引擎名称

        :return: The engine_name of this QueryRestoreList.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this QueryRestoreList.

        引擎名称

        :param engine_name: The engine_name of this QueryRestoreList.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        """Gets the engine_version of this QueryRestoreList.

        引擎版本

        :return: The engine_version of this QueryRestoreList.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this QueryRestoreList.

        引擎版本

        :param engine_version: The engine_version of this QueryRestoreList.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def vpc_id(self):
        """Gets the vpc_id of this QueryRestoreList.

        VPC ID。

        :return: The vpc_id of this QueryRestoreList.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this QueryRestoreList.

        VPC ID。

        :param vpc_id: The vpc_id of this QueryRestoreList.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this QueryRestoreList.

        子网ID列表

        :return: The subnet_ids of this QueryRestoreList.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this QueryRestoreList.

        子网ID列表

        :param subnet_ids: The subnet_ids of this QueryRestoreList.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this QueryRestoreList.

        安全组ID列表

        :return: The security_group_ids of this QueryRestoreList.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this QueryRestoreList.

        安全组ID列表

        :param security_group_ids: The security_group_ids of this QueryRestoreList.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

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
        if not isinstance(other, QueryRestoreList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
