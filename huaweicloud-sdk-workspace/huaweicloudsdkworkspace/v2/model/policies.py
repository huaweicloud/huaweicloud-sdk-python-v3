# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peripherals': 'PoliciesPeripherals',
        'audio': 'PoliciesAudio',
        'client': 'PoliciesClient',
        'display': 'PoliciesDisplay',
        'file_and_clipboard': 'PoliciesFileAndClipboard',
        'access_control': 'AccessControl',
        'session': 'Session',
        'bandwidth': 'Bandwidth',
        'virtual_channel': 'VirtualChannel',
        'watermark': 'Watermark',
        'keyboard_mouse': 'PoliciesKeyboardMouse',
        'seamless': 'PoliciesSeamless',
        'personalized_data_mgmt': 'PoliciesPersonalizedDataMgmt',
        'custom': 'PoliciesCustom',
        'record_audit': 'PoliciesRecordAudit'
    }

    attribute_map = {
        'peripherals': 'peripherals',
        'audio': 'audio',
        'client': 'client',
        'display': 'display',
        'file_and_clipboard': 'file_and_clipboard',
        'access_control': 'access_control',
        'session': 'session',
        'bandwidth': 'bandwidth',
        'virtual_channel': 'virtual_channel',
        'watermark': 'watermark',
        'keyboard_mouse': 'keyboard_mouse',
        'seamless': 'seamless',
        'personalized_data_mgmt': 'personalizedDataMgmt',
        'custom': 'custom',
        'record_audit': 'record_audit'
    }

    def __init__(self, peripherals=None, audio=None, client=None, display=None, file_and_clipboard=None, access_control=None, session=None, bandwidth=None, virtual_channel=None, watermark=None, keyboard_mouse=None, seamless=None, personalized_data_mgmt=None, custom=None, record_audit=None):
        """Policies

        The model defined in huaweicloud sdk

        :param peripherals: 
        :type peripherals: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripherals`
        :param audio: 
        :type audio: :class:`huaweicloudsdkworkspace.v2.PoliciesAudio`
        :param client: 
        :type client: :class:`huaweicloudsdkworkspace.v2.PoliciesClient`
        :param display: 
        :type display: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplay`
        :param file_and_clipboard: 
        :type file_and_clipboard: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboard`
        :param access_control: 
        :type access_control: :class:`huaweicloudsdkworkspace.v2.AccessControl`
        :param session: 
        :type session: :class:`huaweicloudsdkworkspace.v2.Session`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkworkspace.v2.Bandwidth`
        :param virtual_channel: 
        :type virtual_channel: :class:`huaweicloudsdkworkspace.v2.VirtualChannel`
        :param watermark: 
        :type watermark: :class:`huaweicloudsdkworkspace.v2.Watermark`
        :param keyboard_mouse: 
        :type keyboard_mouse: :class:`huaweicloudsdkworkspace.v2.PoliciesKeyboardMouse`
        :param seamless: 
        :type seamless: :class:`huaweicloudsdkworkspace.v2.PoliciesSeamless`
        :param personalized_data_mgmt: 
        :type personalized_data_mgmt: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmt`
        :param custom: 
        :type custom: :class:`huaweicloudsdkworkspace.v2.PoliciesCustom`
        :param record_audit: 
        :type record_audit: :class:`huaweicloudsdkworkspace.v2.PoliciesRecordAudit`
        """
        
        

        self._peripherals = None
        self._audio = None
        self._client = None
        self._display = None
        self._file_and_clipboard = None
        self._access_control = None
        self._session = None
        self._bandwidth = None
        self._virtual_channel = None
        self._watermark = None
        self._keyboard_mouse = None
        self._seamless = None
        self._personalized_data_mgmt = None
        self._custom = None
        self._record_audit = None
        self.discriminator = None

        if peripherals is not None:
            self.peripherals = peripherals
        if audio is not None:
            self.audio = audio
        if client is not None:
            self.client = client
        if display is not None:
            self.display = display
        if file_and_clipboard is not None:
            self.file_and_clipboard = file_and_clipboard
        if access_control is not None:
            self.access_control = access_control
        if session is not None:
            self.session = session
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if virtual_channel is not None:
            self.virtual_channel = virtual_channel
        if watermark is not None:
            self.watermark = watermark
        if keyboard_mouse is not None:
            self.keyboard_mouse = keyboard_mouse
        if seamless is not None:
            self.seamless = seamless
        if personalized_data_mgmt is not None:
            self.personalized_data_mgmt = personalized_data_mgmt
        if custom is not None:
            self.custom = custom
        if record_audit is not None:
            self.record_audit = record_audit

    @property
    def peripherals(self):
        """Gets the peripherals of this Policies.

        :return: The peripherals of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripherals`
        """
        return self._peripherals

    @peripherals.setter
    def peripherals(self, peripherals):
        """Sets the peripherals of this Policies.

        :param peripherals: The peripherals of this Policies.
        :type peripherals: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripherals`
        """
        self._peripherals = peripherals

    @property
    def audio(self):
        """Gets the audio of this Policies.

        :return: The audio of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesAudio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this Policies.

        :param audio: The audio of this Policies.
        :type audio: :class:`huaweicloudsdkworkspace.v2.PoliciesAudio`
        """
        self._audio = audio

    @property
    def client(self):
        """Gets the client of this Policies.

        :return: The client of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesClient`
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this Policies.

        :param client: The client of this Policies.
        :type client: :class:`huaweicloudsdkworkspace.v2.PoliciesClient`
        """
        self._client = client

    @property
    def display(self):
        """Gets the display of this Policies.

        :return: The display of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplay`
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this Policies.

        :param display: The display of this Policies.
        :type display: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplay`
        """
        self._display = display

    @property
    def file_and_clipboard(self):
        """Gets the file_and_clipboard of this Policies.

        :return: The file_and_clipboard of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboard`
        """
        return self._file_and_clipboard

    @file_and_clipboard.setter
    def file_and_clipboard(self, file_and_clipboard):
        """Sets the file_and_clipboard of this Policies.

        :param file_and_clipboard: The file_and_clipboard of this Policies.
        :type file_and_clipboard: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboard`
        """
        self._file_and_clipboard = file_and_clipboard

    @property
    def access_control(self):
        """Gets the access_control of this Policies.

        :return: The access_control of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AccessControl`
        """
        return self._access_control

    @access_control.setter
    def access_control(self, access_control):
        """Sets the access_control of this Policies.

        :param access_control: The access_control of this Policies.
        :type access_control: :class:`huaweicloudsdkworkspace.v2.AccessControl`
        """
        self._access_control = access_control

    @property
    def session(self):
        """Gets the session of this Policies.

        :return: The session of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Session`
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this Policies.

        :param session: The session of this Policies.
        :type session: :class:`huaweicloudsdkworkspace.v2.Session`
        """
        self._session = session

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Policies.

        :return: The bandwidth of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Bandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Policies.

        :param bandwidth: The bandwidth of this Policies.
        :type bandwidth: :class:`huaweicloudsdkworkspace.v2.Bandwidth`
        """
        self._bandwidth = bandwidth

    @property
    def virtual_channel(self):
        """Gets the virtual_channel of this Policies.

        :return: The virtual_channel of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VirtualChannel`
        """
        return self._virtual_channel

    @virtual_channel.setter
    def virtual_channel(self, virtual_channel):
        """Sets the virtual_channel of this Policies.

        :param virtual_channel: The virtual_channel of this Policies.
        :type virtual_channel: :class:`huaweicloudsdkworkspace.v2.VirtualChannel`
        """
        self._virtual_channel = virtual_channel

    @property
    def watermark(self):
        """Gets the watermark of this Policies.

        :return: The watermark of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Watermark`
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """Sets the watermark of this Policies.

        :param watermark: The watermark of this Policies.
        :type watermark: :class:`huaweicloudsdkworkspace.v2.Watermark`
        """
        self._watermark = watermark

    @property
    def keyboard_mouse(self):
        """Gets the keyboard_mouse of this Policies.

        :return: The keyboard_mouse of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesKeyboardMouse`
        """
        return self._keyboard_mouse

    @keyboard_mouse.setter
    def keyboard_mouse(self, keyboard_mouse):
        """Sets the keyboard_mouse of this Policies.

        :param keyboard_mouse: The keyboard_mouse of this Policies.
        :type keyboard_mouse: :class:`huaweicloudsdkworkspace.v2.PoliciesKeyboardMouse`
        """
        self._keyboard_mouse = keyboard_mouse

    @property
    def seamless(self):
        """Gets the seamless of this Policies.

        :return: The seamless of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesSeamless`
        """
        return self._seamless

    @seamless.setter
    def seamless(self, seamless):
        """Sets the seamless of this Policies.

        :param seamless: The seamless of this Policies.
        :type seamless: :class:`huaweicloudsdkworkspace.v2.PoliciesSeamless`
        """
        self._seamless = seamless

    @property
    def personalized_data_mgmt(self):
        """Gets the personalized_data_mgmt of this Policies.

        :return: The personalized_data_mgmt of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmt`
        """
        return self._personalized_data_mgmt

    @personalized_data_mgmt.setter
    def personalized_data_mgmt(self, personalized_data_mgmt):
        """Sets the personalized_data_mgmt of this Policies.

        :param personalized_data_mgmt: The personalized_data_mgmt of this Policies.
        :type personalized_data_mgmt: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmt`
        """
        self._personalized_data_mgmt = personalized_data_mgmt

    @property
    def custom(self):
        """Gets the custom of this Policies.

        :return: The custom of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesCustom`
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this Policies.

        :param custom: The custom of this Policies.
        :type custom: :class:`huaweicloudsdkworkspace.v2.PoliciesCustom`
        """
        self._custom = custom

    @property
    def record_audit(self):
        """Gets the record_audit of this Policies.

        :return: The record_audit of this Policies.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesRecordAudit`
        """
        return self._record_audit

    @record_audit.setter
    def record_audit(self, record_audit):
        """Sets the record_audit of this Policies.

        :param record_audit: The record_audit of this Policies.
        :type record_audit: :class:`huaweicloudsdkworkspace.v2.PoliciesRecordAudit`
        """
        self._record_audit = record_audit

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
        if not isinstance(other, Policies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
