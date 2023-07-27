# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'migrate_type': 'str',
        'configurations': 'list[ConfigBody]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'migrate_type': 'migrate_type',
        'configurations': 'configurations'
    }

    def __init__(self, task_id=None, migrate_type=None, configurations=None):
        """ShowConfigSettingResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param migrate_type: 迁移类型
        :type migrate_type: str
        :param configurations: 配置项的具体配置信息
        :type configurations: list[:class:`huaweicloudsdksms.v3.ConfigBody`]
        """
        
        super(ShowConfigSettingResponse, self).__init__()

        self._task_id = None
        self._migrate_type = None
        self._configurations = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if migrate_type is not None:
            self.migrate_type = migrate_type
        if configurations is not None:
            self.configurations = configurations

    @property
    def task_id(self):
        """Gets the task_id of this ShowConfigSettingResponse.

        任务ID

        :return: The task_id of this ShowConfigSettingResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowConfigSettingResponse.

        任务ID

        :param task_id: The task_id of this ShowConfigSettingResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def migrate_type(self):
        """Gets the migrate_type of this ShowConfigSettingResponse.

        迁移类型

        :return: The migrate_type of this ShowConfigSettingResponse.
        :rtype: str
        """
        return self._migrate_type

    @migrate_type.setter
    def migrate_type(self, migrate_type):
        """Sets the migrate_type of this ShowConfigSettingResponse.

        迁移类型

        :param migrate_type: The migrate_type of this ShowConfigSettingResponse.
        :type migrate_type: str
        """
        self._migrate_type = migrate_type

    @property
    def configurations(self):
        """Gets the configurations of this ShowConfigSettingResponse.

        配置项的具体配置信息

        :return: The configurations of this ShowConfigSettingResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.ConfigBody`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this ShowConfigSettingResponse.

        配置项的具体配置信息

        :param configurations: The configurations of this ShowConfigSettingResponse.
        :type configurations: list[:class:`huaweicloudsdksms.v3.ConfigBody`]
        """
        self._configurations = configurations

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
        if not isinstance(other, ShowConfigSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
