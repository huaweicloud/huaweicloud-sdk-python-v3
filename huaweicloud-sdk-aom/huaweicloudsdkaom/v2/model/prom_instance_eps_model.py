# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PromInstanceEpsModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prom_name': 'str',
        'prom_id': 'str',
        'prom_type': 'str',
        'prom_version': 'str',
        'prom_create_timestamp': 'int',
        'prom_update_timestamp': 'int',
        'prom_status': 'str',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'is_deleted_tag': 'int',
        'deleted_time': 'int',
        'prom_spec_config': 'PromConfigModel',
        'cce_spec_config': 'str'
    }

    attribute_map = {
        'prom_name': 'prom_name',
        'prom_id': 'prom_id',
        'prom_type': 'prom_type',
        'prom_version': 'prom_version',
        'prom_create_timestamp': 'prom_create_timestamp',
        'prom_update_timestamp': 'prom_update_timestamp',
        'prom_status': 'prom_status',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'is_deleted_tag': 'is_deleted_tag',
        'deleted_time': 'deleted_time',
        'prom_spec_config': 'prom_spec_config',
        'cce_spec_config': 'cce_spec_config'
    }

    def __init__(self, prom_name=None, prom_id=None, prom_type=None, prom_version=None, prom_create_timestamp=None, prom_update_timestamp=None, prom_status=None, enterprise_project_id=None, project_id=None, is_deleted_tag=None, deleted_time=None, prom_spec_config=None, cce_spec_config=None):
        r"""PromInstanceEpsModel

        The model defined in huaweicloud sdk

        :param prom_name: Prometheus实例名称 名称不能以下划线或中划线开头结尾，只含有中文、英文、数字、下划线、中划线、长度1-100。
        :type prom_name: str
        :param prom_id: Prometheus实例id。
        :type prom_id: str
        :param prom_type: Prometheus实例类型（暂时不支持VPC、KUBERNETES）。
        :type prom_type: str
        :param prom_version: Prometheus实例版本号。
        :type prom_version: str
        :param prom_create_timestamp: Prometheus实例创建时间戳。
        :type prom_create_timestamp: int
        :param prom_update_timestamp: Prometheus实例更新时间戳。
        :type prom_update_timestamp: int
        :param prom_status: Prometheus实例状态。
        :type prom_status: str
        :param enterprise_project_id: Prometheus实例所属的企业项目。
        :type enterprise_project_id: str
        :param project_id: Prometheus实例所属projectId。
        :type project_id: str
        :param is_deleted_tag: 删除标记。
        :type is_deleted_tag: int
        :param deleted_time: 删除时间。
        :type deleted_time: int
        :param prom_spec_config: 
        :type prom_spec_config: :class:`huaweicloudsdkaom.v2.PromConfigModel`
        :param cce_spec_config: Prometheus实例所属CCE特殊配置。
        :type cce_spec_config: str
        """
        
        

        self._prom_name = None
        self._prom_id = None
        self._prom_type = None
        self._prom_version = None
        self._prom_create_timestamp = None
        self._prom_update_timestamp = None
        self._prom_status = None
        self._enterprise_project_id = None
        self._project_id = None
        self._is_deleted_tag = None
        self._deleted_time = None
        self._prom_spec_config = None
        self._cce_spec_config = None
        self.discriminator = None

        self.prom_name = prom_name
        if prom_id is not None:
            self.prom_id = prom_id
        self.prom_type = prom_type
        if prom_version is not None:
            self.prom_version = prom_version
        if prom_create_timestamp is not None:
            self.prom_create_timestamp = prom_create_timestamp
        if prom_update_timestamp is not None:
            self.prom_update_timestamp = prom_update_timestamp
        if prom_status is not None:
            self.prom_status = prom_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if project_id is not None:
            self.project_id = project_id
        if is_deleted_tag is not None:
            self.is_deleted_tag = is_deleted_tag
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if prom_spec_config is not None:
            self.prom_spec_config = prom_spec_config
        if cce_spec_config is not None:
            self.cce_spec_config = cce_spec_config

    @property
    def prom_name(self):
        r"""Gets the prom_name of this PromInstanceEpsModel.

        Prometheus实例名称 名称不能以下划线或中划线开头结尾，只含有中文、英文、数字、下划线、中划线、长度1-100。

        :return: The prom_name of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._prom_name

    @prom_name.setter
    def prom_name(self, prom_name):
        r"""Sets the prom_name of this PromInstanceEpsModel.

        Prometheus实例名称 名称不能以下划线或中划线开头结尾，只含有中文、英文、数字、下划线、中划线、长度1-100。

        :param prom_name: The prom_name of this PromInstanceEpsModel.
        :type prom_name: str
        """
        self._prom_name = prom_name

    @property
    def prom_id(self):
        r"""Gets the prom_id of this PromInstanceEpsModel.

        Prometheus实例id。

        :return: The prom_id of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._prom_id

    @prom_id.setter
    def prom_id(self, prom_id):
        r"""Sets the prom_id of this PromInstanceEpsModel.

        Prometheus实例id。

        :param prom_id: The prom_id of this PromInstanceEpsModel.
        :type prom_id: str
        """
        self._prom_id = prom_id

    @property
    def prom_type(self):
        r"""Gets the prom_type of this PromInstanceEpsModel.

        Prometheus实例类型（暂时不支持VPC、KUBERNETES）。

        :return: The prom_type of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._prom_type

    @prom_type.setter
    def prom_type(self, prom_type):
        r"""Sets the prom_type of this PromInstanceEpsModel.

        Prometheus实例类型（暂时不支持VPC、KUBERNETES）。

        :param prom_type: The prom_type of this PromInstanceEpsModel.
        :type prom_type: str
        """
        self._prom_type = prom_type

    @property
    def prom_version(self):
        r"""Gets the prom_version of this PromInstanceEpsModel.

        Prometheus实例版本号。

        :return: The prom_version of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._prom_version

    @prom_version.setter
    def prom_version(self, prom_version):
        r"""Sets the prom_version of this PromInstanceEpsModel.

        Prometheus实例版本号。

        :param prom_version: The prom_version of this PromInstanceEpsModel.
        :type prom_version: str
        """
        self._prom_version = prom_version

    @property
    def prom_create_timestamp(self):
        r"""Gets the prom_create_timestamp of this PromInstanceEpsModel.

        Prometheus实例创建时间戳。

        :return: The prom_create_timestamp of this PromInstanceEpsModel.
        :rtype: int
        """
        return self._prom_create_timestamp

    @prom_create_timestamp.setter
    def prom_create_timestamp(self, prom_create_timestamp):
        r"""Sets the prom_create_timestamp of this PromInstanceEpsModel.

        Prometheus实例创建时间戳。

        :param prom_create_timestamp: The prom_create_timestamp of this PromInstanceEpsModel.
        :type prom_create_timestamp: int
        """
        self._prom_create_timestamp = prom_create_timestamp

    @property
    def prom_update_timestamp(self):
        r"""Gets the prom_update_timestamp of this PromInstanceEpsModel.

        Prometheus实例更新时间戳。

        :return: The prom_update_timestamp of this PromInstanceEpsModel.
        :rtype: int
        """
        return self._prom_update_timestamp

    @prom_update_timestamp.setter
    def prom_update_timestamp(self, prom_update_timestamp):
        r"""Sets the prom_update_timestamp of this PromInstanceEpsModel.

        Prometheus实例更新时间戳。

        :param prom_update_timestamp: The prom_update_timestamp of this PromInstanceEpsModel.
        :type prom_update_timestamp: int
        """
        self._prom_update_timestamp = prom_update_timestamp

    @property
    def prom_status(self):
        r"""Gets the prom_status of this PromInstanceEpsModel.

        Prometheus实例状态。

        :return: The prom_status of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._prom_status

    @prom_status.setter
    def prom_status(self, prom_status):
        r"""Sets the prom_status of this PromInstanceEpsModel.

        Prometheus实例状态。

        :param prom_status: The prom_status of this PromInstanceEpsModel.
        :type prom_status: str
        """
        self._prom_status = prom_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this PromInstanceEpsModel.

        Prometheus实例所属的企业项目。

        :return: The enterprise_project_id of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this PromInstanceEpsModel.

        Prometheus实例所属的企业项目。

        :param enterprise_project_id: The enterprise_project_id of this PromInstanceEpsModel.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this PromInstanceEpsModel.

        Prometheus实例所属projectId。

        :return: The project_id of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PromInstanceEpsModel.

        Prometheus实例所属projectId。

        :param project_id: The project_id of this PromInstanceEpsModel.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_deleted_tag(self):
        r"""Gets the is_deleted_tag of this PromInstanceEpsModel.

        删除标记。

        :return: The is_deleted_tag of this PromInstanceEpsModel.
        :rtype: int
        """
        return self._is_deleted_tag

    @is_deleted_tag.setter
    def is_deleted_tag(self, is_deleted_tag):
        r"""Sets the is_deleted_tag of this PromInstanceEpsModel.

        删除标记。

        :param is_deleted_tag: The is_deleted_tag of this PromInstanceEpsModel.
        :type is_deleted_tag: int
        """
        self._is_deleted_tag = is_deleted_tag

    @property
    def deleted_time(self):
        r"""Gets the deleted_time of this PromInstanceEpsModel.

        删除时间。

        :return: The deleted_time of this PromInstanceEpsModel.
        :rtype: int
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        r"""Sets the deleted_time of this PromInstanceEpsModel.

        删除时间。

        :param deleted_time: The deleted_time of this PromInstanceEpsModel.
        :type deleted_time: int
        """
        self._deleted_time = deleted_time

    @property
    def prom_spec_config(self):
        r"""Gets the prom_spec_config of this PromInstanceEpsModel.

        :return: The prom_spec_config of this PromInstanceEpsModel.
        :rtype: :class:`huaweicloudsdkaom.v2.PromConfigModel`
        """
        return self._prom_spec_config

    @prom_spec_config.setter
    def prom_spec_config(self, prom_spec_config):
        r"""Sets the prom_spec_config of this PromInstanceEpsModel.

        :param prom_spec_config: The prom_spec_config of this PromInstanceEpsModel.
        :type prom_spec_config: :class:`huaweicloudsdkaom.v2.PromConfigModel`
        """
        self._prom_spec_config = prom_spec_config

    @property
    def cce_spec_config(self):
        r"""Gets the cce_spec_config of this PromInstanceEpsModel.

        Prometheus实例所属CCE特殊配置。

        :return: The cce_spec_config of this PromInstanceEpsModel.
        :rtype: str
        """
        return self._cce_spec_config

    @cce_spec_config.setter
    def cce_spec_config(self, cce_spec_config):
        r"""Sets the cce_spec_config of this PromInstanceEpsModel.

        Prometheus实例所属CCE特殊配置。

        :param cce_spec_config: The cce_spec_config of this PromInstanceEpsModel.
        :type cce_spec_config: str
        """
        self._cce_spec_config = cce_spec_config

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
        if not isinstance(other, PromInstanceEpsModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
