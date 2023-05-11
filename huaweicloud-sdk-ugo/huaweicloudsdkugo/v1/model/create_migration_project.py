# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMigrationProject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migration_project_name': 'str',
        'evaluation_project_id': 'int',
        'target_db_info': 'TargetDBInfo',
        'open_gauss_config': 'OpenGaussConfig'
    }

    attribute_map = {
        'migration_project_name': 'migration_project_name',
        'evaluation_project_id': 'evaluation_project_id',
        'target_db_info': 'target_db_info',
        'open_gauss_config': 'open_gauss_config'
    }

    def __init__(self, migration_project_name=None, evaluation_project_id=None, target_db_info=None, open_gauss_config=None):
        """CreateMigrationProject

        The model defined in huaweicloud sdk

        :param migration_project_name: 迁移项目名称。长度为5-50个字符，以英文字母开头，英文字母或数字结束，允许包含下划线和中划线。不允许重复。
        :type migration_project_name: str
        :param evaluation_project_id: 评估项目ID。
        :type evaluation_project_id: int
        :param target_db_info: 
        :type target_db_info: :class:`huaweicloudsdkugo.v1.TargetDBInfo`
        :param open_gauss_config: 
        :type open_gauss_config: :class:`huaweicloudsdkugo.v1.OpenGaussConfig`
        """
        
        

        self._migration_project_name = None
        self._evaluation_project_id = None
        self._target_db_info = None
        self._open_gauss_config = None
        self.discriminator = None

        self.migration_project_name = migration_project_name
        self.evaluation_project_id = evaluation_project_id
        self.target_db_info = target_db_info
        if open_gauss_config is not None:
            self.open_gauss_config = open_gauss_config

    @property
    def migration_project_name(self):
        """Gets the migration_project_name of this CreateMigrationProject.

        迁移项目名称。长度为5-50个字符，以英文字母开头，英文字母或数字结束，允许包含下划线和中划线。不允许重复。

        :return: The migration_project_name of this CreateMigrationProject.
        :rtype: str
        """
        return self._migration_project_name

    @migration_project_name.setter
    def migration_project_name(self, migration_project_name):
        """Sets the migration_project_name of this CreateMigrationProject.

        迁移项目名称。长度为5-50个字符，以英文字母开头，英文字母或数字结束，允许包含下划线和中划线。不允许重复。

        :param migration_project_name: The migration_project_name of this CreateMigrationProject.
        :type migration_project_name: str
        """
        self._migration_project_name = migration_project_name

    @property
    def evaluation_project_id(self):
        """Gets the evaluation_project_id of this CreateMigrationProject.

        评估项目ID。

        :return: The evaluation_project_id of this CreateMigrationProject.
        :rtype: int
        """
        return self._evaluation_project_id

    @evaluation_project_id.setter
    def evaluation_project_id(self, evaluation_project_id):
        """Sets the evaluation_project_id of this CreateMigrationProject.

        评估项目ID。

        :param evaluation_project_id: The evaluation_project_id of this CreateMigrationProject.
        :type evaluation_project_id: int
        """
        self._evaluation_project_id = evaluation_project_id

    @property
    def target_db_info(self):
        """Gets the target_db_info of this CreateMigrationProject.

        :return: The target_db_info of this CreateMigrationProject.
        :rtype: :class:`huaweicloudsdkugo.v1.TargetDBInfo`
        """
        return self._target_db_info

    @target_db_info.setter
    def target_db_info(self, target_db_info):
        """Sets the target_db_info of this CreateMigrationProject.

        :param target_db_info: The target_db_info of this CreateMigrationProject.
        :type target_db_info: :class:`huaweicloudsdkugo.v1.TargetDBInfo`
        """
        self._target_db_info = target_db_info

    @property
    def open_gauss_config(self):
        """Gets the open_gauss_config of this CreateMigrationProject.

        :return: The open_gauss_config of this CreateMigrationProject.
        :rtype: :class:`huaweicloudsdkugo.v1.OpenGaussConfig`
        """
        return self._open_gauss_config

    @open_gauss_config.setter
    def open_gauss_config(self, open_gauss_config):
        """Sets the open_gauss_config of this CreateMigrationProject.

        :param open_gauss_config: The open_gauss_config of this CreateMigrationProject.
        :type open_gauss_config: :class:`huaweicloudsdkugo.v1.OpenGaussConfig`
        """
        self._open_gauss_config = open_gauss_config

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
        if not isinstance(other, CreateMigrationProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
