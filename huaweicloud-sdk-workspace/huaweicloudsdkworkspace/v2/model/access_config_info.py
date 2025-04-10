# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'backup_mode': 'str',
        'backup_info': 'list[BackupInfo]'
    }

    attribute_map = {
        'site_id': 'site_id',
        'backup_mode': 'backup_mode',
        'backup_info': 'backup_info'
    }

    def __init__(self, site_id=None, backup_mode=None, backup_info=None):
        r"""AccessConfigInfo

        The model defined in huaweicloud sdk

        :param site_id: 站点Id。
        :type site_id: str
        :param backup_mode: 备份模式是否开启。 - ON:开启。 - OFF:关闭。
        :type backup_mode: str
        :param backup_info: 备份信息。
        :type backup_info: list[:class:`huaweicloudsdkworkspace.v2.BackupInfo`]
        """
        
        

        self._site_id = None
        self._backup_mode = None
        self._backup_info = None
        self.discriminator = None

        self.site_id = site_id
        self.backup_mode = backup_mode
        if backup_info is not None:
            self.backup_info = backup_info

    @property
    def site_id(self):
        r"""Gets the site_id of this AccessConfigInfo.

        站点Id。

        :return: The site_id of this AccessConfigInfo.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this AccessConfigInfo.

        站点Id。

        :param site_id: The site_id of this AccessConfigInfo.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def backup_mode(self):
        r"""Gets the backup_mode of this AccessConfigInfo.

        备份模式是否开启。 - ON:开启。 - OFF:关闭。

        :return: The backup_mode of this AccessConfigInfo.
        :rtype: str
        """
        return self._backup_mode

    @backup_mode.setter
    def backup_mode(self, backup_mode):
        r"""Sets the backup_mode of this AccessConfigInfo.

        备份模式是否开启。 - ON:开启。 - OFF:关闭。

        :param backup_mode: The backup_mode of this AccessConfigInfo.
        :type backup_mode: str
        """
        self._backup_mode = backup_mode

    @property
    def backup_info(self):
        r"""Gets the backup_info of this AccessConfigInfo.

        备份信息。

        :return: The backup_info of this AccessConfigInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.BackupInfo`]
        """
        return self._backup_info

    @backup_info.setter
    def backup_info(self, backup_info):
        r"""Sets the backup_info of this AccessConfigInfo.

        备份信息。

        :param backup_info: The backup_info of this AccessConfigInfo.
        :type backup_info: list[:class:`huaweicloudsdkworkspace.v2.BackupInfo`]
        """
        self._backup_info = backup_info

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
        if not isinstance(other, AccessConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
