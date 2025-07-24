# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBackendTargetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'target_id': 'str',
        'delete_data_in_file_system': 'bool'
    }

    attribute_map = {
        'share_id': 'share_id',
        'target_id': 'target_id',
        'delete_data_in_file_system': 'delete_data_in_file_system'
    }

    def __init__(self, share_id=None, target_id=None, delete_data_in_file_system=None):
        r"""DeleteBackendTargetRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统ID
        :type share_id: str
        :param target_id: 绑定关系ID
        :type target_id: str
        :param delete_data_in_file_system: 删除后端存储时是否同时删除文件系统内的联动目录及其数据文件，默认为 false。数据删除后无法恢复，请谨慎操作。
        :type delete_data_in_file_system: bool
        """
        
        

        self._share_id = None
        self._target_id = None
        self._delete_data_in_file_system = None
        self.discriminator = None

        self.share_id = share_id
        self.target_id = target_id
        if delete_data_in_file_system is not None:
            self.delete_data_in_file_system = delete_data_in_file_system

    @property
    def share_id(self):
        r"""Gets the share_id of this DeleteBackendTargetRequest.

        文件系统ID

        :return: The share_id of this DeleteBackendTargetRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this DeleteBackendTargetRequest.

        文件系统ID

        :param share_id: The share_id of this DeleteBackendTargetRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def target_id(self):
        r"""Gets the target_id of this DeleteBackendTargetRequest.

        绑定关系ID

        :return: The target_id of this DeleteBackendTargetRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this DeleteBackendTargetRequest.

        绑定关系ID

        :param target_id: The target_id of this DeleteBackendTargetRequest.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def delete_data_in_file_system(self):
        r"""Gets the delete_data_in_file_system of this DeleteBackendTargetRequest.

        删除后端存储时是否同时删除文件系统内的联动目录及其数据文件，默认为 false。数据删除后无法恢复，请谨慎操作。

        :return: The delete_data_in_file_system of this DeleteBackendTargetRequest.
        :rtype: bool
        """
        return self._delete_data_in_file_system

    @delete_data_in_file_system.setter
    def delete_data_in_file_system(self, delete_data_in_file_system):
        r"""Sets the delete_data_in_file_system of this DeleteBackendTargetRequest.

        删除后端存储时是否同时删除文件系统内的联动目录及其数据文件，默认为 false。数据删除后无法恢复，请谨慎操作。

        :param delete_data_in_file_system: The delete_data_in_file_system of this DeleteBackendTargetRequest.
        :type delete_data_in_file_system: bool
        """
        self._delete_data_in_file_system = delete_data_in_file_system

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
        if not isinstance(other, DeleteBackendTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
