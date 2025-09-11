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
        'origin': 'str',
        'version': 'str',
        'remote_install_meta': 'list[RemoteInstallHostInfo]'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'invocation_type': 'invocation_type',
        'invocation_target': 'invocation_target',
        'invocation_ids': 'invocation_ids',
        'version_type': 'version_type',
        'origin': 'origin',
        'version': 'version',
        'remote_install_meta': 'remote_install_meta'
    }

    def __init__(self, instance_ids=None, invocation_type=None, invocation_target=None, invocation_ids=None, version_type=None, origin=None, version=None, remote_install_meta=None):
        r"""BatchCreateInvocationRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: **参数解释**: 主机id列表（INSTALL和UPDATE时必须） **取值范围**: 数组长度范围为[1,100] 
        :type instance_ids: list[str]
        :param invocation_type: **参数解释**: 任务类型 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回滚 - RETRY：重试 - SET_REMOTE_INSTALLER：设置远程安装主机 - REMOTE_INSTALL：执行远程安装 
        :type invocation_type: str
        :param invocation_target: **参数解释**: 任务对象，目前仅支持telescope **取值范围**: - telescope：主机监控插件telescope 
        :type invocation_target: str
        :param invocation_ids: **参数解释**: 任务ID列表（ROLLBACK和RETRY时必须） **取值范围**: 数组长度范围为[1,100] 
        :type invocation_ids: list[str]
        :param version_type: **参数解释**: 插件升级时需要选择升级“基础版本”还是“增强版本” **取值范围**: - BASIC_VERSION: 升级成基础版本 - ADVANCE_VERSION: 升级成增强版本 
        :type version_type: str
        :param origin: **参数解释**: Agent任务接口调用源 **取值范围**: - CES: 由Console调用 - APICOM_BMS: 由裸金属服务器调用 - ADMIN_SERVER: 由运维平台调用 
        :type origin: str
        :param version: **参数解释**: 版本号 **取值范围**: 数组长度范围为[0,64] 
        :type version: str
        :param remote_install_meta: **参数解释**: 创建远程安装任务时需要下发的被安装主机相关信息 **取值范围**: 数组长度范围为[0,100] 
        :type remote_install_meta: list[:class:`huaweicloudsdkces.v3.RemoteInstallHostInfo`]
        """
        
        

        self._instance_ids = None
        self._invocation_type = None
        self._invocation_target = None
        self._invocation_ids = None
        self._version_type = None
        self._origin = None
        self._version = None
        self._remote_install_meta = None
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
        if version is not None:
            self.version = version
        if remote_install_meta is not None:
            self.remote_install_meta = remote_install_meta

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchCreateInvocationRequestBody.

        **参数解释**: 主机id列表（INSTALL和UPDATE时必须） **取值范围**: 数组长度范围为[1,100] 

        :return: The instance_ids of this BatchCreateInvocationRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchCreateInvocationRequestBody.

        **参数解释**: 主机id列表（INSTALL和UPDATE时必须） **取值范围**: 数组长度范围为[1,100] 

        :param instance_ids: The instance_ids of this BatchCreateInvocationRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def invocation_type(self):
        r"""Gets the invocation_type of this BatchCreateInvocationRequestBody.

        **参数解释**: 任务类型 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回滚 - RETRY：重试 - SET_REMOTE_INSTALLER：设置远程安装主机 - REMOTE_INSTALL：执行远程安装 

        :return: The invocation_type of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        r"""Sets the invocation_type of this BatchCreateInvocationRequestBody.

        **参数解释**: 任务类型 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回滚 - RETRY：重试 - SET_REMOTE_INSTALLER：设置远程安装主机 - REMOTE_INSTALL：执行远程安装 

        :param invocation_type: The invocation_type of this BatchCreateInvocationRequestBody.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def invocation_target(self):
        r"""Gets the invocation_target of this BatchCreateInvocationRequestBody.

        **参数解释**: 任务对象，目前仅支持telescope **取值范围**: - telescope：主机监控插件telescope 

        :return: The invocation_target of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._invocation_target

    @invocation_target.setter
    def invocation_target(self, invocation_target):
        r"""Sets the invocation_target of this BatchCreateInvocationRequestBody.

        **参数解释**: 任务对象，目前仅支持telescope **取值范围**: - telescope：主机监控插件telescope 

        :param invocation_target: The invocation_target of this BatchCreateInvocationRequestBody.
        :type invocation_target: str
        """
        self._invocation_target = invocation_target

    @property
    def invocation_ids(self):
        r"""Gets the invocation_ids of this BatchCreateInvocationRequestBody.

        **参数解释**: 任务ID列表（ROLLBACK和RETRY时必须） **取值范围**: 数组长度范围为[1,100] 

        :return: The invocation_ids of this BatchCreateInvocationRequestBody.
        :rtype: list[str]
        """
        return self._invocation_ids

    @invocation_ids.setter
    def invocation_ids(self, invocation_ids):
        r"""Sets the invocation_ids of this BatchCreateInvocationRequestBody.

        **参数解释**: 任务ID列表（ROLLBACK和RETRY时必须） **取值范围**: 数组长度范围为[1,100] 

        :param invocation_ids: The invocation_ids of this BatchCreateInvocationRequestBody.
        :type invocation_ids: list[str]
        """
        self._invocation_ids = invocation_ids

    @property
    def version_type(self):
        r"""Gets the version_type of this BatchCreateInvocationRequestBody.

        **参数解释**: 插件升级时需要选择升级“基础版本”还是“增强版本” **取值范围**: - BASIC_VERSION: 升级成基础版本 - ADVANCE_VERSION: 升级成增强版本 

        :return: The version_type of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this BatchCreateInvocationRequestBody.

        **参数解释**: 插件升级时需要选择升级“基础版本”还是“增强版本” **取值范围**: - BASIC_VERSION: 升级成基础版本 - ADVANCE_VERSION: 升级成增强版本 

        :param version_type: The version_type of this BatchCreateInvocationRequestBody.
        :type version_type: str
        """
        self._version_type = version_type

    @property
    def origin(self):
        r"""Gets the origin of this BatchCreateInvocationRequestBody.

        **参数解释**: Agent任务接口调用源 **取值范围**: - CES: 由Console调用 - APICOM_BMS: 由裸金属服务器调用 - ADMIN_SERVER: 由运维平台调用 

        :return: The origin of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this BatchCreateInvocationRequestBody.

        **参数解释**: Agent任务接口调用源 **取值范围**: - CES: 由Console调用 - APICOM_BMS: 由裸金属服务器调用 - ADMIN_SERVER: 由运维平台调用 

        :param origin: The origin of this BatchCreateInvocationRequestBody.
        :type origin: str
        """
        self._origin = origin

    @property
    def version(self):
        r"""Gets the version of this BatchCreateInvocationRequestBody.

        **参数解释**: 版本号 **取值范围**: 数组长度范围为[0,64] 

        :return: The version of this BatchCreateInvocationRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this BatchCreateInvocationRequestBody.

        **参数解释**: 版本号 **取值范围**: 数组长度范围为[0,64] 

        :param version: The version of this BatchCreateInvocationRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def remote_install_meta(self):
        r"""Gets the remote_install_meta of this BatchCreateInvocationRequestBody.

        **参数解释**: 创建远程安装任务时需要下发的被安装主机相关信息 **取值范围**: 数组长度范围为[0,100] 

        :return: The remote_install_meta of this BatchCreateInvocationRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v3.RemoteInstallHostInfo`]
        """
        return self._remote_install_meta

    @remote_install_meta.setter
    def remote_install_meta(self, remote_install_meta):
        r"""Sets the remote_install_meta of this BatchCreateInvocationRequestBody.

        **参数解释**: 创建远程安装任务时需要下发的被安装主机相关信息 **取值范围**: 数组长度范围为[0,100] 

        :param remote_install_meta: The remote_install_meta of this BatchCreateInvocationRequestBody.
        :type remote_install_meta: list[:class:`huaweicloudsdkces.v3.RemoteInstallHostInfo`]
        """
        self._remote_install_meta = remote_install_meta

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
