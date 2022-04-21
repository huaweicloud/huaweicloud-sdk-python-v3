# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteReplicationRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'delete_target_volume': 'bool'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'delete_target_volume': 'delete_target_volume'
    }

    def __init__(self, server_group_id=None, delete_target_volume=None):
        """DeleteReplicationRequestParams

        The model defined in huaweicloud sdk

        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param delete_target_volume: 是否删除容灾站点磁盘，默认值为false。
        :type delete_target_volume: bool
        """
        
        

        self._server_group_id = None
        self._delete_target_volume = None
        self.discriminator = None

        if server_group_id is not None:
            self.server_group_id = server_group_id
        if delete_target_volume is not None:
            self.delete_target_volume = delete_target_volume

    @property
    def server_group_id(self):
        """Gets the server_group_id of this DeleteReplicationRequestParams.

        保护组的ID。

        :return: The server_group_id of this DeleteReplicationRequestParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this DeleteReplicationRequestParams.

        保护组的ID。

        :param server_group_id: The server_group_id of this DeleteReplicationRequestParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def delete_target_volume(self):
        """Gets the delete_target_volume of this DeleteReplicationRequestParams.

        是否删除容灾站点磁盘，默认值为false。

        :return: The delete_target_volume of this DeleteReplicationRequestParams.
        :rtype: bool
        """
        return self._delete_target_volume

    @delete_target_volume.setter
    def delete_target_volume(self, delete_target_volume):
        """Sets the delete_target_volume of this DeleteReplicationRequestParams.

        是否删除容灾站点磁盘，默认值为false。

        :param delete_target_volume: The delete_target_volume of this DeleteReplicationRequestParams.
        :type delete_target_volume: bool
        """
        self._delete_target_volume = delete_target_volume

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
        if not isinstance(other, DeleteReplicationRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
