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
        'custom': 'PoliciesCustom',
        'cloud_storage': 'PoliciesCloudStorage',
        'user_profile': 'PoliciesUserProfile',
        'url_redirection': 'PoliciesUrlRedirection',
        'folder_redirection': 'PoliciesFolderRedirection'
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
        'custom': 'custom',
        'cloud_storage': 'cloud_storage',
        'user_profile': 'user_profile',
        'url_redirection': 'url_redirection',
        'folder_redirection': 'folder_redirection'
    }

    def __init__(self, peripherals=None, audio=None, client=None, display=None, file_and_clipboard=None, session=None, virtual_channel=None, keyboard_mouse=None, bandwidth=None, custom=None, cloud_storage=None, user_profile=None, url_redirection=None, folder_redirection=None):
        r"""Policies

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
        :param cloud_storage: 
        :type cloud_storage: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCloudStorage`
        :param user_profile: 
        :type user_profile: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesUserProfile`
        :param url_redirection: 
        :type url_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesUrlRedirection`
        :param folder_redirection: 
        :type folder_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFolderRedirection`
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
        self._cloud_storage = None
        self._user_profile = None
        self._url_redirection = None
        self._folder_redirection = None
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
        if cloud_storage is not None:
            self.cloud_storage = cloud_storage
        if user_profile is not None:
            self.user_profile = user_profile
        if url_redirection is not None:
            self.url_redirection = url_redirection
        if folder_redirection is not None:
            self.folder_redirection = folder_redirection

    @property
    def peripherals(self):
        r"""Gets the peripherals of this Policies.

        :return: The peripherals of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripherals`
        """
        return self._peripherals

    @peripherals.setter
    def peripherals(self, peripherals):
        r"""Sets the peripherals of this Policies.

        :param peripherals: The peripherals of this Policies.
        :type peripherals: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripherals`
        """
        self._peripherals = peripherals

    @property
    def audio(self):
        r"""Gets the audio of this Policies.

        :return: The audio of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesAudio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        r"""Sets the audio of this Policies.

        :param audio: The audio of this Policies.
        :type audio: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesAudio`
        """
        self._audio = audio

    @property
    def client(self):
        r"""Gets the client of this Policies.

        :return: The client of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesClient`
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this Policies.

        :param client: The client of this Policies.
        :type client: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesClient`
        """
        self._client = client

    @property
    def display(self):
        r"""Gets the display of this Policies.

        :return: The display of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplay`
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this Policies.

        :param display: The display of this Policies.
        :type display: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplay`
        """
        self._display = display

    @property
    def file_and_clipboard(self):
        r"""Gets the file_and_clipboard of this Policies.

        :return: The file_and_clipboard of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboard`
        """
        return self._file_and_clipboard

    @file_and_clipboard.setter
    def file_and_clipboard(self, file_and_clipboard):
        r"""Sets the file_and_clipboard of this Policies.

        :param file_and_clipboard: The file_and_clipboard of this Policies.
        :type file_and_clipboard: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboard`
        """
        self._file_and_clipboard = file_and_clipboard

    @property
    def session(self):
        r"""Gets the session of this Policies.

        :return: The session of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Session`
        """
        return self._session

    @session.setter
    def session(self, session):
        r"""Sets the session of this Policies.

        :param session: The session of this Policies.
        :type session: :class:`huaweicloudsdkworkspaceapp.v1.Session`
        """
        self._session = session

    @property
    def virtual_channel(self):
        r"""Gets the virtual_channel of this Policies.

        :return: The virtual_channel of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannel`
        """
        return self._virtual_channel

    @virtual_channel.setter
    def virtual_channel(self, virtual_channel):
        r"""Sets the virtual_channel of this Policies.

        :param virtual_channel: The virtual_channel of this Policies.
        :type virtual_channel: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannel`
        """
        self._virtual_channel = virtual_channel

    @property
    def keyboard_mouse(self):
        r"""Gets the keyboard_mouse of this Policies.

        :return: The keyboard_mouse of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesKeyboardMouse`
        """
        return self._keyboard_mouse

    @keyboard_mouse.setter
    def keyboard_mouse(self, keyboard_mouse):
        r"""Sets the keyboard_mouse of this Policies.

        :param keyboard_mouse: The keyboard_mouse of this Policies.
        :type keyboard_mouse: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesKeyboardMouse`
        """
        self._keyboard_mouse = keyboard_mouse

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this Policies.

        :return: The bandwidth of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Bandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this Policies.

        :param bandwidth: The bandwidth of this Policies.
        :type bandwidth: :class:`huaweicloudsdkworkspaceapp.v1.Bandwidth`
        """
        self._bandwidth = bandwidth

    @property
    def custom(self):
        r"""Gets the custom of this Policies.

        :return: The custom of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCustom`
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        r"""Sets the custom of this Policies.

        :param custom: The custom of this Policies.
        :type custom: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCustom`
        """
        self._custom = custom

    @property
    def cloud_storage(self):
        r"""Gets the cloud_storage of this Policies.

        :return: The cloud_storage of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCloudStorage`
        """
        return self._cloud_storage

    @cloud_storage.setter
    def cloud_storage(self, cloud_storage):
        r"""Sets the cloud_storage of this Policies.

        :param cloud_storage: The cloud_storage of this Policies.
        :type cloud_storage: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesCloudStorage`
        """
        self._cloud_storage = cloud_storage

    @property
    def user_profile(self):
        r"""Gets the user_profile of this Policies.

        :return: The user_profile of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesUserProfile`
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        r"""Sets the user_profile of this Policies.

        :param user_profile: The user_profile of this Policies.
        :type user_profile: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesUserProfile`
        """
        self._user_profile = user_profile

    @property
    def url_redirection(self):
        r"""Gets the url_redirection of this Policies.

        :return: The url_redirection of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesUrlRedirection`
        """
        return self._url_redirection

    @url_redirection.setter
    def url_redirection(self, url_redirection):
        r"""Sets the url_redirection of this Policies.

        :param url_redirection: The url_redirection of this Policies.
        :type url_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesUrlRedirection`
        """
        self._url_redirection = url_redirection

    @property
    def folder_redirection(self):
        r"""Gets the folder_redirection of this Policies.

        :return: The folder_redirection of this Policies.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFolderRedirection`
        """
        return self._folder_redirection

    @folder_redirection.setter
    def folder_redirection(self, folder_redirection):
        r"""Sets the folder_redirection of this Policies.

        :param folder_redirection: The folder_redirection of this Policies.
        :type folder_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFolderRedirection`
        """
        self._folder_redirection = folder_redirection

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
