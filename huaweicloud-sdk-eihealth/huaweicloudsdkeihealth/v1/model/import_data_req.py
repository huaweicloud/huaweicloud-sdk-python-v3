# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDataReq:

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
        'source_project_id': 'str',
        'sub_paths': 'list[str]',
        'target_folder': 'str'
    }

    attribute_map = {
        'overwrite': 'overwrite',
        'source_project_id': 'source_project_id',
        'sub_paths': 'sub_paths',
        'target_folder': 'target_folder'
    }

    def __init__(self, overwrite=None, source_project_id=None, sub_paths=None, target_folder=None):
        """ImportDataReq

        The model defined in huaweicloud sdk

        :param overwrite: 执行策略（true：全部覆盖，false：全部跳过，默认为true）
        :type overwrite: bool
        :param source_project_id: 源项目ID
        :type source_project_id: str
        :param sub_paths: 导入路径集
        :type sub_paths: list[str]
        :param target_folder: 目标文件夹
        :type target_folder: str
        """
        
        

        self._overwrite = None
        self._source_project_id = None
        self._sub_paths = None
        self._target_folder = None
        self.discriminator = None

        if overwrite is not None:
            self.overwrite = overwrite
        self.source_project_id = source_project_id
        self.sub_paths = sub_paths
        if target_folder is not None:
            self.target_folder = target_folder

    @property
    def overwrite(self):
        """Gets the overwrite of this ImportDataReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :return: The overwrite of this ImportDataReq.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this ImportDataReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :param overwrite: The overwrite of this ImportDataReq.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def source_project_id(self):
        """Gets the source_project_id of this ImportDataReq.

        源项目ID

        :return: The source_project_id of this ImportDataReq.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this ImportDataReq.

        源项目ID

        :param source_project_id: The source_project_id of this ImportDataReq.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def sub_paths(self):
        """Gets the sub_paths of this ImportDataReq.

        导入路径集

        :return: The sub_paths of this ImportDataReq.
        :rtype: list[str]
        """
        return self._sub_paths

    @sub_paths.setter
    def sub_paths(self, sub_paths):
        """Sets the sub_paths of this ImportDataReq.

        导入路径集

        :param sub_paths: The sub_paths of this ImportDataReq.
        :type sub_paths: list[str]
        """
        self._sub_paths = sub_paths

    @property
    def target_folder(self):
        """Gets the target_folder of this ImportDataReq.

        目标文件夹

        :return: The target_folder of this ImportDataReq.
        :rtype: str
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        """Sets the target_folder of this ImportDataReq.

        目标文件夹

        :param target_folder: The target_folder of this ImportDataReq.
        :type target_folder: str
        """
        self._target_folder = target_folder

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
        if not isinstance(other, ImportDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
