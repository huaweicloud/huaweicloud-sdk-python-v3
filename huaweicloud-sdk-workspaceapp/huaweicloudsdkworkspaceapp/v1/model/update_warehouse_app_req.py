# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWarehouseAppReq:

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
        'app_icon': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_category': 'app_category',
        'os_type': 'os_type',
        'version_id': 'version_id',
        'app_description': 'app_description',
        'version_name': 'version_name',
        'app_icon': 'app_icon'
    }

    def __init__(self, app_name=None, app_category=None, os_type=None, version_id=None, app_description=None, version_name=None, app_icon=None):
        r"""UpdateWarehouseAppReq

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
        :param app_icon: &gt; - 图片的默认大小当前限制为8KB，即1024 * 8字节。 &gt; - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。
        :type app_icon: str
        """
        
        

        self._app_name = None
        self._app_category = None
        self._os_type = None
        self._version_id = None
        self._app_description = None
        self._version_name = None
        self._app_icon = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_category is not None:
            self.app_category = app_category
        if os_type is not None:
            self.os_type = os_type
        if version_id is not None:
            self.version_id = version_id
        if app_description is not None:
            self.app_description = app_description
        if version_name is not None:
            self.version_name = version_name
        if app_icon is not None:
            self.app_icon = app_icon

    @property
    def app_name(self):
        r"""Gets the app_name of this UpdateWarehouseAppReq.

        应用名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成。 2. 长度范围1~64个字符。

        :return: The app_name of this UpdateWarehouseAppReq.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this UpdateWarehouseAppReq.

        应用名称,名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成。 2. 长度范围1~64个字符。

        :param app_name: The app_name of this UpdateWarehouseAppReq.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_category(self):
        r"""Gets the app_category of this UpdateWarehouseAppReq.

        :return: The app_category of this UpdateWarehouseAppReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        """
        return self._app_category

    @app_category.setter
    def app_category(self, app_category):
        r"""Sets the app_category of this UpdateWarehouseAppReq.

        :param app_category: The app_category of this UpdateWarehouseAppReq.
        :type app_category: :class:`huaweicloudsdkworkspaceapp.v1.AppCategoryEnum`
        """
        self._app_category = app_category

    @property
    def os_type(self):
        r"""Gets the os_type of this UpdateWarehouseAppReq.

        :return: The os_type of this UpdateWarehouseAppReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this UpdateWarehouseAppReq.

        :param os_type: The os_type of this UpdateWarehouseAppReq.
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        self._os_type = os_type

    @property
    def version_id(self):
        r"""Gets the version_id of this UpdateWarehouseAppReq.

        版本号,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~64个字符。

        :return: The version_id of this UpdateWarehouseAppReq.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this UpdateWarehouseAppReq.

        版本号,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~64个字符。

        :param version_id: The version_id of this UpdateWarehouseAppReq.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def app_description(self):
        r"""Gets the app_description of this UpdateWarehouseAppReq.

        应用仓库中的应用描述。

        :return: The app_description of this UpdateWarehouseAppReq.
        :rtype: str
        """
        return self._app_description

    @app_description.setter
    def app_description(self, app_description):
        r"""Sets the app_description of this UpdateWarehouseAppReq.

        应用仓库中的应用描述。

        :param app_description: The app_description of this UpdateWarehouseAppReq.
        :type app_description: str
        """
        self._app_description = app_description

    @property
    def version_name(self):
        r"""Gets the version_name of this UpdateWarehouseAppReq.

        版本描述,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~255个字符。

        :return: The version_name of this UpdateWarehouseAppReq.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this UpdateWarehouseAppReq.

        版本描述,名称需满足如下规则: 1. 由可见字符组成。 2. 长度范围1~255个字符。

        :param version_name: The version_name of this UpdateWarehouseAppReq.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def app_icon(self):
        r"""Gets the app_icon of this UpdateWarehouseAppReq.

        > - 图片的默认大小当前限制为8KB，即1024 * 8字节。 > - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。

        :return: The app_icon of this UpdateWarehouseAppReq.
        :rtype: str
        """
        return self._app_icon

    @app_icon.setter
    def app_icon(self, app_icon):
        r"""Sets the app_icon of this UpdateWarehouseAppReq.

        > - 图片的默认大小当前限制为8KB，即1024 * 8字节。 > - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。

        :param app_icon: The app_icon of this UpdateWarehouseAppReq.
        :type app_icon: str
        """
        self._app_icon = app_icon

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
        if not isinstance(other, UpdateWarehouseAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
