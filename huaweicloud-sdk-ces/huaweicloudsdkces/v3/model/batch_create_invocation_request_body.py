# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateInvocationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'invocation_type': 'str',
        'invocation_target': 'str',
        'invocation_ids': 'list[str]',
        'version_type': 'str',
        'origin': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'invocation_type': 'invocation_type',
        'invocation_target': 'invocation_target',
        'invocation_ids': 'invocation_ids',
        'version_type': 'version_type',
        'origin': 'origin'
    }

    def __init__(self, instance_ids=None, invocation_type=None, invocation_target=None, invocation_ids=None, version_type=None, origin=None):
        """BatchCreateInvocationRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: 主机id列表（INSTALL和UPDATE时必须）
        :type instance_ids: list[str]
        :param invocation_type: 任务类型，INSTALL 安装，UPDATE升级，ROLLBACK回退，RETRY重试
        :type invocation_type: str
        :param invocation_target: 任务对象，目前仅支持telescope
        :type invocation_target: str
        :param invocation_ids: 任务ID列表（ROLLBACK和RETRY时必须）
        :type invocation_ids: list[str]
        :param version_type: 插件升级时需要选择升级“基础版本”还是“增强版本”，传值“BASIC_VERSION”表示升级成基础版本，传值“ADVANCE_VERSION”表示升级成增强版本
        :type version_type: str
        :param origin: Agent任务接口调用源，CES表示由Console调用，APICOM_BMS表示由裸金属服务器调用，ADMIN_SERVER表示由运维平台调用
        :type origin: str
        """
        
        

        self._instance_ids = None
        self._invocation_type = None
        self._invocation_target = None
        self._invocation_ids = None
        self._version_type = None
        self._origin = None
        self.discriminator = None

        if instance_ids is not None:
            self.instance_ids = instance_ids
        self.invocation_type = invocation_type
        if invocation_target is not None:
            self.invocation_target = invocation_target
        if invocation_ids is not None:
            self.invocation_ids = invocation_ids
        if version_type is not None:
            self.version_type = version_type
        if origin is not None:
            self.origin = origin

    @property
    def instance_ids(self):
        """Gets the instance_ids of this BatchCreateInvocationRequestBody.

        主机id列表（INSTALL和UPDATE时必须）

        :return: The instance_ids of this BatchCreateInvocationRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this BatchCreateInvocationRequestBody.

        主机id列表（INSTALL和UPDATE时必须）

        :param instance_ids: The instance_ids of this BatchCreateInvocationRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def invocation_type(self):
        """Gets the invocation_type of this BatchCreateInvocationRequestBody.

        任务类型，INSTALL 安装，UPDATE升级，ROLLBACK回退，RETRY重试

        :return: The invocation_type of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        """Sets the invocation_type of this BatchCreateInvocationRequestBody.

        任务类型，INSTALL 安装，UPDATE升级，ROLLBACK回退，RETRY重试

        :param invocation_type: The invocation_type of this BatchCreateInvocationRequestBody.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def invocation_target(self):
        """Gets the invocation_target of this BatchCreateInvocationRequestBody.

        任务对象，目前仅支持telescope

        :return: The invocation_target of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._invocation_target

    @invocation_target.setter
    def invocation_target(self, invocation_target):
        """Sets the invocation_target of this BatchCreateInvocationRequestBody.

        任务对象，目前仅支持telescope

        :param invocation_target: The invocation_target of this BatchCreateInvocationRequestBody.
        :type invocation_target: str
        """
        self._invocation_target = invocation_target

    @property
    def invocation_ids(self):
        """Gets the invocation_ids of this BatchCreateInvocationRequestBody.

        任务ID列表（ROLLBACK和RETRY时必须）

        :return: The invocation_ids of this BatchCreateInvocationRequestBody.
        :rtype: list[str]
        """
        return self._invocation_ids

    @invocation_ids.setter
    def invocation_ids(self, invocation_ids):
        """Sets the invocation_ids of this BatchCreateInvocationRequestBody.

        任务ID列表（ROLLBACK和RETRY时必须）

        :param invocation_ids: The invocation_ids of this BatchCreateInvocationRequestBody.
        :type invocation_ids: list[str]
        """
        self._invocation_ids = invocation_ids

    @property
    def version_type(self):
        """Gets the version_type of this BatchCreateInvocationRequestBody.

        插件升级时需要选择升级“基础版本”还是“增强版本”，传值“BASIC_VERSION”表示升级成基础版本，传值“ADVANCE_VERSION”表示升级成增强版本

        :return: The version_type of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this BatchCreateInvocationRequestBody.

        插件升级时需要选择升级“基础版本”还是“增强版本”，传值“BASIC_VERSION”表示升级成基础版本，传值“ADVANCE_VERSION”表示升级成增强版本

        :param version_type: The version_type of this BatchCreateInvocationRequestBody.
        :type version_type: str
        """
        self._version_type = version_type

    @property
    def origin(self):
        """Gets the origin of this BatchCreateInvocationRequestBody.

        Agent任务接口调用源，CES表示由Console调用，APICOM_BMS表示由裸金属服务器调用，ADMIN_SERVER表示由运维平台调用

        :return: The origin of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BatchCreateInvocationRequestBody.

        Agent任务接口调用源，CES表示由Console调用，APICOM_BMS表示由裸金属服务器调用，ADMIN_SERVER表示由运维平台调用

        :param origin: The origin of this BatchCreateInvocationRequestBody.
        :type origin: str
        """
        self._origin = origin

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
        if not isinstance(other, BatchCreateInvocationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
