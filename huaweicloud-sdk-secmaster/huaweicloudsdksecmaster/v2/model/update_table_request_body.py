# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_alias': 'str',
        'table_alias_en': 'str',
        'table_alias_fr': 'str',
        'description': 'str',
        'description_en': 'str',
        'description_fr': 'str',
        'directory': 'str',
        'directory_en': 'str',
        'directory_fr': 'str',
        'storage_setting': 'IsapTableStorageSettingDto',
        'display_setting': 'IsapTableDisplaySettingDto'
    }

    attribute_map = {
        'table_alias': 'table_alias',
        'table_alias_en': 'table_alias_en',
        'table_alias_fr': 'table_alias_fr',
        'description': 'description',
        'description_en': 'description_en',
        'description_fr': 'description_fr',
        'directory': 'directory',
        'directory_en': 'directory_en',
        'directory_fr': 'directory_fr',
        'storage_setting': 'storage_setting',
        'display_setting': 'display_setting'
    }

    def __init__(self, table_alias=None, table_alias_en=None, table_alias_fr=None, description=None, description_en=None, description_fr=None, directory=None, directory_en=None, directory_fr=None, storage_setting=None, display_setting=None):
        r"""UpdateTableRequestBody

        The model defined in huaweicloud sdk

        :param table_alias: 表别名
        :type table_alias: str
        :param table_alias_en: 表别名
        :type table_alias_en: str
        :param table_alias_fr: 表别名
        :type table_alias_fr: str
        :param description: 表相关描述
        :type description: str
        :param description_en: 表相关描述
        :type description_en: str
        :param description_fr: 表相关描述
        :type description_fr: str
        :param directory: 目录分组
        :type directory: str
        :param directory_en: 目录分组
        :type directory_en: str
        :param directory_fr: 目录分组
        :type directory_fr: str
        :param storage_setting: 
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.IsapTableStorageSettingDto`
        :param display_setting: 
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.IsapTableDisplaySettingDto`
        """
        
        

        self._table_alias = None
        self._table_alias_en = None
        self._table_alias_fr = None
        self._description = None
        self._description_en = None
        self._description_fr = None
        self._directory = None
        self._directory_en = None
        self._directory_fr = None
        self._storage_setting = None
        self._display_setting = None
        self.discriminator = None

        if table_alias is not None:
            self.table_alias = table_alias
        if table_alias_en is not None:
            self.table_alias_en = table_alias_en
        if table_alias_fr is not None:
            self.table_alias_fr = table_alias_fr
        if description is not None:
            self.description = description
        if description_en is not None:
            self.description_en = description_en
        if description_fr is not None:
            self.description_fr = description_fr
        if directory is not None:
            self.directory = directory
        if directory_en is not None:
            self.directory_en = directory_en
        if directory_fr is not None:
            self.directory_fr = directory_fr
        if storage_setting is not None:
            self.storage_setting = storage_setting
        if display_setting is not None:
            self.display_setting = display_setting

    @property
    def table_alias(self):
        r"""Gets the table_alias of this UpdateTableRequestBody.

        表别名

        :return: The table_alias of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        r"""Sets the table_alias of this UpdateTableRequestBody.

        表别名

        :param table_alias: The table_alias of this UpdateTableRequestBody.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def table_alias_en(self):
        r"""Gets the table_alias_en of this UpdateTableRequestBody.

        表别名

        :return: The table_alias_en of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._table_alias_en

    @table_alias_en.setter
    def table_alias_en(self, table_alias_en):
        r"""Sets the table_alias_en of this UpdateTableRequestBody.

        表别名

        :param table_alias_en: The table_alias_en of this UpdateTableRequestBody.
        :type table_alias_en: str
        """
        self._table_alias_en = table_alias_en

    @property
    def table_alias_fr(self):
        r"""Gets the table_alias_fr of this UpdateTableRequestBody.

        表别名

        :return: The table_alias_fr of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._table_alias_fr

    @table_alias_fr.setter
    def table_alias_fr(self, table_alias_fr):
        r"""Sets the table_alias_fr of this UpdateTableRequestBody.

        表别名

        :param table_alias_fr: The table_alias_fr of this UpdateTableRequestBody.
        :type table_alias_fr: str
        """
        self._table_alias_fr = table_alias_fr

    @property
    def description(self):
        r"""Gets the description of this UpdateTableRequestBody.

        表相关描述

        :return: The description of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateTableRequestBody.

        表相关描述

        :param description: The description of this UpdateTableRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        r"""Gets the description_en of this UpdateTableRequestBody.

        表相关描述

        :return: The description_en of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this UpdateTableRequestBody.

        表相关描述

        :param description_en: The description_en of this UpdateTableRequestBody.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def description_fr(self):
        r"""Gets the description_fr of this UpdateTableRequestBody.

        表相关描述

        :return: The description_fr of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._description_fr

    @description_fr.setter
    def description_fr(self, description_fr):
        r"""Sets the description_fr of this UpdateTableRequestBody.

        表相关描述

        :param description_fr: The description_fr of this UpdateTableRequestBody.
        :type description_fr: str
        """
        self._description_fr = description_fr

    @property
    def directory(self):
        r"""Gets the directory of this UpdateTableRequestBody.

        目录分组

        :return: The directory of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this UpdateTableRequestBody.

        目录分组

        :param directory: The directory of this UpdateTableRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def directory_en(self):
        r"""Gets the directory_en of this UpdateTableRequestBody.

        目录分组

        :return: The directory_en of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._directory_en

    @directory_en.setter
    def directory_en(self, directory_en):
        r"""Sets the directory_en of this UpdateTableRequestBody.

        目录分组

        :param directory_en: The directory_en of this UpdateTableRequestBody.
        :type directory_en: str
        """
        self._directory_en = directory_en

    @property
    def directory_fr(self):
        r"""Gets the directory_fr of this UpdateTableRequestBody.

        目录分组

        :return: The directory_fr of this UpdateTableRequestBody.
        :rtype: str
        """
        return self._directory_fr

    @directory_fr.setter
    def directory_fr(self, directory_fr):
        r"""Sets the directory_fr of this UpdateTableRequestBody.

        目录分组

        :param directory_fr: The directory_fr of this UpdateTableRequestBody.
        :type directory_fr: str
        """
        self._directory_fr = directory_fr

    @property
    def storage_setting(self):
        r"""Gets the storage_setting of this UpdateTableRequestBody.

        :return: The storage_setting of this UpdateTableRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapTableStorageSettingDto`
        """
        return self._storage_setting

    @storage_setting.setter
    def storage_setting(self, storage_setting):
        r"""Sets the storage_setting of this UpdateTableRequestBody.

        :param storage_setting: The storage_setting of this UpdateTableRequestBody.
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.IsapTableStorageSettingDto`
        """
        self._storage_setting = storage_setting

    @property
    def display_setting(self):
        r"""Gets the display_setting of this UpdateTableRequestBody.

        :return: The display_setting of this UpdateTableRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapTableDisplaySettingDto`
        """
        return self._display_setting

    @display_setting.setter
    def display_setting(self, display_setting):
        r"""Sets the display_setting of this UpdateTableRequestBody.

        :param display_setting: The display_setting of this UpdateTableRequestBody.
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.IsapTableDisplaySettingDto`
        """
        self._display_setting = display_setting

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
