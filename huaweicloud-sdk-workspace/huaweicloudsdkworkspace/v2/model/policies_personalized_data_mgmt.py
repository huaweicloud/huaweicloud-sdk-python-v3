# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPersonalizedDataMgmt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'personalized_data_mgmt_path': 'str',
        'user_data_roaming_enable': 'bool',
        'user_data_roaming_options': 'PoliciesPersonalizedDataMgmtUserDataRoamingOptions',
        'user_folder_redirection_enable': 'bool',
        'user_folder_redirection_options': 'PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions',
        'logoff_delete_user_configuration': 'bool',
        'network_drive_mapping_enable': 'bool',
        'network_drive_mapping_options': 'PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions'
    }

    attribute_map = {
        'personalized_data_mgmt_path': 'personalized_data_mgmt_path',
        'user_data_roaming_enable': 'user_data_roaming_enable',
        'user_data_roaming_options': 'user_data_roaming_options',
        'user_folder_redirection_enable': 'user_folder_redirection_enable',
        'user_folder_redirection_options': 'user_folder_redirection_options',
        'logoff_delete_user_configuration': 'logoff_delete_user_configuration',
        'network_drive_mapping_enable': 'network_drive_mapping_enable',
        'network_drive_mapping_options': 'network_drive_mapping_options'
    }

    def __init__(self, personalized_data_mgmt_path=None, user_data_roaming_enable=None, user_data_roaming_options=None, user_folder_redirection_enable=None, user_folder_redirection_options=None, logoff_delete_user_configuration=None, network_drive_mapping_enable=None, network_drive_mapping_options=None):
        r"""PoliciesPersonalizedDataMgmt

        The model defined in huaweicloud sdk

        :param personalized_data_mgmt_path: 个性化数据管理路径。
        :type personalized_data_mgmt_path: str
        :param user_data_roaming_enable: 用户数据漫游。
        :type user_data_roaming_enable: bool
        :param user_data_roaming_options: 
        :type user_data_roaming_options: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtUserDataRoamingOptions`
        :param user_folder_redirection_enable: 启用用户文件夹重定向。
        :type user_folder_redirection_enable: bool
        :param user_folder_redirection_options: 
        :type user_folder_redirection_options: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions`
        :param logoff_delete_user_configuration: 启用用户文件夹重定向。
        :type logoff_delete_user_configuration: bool
        :param network_drive_mapping_enable: 启用用户文件夹重定向。
        :type network_drive_mapping_enable: bool
        :param network_drive_mapping_options: 
        :type network_drive_mapping_options: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions`
        """
        
        

        self._personalized_data_mgmt_path = None
        self._user_data_roaming_enable = None
        self._user_data_roaming_options = None
        self._user_folder_redirection_enable = None
        self._user_folder_redirection_options = None
        self._logoff_delete_user_configuration = None
        self._network_drive_mapping_enable = None
        self._network_drive_mapping_options = None
        self.discriminator = None

        if personalized_data_mgmt_path is not None:
            self.personalized_data_mgmt_path = personalized_data_mgmt_path
        if user_data_roaming_enable is not None:
            self.user_data_roaming_enable = user_data_roaming_enable
        if user_data_roaming_options is not None:
            self.user_data_roaming_options = user_data_roaming_options
        if user_folder_redirection_enable is not None:
            self.user_folder_redirection_enable = user_folder_redirection_enable
        if user_folder_redirection_options is not None:
            self.user_folder_redirection_options = user_folder_redirection_options
        if logoff_delete_user_configuration is not None:
            self.logoff_delete_user_configuration = logoff_delete_user_configuration
        if network_drive_mapping_enable is not None:
            self.network_drive_mapping_enable = network_drive_mapping_enable
        if network_drive_mapping_options is not None:
            self.network_drive_mapping_options = network_drive_mapping_options

    @property
    def personalized_data_mgmt_path(self):
        r"""Gets the personalized_data_mgmt_path of this PoliciesPersonalizedDataMgmt.

        个性化数据管理路径。

        :return: The personalized_data_mgmt_path of this PoliciesPersonalizedDataMgmt.
        :rtype: str
        """
        return self._personalized_data_mgmt_path

    @personalized_data_mgmt_path.setter
    def personalized_data_mgmt_path(self, personalized_data_mgmt_path):
        r"""Sets the personalized_data_mgmt_path of this PoliciesPersonalizedDataMgmt.

        个性化数据管理路径。

        :param personalized_data_mgmt_path: The personalized_data_mgmt_path of this PoliciesPersonalizedDataMgmt.
        :type personalized_data_mgmt_path: str
        """
        self._personalized_data_mgmt_path = personalized_data_mgmt_path

    @property
    def user_data_roaming_enable(self):
        r"""Gets the user_data_roaming_enable of this PoliciesPersonalizedDataMgmt.

        用户数据漫游。

        :return: The user_data_roaming_enable of this PoliciesPersonalizedDataMgmt.
        :rtype: bool
        """
        return self._user_data_roaming_enable

    @user_data_roaming_enable.setter
    def user_data_roaming_enable(self, user_data_roaming_enable):
        r"""Sets the user_data_roaming_enable of this PoliciesPersonalizedDataMgmt.

        用户数据漫游。

        :param user_data_roaming_enable: The user_data_roaming_enable of this PoliciesPersonalizedDataMgmt.
        :type user_data_roaming_enable: bool
        """
        self._user_data_roaming_enable = user_data_roaming_enable

    @property
    def user_data_roaming_options(self):
        r"""Gets the user_data_roaming_options of this PoliciesPersonalizedDataMgmt.

        :return: The user_data_roaming_options of this PoliciesPersonalizedDataMgmt.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtUserDataRoamingOptions`
        """
        return self._user_data_roaming_options

    @user_data_roaming_options.setter
    def user_data_roaming_options(self, user_data_roaming_options):
        r"""Sets the user_data_roaming_options of this PoliciesPersonalizedDataMgmt.

        :param user_data_roaming_options: The user_data_roaming_options of this PoliciesPersonalizedDataMgmt.
        :type user_data_roaming_options: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtUserDataRoamingOptions`
        """
        self._user_data_roaming_options = user_data_roaming_options

    @property
    def user_folder_redirection_enable(self):
        r"""Gets the user_folder_redirection_enable of this PoliciesPersonalizedDataMgmt.

        启用用户文件夹重定向。

        :return: The user_folder_redirection_enable of this PoliciesPersonalizedDataMgmt.
        :rtype: bool
        """
        return self._user_folder_redirection_enable

    @user_folder_redirection_enable.setter
    def user_folder_redirection_enable(self, user_folder_redirection_enable):
        r"""Sets the user_folder_redirection_enable of this PoliciesPersonalizedDataMgmt.

        启用用户文件夹重定向。

        :param user_folder_redirection_enable: The user_folder_redirection_enable of this PoliciesPersonalizedDataMgmt.
        :type user_folder_redirection_enable: bool
        """
        self._user_folder_redirection_enable = user_folder_redirection_enable

    @property
    def user_folder_redirection_options(self):
        r"""Gets the user_folder_redirection_options of this PoliciesPersonalizedDataMgmt.

        :return: The user_folder_redirection_options of this PoliciesPersonalizedDataMgmt.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions`
        """
        return self._user_folder_redirection_options

    @user_folder_redirection_options.setter
    def user_folder_redirection_options(self, user_folder_redirection_options):
        r"""Sets the user_folder_redirection_options of this PoliciesPersonalizedDataMgmt.

        :param user_folder_redirection_options: The user_folder_redirection_options of this PoliciesPersonalizedDataMgmt.
        :type user_folder_redirection_options: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtUserFolderRedirectionOptions`
        """
        self._user_folder_redirection_options = user_folder_redirection_options

    @property
    def logoff_delete_user_configuration(self):
        r"""Gets the logoff_delete_user_configuration of this PoliciesPersonalizedDataMgmt.

        启用用户文件夹重定向。

        :return: The logoff_delete_user_configuration of this PoliciesPersonalizedDataMgmt.
        :rtype: bool
        """
        return self._logoff_delete_user_configuration

    @logoff_delete_user_configuration.setter
    def logoff_delete_user_configuration(self, logoff_delete_user_configuration):
        r"""Sets the logoff_delete_user_configuration of this PoliciesPersonalizedDataMgmt.

        启用用户文件夹重定向。

        :param logoff_delete_user_configuration: The logoff_delete_user_configuration of this PoliciesPersonalizedDataMgmt.
        :type logoff_delete_user_configuration: bool
        """
        self._logoff_delete_user_configuration = logoff_delete_user_configuration

    @property
    def network_drive_mapping_enable(self):
        r"""Gets the network_drive_mapping_enable of this PoliciesPersonalizedDataMgmt.

        启用用户文件夹重定向。

        :return: The network_drive_mapping_enable of this PoliciesPersonalizedDataMgmt.
        :rtype: bool
        """
        return self._network_drive_mapping_enable

    @network_drive_mapping_enable.setter
    def network_drive_mapping_enable(self, network_drive_mapping_enable):
        r"""Sets the network_drive_mapping_enable of this PoliciesPersonalizedDataMgmt.

        启用用户文件夹重定向。

        :param network_drive_mapping_enable: The network_drive_mapping_enable of this PoliciesPersonalizedDataMgmt.
        :type network_drive_mapping_enable: bool
        """
        self._network_drive_mapping_enable = network_drive_mapping_enable

    @property
    def network_drive_mapping_options(self):
        r"""Gets the network_drive_mapping_options of this PoliciesPersonalizedDataMgmt.

        :return: The network_drive_mapping_options of this PoliciesPersonalizedDataMgmt.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions`
        """
        return self._network_drive_mapping_options

    @network_drive_mapping_options.setter
    def network_drive_mapping_options(self, network_drive_mapping_options):
        r"""Sets the network_drive_mapping_options of this PoliciesPersonalizedDataMgmt.

        :param network_drive_mapping_options: The network_drive_mapping_options of this PoliciesPersonalizedDataMgmt.
        :type network_drive_mapping_options: :class:`huaweicloudsdkworkspace.v2.PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions`
        """
        self._network_drive_mapping_options = network_drive_mapping_options

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
        if not isinstance(other, PoliciesPersonalizedDataMgmt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
