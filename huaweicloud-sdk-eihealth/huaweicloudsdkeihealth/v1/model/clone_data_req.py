# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneDataReq:

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
        'sub_paths': 'list[str]',
        'target_folder': 'str'
    }

    attribute_map = {
        'overwrite': 'overwrite',
        'sub_paths': 'sub_paths',
        'target_folder': 'target_folder'
    }

    def __init__(self, overwrite=None, sub_paths=None, target_folder=None):
        """CloneDataReq

        The model defined in huaweicloud sdk

        :param overwrite: 执行策略（true：全部覆盖，false：全部跳过，默认为true）
        :type overwrite: bool
        :param sub_paths: 复制的路径集
        :type sub_paths: list[str]
        :param target_folder: 目标文件夹
        :type target_folder: str
        """
        
        

        self._overwrite = None
        self._sub_paths = None
        self._target_folder = None
        self.discriminator = None

        if overwrite is not None:
            self.overwrite = overwrite
        self.sub_paths = sub_paths
        if target_folder is not None:
            self.target_folder = target_folder

    @property
    def overwrite(self):
        """Gets the overwrite of this CloneDataReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :return: The overwrite of this CloneDataReq.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this CloneDataReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :param overwrite: The overwrite of this CloneDataReq.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def sub_paths(self):
        """Gets the sub_paths of this CloneDataReq.

        复制的路径集

        :return: The sub_paths of this CloneDataReq.
        :rtype: list[str]
        """
        return self._sub_paths

    @sub_paths.setter
    def sub_paths(self, sub_paths):
        """Sets the sub_paths of this CloneDataReq.

        复制的路径集

        :param sub_paths: The sub_paths of this CloneDataReq.
        :type sub_paths: list[str]
        """
        self._sub_paths = sub_paths

    @property
    def target_folder(self):
        """Gets the target_folder of this CloneDataReq.

        目标文件夹

        :return: The target_folder of this CloneDataReq.
        :rtype: str
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        """Sets the target_folder of this CloneDataReq.

        目标文件夹

        :param target_folder: The target_folder of this CloneDataReq.
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
        if not isinstance(other, CloneDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
