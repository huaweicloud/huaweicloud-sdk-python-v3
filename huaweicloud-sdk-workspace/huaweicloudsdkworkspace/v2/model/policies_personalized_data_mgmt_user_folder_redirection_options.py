# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_local_directories_enable': 'bool',
        'app_data_roaming_enale': 'bool',
        'redirec_desktop': 'bool',
        'redirec_start_menu': 'bool',
        'redirec_documents': 'bool',
        'redirec_pictures': 'bool',
        'redirec_music': 'bool',
        'redirec_videos': 'bool',
        'redirec_favorites': 'bool',
        'redirec_contacts': 'bool',
        'redirec_downloads': 'bool',
        'redirec_links': 'bool',
        'redirec_searches': 'bool',
        'redirec_saved_games': 'bool'
    }

    attribute_map = {
        'restore_local_directories_enable': 'restore_local_directories_enable',
        'app_data_roaming_enale': 'appData_roaming_enale',
        'redirec_desktop': 'redirec_desktop',
        'redirec_start_menu': 'redirec_start_menu',
        'redirec_documents': 'redirec_documents',
        'redirec_pictures': 'redirec_pictures',
        'redirec_music': 'redirec_music',
        'redirec_videos': 'redirec_videos',
        'redirec_favorites': 'redirec_favorites',
        'redirec_contacts': 'redirec_contacts',
        'redirec_downloads': 'redirec_downloads',
        'redirec_links': 'redirec_links',
        'redirec_searches': 'redirec_searches',
        'redirec_saved_games': 'redirec_saved_games'
    }

    def __init__(self, restore_local_directories_enable=None, app_data_roaming_enale=None, redirec_desktop=None, redirec_start_menu=None, redirec_documents=None, redirec_pictures=None, redirec_music=None, redirec_videos=None, redirec_favorites=None, redirec_contacts=None, redirec_downloads=None, redirec_links=None, redirec_searches=None, redirec_saved_games=None):
        r"""PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions

        The model defined in huaweicloud sdk

        :param restore_local_directories_enable: 还原本地目录启用。
        :type restore_local_directories_enable: bool
        :param app_data_roaming_enale: 应用数据漫游启用。
        :type app_data_roaming_enale: bool
        :param redirec_desktop: 桌面重定向。
        :type redirec_desktop: bool
        :param redirec_start_menu: 开始菜单。
        :type redirec_start_menu: bool
        :param redirec_documents: 文档。
        :type redirec_documents: bool
        :param redirec_pictures: 照片。
        :type redirec_pictures: bool
        :param redirec_music: 音乐。
        :type redirec_music: bool
        :param redirec_videos: 录音。
        :type redirec_videos: bool
        :param redirec_favorites: 最爱。
        :type redirec_favorites: bool
        :param redirec_contacts: 录音。
        :type redirec_contacts: bool
        :param redirec_downloads: 下载。
        :type redirec_downloads: bool
        :param redirec_links: 链接。
        :type redirec_links: bool
        :param redirec_searches: 查找。
        :type redirec_searches: bool
        :param redirec_saved_games: 游戏存储。
        :type redirec_saved_games: bool
        """
        
        

        self._restore_local_directories_enable = None
        self._app_data_roaming_enale = None
        self._redirec_desktop = None
        self._redirec_start_menu = None
        self._redirec_documents = None
        self._redirec_pictures = None
        self._redirec_music = None
        self._redirec_videos = None
        self._redirec_favorites = None
        self._redirec_contacts = None
        self._redirec_downloads = None
        self._redirec_links = None
        self._redirec_searches = None
        self._redirec_saved_games = None
        self.discriminator = None

        if restore_local_directories_enable is not None:
            self.restore_local_directories_enable = restore_local_directories_enable
        if app_data_roaming_enale is not None:
            self.app_data_roaming_enale = app_data_roaming_enale
        if redirec_desktop is not None:
            self.redirec_desktop = redirec_desktop
        if redirec_start_menu is not None:
            self.redirec_start_menu = redirec_start_menu
        if redirec_documents is not None:
            self.redirec_documents = redirec_documents
        if redirec_pictures is not None:
            self.redirec_pictures = redirec_pictures
        if redirec_music is not None:
            self.redirec_music = redirec_music
        if redirec_videos is not None:
            self.redirec_videos = redirec_videos
        if redirec_favorites is not None:
            self.redirec_favorites = redirec_favorites
        if redirec_contacts is not None:
            self.redirec_contacts = redirec_contacts
        if redirec_downloads is not None:
            self.redirec_downloads = redirec_downloads
        if redirec_links is not None:
            self.redirec_links = redirec_links
        if redirec_searches is not None:
            self.redirec_searches = redirec_searches
        if redirec_saved_games is not None:
            self.redirec_saved_games = redirec_saved_games

    @property
    def restore_local_directories_enable(self):
        r"""Gets the restore_local_directories_enable of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        还原本地目录启用。

        :return: The restore_local_directories_enable of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._restore_local_directories_enable

    @restore_local_directories_enable.setter
    def restore_local_directories_enable(self, restore_local_directories_enable):
        r"""Sets the restore_local_directories_enable of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        还原本地目录启用。

        :param restore_local_directories_enable: The restore_local_directories_enable of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type restore_local_directories_enable: bool
        """
        self._restore_local_directories_enable = restore_local_directories_enable

    @property
    def app_data_roaming_enale(self):
        r"""Gets the app_data_roaming_enale of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        应用数据漫游启用。

        :return: The app_data_roaming_enale of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._app_data_roaming_enale

    @app_data_roaming_enale.setter
    def app_data_roaming_enale(self, app_data_roaming_enale):
        r"""Sets the app_data_roaming_enale of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        应用数据漫游启用。

        :param app_data_roaming_enale: The app_data_roaming_enale of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type app_data_roaming_enale: bool
        """
        self._app_data_roaming_enale = app_data_roaming_enale

    @property
    def redirec_desktop(self):
        r"""Gets the redirec_desktop of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        桌面重定向。

        :return: The redirec_desktop of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_desktop

    @redirec_desktop.setter
    def redirec_desktop(self, redirec_desktop):
        r"""Sets the redirec_desktop of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        桌面重定向。

        :param redirec_desktop: The redirec_desktop of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_desktop: bool
        """
        self._redirec_desktop = redirec_desktop

    @property
    def redirec_start_menu(self):
        r"""Gets the redirec_start_menu of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        开始菜单。

        :return: The redirec_start_menu of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_start_menu

    @redirec_start_menu.setter
    def redirec_start_menu(self, redirec_start_menu):
        r"""Sets the redirec_start_menu of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        开始菜单。

        :param redirec_start_menu: The redirec_start_menu of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_start_menu: bool
        """
        self._redirec_start_menu = redirec_start_menu

    @property
    def redirec_documents(self):
        r"""Gets the redirec_documents of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        文档。

        :return: The redirec_documents of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_documents

    @redirec_documents.setter
    def redirec_documents(self, redirec_documents):
        r"""Sets the redirec_documents of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        文档。

        :param redirec_documents: The redirec_documents of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_documents: bool
        """
        self._redirec_documents = redirec_documents

    @property
    def redirec_pictures(self):
        r"""Gets the redirec_pictures of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        照片。

        :return: The redirec_pictures of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_pictures

    @redirec_pictures.setter
    def redirec_pictures(self, redirec_pictures):
        r"""Sets the redirec_pictures of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        照片。

        :param redirec_pictures: The redirec_pictures of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_pictures: bool
        """
        self._redirec_pictures = redirec_pictures

    @property
    def redirec_music(self):
        r"""Gets the redirec_music of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        音乐。

        :return: The redirec_music of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_music

    @redirec_music.setter
    def redirec_music(self, redirec_music):
        r"""Sets the redirec_music of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        音乐。

        :param redirec_music: The redirec_music of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_music: bool
        """
        self._redirec_music = redirec_music

    @property
    def redirec_videos(self):
        r"""Gets the redirec_videos of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        录音。

        :return: The redirec_videos of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_videos

    @redirec_videos.setter
    def redirec_videos(self, redirec_videos):
        r"""Sets the redirec_videos of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        录音。

        :param redirec_videos: The redirec_videos of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_videos: bool
        """
        self._redirec_videos = redirec_videos

    @property
    def redirec_favorites(self):
        r"""Gets the redirec_favorites of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        最爱。

        :return: The redirec_favorites of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_favorites

    @redirec_favorites.setter
    def redirec_favorites(self, redirec_favorites):
        r"""Sets the redirec_favorites of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        最爱。

        :param redirec_favorites: The redirec_favorites of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_favorites: bool
        """
        self._redirec_favorites = redirec_favorites

    @property
    def redirec_contacts(self):
        r"""Gets the redirec_contacts of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        录音。

        :return: The redirec_contacts of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_contacts

    @redirec_contacts.setter
    def redirec_contacts(self, redirec_contacts):
        r"""Sets the redirec_contacts of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        录音。

        :param redirec_contacts: The redirec_contacts of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_contacts: bool
        """
        self._redirec_contacts = redirec_contacts

    @property
    def redirec_downloads(self):
        r"""Gets the redirec_downloads of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        下载。

        :return: The redirec_downloads of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_downloads

    @redirec_downloads.setter
    def redirec_downloads(self, redirec_downloads):
        r"""Sets the redirec_downloads of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        下载。

        :param redirec_downloads: The redirec_downloads of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_downloads: bool
        """
        self._redirec_downloads = redirec_downloads

    @property
    def redirec_links(self):
        r"""Gets the redirec_links of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        链接。

        :return: The redirec_links of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_links

    @redirec_links.setter
    def redirec_links(self, redirec_links):
        r"""Sets the redirec_links of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        链接。

        :param redirec_links: The redirec_links of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_links: bool
        """
        self._redirec_links = redirec_links

    @property
    def redirec_searches(self):
        r"""Gets the redirec_searches of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        查找。

        :return: The redirec_searches of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_searches

    @redirec_searches.setter
    def redirec_searches(self, redirec_searches):
        r"""Sets the redirec_searches of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        查找。

        :param redirec_searches: The redirec_searches of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_searches: bool
        """
        self._redirec_searches = redirec_searches

    @property
    def redirec_saved_games(self):
        r"""Gets the redirec_saved_games of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        游戏存储。

        :return: The redirec_saved_games of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :rtype: bool
        """
        return self._redirec_saved_games

    @redirec_saved_games.setter
    def redirec_saved_games(self, redirec_saved_games):
        r"""Sets the redirec_saved_games of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.

        游戏存储。

        :param redirec_saved_games: The redirec_saved_games of this PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions.
        :type redirec_saved_games: bool
        """
        self._redirec_saved_games = redirec_saved_games

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
        if not isinstance(other, PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
