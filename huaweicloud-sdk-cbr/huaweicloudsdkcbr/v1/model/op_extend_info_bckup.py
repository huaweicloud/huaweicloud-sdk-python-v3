# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpExtendInfoBckup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_consistency_error_code': 'str',
        'app_consistency_error_message': 'str',
        'app_consistency_status': 'str',
        'backup_id': 'str',
        'backup_name': 'str',
        'incremental': 'str'
    }

    attribute_map = {
        'app_consistency_error_code': 'app_consistency_error_code',
        'app_consistency_error_message': 'app_consistency_error_message',
        'app_consistency_status': 'app_consistency_status',
        'backup_id': 'backup_id',
        'backup_name': 'backup_name',
        'incremental': 'incremental'
    }

    def __init__(self, app_consistency_error_code=None, app_consistency_error_message=None, app_consistency_status=None, backup_id=None, backup_name=None, incremental=None):
        """OpExtendInfoBckup

        The model defined in huaweicloud sdk

        :param app_consistency_error_code: 应用一致性备份失败错误码。请参见[错误码](ErrorCode.xml)。
        :type app_consistency_error_code: str
        :param app_consistency_error_message: 应用一致性备份错误信息
        :type app_consistency_error_message: str
        :param app_consistency_status: 应用一致性备份状态；0:非应用一致性，1：应用一致性备份
        :type app_consistency_status: str
        :param backup_id: 备份副本ID
        :type backup_id: str
        :param backup_name: 备份名称
        :type backup_name: str
        :param incremental: 是否增备
        :type incremental: str
        """
        
        

        self._app_consistency_error_code = None
        self._app_consistency_error_message = None
        self._app_consistency_status = None
        self._backup_id = None
        self._backup_name = None
        self._incremental = None
        self.discriminator = None

        if app_consistency_error_code is not None:
            self.app_consistency_error_code = app_consistency_error_code
        if app_consistency_error_message is not None:
            self.app_consistency_error_message = app_consistency_error_message
        if app_consistency_status is not None:
            self.app_consistency_status = app_consistency_status
        self.backup_id = backup_id
        if backup_name is not None:
            self.backup_name = backup_name
        if incremental is not None:
            self.incremental = incremental

    @property
    def app_consistency_error_code(self):
        """Gets the app_consistency_error_code of this OpExtendInfoBckup.

        应用一致性备份失败错误码。请参见[错误码](ErrorCode.xml)。

        :return: The app_consistency_error_code of this OpExtendInfoBckup.
        :rtype: str
        """
        return self._app_consistency_error_code

    @app_consistency_error_code.setter
    def app_consistency_error_code(self, app_consistency_error_code):
        """Sets the app_consistency_error_code of this OpExtendInfoBckup.

        应用一致性备份失败错误码。请参见[错误码](ErrorCode.xml)。

        :param app_consistency_error_code: The app_consistency_error_code of this OpExtendInfoBckup.
        :type app_consistency_error_code: str
        """
        self._app_consistency_error_code = app_consistency_error_code

    @property
    def app_consistency_error_message(self):
        """Gets the app_consistency_error_message of this OpExtendInfoBckup.

        应用一致性备份错误信息

        :return: The app_consistency_error_message of this OpExtendInfoBckup.
        :rtype: str
        """
        return self._app_consistency_error_message

    @app_consistency_error_message.setter
    def app_consistency_error_message(self, app_consistency_error_message):
        """Sets the app_consistency_error_message of this OpExtendInfoBckup.

        应用一致性备份错误信息

        :param app_consistency_error_message: The app_consistency_error_message of this OpExtendInfoBckup.
        :type app_consistency_error_message: str
        """
        self._app_consistency_error_message = app_consistency_error_message

    @property
    def app_consistency_status(self):
        """Gets the app_consistency_status of this OpExtendInfoBckup.

        应用一致性备份状态；0:非应用一致性，1：应用一致性备份

        :return: The app_consistency_status of this OpExtendInfoBckup.
        :rtype: str
        """
        return self._app_consistency_status

    @app_consistency_status.setter
    def app_consistency_status(self, app_consistency_status):
        """Sets the app_consistency_status of this OpExtendInfoBckup.

        应用一致性备份状态；0:非应用一致性，1：应用一致性备份

        :param app_consistency_status: The app_consistency_status of this OpExtendInfoBckup.
        :type app_consistency_status: str
        """
        self._app_consistency_status = app_consistency_status

    @property
    def backup_id(self):
        """Gets the backup_id of this OpExtendInfoBckup.

        备份副本ID

        :return: The backup_id of this OpExtendInfoBckup.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this OpExtendInfoBckup.

        备份副本ID

        :param backup_id: The backup_id of this OpExtendInfoBckup.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_name(self):
        """Gets the backup_name of this OpExtendInfoBckup.

        备份名称

        :return: The backup_name of this OpExtendInfoBckup.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """Sets the backup_name of this OpExtendInfoBckup.

        备份名称

        :param backup_name: The backup_name of this OpExtendInfoBckup.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def incremental(self):
        """Gets the incremental of this OpExtendInfoBckup.

        是否增备

        :return: The incremental of this OpExtendInfoBckup.
        :rtype: str
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this OpExtendInfoBckup.

        是否增备

        :param incremental: The incremental of this OpExtendInfoBckup.
        :type incremental: str
        """
        self._incremental = incremental

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
        if not isinstance(other, OpExtendInfoBckup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
