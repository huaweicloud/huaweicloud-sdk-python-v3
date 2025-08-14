# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWarehouseAppReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_category': 'AppCategoryEnum',
        'os_type': 'OsTypeEnum',
        'version_id': 'str',
        'app_description': 'str',
        'version_name': 'str',
        'appfile_store_path': 'str',
        'app_icon': 'str',
        'app_file_size': 'int',
        'app_extended_info': 'AppExtendedInfo'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_category': 'app_category',
        'os_type': 'os_type',
        'version_id': 'version_id',
        'app_description': 'app_description',
        'version_name': 'version_name',
        'appfile_store_path': 'appfile_store_path',
        'app_icon': 'app_icon',
        'app_file_size': 'app_file_size',
        'app_extended_info': 'app_extended_info'
    }

    def __init__(self, app_name=None, app_category=None, os_type=None, version_id=None, app_description=None, version_name=None, appfile_store_path=None, app_icon=None, app_file_size=None, app_extended_info=None):
        r"""CreateWarehouseAppReq

        The model defined in huaweicloud sdk

        :param app_name: 应用名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成。 2. 长度范围1~64个字符。
        :type app_name: str
        :param app_category: 
        :type app_category: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        :param os_type: 
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        :param version_id: 版本号,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~64个字符。
        :type version_id: str
        :param app_description: 应用仓库中的应用描述。
        :type app_description: str
        :param version_name: 版本描述,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~255个字符。
        :type version_name: str
        :param appfile_store_path: 应用在obs桶的存储路径。
        :type appfile_store_path: str
        :param app_icon: &gt; - 图片的默认大小当前限制为8KB，即1024 * 8字节。 &gt; - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。
        :type app_icon: str
        :param app_file_size: 应用文件大小，单位为KB。
        :type app_file_size: int
        :param app_extended_info: 
        :type app_extended_info: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        
        

        self._app_name = None
        self._app_category = None
        self._os_type = None
        self._version_id = None
        self._app_description = None
        self._version_name = None
        self._appfile_store_path = None
        self._app_icon = None
        self._app_file_size = None
        self._app_extended_info = None
        self.discriminator = None

        self.app_name = app_name
        self.app_category = app_category
        self.os_type = os_type
        self.version_id = version_id
        if app_description is not None:
            self.app_description = app_description
        self.version_name = version_name
        self.appfile_store_path = appfile_store_path
        if app_icon is not None:
            self.app_icon = app_icon
        if app_file_size is not None:
            self.app_file_size = app_file_size
        if app_extended_info is not None:
            self.app_extended_info = app_extended_info

    @property
    def app_name(self):
        r"""Gets the app_name of this CreateWarehouseAppReq.

        应用名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成。 2. 长度范围1~64个字符。

        :return: The app_name of this CreateWarehouseAppReq.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this CreateWarehouseAppReq.

        应用名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成。 2. 长度范围1~64个字符。

        :param app_name: The app_name of this CreateWarehouseAppReq.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_category(self):
        r"""Gets the app_category of this CreateWarehouseAppReq.

        :return: The app_category of this CreateWarehouseAppReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        """
        return self._app_category

    @app_category.setter
    def app_category(self, app_category):
        r"""Sets the app_category of this CreateWarehouseAppReq.

        :param app_category: The app_category of this CreateWarehouseAppReq.
        :type app_category: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        """
        self._app_category = app_category

    @property
    def os_type(self):
        r"""Gets the os_type of this CreateWarehouseAppReq.

        :return: The os_type of this CreateWarehouseAppReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this CreateWarehouseAppReq.

        :param os_type: The os_type of this CreateWarehouseAppReq.
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        self._os_type = os_type

    @property
    def version_id(self):
        r"""Gets the version_id of this CreateWarehouseAppReq.

        版本号,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~64个字符。

        :return: The version_id of this CreateWarehouseAppReq.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CreateWarehouseAppReq.

        版本号,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~64个字符。

        :param version_id: The version_id of this CreateWarehouseAppReq.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def app_description(self):
        r"""Gets the app_description of this CreateWarehouseAppReq.

        应用仓库中的应用描述。

        :return: The app_description of this CreateWarehouseAppReq.
        :rtype: str
        """
        return self._app_description

    @app_description.setter
    def app_description(self, app_description):
        r"""Sets the app_description of this CreateWarehouseAppReq.

        应用仓库中的应用描述。

        :param app_description: The app_description of this CreateWarehouseAppReq.
        :type app_description: str
        """
        self._app_description = app_description

    @property
    def version_name(self):
        r"""Gets the version_name of this CreateWarehouseAppReq.

        版本描述,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~255个字符。

        :return: The version_name of this CreateWarehouseAppReq.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this CreateWarehouseAppReq.

        版本描述,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~255个字符。

        :param version_name: The version_name of this CreateWarehouseAppReq.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def appfile_store_path(self):
        r"""Gets the appfile_store_path of this CreateWarehouseAppReq.

        应用在obs桶的存储路径。

        :return: The appfile_store_path of this CreateWarehouseAppReq.
        :rtype: str
        """
        return self._appfile_store_path

    @appfile_store_path.setter
    def appfile_store_path(self, appfile_store_path):
        r"""Sets the appfile_store_path of this CreateWarehouseAppReq.

        应用在obs桶的存储路径。

        :param appfile_store_path: The appfile_store_path of this CreateWarehouseAppReq.
        :type appfile_store_path: str
        """
        self._appfile_store_path = appfile_store_path

    @property
    def app_icon(self):
        r"""Gets the app_icon of this CreateWarehouseAppReq.

        > - 图片的默认大小当前限制为8KB，即1024 * 8字节。 > - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。

        :return: The app_icon of this CreateWarehouseAppReq.
        :rtype: str
        """
        return self._app_icon

    @app_icon.setter
    def app_icon(self, app_icon):
        r"""Sets the app_icon of this CreateWarehouseAppReq.

        > - 图片的默认大小当前限制为8KB，即1024 * 8字节。 > - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。

        :param app_icon: The app_icon of this CreateWarehouseAppReq.
        :type app_icon: str
        """
        self._app_icon = app_icon

    @property
    def app_file_size(self):
        r"""Gets the app_file_size of this CreateWarehouseAppReq.

        应用文件大小，单位为KB。

        :return: The app_file_size of this CreateWarehouseAppReq.
        :rtype: int
        """
        return self._app_file_size

    @app_file_size.setter
    def app_file_size(self, app_file_size):
        r"""Sets the app_file_size of this CreateWarehouseAppReq.

        应用文件大小，单位为KB。

        :param app_file_size: The app_file_size of this CreateWarehouseAppReq.
        :type app_file_size: int
        """
        self._app_file_size = app_file_size

    @property
    def app_extended_info(self):
        r"""Gets the app_extended_info of this CreateWarehouseAppReq.

        :return: The app_extended_info of this CreateWarehouseAppReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        return self._app_extended_info

    @app_extended_info.setter
    def app_extended_info(self, app_extended_info):
        r"""Sets the app_extended_info of this CreateWarehouseAppReq.

        :param app_extended_info: The app_extended_info of this CreateWarehouseAppReq.
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
        if not isinstance(other, CreateWarehouseAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
