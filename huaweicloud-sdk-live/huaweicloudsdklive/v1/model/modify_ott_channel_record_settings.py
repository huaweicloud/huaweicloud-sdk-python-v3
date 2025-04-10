# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyOttChannelRecordSettings:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'id': 'str',
        'record_settings': 'ModifyOttChannelRecordSettingsRecordSettings'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id',
        'record_settings': 'record_settings'
    }

    def __init__(self, domain=None, app_name=None, id=None, record_settings=None):
        r"""ModifyOttChannelRecordSettings

        The model defined in huaweicloud sdk

        :param domain: 频道推流域名
        :type domain: str
        :param app_name: 组名或应用名
        :type app_name: str
        :param id: 频道ID。频道唯一标识，为必填项
        :type id: str
        :param record_settings: 
        :type record_settings: :class:`huaweicloudsdklive.v1.ModifyOttChannelRecordSettingsRecordSettings`
        """
        
        

        self._domain = None
        self._app_name = None
        self._id = None
        self._record_settings = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name
        self.id = id
        if record_settings is not None:
            self.record_settings = record_settings

    @property
    def domain(self):
        r"""Gets the domain of this ModifyOttChannelRecordSettings.

        频道推流域名

        :return: The domain of this ModifyOttChannelRecordSettings.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ModifyOttChannelRecordSettings.

        频道推流域名

        :param domain: The domain of this ModifyOttChannelRecordSettings.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this ModifyOttChannelRecordSettings.

        组名或应用名

        :return: The app_name of this ModifyOttChannelRecordSettings.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ModifyOttChannelRecordSettings.

        组名或应用名

        :param app_name: The app_name of this ModifyOttChannelRecordSettings.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this ModifyOttChannelRecordSettings.

        频道ID。频道唯一标识，为必填项

        :return: The id of this ModifyOttChannelRecordSettings.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModifyOttChannelRecordSettings.

        频道ID。频道唯一标识，为必填项

        :param id: The id of this ModifyOttChannelRecordSettings.
        :type id: str
        """
        self._id = id

    @property
    def record_settings(self):
        r"""Gets the record_settings of this ModifyOttChannelRecordSettings.

        :return: The record_settings of this ModifyOttChannelRecordSettings.
        :rtype: :class:`huaweicloudsdklive.v1.ModifyOttChannelRecordSettingsRecordSettings`
        """
        return self._record_settings

    @record_settings.setter
    def record_settings(self, record_settings):
        r"""Sets the record_settings of this ModifyOttChannelRecordSettings.

        :param record_settings: The record_settings of this ModifyOttChannelRecordSettings.
        :type record_settings: :class:`huaweicloudsdklive.v1.ModifyOttChannelRecordSettingsRecordSettings`
        """
        self._record_settings = record_settings

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
        if not isinstance(other, ModifyOttChannelRecordSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
