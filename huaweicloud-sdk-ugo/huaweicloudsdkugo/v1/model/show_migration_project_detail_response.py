# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMigrationProjectDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migration_project_id': 'int',
        'migration_project_name': 'str',
        'evaluation_project_name': 'str',
        'source_db_info': 'DataBase',
        'target_db_info': 'DataBase',
        'created_time': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'migration_project_id': 'migration_project_id',
        'migration_project_name': 'migration_project_name',
        'evaluation_project_name': 'evaluation_project_name',
        'source_db_info': 'source_db_info',
        'target_db_info': 'target_db_info',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, migration_project_id=None, migration_project_name=None, evaluation_project_name=None, source_db_info=None, target_db_info=None, created_time=None, updated_time=None):
        """ShowMigrationProjectDetailResponse

        The model defined in huaweicloud sdk

        :param migration_project_id: 迁移项目ID。
        :type migration_project_id: int
        :param migration_project_name: 迁移项目状态。
        :type migration_project_name: str
        :param evaluation_project_name: 对应的评估项目名称。
        :type evaluation_project_name: str
        :param source_db_info: 
        :type source_db_info: :class:`huaweicloudsdkugo.v1.DataBase`
        :param target_db_info: 
        :type target_db_info: :class:`huaweicloudsdkugo.v1.DataBase`
        :param created_time: 创建时间。
        :type created_time: str
        :param updated_time: 更新时间。
        :type updated_time: str
        """
        
        super(ShowMigrationProjectDetailResponse, self).__init__()

        self._migration_project_id = None
        self._migration_project_name = None
        self._evaluation_project_name = None
        self._source_db_info = None
        self._target_db_info = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if migration_project_id is not None:
            self.migration_project_id = migration_project_id
        if migration_project_name is not None:
            self.migration_project_name = migration_project_name
        if evaluation_project_name is not None:
            self.evaluation_project_name = evaluation_project_name
        if source_db_info is not None:
            self.source_db_info = source_db_info
        if target_db_info is not None:
            self.target_db_info = target_db_info
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def migration_project_id(self):
        """Gets the migration_project_id of this ShowMigrationProjectDetailResponse.

        迁移项目ID。

        :return: The migration_project_id of this ShowMigrationProjectDetailResponse.
        :rtype: int
        """
        return self._migration_project_id

    @migration_project_id.setter
    def migration_project_id(self, migration_project_id):
        """Sets the migration_project_id of this ShowMigrationProjectDetailResponse.

        迁移项目ID。

        :param migration_project_id: The migration_project_id of this ShowMigrationProjectDetailResponse.
        :type migration_project_id: int
        """
        self._migration_project_id = migration_project_id

    @property
    def migration_project_name(self):
        """Gets the migration_project_name of this ShowMigrationProjectDetailResponse.

        迁移项目状态。

        :return: The migration_project_name of this ShowMigrationProjectDetailResponse.
        :rtype: str
        """
        return self._migration_project_name

    @migration_project_name.setter
    def migration_project_name(self, migration_project_name):
        """Sets the migration_project_name of this ShowMigrationProjectDetailResponse.

        迁移项目状态。

        :param migration_project_name: The migration_project_name of this ShowMigrationProjectDetailResponse.
        :type migration_project_name: str
        """
        self._migration_project_name = migration_project_name

    @property
    def evaluation_project_name(self):
        """Gets the evaluation_project_name of this ShowMigrationProjectDetailResponse.

        对应的评估项目名称。

        :return: The evaluation_project_name of this ShowMigrationProjectDetailResponse.
        :rtype: str
        """
        return self._evaluation_project_name

    @evaluation_project_name.setter
    def evaluation_project_name(self, evaluation_project_name):
        """Sets the evaluation_project_name of this ShowMigrationProjectDetailResponse.

        对应的评估项目名称。

        :param evaluation_project_name: The evaluation_project_name of this ShowMigrationProjectDetailResponse.
        :type evaluation_project_name: str
        """
        self._evaluation_project_name = evaluation_project_name

    @property
    def source_db_info(self):
        """Gets the source_db_info of this ShowMigrationProjectDetailResponse.

        :return: The source_db_info of this ShowMigrationProjectDetailResponse.
        :rtype: :class:`huaweicloudsdkugo.v1.DataBase`
        """
        return self._source_db_info

    @source_db_info.setter
    def source_db_info(self, source_db_info):
        """Sets the source_db_info of this ShowMigrationProjectDetailResponse.

        :param source_db_info: The source_db_info of this ShowMigrationProjectDetailResponse.
        :type source_db_info: :class:`huaweicloudsdkugo.v1.DataBase`
        """
        self._source_db_info = source_db_info

    @property
    def target_db_info(self):
        """Gets the target_db_info of this ShowMigrationProjectDetailResponse.

        :return: The target_db_info of this ShowMigrationProjectDetailResponse.
        :rtype: :class:`huaweicloudsdkugo.v1.DataBase`
        """
        return self._target_db_info

    @target_db_info.setter
    def target_db_info(self, target_db_info):
        """Sets the target_db_info of this ShowMigrationProjectDetailResponse.

        :param target_db_info: The target_db_info of this ShowMigrationProjectDetailResponse.
        :type target_db_info: :class:`huaweicloudsdkugo.v1.DataBase`
        """
        self._target_db_info = target_db_info

    @property
    def created_time(self):
        """Gets the created_time of this ShowMigrationProjectDetailResponse.

        创建时间。

        :return: The created_time of this ShowMigrationProjectDetailResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowMigrationProjectDetailResponse.

        创建时间。

        :param created_time: The created_time of this ShowMigrationProjectDetailResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowMigrationProjectDetailResponse.

        更新时间。

        :return: The updated_time of this ShowMigrationProjectDetailResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowMigrationProjectDetailResponse.

        更新时间。

        :param updated_time: The updated_time of this ShowMigrationProjectDetailResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, ShowMigrationProjectDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
