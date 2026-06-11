# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FolderRedirectionV2Options:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_data_roaming_configurations': 'AppDataRoamingConfigurations',
        'desktop_configurations': 'DesktopConfigurations',
        'start_menu_configurations': 'StartMenuConfigurations',
        'documents_configurations': 'DocumentsConfigurations',
        'pictures_configurations': 'PicturesConfigurations',
        'music_configurations': 'MusicConfigurations',
        'videos_configurations': 'VideosConfigurations',
        'favorites_configurations': 'FavoritesConfigurations',
        'contacts_configurations': 'ContactsConfigurations',
        'downloads_configurations': 'DownloadsConfigurations',
        'links_configurations': 'LinksConfigurations',
        'searches_configurations': 'SearchesConfigurations',
        'saved_games_configurations': 'SavedGamesConfigurations'
    }

    attribute_map = {
        'app_data_roaming_configurations': 'app_data_roaming_configurations',
        'desktop_configurations': 'desktop_configurations',
        'start_menu_configurations': 'start_menu_configurations',
        'documents_configurations': 'documents_configurations',
        'pictures_configurations': 'pictures_configurations',
        'music_configurations': 'music_configurations',
        'videos_configurations': 'videos_configurations',
        'favorites_configurations': 'favorites_configurations',
        'contacts_configurations': 'contacts_configurations',
        'downloads_configurations': 'downloads_configurations',
        'links_configurations': 'links_configurations',
        'searches_configurations': 'searches_configurations',
        'saved_games_configurations': 'saved_games_configurations'
    }

    def __init__(self, app_data_roaming_configurations=None, desktop_configurations=None, start_menu_configurations=None, documents_configurations=None, pictures_configurations=None, music_configurations=None, videos_configurations=None, favorites_configurations=None, contacts_configurations=None, downloads_configurations=None, links_configurations=None, searches_configurations=None, saved_games_configurations=None):
        r"""FolderRedirectionV2Options

        The model defined in huaweicloud sdk

        :param app_data_roaming_configurations: 
        :type app_data_roaming_configurations: :class:`huaweicloudsdkworkspaceapp.v1.AppDataRoamingConfigurations`
        :param desktop_configurations: 
        :type desktop_configurations: :class:`huaweicloudsdkworkspaceapp.v1.DesktopConfigurations`
        :param start_menu_configurations: 
        :type start_menu_configurations: :class:`huaweicloudsdkworkspaceapp.v1.StartMenuConfigurations`
        :param documents_configurations: 
        :type documents_configurations: :class:`huaweicloudsdkworkspaceapp.v1.DocumentsConfigurations`
        :param pictures_configurations: 
        :type pictures_configurations: :class:`huaweicloudsdkworkspaceapp.v1.PicturesConfigurations`
        :param music_configurations: 
        :type music_configurations: :class:`huaweicloudsdkworkspaceapp.v1.MusicConfigurations`
        :param videos_configurations: 
        :type videos_configurations: :class:`huaweicloudsdkworkspaceapp.v1.VideosConfigurations`
        :param favorites_configurations: 
        :type favorites_configurations: :class:`huaweicloudsdkworkspaceapp.v1.FavoritesConfigurations`
        :param contacts_configurations: 
        :type contacts_configurations: :class:`huaweicloudsdkworkspaceapp.v1.ContactsConfigurations`
        :param downloads_configurations: 
        :type downloads_configurations: :class:`huaweicloudsdkworkspaceapp.v1.DownloadsConfigurations`
        :param links_configurations: 
        :type links_configurations: :class:`huaweicloudsdkworkspaceapp.v1.LinksConfigurations`
        :param searches_configurations: 
        :type searches_configurations: :class:`huaweicloudsdkworkspaceapp.v1.SearchesConfigurations`
        :param saved_games_configurations: 
        :type saved_games_configurations: :class:`huaweicloudsdkworkspaceapp.v1.SavedGamesConfigurations`
        """
        
        

        self._app_data_roaming_configurations = None
        self._desktop_configurations = None
        self._start_menu_configurations = None
        self._documents_configurations = None
        self._pictures_configurations = None
        self._music_configurations = None
        self._videos_configurations = None
        self._favorites_configurations = None
        self._contacts_configurations = None
        self._downloads_configurations = None
        self._links_configurations = None
        self._searches_configurations = None
        self._saved_games_configurations = None
        self.discriminator = None

        if app_data_roaming_configurations is not None:
            self.app_data_roaming_configurations = app_data_roaming_configurations
        if desktop_configurations is not None:
            self.desktop_configurations = desktop_configurations
        if start_menu_configurations is not None:
            self.start_menu_configurations = start_menu_configurations
        if documents_configurations is not None:
            self.documents_configurations = documents_configurations
        if pictures_configurations is not None:
            self.pictures_configurations = pictures_configurations
        if music_configurations is not None:
            self.music_configurations = music_configurations
        if videos_configurations is not None:
            self.videos_configurations = videos_configurations
        if favorites_configurations is not None:
            self.favorites_configurations = favorites_configurations
        if contacts_configurations is not None:
            self.contacts_configurations = contacts_configurations
        if downloads_configurations is not None:
            self.downloads_configurations = downloads_configurations
        if links_configurations is not None:
            self.links_configurations = links_configurations
        if searches_configurations is not None:
            self.searches_configurations = searches_configurations
        if saved_games_configurations is not None:
            self.saved_games_configurations = saved_games_configurations

    @property
    def app_data_roaming_configurations(self):
        r"""Gets the app_data_roaming_configurations of this FolderRedirectionV2Options.

        :return: The app_data_roaming_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppDataRoamingConfigurations`
        """
        return self._app_data_roaming_configurations

    @app_data_roaming_configurations.setter
    def app_data_roaming_configurations(self, app_data_roaming_configurations):
        r"""Sets the app_data_roaming_configurations of this FolderRedirectionV2Options.

        :param app_data_roaming_configurations: The app_data_roaming_configurations of this FolderRedirectionV2Options.
        :type app_data_roaming_configurations: :class:`huaweicloudsdkworkspaceapp.v1.AppDataRoamingConfigurations`
        """
        self._app_data_roaming_configurations = app_data_roaming_configurations

    @property
    def desktop_configurations(self):
        r"""Gets the desktop_configurations of this FolderRedirectionV2Options.

        :return: The desktop_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DesktopConfigurations`
        """
        return self._desktop_configurations

    @desktop_configurations.setter
    def desktop_configurations(self, desktop_configurations):
        r"""Sets the desktop_configurations of this FolderRedirectionV2Options.

        :param desktop_configurations: The desktop_configurations of this FolderRedirectionV2Options.
        :type desktop_configurations: :class:`huaweicloudsdkworkspaceapp.v1.DesktopConfigurations`
        """
        self._desktop_configurations = desktop_configurations

    @property
    def start_menu_configurations(self):
        r"""Gets the start_menu_configurations of this FolderRedirectionV2Options.

        :return: The start_menu_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.StartMenuConfigurations`
        """
        return self._start_menu_configurations

    @start_menu_configurations.setter
    def start_menu_configurations(self, start_menu_configurations):
        r"""Sets the start_menu_configurations of this FolderRedirectionV2Options.

        :param start_menu_configurations: The start_menu_configurations of this FolderRedirectionV2Options.
        :type start_menu_configurations: :class:`huaweicloudsdkworkspaceapp.v1.StartMenuConfigurations`
        """
        self._start_menu_configurations = start_menu_configurations

    @property
    def documents_configurations(self):
        r"""Gets the documents_configurations of this FolderRedirectionV2Options.

        :return: The documents_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DocumentsConfigurations`
        """
        return self._documents_configurations

    @documents_configurations.setter
    def documents_configurations(self, documents_configurations):
        r"""Sets the documents_configurations of this FolderRedirectionV2Options.

        :param documents_configurations: The documents_configurations of this FolderRedirectionV2Options.
        :type documents_configurations: :class:`huaweicloudsdkworkspaceapp.v1.DocumentsConfigurations`
        """
        self._documents_configurations = documents_configurations

    @property
    def pictures_configurations(self):
        r"""Gets the pictures_configurations of this FolderRedirectionV2Options.

        :return: The pictures_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PicturesConfigurations`
        """
        return self._pictures_configurations

    @pictures_configurations.setter
    def pictures_configurations(self, pictures_configurations):
        r"""Sets the pictures_configurations of this FolderRedirectionV2Options.

        :param pictures_configurations: The pictures_configurations of this FolderRedirectionV2Options.
        :type pictures_configurations: :class:`huaweicloudsdkworkspaceapp.v1.PicturesConfigurations`
        """
        self._pictures_configurations = pictures_configurations

    @property
    def music_configurations(self):
        r"""Gets the music_configurations of this FolderRedirectionV2Options.

        :return: The music_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.MusicConfigurations`
        """
        return self._music_configurations

    @music_configurations.setter
    def music_configurations(self, music_configurations):
        r"""Sets the music_configurations of this FolderRedirectionV2Options.

        :param music_configurations: The music_configurations of this FolderRedirectionV2Options.
        :type music_configurations: :class:`huaweicloudsdkworkspaceapp.v1.MusicConfigurations`
        """
        self._music_configurations = music_configurations

    @property
    def videos_configurations(self):
        r"""Gets the videos_configurations of this FolderRedirectionV2Options.

        :return: The videos_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VideosConfigurations`
        """
        return self._videos_configurations

    @videos_configurations.setter
    def videos_configurations(self, videos_configurations):
        r"""Sets the videos_configurations of this FolderRedirectionV2Options.

        :param videos_configurations: The videos_configurations of this FolderRedirectionV2Options.
        :type videos_configurations: :class:`huaweicloudsdkworkspaceapp.v1.VideosConfigurations`
        """
        self._videos_configurations = videos_configurations

    @property
    def favorites_configurations(self):
        r"""Gets the favorites_configurations of this FolderRedirectionV2Options.

        :return: The favorites_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FavoritesConfigurations`
        """
        return self._favorites_configurations

    @favorites_configurations.setter
    def favorites_configurations(self, favorites_configurations):
        r"""Sets the favorites_configurations of this FolderRedirectionV2Options.

        :param favorites_configurations: The favorites_configurations of this FolderRedirectionV2Options.
        :type favorites_configurations: :class:`huaweicloudsdkworkspaceapp.v1.FavoritesConfigurations`
        """
        self._favorites_configurations = favorites_configurations

    @property
    def contacts_configurations(self):
        r"""Gets the contacts_configurations of this FolderRedirectionV2Options.

        :return: The contacts_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ContactsConfigurations`
        """
        return self._contacts_configurations

    @contacts_configurations.setter
    def contacts_configurations(self, contacts_configurations):
        r"""Sets the contacts_configurations of this FolderRedirectionV2Options.

        :param contacts_configurations: The contacts_configurations of this FolderRedirectionV2Options.
        :type contacts_configurations: :class:`huaweicloudsdkworkspaceapp.v1.ContactsConfigurations`
        """
        self._contacts_configurations = contacts_configurations

    @property
    def downloads_configurations(self):
        r"""Gets the downloads_configurations of this FolderRedirectionV2Options.

        :return: The downloads_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DownloadsConfigurations`
        """
        return self._downloads_configurations

    @downloads_configurations.setter
    def downloads_configurations(self, downloads_configurations):
        r"""Sets the downloads_configurations of this FolderRedirectionV2Options.

        :param downloads_configurations: The downloads_configurations of this FolderRedirectionV2Options.
        :type downloads_configurations: :class:`huaweicloudsdkworkspaceapp.v1.DownloadsConfigurations`
        """
        self._downloads_configurations = downloads_configurations

    @property
    def links_configurations(self):
        r"""Gets the links_configurations of this FolderRedirectionV2Options.

        :return: The links_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.LinksConfigurations`
        """
        return self._links_configurations

    @links_configurations.setter
    def links_configurations(self, links_configurations):
        r"""Sets the links_configurations of this FolderRedirectionV2Options.

        :param links_configurations: The links_configurations of this FolderRedirectionV2Options.
        :type links_configurations: :class:`huaweicloudsdkworkspaceapp.v1.LinksConfigurations`
        """
        self._links_configurations = links_configurations

    @property
    def searches_configurations(self):
        r"""Gets the searches_configurations of this FolderRedirectionV2Options.

        :return: The searches_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SearchesConfigurations`
        """
        return self._searches_configurations

    @searches_configurations.setter
    def searches_configurations(self, searches_configurations):
        r"""Sets the searches_configurations of this FolderRedirectionV2Options.

        :param searches_configurations: The searches_configurations of this FolderRedirectionV2Options.
        :type searches_configurations: :class:`huaweicloudsdkworkspaceapp.v1.SearchesConfigurations`
        """
        self._searches_configurations = searches_configurations

    @property
    def saved_games_configurations(self):
        r"""Gets the saved_games_configurations of this FolderRedirectionV2Options.

        :return: The saved_games_configurations of this FolderRedirectionV2Options.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SavedGamesConfigurations`
        """
        return self._saved_games_configurations

    @saved_games_configurations.setter
    def saved_games_configurations(self, saved_games_configurations):
        r"""Sets the saved_games_configurations of this FolderRedirectionV2Options.

        :param saved_games_configurations: The saved_games_configurations of this FolderRedirectionV2Options.
        :type saved_games_configurations: :class:`huaweicloudsdkworkspaceapp.v1.SavedGamesConfigurations`
        """
        self._saved_games_configurations = saved_games_configurations

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
        if not isinstance(other, FolderRedirectionV2Options):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
