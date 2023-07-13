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
        'session': 'Session',
        'virtual_channel': 'VirtualChannel',
        'keyboard_mouse': 'PoliciesKeyboardMouse',
        'bandwidth': 'Bandwidth',
        'custom': 'PoliciesCustom'
    }

    attribute_map = {
        'peripherals': 'peripherals',
        'audio': 'audio',
        'client': 'client',
        'display': 'display',
        'file_and_clipboard': 'file_and_clipboard',
        'session': 'session',
        'virtual_channel': 'virtual_channel',
        'keyboard_mouse': 'keyboard_mouse',
        'bandwidth': 'bandwidth',
        'custom': 'custom'
    }

    def __init__(self, peripherals=None, audio=None, client=None, display=None, file_and_clipboard=None, session=None, virtual_channel=None, keyboard_mouse=None, bandwidth=None, custom=None):
        """Policies

        The model defined in huaweicloud sdk

        :param peripherals: 
        :type peripherals: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripherals`
        :param audio: 
        :type audio: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesAudio`
        :param client: 
        :type client: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesClient`
        :param display: 
        :type display: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplay`
        :param file_and_clipboard: 
        :type file_and_clipboard: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboard`
        :param session: 
        :type session: :class:`huaweicloudsdkworkspaceapp.v1.Session`
        :param virtual_channel: 
        :type virtual_channel: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannel`
        :param keyboard_mouse: 
        :type keyboard_mouse: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesKeyboardMouse`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkworkspaceapp.v1.Bandwidth`
        :param custom: 
        :type custom: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCustom`
        """
        
        

        self._peripherals = None
        self._audio = None
        self._client = None
        self._display = None
        self._file_and_clipboard = None
        self._session = None
        self._virtual_channel = None
        self._keyboard_mouse = None
        self._bandwidth = None
        self._custom = None
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
        if session is not None:
            self.session = session
        if virtual_channel is not None:
            self.virtual_channel = virtual_channel
        if keyboard_mouse is not None:
            self.keyboard_mouse = keyboard_mouse
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if custom is not None:
            self.custom = custom

    @property
    def peripherals(self):
        """Gets the peripherals of this Policies.

        :return: The peripherals of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripherals`
        """
        return self._peripherals

    @peripherals.setter
    def peripherals(self, peripherals):
        """Sets the peripherals of this Policies.

        :param peripherals: The peripherals of this Policies.
        :type peripherals: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripherals`
        """
        self._peripherals = peripherals

    @property
    def audio(self):
        """Gets the audio of this Policies.

        :return: The audio of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesAudio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this Policies.

        :param audio: The audio of this Policies.
        :type audio: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesAudio`
        """
        self._audio = audio

    @property
    def client(self):
        """Gets the client of this Policies.

        :return: The client of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesClient`
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this Policies.

        :param client: The client of this Policies.
        :type client: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesClient`
        """
        self._client = client

    @property
    def display(self):
        """Gets the display of this Policies.

        :return: The display of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplay`
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this Policies.

        :param display: The display of this Policies.
        :type display: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplay`
        """
        self._display = display

    @property
    def file_and_clipboard(self):
        """Gets the file_and_clipboard of this Policies.

        :return: The file_and_clipboard of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboard`
        """
        return self._file_and_clipboard

    @file_and_clipboard.setter
    def file_and_clipboard(self, file_and_clipboard):
        """Sets the file_and_clipboard of this Policies.

        :param file_and_clipboard: The file_and_clipboard of this Policies.
        :type file_and_clipboard: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboard`
        """
        self._file_and_clipboard = file_and_clipboard

    @property
    def session(self):
        """Gets the session of this Policies.

        :return: The session of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Session`
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this Policies.

        :param session: The session of this Policies.
        :type session: :class:`huaweicloudsdkworkspaceapp.v1.Session`
        """
        self._session = session

    @property
    def virtual_channel(self):
        """Gets the virtual_channel of this Policies.

        :return: The virtual_channel of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannel`
        """
        return self._virtual_channel

    @virtual_channel.setter
    def virtual_channel(self, virtual_channel):
        """Sets the virtual_channel of this Policies.

        :param virtual_channel: The virtual_channel of this Policies.
        :type virtual_channel: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannel`
        """
        self._virtual_channel = virtual_channel

    @property
    def keyboard_mouse(self):
        """Gets the keyboard_mouse of this Policies.

        :return: The keyboard_mouse of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesKeyboardMouse`
        """
        return self._keyboard_mouse

    @keyboard_mouse.setter
    def keyboard_mouse(self, keyboard_mouse):
        """Sets the keyboard_mouse of this Policies.

        :param keyboard_mouse: The keyboard_mouse of this Policies.
        :type keyboard_mouse: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesKeyboardMouse`
        """
        self._keyboard_mouse = keyboard_mouse

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Policies.

        :return: The bandwidth of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Bandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Policies.

        :param bandwidth: The bandwidth of this Policies.
        :type bandwidth: :class:`huaweicloudsdkworkspaceapp.v1.Bandwidth`
        """
        self._bandwidth = bandwidth

    @property
    def custom(self):
        """Gets the custom of this Policies.

        :return: The custom of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCustom`
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this Policies.

        :param custom: The custom of this Policies.
        :type custom: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCustom`
        """
        self._custom = custom

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
