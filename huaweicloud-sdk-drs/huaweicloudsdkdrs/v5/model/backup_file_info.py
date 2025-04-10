# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupFileInfo:

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
        'obs_path': 'str',
        'rds_version': 'str',
        'rds_source_instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'obs_path': 'obs_path',
        'rds_version': 'rds_version',
        'rds_source_instance_id': 'rds_source_instance_id'
    }

    def __init__(self, name=None, obs_path=None, rds_version=None, rds_source_instance_id=None):
        r"""BackupFileInfo

        The model defined in huaweicloud sdk

        :param name: 备份文件名称。
        :type name: str
        :param obs_path: OBS桶中文件路径。  OBS场景：必选  RDS场景：缺省
        :type obs_path: str
        :param rds_version: bak文件数据库版本。  OBS场景：缺省  RDS场景：必选
        :type rds_version: str
        :param rds_source_instance_id: bak文件所属实例。  OBS场景：缺省  RDS场景：必选
        :type rds_source_instance_id: str
        """
        
        

        self._name = None
        self._obs_path = None
        self._rds_version = None
        self._rds_source_instance_id = None
        self.discriminator = None

        self.name = name
        if obs_path is not None:
            self.obs_path = obs_path
        if rds_version is not None:
            self.rds_version = rds_version
        if rds_source_instance_id is not None:
            self.rds_source_instance_id = rds_source_instance_id

    @property
    def name(self):
        r"""Gets the name of this BackupFileInfo.

        备份文件名称。

        :return: The name of this BackupFileInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupFileInfo.

        备份文件名称。

        :param name: The name of this BackupFileInfo.
        :type name: str
        """
        self._name = name

    @property
    def obs_path(self):
        r"""Gets the obs_path of this BackupFileInfo.

        OBS桶中文件路径。  OBS场景：必选  RDS场景：缺省

        :return: The obs_path of this BackupFileInfo.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        r"""Sets the obs_path of this BackupFileInfo.

        OBS桶中文件路径。  OBS场景：必选  RDS场景：缺省

        :param obs_path: The obs_path of this BackupFileInfo.
        :type obs_path: str
        """
        self._obs_path = obs_path

    @property
    def rds_version(self):
        r"""Gets the rds_version of this BackupFileInfo.

        bak文件数据库版本。  OBS场景：缺省  RDS场景：必选

        :return: The rds_version of this BackupFileInfo.
        :rtype: str
        """
        return self._rds_version

    @rds_version.setter
    def rds_version(self, rds_version):
        r"""Sets the rds_version of this BackupFileInfo.

        bak文件数据库版本。  OBS场景：缺省  RDS场景：必选

        :param rds_version: The rds_version of this BackupFileInfo.
        :type rds_version: str
        """
        self._rds_version = rds_version

    @property
    def rds_source_instance_id(self):
        r"""Gets the rds_source_instance_id of this BackupFileInfo.

        bak文件所属实例。  OBS场景：缺省  RDS场景：必选

        :return: The rds_source_instance_id of this BackupFileInfo.
        :rtype: str
        """
        return self._rds_source_instance_id

    @rds_source_instance_id.setter
    def rds_source_instance_id(self, rds_source_instance_id):
        r"""Sets the rds_source_instance_id of this BackupFileInfo.

        bak文件所属实例。  OBS场景：缺省  RDS场景：必选

        :param rds_source_instance_id: The rds_source_instance_id of this BackupFileInfo.
        :type rds_source_instance_id: str
        """
        self._rds_source_instance_id = rds_source_instance_id

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
        if not isinstance(other, BackupFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
