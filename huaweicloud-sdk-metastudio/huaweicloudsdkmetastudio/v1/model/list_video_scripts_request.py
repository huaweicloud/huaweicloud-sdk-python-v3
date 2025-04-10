# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVideoScriptsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'script_catalog': 'str',
        'view_mode': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'script_catalog': 'script_catalog',
        'view_mode': 'view_mode'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, name=None, script_catalog=None, view_mode=None):
        r"""ListVideoScriptsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param name: 按名称模糊查询。
        :type name: str
        :param script_catalog: 剧本类型。默认查询VIDEO_DRAFT。 * VIDEO_DRAFT：视频草稿。 * SYSTEM_VIDEO_TEMPLET： 系统视频模板。
        :type script_catalog: str
        :param view_mode: 横竖屏类型（内部参数，不对外开放）。默认值是LANDSCAPE。 * LANDSCAPE：横屏。 * VERTICAL：竖屏。
        :type view_mode: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._script_catalog = None
        self._view_mode = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if script_catalog is not None:
            self.script_catalog = script_catalog
        if view_mode is not None:
            self.view_mode = view_mode

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListVideoScriptsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListVideoScriptsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListVideoScriptsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListVideoScriptsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListVideoScriptsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListVideoScriptsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVideoScriptsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListVideoScriptsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVideoScriptsRequest.

        每页显示的条目数量。

        :return: The limit of this ListVideoScriptsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVideoScriptsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListVideoScriptsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListVideoScriptsRequest.

        按名称模糊查询。

        :return: The name of this ListVideoScriptsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVideoScriptsRequest.

        按名称模糊查询。

        :param name: The name of this ListVideoScriptsRequest.
        :type name: str
        """
        self._name = name

    @property
    def script_catalog(self):
        r"""Gets the script_catalog of this ListVideoScriptsRequest.

        剧本类型。默认查询VIDEO_DRAFT。 * VIDEO_DRAFT：视频草稿。 * SYSTEM_VIDEO_TEMPLET： 系统视频模板。

        :return: The script_catalog of this ListVideoScriptsRequest.
        :rtype: str
        """
        return self._script_catalog

    @script_catalog.setter
    def script_catalog(self, script_catalog):
        r"""Sets the script_catalog of this ListVideoScriptsRequest.

        剧本类型。默认查询VIDEO_DRAFT。 * VIDEO_DRAFT：视频草稿。 * SYSTEM_VIDEO_TEMPLET： 系统视频模板。

        :param script_catalog: The script_catalog of this ListVideoScriptsRequest.
        :type script_catalog: str
        """
        self._script_catalog = script_catalog

    @property
    def view_mode(self):
        r"""Gets the view_mode of this ListVideoScriptsRequest.

        横竖屏类型（内部参数，不对外开放）。默认值是LANDSCAPE。 * LANDSCAPE：横屏。 * VERTICAL：竖屏。

        :return: The view_mode of this ListVideoScriptsRequest.
        :rtype: str
        """
        return self._view_mode

    @view_mode.setter
    def view_mode(self, view_mode):
        r"""Sets the view_mode of this ListVideoScriptsRequest.

        横竖屏类型（内部参数，不对外开放）。默认值是LANDSCAPE。 * LANDSCAPE：横屏。 * VERTICAL：竖屏。

        :param view_mode: The view_mode of this ListVideoScriptsRequest.
        :type view_mode: str
        """
        self._view_mode = view_mode

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
        if not isinstance(other, ListVideoScriptsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
