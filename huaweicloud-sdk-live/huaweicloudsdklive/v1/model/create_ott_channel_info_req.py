# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOttChannelInfoReq:

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
        'name': 'str',
        'state': 'str',
        'mode': 'str',
        'region': 'str',
        'input': 'InputStreamInfo',
        'encoder_settings': 'list[ModifyOttChannelEncoderSettingsEncoderSettings]',
        'record_settings': 'CreateOttChannelInfoReqRecordSettings',
        'endpoints': 'list[EndpointItem]',
        'encoder_settings_expand': 'EncoderSettingsExpand'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'mode': 'mode',
        'region': 'region',
        'input': 'input',
        'encoder_settings': 'encoder_settings',
        'record_settings': 'record_settings',
        'endpoints': 'endpoints',
        'encoder_settings_expand': 'encoder_settings_expand'
    }

    def __init__(self, domain=None, app_name=None, id=None, name=None, state=None, mode=None, region=None, input=None, encoder_settings=None, record_settings=None, endpoints=None, encoder_settings_expand=None):
        r"""CreateOttChannelInfoReq

        The model defined in huaweicloud sdk

        :param domain: 频道推流域名
        :type domain: str
        :param app_name: 组名或应用名
        :type app_name: str
        :param id: 频道ID。频道唯一标识，为必填项。
        :type id: str
        :param name: 频道名。可选配置
        :type name: str
        :param state: 频道状态 - ON：频道下发成功后，自动启动拉流、转码、录制等功能 - OFF：仅保存频道信息，不启动频道
        :type state: str
        :param mode: 频道模式 ADD_CDN：一站式服务，源站和CDN绑在一起（默认） ONLY_OS：独立源站服务，CDN和源站解耦
        :type mode: str
        :param region: 当mode是ONLY_OS时，该字段生效，表示频道所在Region
        :type region: str
        :param input: 
        :type input: :class:`huaweicloudsdklive.v1.InputStreamInfo`
        :param encoder_settings: 转码模板配置
        :type encoder_settings: list[:class:`huaweicloudsdklive.v1.ModifyOttChannelEncoderSettingsEncoderSettings`]
        :param record_settings: 
        :type record_settings: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoReqRecordSettings`
        :param endpoints: 频道出流信息
        :type endpoints: list[:class:`huaweicloudsdklive.v1.EndpointItem`]
        :param encoder_settings_expand: 
        :type encoder_settings_expand: :class:`huaweicloudsdklive.v1.EncoderSettingsExpand`
        """
        
        

        self._domain = None
        self._app_name = None
        self._id = None
        self._name = None
        self._state = None
        self._mode = None
        self._region = None
        self._input = None
        self._encoder_settings = None
        self._record_settings = None
        self._endpoints = None
        self._encoder_settings_expand = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name
        self.id = id
        if name is not None:
            self.name = name
        self.state = state
        if mode is not None:
            self.mode = mode
        if region is not None:
            self.region = region
        self.input = input
        if encoder_settings is not None:
            self.encoder_settings = encoder_settings
        self.record_settings = record_settings
        self.endpoints = endpoints
        if encoder_settings_expand is not None:
            self.encoder_settings_expand = encoder_settings_expand

    @property
    def domain(self):
        r"""Gets the domain of this CreateOttChannelInfoReq.

        频道推流域名

        :return: The domain of this CreateOttChannelInfoReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CreateOttChannelInfoReq.

        频道推流域名

        :param domain: The domain of this CreateOttChannelInfoReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this CreateOttChannelInfoReq.

        组名或应用名

        :return: The app_name of this CreateOttChannelInfoReq.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this CreateOttChannelInfoReq.

        组名或应用名

        :param app_name: The app_name of this CreateOttChannelInfoReq.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this CreateOttChannelInfoReq.

        频道ID。频道唯一标识，为必填项。

        :return: The id of this CreateOttChannelInfoReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateOttChannelInfoReq.

        频道ID。频道唯一标识，为必填项。

        :param id: The id of this CreateOttChannelInfoReq.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateOttChannelInfoReq.

        频道名。可选配置

        :return: The name of this CreateOttChannelInfoReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOttChannelInfoReq.

        频道名。可选配置

        :param name: The name of this CreateOttChannelInfoReq.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this CreateOttChannelInfoReq.

        频道状态 - ON：频道下发成功后，自动启动拉流、转码、录制等功能 - OFF：仅保存频道信息，不启动频道

        :return: The state of this CreateOttChannelInfoReq.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CreateOttChannelInfoReq.

        频道状态 - ON：频道下发成功后，自动启动拉流、转码、录制等功能 - OFF：仅保存频道信息，不启动频道

        :param state: The state of this CreateOttChannelInfoReq.
        :type state: str
        """
        self._state = state

    @property
    def mode(self):
        r"""Gets the mode of this CreateOttChannelInfoReq.

        频道模式 ADD_CDN：一站式服务，源站和CDN绑在一起（默认） ONLY_OS：独立源站服务，CDN和源站解耦

        :return: The mode of this CreateOttChannelInfoReq.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateOttChannelInfoReq.

        频道模式 ADD_CDN：一站式服务，源站和CDN绑在一起（默认） ONLY_OS：独立源站服务，CDN和源站解耦

        :param mode: The mode of this CreateOttChannelInfoReq.
        :type mode: str
        """
        self._mode = mode

    @property
    def region(self):
        r"""Gets the region of this CreateOttChannelInfoReq.

        当mode是ONLY_OS时，该字段生效，表示频道所在Region

        :return: The region of this CreateOttChannelInfoReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateOttChannelInfoReq.

        当mode是ONLY_OS时，该字段生效，表示频道所在Region

        :param region: The region of this CreateOttChannelInfoReq.
        :type region: str
        """
        self._region = region

    @property
    def input(self):
        r"""Gets the input of this CreateOttChannelInfoReq.

        :return: The input of this CreateOttChannelInfoReq.
        :rtype: :class:`huaweicloudsdklive.v1.InputStreamInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this CreateOttChannelInfoReq.

        :param input: The input of this CreateOttChannelInfoReq.
        :type input: :class:`huaweicloudsdklive.v1.InputStreamInfo`
        """
        self._input = input

    @property
    def encoder_settings(self):
        r"""Gets the encoder_settings of this CreateOttChannelInfoReq.

        转码模板配置

        :return: The encoder_settings of this CreateOttChannelInfoReq.
        :rtype: list[:class:`huaweicloudsdklive.v1.ModifyOttChannelEncoderSettingsEncoderSettings`]
        """
        return self._encoder_settings

    @encoder_settings.setter
    def encoder_settings(self, encoder_settings):
        r"""Sets the encoder_settings of this CreateOttChannelInfoReq.

        转码模板配置

        :param encoder_settings: The encoder_settings of this CreateOttChannelInfoReq.
        :type encoder_settings: list[:class:`huaweicloudsdklive.v1.ModifyOttChannelEncoderSettingsEncoderSettings`]
        """
        self._encoder_settings = encoder_settings

    @property
    def record_settings(self):
        r"""Gets the record_settings of this CreateOttChannelInfoReq.

        :return: The record_settings of this CreateOttChannelInfoReq.
        :rtype: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoReqRecordSettings`
        """
        return self._record_settings

    @record_settings.setter
    def record_settings(self, record_settings):
        r"""Sets the record_settings of this CreateOttChannelInfoReq.

        :param record_settings: The record_settings of this CreateOttChannelInfoReq.
        :type record_settings: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoReqRecordSettings`
        """
        self._record_settings = record_settings

    @property
    def endpoints(self):
        r"""Gets the endpoints of this CreateOttChannelInfoReq.

        频道出流信息

        :return: The endpoints of this CreateOttChannelInfoReq.
        :rtype: list[:class:`huaweicloudsdklive.v1.EndpointItem`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this CreateOttChannelInfoReq.

        频道出流信息

        :param endpoints: The endpoints of this CreateOttChannelInfoReq.
        :type endpoints: list[:class:`huaweicloudsdklive.v1.EndpointItem`]
        """
        self._endpoints = endpoints

    @property
    def encoder_settings_expand(self):
        r"""Gets the encoder_settings_expand of this CreateOttChannelInfoReq.

        :return: The encoder_settings_expand of this CreateOttChannelInfoReq.
        :rtype: :class:`huaweicloudsdklive.v1.EncoderSettingsExpand`
        """
        return self._encoder_settings_expand

    @encoder_settings_expand.setter
    def encoder_settings_expand(self, encoder_settings_expand):
        r"""Sets the encoder_settings_expand of this CreateOttChannelInfoReq.

        :param encoder_settings_expand: The encoder_settings_expand of this CreateOttChannelInfoReq.
        :type encoder_settings_expand: :class:`huaweicloudsdklive.v1.EncoderSettingsExpand`
        """
        self._encoder_settings_expand = encoder_settings_expand

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
        if not isinstance(other, CreateOttChannelInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
