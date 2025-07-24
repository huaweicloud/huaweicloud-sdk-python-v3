# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareTypeResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_type': 'str',
        'scenario': 'str',
        'attribution': 'ShareTypesAttribution',
        'spec_id': 'str',
        'share_type_usage': 'ShareTypeUsage',
        'support_period': 'bool',
        'available_zones': 'list[ShareTypeAvailableZone]',
        'spec_code': 'str',
        'storage_media': 'str',
        'features': 'list[str]'
    }

    attribute_map = {
        'share_type': 'share_type',
        'scenario': 'scenario',
        'attribution': 'attribution',
        'spec_id': 'spec_id',
        'share_type_usage': 'share_type_usage',
        'support_period': 'support_period',
        'available_zones': 'available_zones',
        'spec_code': 'spec_code',
        'storage_media': 'storage_media',
        'features': 'features'
    }

    def __init__(self, share_type=None, scenario=None, attribution=None, spec_id=None, share_type_usage=None, support_period=None, available_zones=None, spec_code=None, storage_media=None, features=None):
        r"""ShareTypeResponseBody

        The model defined in huaweicloud sdk

        :param share_type: 文件系统类型
        :type share_type: str
        :param scenario: 文件系统场景
        :type scenario: str
        :param attribution: 
        :type attribution: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttribution`
        :param spec_id: 文件系统规格ID
        :type spec_id: str
        :param share_type_usage: 
        :type share_type_usage: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsage`
        :param support_period: 是否支持包周期
        :type support_period: bool
        :param available_zones: 可用区
        :type available_zones: list[:class:`huaweicloudsdksfsturbo.v1.ShareTypeAvailableZone`]
        :param spec_code: 文件系统规格编码
        :type spec_code: str
        :param storage_media: 存储类型
        :type storage_media: str
        :param features: 实例支持的特性列表
        :type features: list[str]
        """
        
        

        self._share_type = None
        self._scenario = None
        self._attribution = None
        self._spec_id = None
        self._share_type_usage = None
        self._support_period = None
        self._available_zones = None
        self._spec_code = None
        self._storage_media = None
        self._features = None
        self.discriminator = None

        if share_type is not None:
            self.share_type = share_type
        if scenario is not None:
            self.scenario = scenario
        if attribution is not None:
            self.attribution = attribution
        if spec_id is not None:
            self.spec_id = spec_id
        if share_type_usage is not None:
            self.share_type_usage = share_type_usage
        if support_period is not None:
            self.support_period = support_period
        if available_zones is not None:
            self.available_zones = available_zones
        if spec_code is not None:
            self.spec_code = spec_code
        if storage_media is not None:
            self.storage_media = storage_media
        if features is not None:
            self.features = features

    @property
    def share_type(self):
        r"""Gets the share_type of this ShareTypeResponseBody.

        文件系统类型

        :return: The share_type of this ShareTypeResponseBody.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this ShareTypeResponseBody.

        文件系统类型

        :param share_type: The share_type of this ShareTypeResponseBody.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def scenario(self):
        r"""Gets the scenario of this ShareTypeResponseBody.

        文件系统场景

        :return: The scenario of this ShareTypeResponseBody.
        :rtype: str
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        r"""Sets the scenario of this ShareTypeResponseBody.

        文件系统场景

        :param scenario: The scenario of this ShareTypeResponseBody.
        :type scenario: str
        """
        self._scenario = scenario

    @property
    def attribution(self):
        r"""Gets the attribution of this ShareTypeResponseBody.

        :return: The attribution of this ShareTypeResponseBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttribution`
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        r"""Sets the attribution of this ShareTypeResponseBody.

        :param attribution: The attribution of this ShareTypeResponseBody.
        :type attribution: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttribution`
        """
        self._attribution = attribution

    @property
    def spec_id(self):
        r"""Gets the spec_id of this ShareTypeResponseBody.

        文件系统规格ID

        :return: The spec_id of this ShareTypeResponseBody.
        :rtype: str
        """
        return self._spec_id

    @spec_id.setter
    def spec_id(self, spec_id):
        r"""Sets the spec_id of this ShareTypeResponseBody.

        文件系统规格ID

        :param spec_id: The spec_id of this ShareTypeResponseBody.
        :type spec_id: str
        """
        self._spec_id = spec_id

    @property
    def share_type_usage(self):
        r"""Gets the share_type_usage of this ShareTypeResponseBody.

        :return: The share_type_usage of this ShareTypeResponseBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsage`
        """
        return self._share_type_usage

    @share_type_usage.setter
    def share_type_usage(self, share_type_usage):
        r"""Sets the share_type_usage of this ShareTypeResponseBody.

        :param share_type_usage: The share_type_usage of this ShareTypeResponseBody.
        :type share_type_usage: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsage`
        """
        self._share_type_usage = share_type_usage

    @property
    def support_period(self):
        r"""Gets the support_period of this ShareTypeResponseBody.

        是否支持包周期

        :return: The support_period of this ShareTypeResponseBody.
        :rtype: bool
        """
        return self._support_period

    @support_period.setter
    def support_period(self, support_period):
        r"""Sets the support_period of this ShareTypeResponseBody.

        是否支持包周期

        :param support_period: The support_period of this ShareTypeResponseBody.
        :type support_period: bool
        """
        self._support_period = support_period

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ShareTypeResponseBody.

        可用区

        :return: The available_zones of this ShareTypeResponseBody.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ShareTypeAvailableZone`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ShareTypeResponseBody.

        可用区

        :param available_zones: The available_zones of this ShareTypeResponseBody.
        :type available_zones: list[:class:`huaweicloudsdksfsturbo.v1.ShareTypeAvailableZone`]
        """
        self._available_zones = available_zones

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ShareTypeResponseBody.

        文件系统规格编码

        :return: The spec_code of this ShareTypeResponseBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ShareTypeResponseBody.

        文件系统规格编码

        :param spec_code: The spec_code of this ShareTypeResponseBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def storage_media(self):
        r"""Gets the storage_media of this ShareTypeResponseBody.

        存储类型

        :return: The storage_media of this ShareTypeResponseBody.
        :rtype: str
        """
        return self._storage_media

    @storage_media.setter
    def storage_media(self, storage_media):
        r"""Sets the storage_media of this ShareTypeResponseBody.

        存储类型

        :param storage_media: The storage_media of this ShareTypeResponseBody.
        :type storage_media: str
        """
        self._storage_media = storage_media

    @property
    def features(self):
        r"""Gets the features of this ShareTypeResponseBody.

        实例支持的特性列表

        :return: The features of this ShareTypeResponseBody.
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ShareTypeResponseBody.

        实例支持的特性列表

        :param features: The features of this ShareTypeResponseBody.
        :type features: list[str]
        """
        self._features = features

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
        if not isinstance(other, ShareTypeResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
