# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarehouseApp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'app_id': 'str',
        'tenant_id': 'str',
        'app_name': 'str',
        'app_category': 'AppCategoryEnum',
        'os_type': 'OsTypeEnum',
        'version_id': 'str',
        'version_name': 'str',
        'appfile_store_path': 'str',
        'app_file_size': 'str',
        'app_description': 'str',
        'appicon_store_path': 'str',
        'create_time': 'datetime',
        'modify_time': 'datetime',
        'verify_time': 'datetime',
        'verify_status': 'VerifyStatusEnum',
        'verify_comment': 'str',
        'app_icon': 'str',
        'app_extended_info': 'AppExtendedInfo'
    }

    attribute_map = {
        'id': 'id',
        'app_id': 'app_id',
        'tenant_id': 'tenant_id',
        'app_name': 'app_name',
        'app_category': 'app_category',
        'os_type': 'os_type',
        'version_id': 'version_id',
        'version_name': 'version_name',
        'appfile_store_path': 'appfile_store_path',
        'app_file_size': 'app_file_size',
        'app_description': 'app_description',
        'appicon_store_path': 'appicon_store_path',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'verify_time': 'verify_time',
        'verify_status': 'verify_status',
        'verify_comment': 'verify_comment',
        'app_icon': 'app_icon',
        'app_extended_info': 'app_extended_info'
    }

    def __init__(self, id=None, app_id=None, tenant_id=None, app_name=None, app_category=None, os_type=None, version_id=None, version_name=None, appfile_store_path=None, app_file_size=None, app_description=None, appicon_store_path=None, create_time=None, modify_time=None, verify_time=None, verify_status=None, verify_comment=None, app_icon=None, app_extended_info=None):
        r"""WarehouseApp

        The model defined in huaweicloud sdk

        :param id: 应用的记录id。
        :type id: str
        :param app_id: 应用id。
        :type app_id: str
        :param tenant_id: 租户id。
        :type tenant_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param app_category: 
        :type app_category: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        :param os_type: 
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        :param version_id: 版本号。
        :type version_id: str
        :param version_name: 版本名称。
        :type version_name: str
        :param appfile_store_path: 应用文件的存放路径。
        :type appfile_store_path: str
        :param app_file_size: 应用文件的大小，以KB为单位。
        :type app_file_size: str
        :param app_description: 应用描述。
        :type app_description: str
        :param appicon_store_path: 应用文件的存放路径。
        :type appicon_store_path: str
        :param create_time: 应用创建时间。
        :type create_time: datetime
        :param modify_time: 应用修改时间。
        :type modify_time: datetime
        :param verify_time: 应用审核时间。
        :type verify_time: datetime
        :param verify_status: 
        :type verify_status: :class:`huaweicloudsdkworkspaceapp.v1.VerifyStatusEnum`
        :param verify_comment: 审核的评论意见。
        :type verify_comment: str
        :param app_icon: app的图标文件。
        :type app_icon: str
        :param app_extended_info: 
        :type app_extended_info: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        
        

        self._id = None
        self._app_id = None
        self._tenant_id = None
        self._app_name = None
        self._app_category = None
        self._os_type = None
        self._version_id = None
        self._version_name = None
        self._appfile_store_path = None
        self._app_file_size = None
        self._app_description = None
        self._appicon_store_path = None
        self._create_time = None
        self._modify_time = None
        self._verify_time = None
        self._verify_status = None
        self._verify_comment = None
        self._app_icon = None
        self._app_extended_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if app_name is not None:
            self.app_name = app_name
        if app_category is not None:
            self.app_category = app_category
        if os_type is not None:
            self.os_type = os_type
        if version_id is not None:
            self.version_id = version_id
        if version_name is not None:
            self.version_name = version_name
        if appfile_store_path is not None:
            self.appfile_store_path = appfile_store_path
        if app_file_size is not None:
            self.app_file_size = app_file_size
        if app_description is not None:
            self.app_description = app_description
        if appicon_store_path is not None:
            self.appicon_store_path = appicon_store_path
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time
        if verify_time is not None:
            self.verify_time = verify_time
        if verify_status is not None:
            self.verify_status = verify_status
        if verify_comment is not None:
            self.verify_comment = verify_comment
        if app_icon is not None:
            self.app_icon = app_icon
        if app_extended_info is not None:
            self.app_extended_info = app_extended_info

    @property
    def id(self):
        r"""Gets the id of this WarehouseApp.

        应用的记录id。

        :return: The id of this WarehouseApp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WarehouseApp.

        应用的记录id。

        :param id: The id of this WarehouseApp.
        :type id: str
        """
        self._id = id

    @property
    def app_id(self):
        r"""Gets the app_id of this WarehouseApp.

        应用id。

        :return: The app_id of this WarehouseApp.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this WarehouseApp.

        应用id。

        :param app_id: The app_id of this WarehouseApp.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this WarehouseApp.

        租户id。

        :return: The tenant_id of this WarehouseApp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this WarehouseApp.

        租户id。

        :param tenant_id: The tenant_id of this WarehouseApp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def app_name(self):
        r"""Gets the app_name of this WarehouseApp.

        应用名称。

        :return: The app_name of this WarehouseApp.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this WarehouseApp.

        应用名称。

        :param app_name: The app_name of this WarehouseApp.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_category(self):
        r"""Gets the app_category of this WarehouseApp.

        :return: The app_category of this WarehouseApp.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        """
        return self._app_category

    @app_category.setter
    def app_category(self, app_category):
        r"""Sets the app_category of this WarehouseApp.

        :param app_category: The app_category of this WarehouseApp.
        :type app_category: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        """
        self._app_category = app_category

    @property
    def os_type(self):
        r"""Gets the os_type of this WarehouseApp.

        :return: The os_type of this WarehouseApp.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this WarehouseApp.

        :param os_type: The os_type of this WarehouseApp.
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        self._os_type = os_type

    @property
    def version_id(self):
        r"""Gets the version_id of this WarehouseApp.

        版本号。

        :return: The version_id of this WarehouseApp.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this WarehouseApp.

        版本号。

        :param version_id: The version_id of this WarehouseApp.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def version_name(self):
        r"""Gets the version_name of this WarehouseApp.

        版本名称。

        :return: The version_name of this WarehouseApp.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this WarehouseApp.

        版本名称。

        :param version_name: The version_name of this WarehouseApp.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def appfile_store_path(self):
        r"""Gets the appfile_store_path of this WarehouseApp.

        应用文件的存放路径。

        :return: The appfile_store_path of this WarehouseApp.
        :rtype: str
        """
        return self._appfile_store_path

    @appfile_store_path.setter
    def appfile_store_path(self, appfile_store_path):
        r"""Sets the appfile_store_path of this WarehouseApp.

        应用文件的存放路径。

        :param appfile_store_path: The appfile_store_path of this WarehouseApp.
        :type appfile_store_path: str
        """
        self._appfile_store_path = appfile_store_path

    @property
    def app_file_size(self):
        r"""Gets the app_file_size of this WarehouseApp.

        应用文件的大小，以KB为单位。

        :return: The app_file_size of this WarehouseApp.
        :rtype: str
        """
        return self._app_file_size

    @app_file_size.setter
    def app_file_size(self, app_file_size):
        r"""Sets the app_file_size of this WarehouseApp.

        应用文件的大小，以KB为单位。

        :param app_file_size: The app_file_size of this WarehouseApp.
        :type app_file_size: str
        """
        self._app_file_size = app_file_size

    @property
    def app_description(self):
        r"""Gets the app_description of this WarehouseApp.

        应用描述。

        :return: The app_description of this WarehouseApp.
        :rtype: str
        """
        return self._app_description

    @app_description.setter
    def app_description(self, app_description):
        r"""Sets the app_description of this WarehouseApp.

        应用描述。

        :param app_description: The app_description of this WarehouseApp.
        :type app_description: str
        """
        self._app_description = app_description

    @property
    def appicon_store_path(self):
        r"""Gets the appicon_store_path of this WarehouseApp.

        应用文件的存放路径。

        :return: The appicon_store_path of this WarehouseApp.
        :rtype: str
        """
        return self._appicon_store_path

    @appicon_store_path.setter
    def appicon_store_path(self, appicon_store_path):
        r"""Sets the appicon_store_path of this WarehouseApp.

        应用文件的存放路径。

        :param appicon_store_path: The appicon_store_path of this WarehouseApp.
        :type appicon_store_path: str
        """
        self._appicon_store_path = appicon_store_path

    @property
    def create_time(self):
        r"""Gets the create_time of this WarehouseApp.

        应用创建时间。

        :return: The create_time of this WarehouseApp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WarehouseApp.

        应用创建时间。

        :param create_time: The create_time of this WarehouseApp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        r"""Gets the modify_time of this WarehouseApp.

        应用修改时间。

        :return: The modify_time of this WarehouseApp.
        :rtype: datetime
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this WarehouseApp.

        应用修改时间。

        :param modify_time: The modify_time of this WarehouseApp.
        :type modify_time: datetime
        """
        self._modify_time = modify_time

    @property
    def verify_time(self):
        r"""Gets the verify_time of this WarehouseApp.

        应用审核时间。

        :return: The verify_time of this WarehouseApp.
        :rtype: datetime
        """
        return self._verify_time

    @verify_time.setter
    def verify_time(self, verify_time):
        r"""Sets the verify_time of this WarehouseApp.

        应用审核时间。

        :param verify_time: The verify_time of this WarehouseApp.
        :type verify_time: datetime
        """
        self._verify_time = verify_time

    @property
    def verify_status(self):
        r"""Gets the verify_status of this WarehouseApp.

        :return: The verify_status of this WarehouseApp.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VerifyStatusEnum`
        """
        return self._verify_status

    @verify_status.setter
    def verify_status(self, verify_status):
        r"""Sets the verify_status of this WarehouseApp.

        :param verify_status: The verify_status of this WarehouseApp.
        :type verify_status: :class:`huaweicloudsdkworkspaceapp.v1.VerifyStatusEnum`
        """
        self._verify_status = verify_status

    @property
    def verify_comment(self):
        r"""Gets the verify_comment of this WarehouseApp.

        审核的评论意见。

        :return: The verify_comment of this WarehouseApp.
        :rtype: str
        """
        return self._verify_comment

    @verify_comment.setter
    def verify_comment(self, verify_comment):
        r"""Sets the verify_comment of this WarehouseApp.

        审核的评论意见。

        :param verify_comment: The verify_comment of this WarehouseApp.
        :type verify_comment: str
        """
        self._verify_comment = verify_comment

    @property
    def app_icon(self):
        r"""Gets the app_icon of this WarehouseApp.

        app的图标文件。

        :return: The app_icon of this WarehouseApp.
        :rtype: str
        """
        return self._app_icon

    @app_icon.setter
    def app_icon(self, app_icon):
        r"""Sets the app_icon of this WarehouseApp.

        app的图标文件。

        :param app_icon: The app_icon of this WarehouseApp.
        :type app_icon: str
        """
        self._app_icon = app_icon

    @property
    def app_extended_info(self):
        r"""Gets the app_extended_info of this WarehouseApp.

        :return: The app_extended_info of this WarehouseApp.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        return self._app_extended_info

    @app_extended_info.setter
    def app_extended_info(self, app_extended_info):
        r"""Sets the app_extended_info of this WarehouseApp.

        :param app_extended_info: The app_extended_info of this WarehouseApp.
        :type app_extended_info: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        self._app_extended_info = app_extended_info

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
        if not isinstance(other, WarehouseApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
