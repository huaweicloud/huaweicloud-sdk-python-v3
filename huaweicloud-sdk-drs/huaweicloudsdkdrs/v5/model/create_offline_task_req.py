# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOfflineTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_info': 'BackupJobBaseInfo',
        'target_db_info': 'BackupJobEndpointInfo',
        'backup_info': 'BackupInfo',
        'options': 'BackupRestoreOptionInfo'
    }

    attribute_map = {
        'base_info': 'base_info',
        'target_db_info': 'target_db_info',
        'backup_info': 'backup_info',
        'options': 'options'
    }

    def __init__(self, base_info=None, target_db_info=None, backup_info=None, options=None):
        r"""CreateOfflineTaskReq

        The model defined in huaweicloud sdk

        :param base_info: 
        :type base_info: :class:`huaweicloudsdkdrs.v5.BackupJobBaseInfo`
        :param target_db_info: 
        :type target_db_info: :class:`huaweicloudsdkdrs.v5.BackupJobEndpointInfo`
        :param backup_info: 
        :type backup_info: :class:`huaweicloudsdkdrs.v5.BackupInfo`
        :param options: 
        :type options: :class:`huaweicloudsdkdrs.v5.BackupRestoreOptionInfo`
        """
        
        

        self._base_info = None
        self._target_db_info = None
        self._backup_info = None
        self._options = None
        self.discriminator = None

        self.base_info = base_info
        self.target_db_info = target_db_info
        self.backup_info = backup_info
        self.options = options

    @property
    def base_info(self):
        r"""Gets the base_info of this CreateOfflineTaskReq.

        :return: The base_info of this CreateOfflineTaskReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupJobBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this CreateOfflineTaskReq.

        :param base_info: The base_info of this CreateOfflineTaskReq.
        :type base_info: :class:`huaweicloudsdkdrs.v5.BackupJobBaseInfo`
        """
        self._base_info = base_info

    @property
    def target_db_info(self):
        r"""Gets the target_db_info of this CreateOfflineTaskReq.

        :return: The target_db_info of this CreateOfflineTaskReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupJobEndpointInfo`
        """
        return self._target_db_info

    @target_db_info.setter
    def target_db_info(self, target_db_info):
        r"""Sets the target_db_info of this CreateOfflineTaskReq.

        :param target_db_info: The target_db_info of this CreateOfflineTaskReq.
        :type target_db_info: :class:`huaweicloudsdkdrs.v5.BackupJobEndpointInfo`
        """
        self._target_db_info = target_db_info

    @property
    def backup_info(self):
        r"""Gets the backup_info of this CreateOfflineTaskReq.

        :return: The backup_info of this CreateOfflineTaskReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupInfo`
        """
        return self._backup_info

    @backup_info.setter
    def backup_info(self, backup_info):
        r"""Sets the backup_info of this CreateOfflineTaskReq.

        :param backup_info: The backup_info of this CreateOfflineTaskReq.
        :type backup_info: :class:`huaweicloudsdkdrs.v5.BackupInfo`
        """
        self._backup_info = backup_info

    @property
    def options(self):
        r"""Gets the options of this CreateOfflineTaskReq.

        :return: The options of this CreateOfflineTaskReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupRestoreOptionInfo`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this CreateOfflineTaskReq.

        :param options: The options of this CreateOfflineTaskReq.
        :type options: :class:`huaweicloudsdkdrs.v5.BackupRestoreOptionInfo`
        """
        self._options = options

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
        if not isinstance(other, CreateOfflineTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
