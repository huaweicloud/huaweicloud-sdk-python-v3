# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreBackupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'overwrite': 'bool',
        'target_folder': 'str',
        'target_project_id': 'str'
    }

    attribute_map = {
        'overwrite': 'overwrite',
        'target_folder': 'target_folder',
        'target_project_id': 'target_project_id'
    }

    def __init__(self, overwrite=None, target_folder=None, target_project_id=None):
        """RestoreBackupReq

        The model defined in huaweicloud sdk

        :param overwrite: 执行策略（true：全部覆盖，false：全部跳过，默认为true）
        :type overwrite: bool
        :param target_folder: 目标文件夹
        :type target_folder: str
        :param target_project_id: 目标项目ID
        :type target_project_id: str
        """
        
        

        self._overwrite = None
        self._target_folder = None
        self._target_project_id = None
        self.discriminator = None

        if overwrite is not None:
            self.overwrite = overwrite
        if target_folder is not None:
            self.target_folder = target_folder
        self.target_project_id = target_project_id

    @property
    def overwrite(self):
        """Gets the overwrite of this RestoreBackupReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :return: The overwrite of this RestoreBackupReq.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this RestoreBackupReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :param overwrite: The overwrite of this RestoreBackupReq.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def target_folder(self):
        """Gets the target_folder of this RestoreBackupReq.

        目标文件夹

        :return: The target_folder of this RestoreBackupReq.
        :rtype: str
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        """Sets the target_folder of this RestoreBackupReq.

        目标文件夹

        :param target_folder: The target_folder of this RestoreBackupReq.
        :type target_folder: str
        """
        self._target_folder = target_folder

    @property
    def target_project_id(self):
        """Gets the target_project_id of this RestoreBackupReq.

        目标项目ID

        :return: The target_project_id of this RestoreBackupReq.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        """Sets the target_project_id of this RestoreBackupReq.

        目标项目ID

        :param target_project_id: The target_project_id of this RestoreBackupReq.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

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
        if not isinstance(other, RestoreBackupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
