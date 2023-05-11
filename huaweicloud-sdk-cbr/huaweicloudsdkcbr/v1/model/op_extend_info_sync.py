# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpExtendInfoSync:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_backup_num': 'int',
        'delete_backup_num': 'int',
        'err_sync_backup_num': 'int'
    }

    attribute_map = {
        'sync_backup_num': 'sync_backup_num',
        'delete_backup_num': 'delete_backup_num',
        'err_sync_backup_num': 'err_sync_backup_num'
    }

    def __init__(self, sync_backup_num=None, delete_backup_num=None, err_sync_backup_num=None):
        """OpExtendInfoSync

        The model defined in huaweicloud sdk

        :param sync_backup_num: 同步备份副本数
        :type sync_backup_num: int
        :param delete_backup_num: 删除的备份副本数
        :type delete_backup_num: int
        :param err_sync_backup_num: 同步失败备副本数
        :type err_sync_backup_num: int
        """
        
        

        self._sync_backup_num = None
        self._delete_backup_num = None
        self._err_sync_backup_num = None
        self.discriminator = None

        if sync_backup_num is not None:
            self.sync_backup_num = sync_backup_num
        if delete_backup_num is not None:
            self.delete_backup_num = delete_backup_num
        if err_sync_backup_num is not None:
            self.err_sync_backup_num = err_sync_backup_num

    @property
    def sync_backup_num(self):
        """Gets the sync_backup_num of this OpExtendInfoSync.

        同步备份副本数

        :return: The sync_backup_num of this OpExtendInfoSync.
        :rtype: int
        """
        return self._sync_backup_num

    @sync_backup_num.setter
    def sync_backup_num(self, sync_backup_num):
        """Sets the sync_backup_num of this OpExtendInfoSync.

        同步备份副本数

        :param sync_backup_num: The sync_backup_num of this OpExtendInfoSync.
        :type sync_backup_num: int
        """
        self._sync_backup_num = sync_backup_num

    @property
    def delete_backup_num(self):
        """Gets the delete_backup_num of this OpExtendInfoSync.

        删除的备份副本数

        :return: The delete_backup_num of this OpExtendInfoSync.
        :rtype: int
        """
        return self._delete_backup_num

    @delete_backup_num.setter
    def delete_backup_num(self, delete_backup_num):
        """Sets the delete_backup_num of this OpExtendInfoSync.

        删除的备份副本数

        :param delete_backup_num: The delete_backup_num of this OpExtendInfoSync.
        :type delete_backup_num: int
        """
        self._delete_backup_num = delete_backup_num

    @property
    def err_sync_backup_num(self):
        """Gets the err_sync_backup_num of this OpExtendInfoSync.

        同步失败备副本数

        :return: The err_sync_backup_num of this OpExtendInfoSync.
        :rtype: int
        """
        return self._err_sync_backup_num

    @err_sync_backup_num.setter
    def err_sync_backup_num(self, err_sync_backup_num):
        """Sets the err_sync_backup_num of this OpExtendInfoSync.

        同步失败备副本数

        :param err_sync_backup_num: The err_sync_backup_num of this OpExtendInfoSync.
        :type err_sync_backup_num: int
        """
        self._err_sync_backup_num = err_sync_backup_num

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
        if not isinstance(other, OpExtendInfoSync):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
